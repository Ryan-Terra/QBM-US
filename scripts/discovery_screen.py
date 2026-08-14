"""Discovery-stage processing for the tickers that cleared the Universe Filter
and Quantitative Pre-Screen (data/universe_prescreened.csv).

Two steps, per framework/QBM_US_Methodology.md Discovery requirements:

1. Ethical exclusion (weapons manufacturing / gambling / tobacco). GICS
   sub-industry is fetched as a coarse flag -- it is NOT precise enough to
   exclude on by itself (QBM over-broadly excluded Codan on "defence"
   sub-industry grounds before narrowing the policy to "weapons
   manufacturing" specifically). Every flagged ticker is individually
   classified below based on whether weapons manufacturing/gambling is
   genuinely the *principal* activity. This classification is Discovery-stage
   judgment, not a Full QBM Evidence-Verification-Standard pass -- it should
   be re-verified properly if a flagged company ever advances to Full QBM.

2. Quantitative Discovery ranking. "Preliminary Eligibility filters without
   producing full reports" (per Methodology) is operationalised as a
   composite Discovery Score: the average percentile rank of ROE, net
   profit margin and revenue growth -- three numeric proxies for QBM's own
   Investment Principles (capital allocation, cash-generation quality,
   durability). This is explicitly not a valuation or Investment
   Attractiveness judgment; those are Mini/Full QBM questions.

Output: data/universe_discovery_ranked.csv (all eligible, ranked) and
data/discovery_longlist_40.csv (top 40, the Methodology's 30-50 target range).
"""

import io

import pandas as pd
import requests

WIKI_PAGES = {
    "S&P 500": "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
    "S&P 400 (MidCap)": "https://en.wikipedia.org/wiki/List_of_S%26P_400_companies",
    "S&P 600 (SmallCap)": "https://en.wikipedia.org/wiki/List_of_S%26P_600_companies",
}
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

FLAGGED_SUB_INDUSTRIES = ["Aerospace & Defense", "Casinos & Gaming", "Tobacco"]

# Individually classified after the sub-industry flag -- see module docstring.
EXCLUDED = {
    "LMT": "weapons manufacturing (fighter jets, missiles, combat systems)",
    "NOC": "weapons manufacturing (bombers, missiles)",
    "RTX": "weapons manufacturing (missiles, missile defense)",
    "MGM": "gambling (casino operator)",
    "MCRI": "gambling (casino operator)",
    "RSI": "gambling (sports betting/casino operator)",
}
FLAGGED_NOT_EXCLUDED = {
    "GD": "defense-adjacent (Combat Systems segment), majority non-weapons (Gulfstream/Marine/Tech)",
    "BA": "defense-adjacent (Boeing Defense), majority non-weapons (commercial aircraft)",
    "TXT": "defense-adjacent (Bell military/Textron Systems), majority non-weapons (general aviation/industrial)",
    "HWM": "aerospace/defense materials supplier, not a weapons manufacturer",
    "ATI": "aerospace/defense materials supplier, not a weapons manufacturer",
    "CW": "aerospace/defense components supplier, not a weapons manufacturer",
    "HXL": "aerospace/defense composites supplier, not a weapons manufacturer",
    "MOG-A": "aerospace/defense actuation components supplier, not a weapons manufacturer",
    "BWXT": "naval nuclear propulsion components, not a weapons manufacturer",
    "SARO": "aircraft MRO services, not a weapons manufacturer",
}

LONGLIST_SIZE = 40


def fetch_sub_industry() -> pd.DataFrame:
    frames = []
    for name, url in WIKI_PAGES.items():
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        table = pd.read_html(io.StringIO(resp.text))[0]
        table.columns = [str(c).strip() for c in table.columns]
        sym_col = next(c for c in table.columns if c.lower() in ("symbol", "ticker"))
        sub_col = next(c for c in table.columns if "sub-industry" in c.lower() or "sub industry" in c.lower())
        sub = table[[sym_col, sub_col]].copy()
        sub.columns = ["ticker", "sub_industry"]
        sub["ticker"] = sub["ticker"].str.strip().str.replace(".", "-", regex=False)
        frames.append(sub)
    return pd.concat(frames).drop_duplicates(subset="ticker", keep="first")


def main():
    prescreened = pd.read_csv("data/universe_prescreened.csv")
    sub = fetch_sub_industry()
    df = prescreened.merge(sub, on="ticker", how="left")
    df.to_csv("data/universe_with_subindustry.csv", index=False)

    flagged = df["sub_industry"].isin(FLAGGED_SUB_INDUSTRIES)
    print(f"Flagged for individual ethics review via sub-industry: {flagged.sum()}")

    df["ethics_status"] = "Eligible"
    df["ethics_note"] = ""
    for ticker, reason in EXCLUDED.items():
        df.loc[df["ticker"] == ticker, "ethics_status"] = "Excluded"
        df.loc[df["ticker"] == ticker, "ethics_note"] = reason
    for ticker, reason in FLAGGED_NOT_EXCLUDED.items():
        df.loc[df["ticker"] == ticker, "ethics_note"] = reason
    df.to_csv("data/universe_ethics_screened.csv", index=False)

    eligible = df[df["ethics_status"] == "Eligible"].copy()
    print(f"Excluded: {len(df) - len(eligible)}; eligible for Discovery ranking: {len(eligible)}")

    for col in ["roe", "profit_margin", "revenue_growth"]:
        eligible[col + "_pct"] = eligible[col].rank(pct=True)
    eligible["discovery_score"] = eligible[["roe_pct", "profit_margin_pct", "revenue_growth_pct"]].mean(axis=1)
    eligible = eligible.sort_values("discovery_score", ascending=False).reset_index(drop=True)
    eligible["discovery_rank"] = eligible.index + 1
    eligible.to_csv("data/universe_discovery_ranked.csv", index=False)

    longlist = eligible.head(LONGLIST_SIZE)
    longlist.to_csv("data/discovery_longlist_40.csv", index=False)
    print(f"\nDiscovery longlist ({LONGLIST_SIZE}) written to data/discovery_longlist_40.csv")
    print(longlist["sector"].value_counts())


if __name__ == "__main__":
    main()
