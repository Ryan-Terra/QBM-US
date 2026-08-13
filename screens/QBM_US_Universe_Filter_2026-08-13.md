# QBM-US Universe Filter — 13 August 2026

Methodology version: **1.1** — first application of the Universe Filter defined in [QBM_US_Methodology.md](../framework/QBM_US_Methodology.md#universe-filter-added-v11)

This is a pre-Discovery mechanical filter, not a QBM scan. No business-quality, moat or valuation judgment has been applied to any of these companies yet — only market cap, price, liquidity, listing and security-type checks.

## Source universe

S&P 1500 constituents, fetched from Wikipedia:

| Index | Constituents |
|---|---:|
| S&P 500 | 503 |
| S&P 400 (MidCap) | 400 |
| S&P 600 (SmallCap) | 603 |
| **Total, after de-duplication** | **1,506** |

Data date: 13 August 2026. Market cap, price, average daily volume, exchange and security type pulled live via yfinance at fetch time.

## Filter thresholds applied

| Filter | Threshold |
|---|---|
| Market cap | ≥ $2B |
| Avg daily dollar volume | ≥ $5M |
| Share price | ≥ $5 |
| Listing | NYSE/NASDAQ primary |
| Security type | Common stock only |

## Result

| | Count |
|---|---:|
| Source universe | 1,506 |
| **Cleared filter (Discovery-eligible)** | **1,313** |
| Excluded | 193 |

### Exclusion breakdown (a ticker can trigger more than one reason)

| Reason | Count |
|---|---:|
| Market cap below $2B | 190 |
| Share price below $5 | 8 |
| Avg dollar volume below $5M | 5 |
| Exchange not NYSE/NASDAQ | 2 |
| Not common stock (quote type) | 1 |

The dominant reason by far is market cap — expected, since S&P 400/600 (MidCap/SmallCap) intentionally include companies below the $2B floor.

**Raw data, committed permanently:** [QBM_US_Universe_Filter_2026-08-13_filtered.csv](QBM_US_Universe_Filter_2026-08-13_filtered.csv), [QBM_US_Universe_Filter_2026-08-13_excluded.csv](QBM_US_Universe_Filter_2026-08-13_excluded.csv).

## Open question: 1,313 is still not a Discovery-stage number

QBM's own ASX scan worked from a "top-300 liquid proxy," and Discovery on that already meant reviewing every one of those 300 with real, evidence-based research — no invented data. 1,313 is roughly 4.4x that. Genuinely researching 1,313 companies one by one isn't practical in any single pass, and mechanically claiming Discovery-level coverage without doing the work would violate QBM-US's own evidence philosophy.

This isn't resolved yet. Options worth considering once the investor is back, not decided here:

1. Add a further **mechanical, quantitative** pre-screen (e.g. profitability, revenue growth, debt levels, ROE) using data already available from yfinance, to cut 1,313 down to a genuinely reviewable longlist before any qualitative research starts.
2. Work through the 1,313 in **batches** over multiple sessions rather than one pass, disclosing partial coverage honestly each time (the Methodology's "Accuracy and progressive coverage" section already allows this).
3. Narrow the source universe further (e.g. S&P 500 only, or S&P 500 + S&P 400) rather than starting from the full S&P 1500.

No Discovery-stage research has started. This filter step only establishes what's eligible to be researched.
