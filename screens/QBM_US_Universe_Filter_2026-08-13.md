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

## Quantitative Pre-Screen (v1.2) — second pass, same day

Applied to the 1,313 tickers that cleared the Universe Filter, per [QBM_US_Methodology.md v1.2](../framework/QBM_US_Methodology.md#quantitative-pre-screen-added-v12): profitable (net margin > 0%), free cash flow positive, ROE ≥ 10%, revenue growth ≥ 0%, current ratio ≥ 1.0.

| | Count |
|---|---:|
| Input (post Universe Filter) | 1,313 |
| **Passed (Discovery-eligible)** | **454** |
| Excluded | 859 |

### Exclusion breakdown (a ticker can trigger more than one reason)

| Reason | Count |
|---|---:|
| ROE below 10% | 511 |
| Current ratio below 1.0 | 394 |
| Free cash flow not positive | 274 |
| Revenue growth negative | 187 |
| Net margin not positive | 117 |

### Sector spread of the 454 survivors

Industrials 125, Information Technology 66, Health Care 61, Consumer Discretionary 59, Financials 48, Materials 27, Consumer Staples 25, Energy 20, Communication Services 13, Real Estate 10 (remaining sectors smaller).

**Known caveat, disclosed rather than hidden:** "current ratio" is not a meaningful metric for banks and insurers, which don't hold a conventional current/non-current balance-sheet split — the 48 Financials that passed may be under-representing genuinely good financial-sector candidates that got excluded on a metric that doesn't apply cleanly to their business model. Worth a second look before treating any Financials exclusion in this pass as final.

**Raw data, committed permanently:** [QBM_US_Universe_Filter_2026-08-13_prescreened.csv](QBM_US_Universe_Filter_2026-08-13_prescreened.csv), [QBM_US_Universe_Filter_2026-08-13_prescreen_excluded.csv](QBM_US_Universe_Filter_2026-08-13_prescreen_excluded.csv).

## Where this leaves Discovery

454 is much closer to workable than 1,313, but still roughly 1.5x the ~300 companies QBM's own ASX Discovery scan actually covered with genuine research. No Discovery-stage research has started — both steps above are still mechanical, no-judgment filters. Whether to work through all 454, batch it across sessions, or narrow further is a decision for the investor, not made here.
