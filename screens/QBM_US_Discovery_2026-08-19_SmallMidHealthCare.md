# QBM-US Dedicated Discovery Scan — Small/Mid-Cap Health Care & Oncology — 19 August 2026

Methodology version: **1.4** — first application of the Universe Filter market-cap floor reduction and the Health Care Quantitative Pre-Screen exemption, both added this version. See [QBM_US_Methodology.md Changelog](../framework/QBM_US_Methodology.md#changelog).

## Why this scan exists

The 14 Aug 2026 general Full QBM funnel produced only two Add decisions (LLY, MA), both mega-cap. The investor flagged that the result under-represented small/mid-cap opportunity, specifically in health care and oncology. Diagnosis, confirmed by re-reading the funnel mechanics:

1. **The Universe Filter's ≥$2B market-cap floor excluded all genuine small-caps** (conventionally ~$300M–$2B) before Discovery could ever see them.
2. **The Quantitative Pre-Screen required profitability** (net margin > 0%, positive free cash flow, ROE ≥ 10%) before a company reached Discovery — a gate that clinical-stage and early-commercial biotech routinely fails by design, regardless of pipeline or business quality.
3. Of the few Health Care names that did survive the 14 Aug scan, the two closest to small/mid-cap (TGTX, LQDA) were rejected at Mini QBM largely for single-product concentration risk — a near-structural feature of small biotech, meaning the funnel was stacked against this category at three separate points.

Both structural causes (1) and (2) are fixed in Methodology v1.4: the market-cap floor is lowered to $300M, and Health Care is exempted from the profitability/FCF/ROE gates (liquidity still required). This is a dedicated Discovery-stage scan applying the new rules directly to the Health Care sector, rather than waiting for the next general full-market scan to (maybe) surface it.

This is a **Discovery-stage scan only** — mechanical filtering and ranking, no Company Quality, moat or valuation judgment. Nothing here is a Mini QBM or Full QBM conclusion, and no Investment Decision has been made on any of these companies.

## Source universe

S&P 400 (MidCap) + S&P 600 (SmallCap) constituents, GICS Sector = Health Care, fetched from Wikipedia. (The S&P 500 was excluded from the source list for this scan by design — it holds almost no true small/mid-cap names.)

| | Count |
|---|---:|
| S&P 400 (MidCap) + S&P 600 (SmallCap) Health Care constituents | 104 |
| Sub-industry spread | Biotechnology 21, Pharmaceuticals 19, Health Care Equipment 18, Health Care Services 17, Health Care Supplies 9, Health Care Facilities 8, Life Sciences Tools & Services 5, Health Care Technology 5, Managed Health Care 2 |

Data date: 19 August 2026. Market cap, price, volume, exchange, quote type and available financials pulled live via yfinance.

## Universe Filter (v1.4) applied, restricted to the small/mid-cap band

| Filter | Threshold |
|---|---|
| Market cap | ≥ $300M **and** < $10B (this scan intentionally caps at $10B — the general ≥$300M floor has no ceiling, but the point of this dedicated pass is to surface small/mid-cap names the mega-cap-skewed general funnel already under-serves; large/mega-cap Health Care remains eligible in ordinary full-market scans) |
| Avg daily dollar volume | ≥ $5M |
| Share price | ≥ $5 |
| Listing | NYSE/NASDAQ primary (incl. Nasdaq Capital Market) |
| Security type | Common stock only |

| | Count |
|---|---:|
| Input | 104 |
| **Cleared** | **82** |
| Excluded | 22 |

Exclusions were almost entirely companies at $10B+ market cap (19 of 22) — i.e., real, established mid-large Health Care names (EXEL, ILMN, UTHR, HALO, JAZZ, NBIX and others) that are legitimate candidates for the *general* funnel, just out of scope for this small/mid-cap-focused pass by design, not rejected on any quality basis.

## Quantitative Pre-Screen (v1.4, Health Care exemption applied)

Profitability, free cash flow and ROE gates do not apply (Health Care exemption, v1.4). Liquidity gate (current ratio ≥ 1.0) still applies.

| | Count |
|---|---:|
| Input | 82 |
| **Cleared** | **78** |
| Excluded (current ratio < 1.0) | 4 — CHE (0.91), HIMS (0.93), FTRE (0.96), INDV (0.84) |

Of the 78 survivors, 54 are independently profitable anyway (net margin > 0% and ROE > 0%) and 24 are development-stage/unprofitable — i.e., the category the profitability gate would previously have excluded outright, unresearched. **Note on the composition of this 24:** only 4 are pure biotechnology (VIR, XNCR, SRPT, RCUS) — the rest are equipment/supplies/services/pharma names with a temporarily weak metric. This itself is a disclosed limitation: even the *lowered* $300M floor and S&P 400/600 index membership still screen out much of the truly early clinical-stage oncology biotech universe (many trade below $300M or aren't S&P-1500-index-eligible at all, e.g. via Russell 2000/microcap or recent-IPO names). This scan surfaces what's available inside the S&P 1500 small/mid-cap Health Care set; it is not a claim of complete micro-cap oncology coverage.

**Known data-quality caveat, disclosed rather than hidden:** VIR (Vir Biotechnology)'s reported YoY revenue growth figure (+19,582%) is a data artifact from a near-zero prior-period revenue base, not a meaningful growth signal — shown in the raw data but excluded from ranking interpretation.

**Raw data, committed permanently:** [QBM_US_SmallMidHealthCare_2026-08-19_universe.csv](QBM_US_SmallMidHealthCare_2026-08-19_universe.csv), [QBM_US_SmallMidHealthCare_2026-08-19_prescreened.csv](QBM_US_SmallMidHealthCare_2026-08-19_prescreened.csv).

## Ranking methodology

Two cohorts ranked separately, since profitability metrics are not meaningful for development-stage names:

- **Profitable cohort (54 companies):** Discovery Score = average percentile rank across ROE, net margin and revenue growth — identical to the general Discovery methodology.
- **Development-stage cohort (24 companies):** ranked by revenue growth alone (the only metric of the three that remains meaningful pre-profitability), explicitly disclosed as a cruder proxy than the profitable-cohort score.

Top 25 profitable + top 15 development-stage = 40 companies. **RCUS (Arcus Biosciences)** was added as a 41st, manual inclusion: it is a clinical-stage pure-play oncology immunotherapy company that ranked last in its cohort only because a one-off collaboration-revenue comparison produced a large negative YoY figure, not because of any evidenced pipeline or quality problem — flagged here rather than silently dropped, consistent with the Charter's evidence philosophy.

## Longlist (41) — oncology/cancer relevance flagged

**Oncology/cancer relevance is Discovery-stage business-description judgment, not yet run through the Evidence Verification Standard** (the dedicated price/adverse-event/analyst-sentiment search pass required before any Full QBM conclusion). Treat as a starting point for Mini QBM, not a verified classification.

### Flagged as oncology/cancer-relevant (7)

| Ticker | Company | Sub-Industry | Market Cap | Profitability | Rev. growth | Current ratio | Why flagged |
|---|---|---|---:|---|---:|---:|---|
| SDGR | Schrödinger, Inc. | Health Care Services | $1.32B | Dev-stage (exempt) | 7.5% | 2.71 | Computational drug discovery; own + partnered oncology pipeline |
| XNCR | Xencor, Inc. | Biotechnology | $1.89B | Dev-stage (exempt) | 17.5% | 6.39 | Oncology + autoimmune bispecific-antibody biotech, meaningful oncology pipeline |
| NEO | NeoGenomics, Inc. | Health Care Services | $2.04B | Dev-stage (exempt) | 11.2% | 3.60 | Cancer genomics/molecular diagnostics — pure-play oncology testing |
| VCYT | Veracyte, Inc. | Health Care Services | $3.27B | 20.4% margin, 8.8% ROE | 15.5% | 9.16 | Genomic diagnostics incl. thyroid/prostate/lung cancer tests |
| RCUS | Arcus Biosciences, Inc. | Biotechnology | $3.71B | Dev-stage (exempt) | n/m — see note above | 3.82 | Clinical-stage oncology immunotherapy — pure-play |
| RDNT | RadNet, Inc. | Health Care Services | $5.81B | Dev-stage (exempt) | 25.0% | 1.48 | Diagnostic imaging centers incl. mammography/cancer screening |
| LNTH | Lantheus Holdings, Inc. | Health Care Supplies | $6.54B | 17.7% margin, 22.2% ROE | 2.7% | 3.06 | Radiopharmaceuticals; PYLARIFY prostate-cancer PET imaging is majority of revenue |

### Remaining longlist (34) — other Health Care sub-sectors

| Ticker | Company | Sub-Industry | Market Cap | Profitability | Rev. growth | Current ratio |
|---|---|---|---:|---|---:|---:|
| AHCO | AdaptHealth Corp. | Health Care Equipment | $0.78B | Dev-stage (exempt) | 12.7% | 1.12 |
| QDEL | QuidelOrtho Corporation | Health Care Supplies | $0.92B | Dev-stage (exempt) | 2.8% | 1.39 |
| AORT | Artivion, Inc. | Health Care Equipment | $1.41B | Dev-stage (exempt) | 11.3% | 3.47 |
| PAHC | Phibro Animal Health Corporation | Pharmaceuticals | $1.41B | 6.3% margin, 30.3% ROE | 10.3% | 3.17 |
| AZTA | Azenta, Inc. | Life Sciences Tools & Services | $1.44B | Dev-stage (exempt) | 12.0% | 2.50 |
| ENOV | Enovis Corporation | Health Care Equipment | $1.48B | Dev-stage (exempt) | 3.2% | 1.99 |
| INVA | Innoviva, Inc. | Pharmaceuticals | $1.54B | 81.2% margin, 36.7% ROE | 19.3% | 16.01 |
| VIR | Vir Biotechnology, Inc. | Biotechnology | $1.61B | Dev-stage (exempt) | Not meaningful — data artifact, see caveat above | 6.04 |
| TNDM | Tandem Diabetes Care, Inc. | Health Care Equipment | $1.65B | Dev-stage (exempt) | 5.8% | 3.18 |
| BLFS | BioLife Solutions, Inc. | Health Care Supplies | $1.71B | 54.3% margin, 12.8% ROE | 21.5% | 9.69 |
| ANIP | ANI Pharmaceuticals, Inc. | Pharmaceuticals | $1.77B | 11.1% margin, 20.5% ROE | 25.9% | 2.91 |
| LMAT | LeMaitre Vascular, Inc. | Health Care Equipment | $1.86B | 25.0% margin, 16.8% ROE | 9.6% | 16.31 |
| ADMA | ADMA Biologics, Inc. | Biotechnology | $2.14B | 33.0% margin, 41.9% ROE | 15.9% | 6.97 |
| HRMY | Harmony Biosciences Holdings, Inc. | Biotechnology | $2.26B | 18.9% margin, 20.5% ROE | 30.3% | 3.48 |
| VCEL | Vericel Corporation | Biotechnology | $2.27B | 7.9% margin, 7.2% ROE | 22.5% | 5.04 |
| UFPT | UFP Technologies, Inc. | Health Care Equipment | $2.43B | 11.4% margin, 17.1% ROE | 15.1% | 3.00 |
| ALHC | Alignment Healthcare, Inc. | Health Care Services | $2.74B | 0.9% margin, 20.0% ROE | 31.6% | 1.70 |
| SUPN | Supernus Pharmaceuticals, Inc. | Pharmaceuticals | $2.85B | Dev-stage (exempt) | 32.4% | 2.08 |
| TMDX | TransMedics Group, Inc. | Health Care Equipment | $3.14B | 22.7% margin, 36.3% ROE | 20.7% | 6.63 |
| CRVL | CorVel Corporation | Health Care Services | $3.40B | 11.7% margin, 30.7% ROE | 10.7% | 1.94 |
| LIVN | LivaNova PLC | Health Care Equipment | $4.39B | 12.8% margin, 15.4% ROE | 10.8% | 1.45 |
| DOCS | Doximity, Inc. | Health Care Technology | $4.45B | 25.5% margin, 17.2% ROE | 7.3% | 6.08 |
| CON | Concentra Group Holdings Parent, Inc. | Health Care Services | $4.47B | 8.7% margin, 47.1% ROE | 10.0% | 1.38 |
| ACAD | ACADIA Pharmaceuticals Inc. | Pharmaceuticals | $5.20B | 33.4% margin, 35.7% ROE | 16.4% | 3.39 |
| SHC | Sotera Health Company | Health Care Services | $5.28B | 13.4% margin, 27.8% ROE | 9.2% | 2.80 |
| TFX | Teleflex Incorporated | Health Care Equipment | $5.59B | Dev-stage (exempt) | 28.9% | 2.60 |
| LGND | Ligand Pharmaceuticals Incorporated | Biotechnology | $5.73B | 67.9% margin, 22.0% ROE | 33.7% | 31.18 |
| PTCT | PTC Therapeutics, Inc. | Pharmaceuticals | $6.06B | Dev-stage (exempt) | 101.5% | 3.39 |
| AMRX | Amneal Pharmaceuticals, Inc. | Pharmaceuticals | $6.34B | 5.0% margin, 613.0% ROE (unusually high; low equity base — needs Full QBM reconciliation, not taken at face value) | 9.9% | 2.21 |
| LQDA | Liquidia Corporation | Pharmaceuticals | $6.65B | 30.7% margin, 131.8% ROE (small equity base) | 1,842.7% (small prior-year base — see LQDA's own 14 Aug Mini QBM record for context) | 2.31 |
| TGTX | TG Therapeutics, Inc. | Biotechnology | $7.69B | 55.2% margin, 100.3% ROE | 70.3% | 4.27 |
| HQY | HealthEquity, Inc. | Managed Health Care | $8.59B | 17.3% margin, 11.1% ROE | 7.2% | 3.44 |
| BRKR | Bruker Corporation | Health Care Equipment | $8.66B | Dev-stage (exempt) | 5.2% | 1.85 |
| KRYS | Krystal Biotech, Inc. | Biotechnology | $9.85B | 54.8% margin, 20.1% ROE | 24.1% | 8.32 |

Note: LQDA and TGTX both already have a completed Mini QBM record from 14 Aug 2026 (not advanced, quality concerns disclosed there — see [QBM_US_MiniQBM_2026-08-14.md](QBM_US_MiniQBM_2026-08-14.md)); they appear here because they clear the new small/mid-cap band, not because their prior Mini QBM finding has changed.

## What happens next

This 41-company longlist (7 oncology/cancer-flagged, 34 broader Health Care) is Discovery-stage output — an input to Mini QBM, not a conclusion. No Company Quality, moat or valuation judgment has been applied. The investor's stated interest in oncology/cancer specifically points to the 7 flagged names (SDGR, XNCR, NEO, VCYT, RCUS, RDNT, LNTH) as the natural starting point for the next Mini QBM pass, though nothing prevents running the full 41.
