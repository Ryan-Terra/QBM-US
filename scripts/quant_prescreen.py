"""Quantitative pre-screen applied to the 1,313 tickers that cleared the
Universe Filter (screens/QBM_US_Universe_Filter_2026-08-13.md).

This is still a mechanical, no-judgment step -- not Discovery itself. It exists
because 1,313 is far more than can be genuinely, evidence-based researched in
one Discovery pass. The five criteria below are a numeric proxy for QBM's own
Investment Principles (durable cash generation, high returns on capital,
conservative balance sheets, not-shrinking business) -- coarse and imperfect,
but the alternative is either an arbitrary universe cut or pretending to
review 1,313 companies without actually doing the work.

A ticker must pass ALL five to advance into genuine Discovery-stage research:
  1. Profitable            -- trailing net margin > 0%
  2. Free cash flow positive -- freeCashflow > $0
  3. Return on equity       -- >= 10%
  4. Revenue growth (yoy)   -- >= 0% (not shrinking)
  5. Liquidity              -- current ratio >= 1.0

Output: data/universe_prescreened.csv (passed) and
data/universe_prescreen_excluded.csv (failed, with reasons).
"""

import pandas as pd
import yfinance as yf

MIN_ROE = 0.10
MIN_CURRENT_RATIO = 1.0


def main():
    filtered = pd.read_csv("data/universe_filtered.csv")
    tickers = filtered["ticker"].tolist()
    print(f"Applying quantitative pre-screen to {len(tickers)} tickers...")

    passed_rows = []
    excluded_rows = []

    batch_size = 100
    for start in range(0, len(tickers), batch_size):
        batch = tickers[start:start + batch_size]
        print(f"  Batch {start}-{start + len(batch)} of {len(tickers)}...")
        for ticker in batch:
            row = filtered[filtered["ticker"] == ticker].iloc[0].to_dict()
            try:
                info = yf.Ticker(ticker).info
                profit_margin = info.get("profitMargins")
                fcf = info.get("freeCashflow")
                roe = info.get("returnOnEquity")
                rev_growth = info.get("revenueGrowth")
                current_ratio = info.get("currentRatio")

                reasons = []
                if profit_margin is None or profit_margin <= 0:
                    reasons.append(f"profit_margin={profit_margin}")
                if fcf is None or fcf <= 0:
                    reasons.append(f"free_cash_flow={fcf}")
                if roe is None or roe < MIN_ROE:
                    reasons.append(f"roe={roe}")
                if rev_growth is None or rev_growth < 0:
                    reasons.append(f"revenue_growth={rev_growth}")
                if current_ratio is None or current_ratio < MIN_CURRENT_RATIO:
                    reasons.append(f"current_ratio={current_ratio}")

                row.update({
                    "profit_margin": profit_margin,
                    "free_cash_flow": fcf,
                    "roe": roe,
                    "revenue_growth": rev_growth,
                    "current_ratio": current_ratio,
                })

                if reasons:
                    row["exclusion_reasons"] = "; ".join(reasons)
                    excluded_rows.append(row)
                else:
                    passed_rows.append(row)
            except Exception as e:
                row["exclusion_reasons"] = f"fetch_error: {e}"
                excluded_rows.append(row)

    passed = pd.DataFrame(passed_rows)
    excluded = pd.DataFrame(excluded_rows)
    passed.to_csv("data/universe_prescreened.csv", index=False)
    excluded.to_csv("data/universe_prescreen_excluded.csv", index=False)

    print(f"\nDone. {len(passed)} tickers passed the quantitative pre-screen, {len(excluded)} excluded.")
    print("Wrote data/universe_prescreened.csv and data/universe_prescreen_excluded.csv")


if __name__ == "__main__":
    main()
