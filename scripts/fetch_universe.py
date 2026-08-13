"""Fetch the S&P 1500 constituent list and apply the QBM-US Universe Filter
(framework/QBM_US_Methodology.md, v1.1).

S&P 1500 = S&P 500 + S&P MidCap 400 + S&P SmallCap 600. Constituent lists are
scraped from Wikipedia (clean HTML tables, no auth, same pattern used for the
old RCS project's S&P 500 fetch). Market cap, average dollar volume, price,
exchange and security type come from yfinance.

Output: data/universe_raw.csv (all S&P 1500 constituents, before filter) and
data/universe_filtered.csv (post-filter, this is the Discovery-stage universe).
"""

import io
import sys
import time

import pandas as pd
import requests
import yfinance as yf

WIKI_PAGES = {
    "S&P 500": "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
    "S&P 400 (MidCap)": "https://en.wikipedia.org/wiki/List_of_S%26P_400_companies",
    "S&P 600 (SmallCap)": "https://en.wikipedia.org/wiki/List_of_S%26P_600_companies",
}

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

MIN_MARKET_CAP = 2_000_000_000
MIN_AVG_DOLLAR_VOLUME = 5_000_000
MIN_PRICE = 5.0
ALLOWED_EXCHANGES = {"NYQ", "NMS", "NGM", "NCM", "ASE", "PCX"}
# yfinance exchange codes: NYQ=NYSE, NMS/NGM/NCM=NASDAQ tiers, ASE/PCX=NYSE American/Arca


def normalize_ticker(raw: str) -> str:
    return raw.strip().replace(".", "-")


def fetch_index_table(url: str) -> pd.DataFrame:
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    tables = pd.read_html(io.StringIO(resp.text))
    # The constituent table is the first one with a "Symbol" or "Ticker" column
    for t in tables:
        cols = [str(c).strip().lower() for c in t.columns]
        if "symbol" in cols or "ticker" in cols or "ticker symbol" in cols:
            return t
    raise ValueError(f"No constituent table with a ticker column found at {url}")


def main():
    all_rows = []
    for index_name, url in WIKI_PAGES.items():
        print(f"Fetching {index_name} from {url} ...")
        table = fetch_index_table(url)
        table.columns = [str(c).strip() for c in table.columns]
        sym_col = next(c for c in table.columns if c.lower() in ("symbol", "ticker", "ticker symbol"))
        name_col = next((c for c in table.columns if "security" in c.lower() or "company" in c.lower()), None)
        sector_col = next((c for c in table.columns if "sector" in c.lower()), None)
        for _, row in table.iterrows():
            all_rows.append({
                "ticker": normalize_ticker(str(row[sym_col])),
                "name": str(row[name_col]) if name_col else "",
                "sector": str(row[sector_col]) if sector_col else "",
                "index": index_name,
            })
        print(f"  {len(table)} constituents")
        time.sleep(1)

    raw = pd.DataFrame(all_rows)
    before_dedup = len(raw)
    raw = raw.drop_duplicates(subset="ticker", keep="first").reset_index(drop=True)
    print(f"\nTotal rows: {before_dedup}, after de-dup: {len(raw)} unique tickers")
    raw.to_csv("data/universe_raw.csv", index=False)
    print("Wrote data/universe_raw.csv")

    print(f"\nApplying Universe Filter to {len(raw)} tickers (this takes a while)...")
    filtered_rows = []
    excluded_rows = []
    tickers = raw["ticker"].tolist()

    batch_size = 100
    for start in range(0, len(tickers), batch_size):
        batch = tickers[start:start + batch_size]
        print(f"  Batch {start}-{start + len(batch)} of {len(tickers)}...")
        for ticker in batch:
            row = raw[raw["ticker"] == ticker].iloc[0].to_dict()
            try:
                t = yf.Ticker(ticker)
                info = t.info
                market_cap = info.get("marketCap")
                price = info.get("currentPrice") or info.get("regularMarketPrice")
                avg_volume = info.get("averageDailyVolume10Day") or info.get("averageVolume")
                exchange = info.get("exchange")
                quote_type = info.get("quoteType")

                dollar_volume = (avg_volume * price) if (avg_volume and price) else None

                reasons = []
                if not market_cap or market_cap < MIN_MARKET_CAP:
                    reasons.append(f"market_cap={market_cap}")
                if not price or price < MIN_PRICE:
                    reasons.append(f"price={price}")
                if not dollar_volume or dollar_volume < MIN_AVG_DOLLAR_VOLUME:
                    reasons.append(f"dollar_volume={dollar_volume}")
                if exchange not in ALLOWED_EXCHANGES:
                    reasons.append(f"exchange={exchange}")
                if quote_type != "EQUITY":
                    reasons.append(f"quote_type={quote_type}")

                row.update({
                    "market_cap": market_cap,
                    "price": price,
                    "avg_dollar_volume": dollar_volume,
                    "exchange": exchange,
                    "quote_type": quote_type,
                })

                if reasons:
                    row["exclusion_reasons"] = "; ".join(reasons)
                    excluded_rows.append(row)
                else:
                    filtered_rows.append(row)
            except Exception as e:
                row["exclusion_reasons"] = f"fetch_error: {e}"
                excluded_rows.append(row)

    filtered = pd.DataFrame(filtered_rows)
    excluded = pd.DataFrame(excluded_rows)
    filtered.to_csv("data/universe_filtered.csv", index=False)
    excluded.to_csv("data/universe_excluded.csv", index=False)

    print(f"\nDone. {len(filtered)} tickers cleared the Universe Filter, {len(excluded)} excluded.")
    print("Wrote data/universe_filtered.csv and data/universe_excluded.csv")


if __name__ == "__main__":
    main()
