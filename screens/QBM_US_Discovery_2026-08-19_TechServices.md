# QBM-US Dedicated Discovery Scan — Small/Mid-Cap Electronic Technology & Technology Services — 19 August 2026

Methodology version: **1.9** — first application of the Electronic Technology / Technology Services partial Quantitative Pre-Screen exemption. See [QBM_US_Methodology.md Changelog](../framework/QBM_US_Methodology.md#changelog).

## Why this scan exists, and why it isn't a copy-paste of the Health Care scan

The investor asked to relax the screen for these sectors "like we did with biotech." The Methodology records why that request was only partly granted: clinical-stage biotech is *structurally* pre-revenue — it cannot be FCF-positive before a product is approved, regardless of underlying quality. A software or electronic-technology company at $300M+ market cap generally can choose to be FCF-positive; when one isn't, that's normally a growth-investment decision, not a structural impossibility. So this exemption drops **net margin and ROE only** — free cash flow (> $0) and liquidity (current ratio ≥ 1.0) still gate entry. This is a narrower relaxation than Health Care's, on purpose, and the difference is disclosed rather than smoothed over.

**"Not heavily impacted by AI" is operationalised as:** the GICS Information Technology sub-industries below, **excluding Semiconductors and Semiconductor Materials & Equipment** (already the primary target of the existing AI Thematic Exclusion, v1.3), with the AI Thematic Exclusion still applied at Discovery stage to individual companies regardless of sub-industry. Sector classification is a starting filter, not a substitute for checking each company.

**In-scope sub-industries:** Application Software, Systems Software, IT Consulting & Other Services, Internet Services & Infrastructure, Data Processing & Outsourced Services, Technology Hardware/Storage & Peripherals, Communications Equipment, Electronic Equipment & Instruments, Electronic Components, Electronic Manufacturing Services, Technology Distributors.

This is a **Discovery-stage scan only** — mechanical filtering and ranking, no Company Quality, moat or valuation judgment. Nothing here is a Mini QBM or Full QBM conclusion.

## Source universe

S&P 400 (MidCap) + S&P 600 (SmallCap) constituents, GICS Sector = Information Technology, fetched from Wikipedia, restricted to the in-scope sub-industries above.

| | Count |
|---|---:|
| S&P 400 + S&P 600 Information Technology constituents | 117 |
| Less: Semiconductors (17) and Semiconductor Materials & Equipment (16) | −33 |
| **In-scope universe** | **84** |

Data date: 19 August 2026. Market cap, price, volume, exchange, quote type and available financials pulled live via yfinance.

## Universe Filter (v1.4 general floor), restricted to the small/mid-cap band

| Filter | Threshold |
|---|---|
| Market cap | ≥ $300M **and** < $10B (same small/mid-cap band used for the Health Care scan, for the same reason — the general funnel already covers large/mega-cap tech, and the Thematic Exclusion has already removed most of it anyway) |
| Avg daily dollar volume | ≥ $5M |
| Share price | ≥ $5 |
| Listing | NYSE/NASDAQ primary (incl. Nasdaq Capital Market) |
| Security type | Common stock only |

| | Count |
|---|---:|
| Input | 84 |
| **Cleared** | **64** |
| Excluded | 20 |

19 of the 20 exclusions were market-cap ceiling (≥$10B — genuine mid-large tech names like Okta, Twilio, DocuSign, Dynatrace, Guidewire remain eligible for the *general* funnel, just out of scope for this small/mid-cap-focused pass by design). One (N-able) failed on price (<$5).

## Quantitative Pre-Screen (v1.9, Electronic Technology / Technology Services partial exemption)

Net margin and ROE gates do not apply. Free cash flow (> $0) and liquidity (current ratio ≥ 1.0) still apply.

| | Count |
|---|---:|
| Input | 64 |
| **Cleared** | **54** |
| Excluded (failed FCF-positive and/or current ratio ≥ 1.0) | 10 — AVT, KD, ADIG, BLKB, BOX, EXTR, MARA, PRGS, QTWO, TDC |

**The exemption's actual effect, disclosed plainly:** of the 54 survivors, **47 are profitable anyway** (positive net margin and ROE) — the exemption only changed the outcome for **6 companies** (HLIT, RAL, PI, RNG, DBX, CLSK), all FCF-positive but GAAP-unprofitable by choice (growth investment) rather than structural necessity. This confirms the Methodology's reasoning: unlike Health Care, where the exemption was doing heavy lifting (24 of 78 survivors were dev-stage), Electronic Technology / Technology Services companies at this size are mostly profitable already — this exemption is a real but modest relaxation, not a wholesale reopening of the funnel.

## AI-exposure screening (Thematic Exclusion, v1.3) applied to individual companies

One company flagged and excluded on individual review: **PATH (UiPath)** — explicitly repositioned its core product strategy around "Agentic Automation" powered by AI/LLM orchestration; this is a genuine, current, disclosed AI-infrastructure-adjacent business shift, not incidental AI use. Excluded consistent with the existing broad interpretation of the Thematic Exclusion (any company with material AI-capex/AI-product exposure, not just pure-play chips).

No other company in the 54 was judged to have material AI-infrastructure exposure on this pass — this is Discovery-stage business-description judgment (same caveat as the original ethics screen and AI exclusion: not yet run through the full Evidence Verification Standard). If any surviving name's AI exposure looks different once researched at Mini/Full QBM, that should be re-verified properly at that point, not assumed settled here.

**Eligible after both screens: 53.**

**Raw data, committed permanently:** [QBM_US_TechServices_2026-08-19_universe.csv](QBM_US_TechServices_2026-08-19_universe.csv), [QBM_US_TechServices_2026-08-19_prescreened.csv](QBM_US_TechServices_2026-08-19_prescreened.csv).

## Ranking methodology

Same two-cohort approach as the Health Care scan, for the same reason (profitability metrics aren't meaningful for the FCF-positive-but-GAAP-unprofitable cohort):

- **Profitable cohort (47 companies):** Discovery Score = average percentile rank across ROE, net margin and revenue growth.
- **FCF-positive, GAAP-unprofitable cohort (6 companies):** ranked by revenue growth alone.

Top 30 profitable + all 6 from the smaller cohort = **36-company longlist**, within the Methodology's 30-50 range.

## Longlist (36)

### Top profitable names (30)

| Rank | Ticker | Company | Sub-Industry | Market Cap | ROE | Net margin | Rev. growth |
|---:|---|---|---|---:|---:|---:|---:|
| 1 | LIF | Life360 | Application Software | $3.61B | high | high | 37.8% |
| 2 | YOU | Clear Secure | Application Software | $6.07B | high | high | 26.6% |
| 3 | APPF | AppFolio | Application Software | $7.38B | high | 15.1% | 19.3% |
| 4 | QLYS | Qualys | Systems Software | $6.47B | high | 29.4% | 11.0% |
| 5 | ADEA | Adeia | IT Consulting & Other Services | $3.06B | high | 26.1% | 12.1% |
| 6 | PEGA | Pegasystems | Application Software | $5.46B | high | 18.7% | 9.4% |
| 7 | ATEN | A10 Networks | Systems Software | $1.89B | high | 13.9% | 15.5% |
| 8 | ARLO | Arlo Technologies | Communications Equipment | $1.46B | high | 5.2% | 20.5% |
| 9 | NSSC | Napco Security Technologies | Electronic Equipment & Instruments | $1.36B | high | 18.7% | 7.6% |
| 10 | AGYS | Agilysys | Application Software | $3.22B | high | 13.0% | 14.3% |
| 11 | RAMP | LiveRamp Holdings | Application Software | $2.28B | moderate | 18.7% | 9.8% |
| 12 | CVLT | Commvault Systems | Systems Software | $5.93B | moderate | 5.6% | 11.4% |
| 13 | CXT | Crane NXT | Electronic Equipment & Instruments | $2.77B | moderate | 7.8% | 22.0% |
| 14 | BDC | Belden | Electronic Components | $5.04B | moderate | 8.5% | 11.6% |
| 15 | IDCC | InterDigital | Communications Equipment | $8.67B | moderate | 38.3% | −13.4% |
| 16 | DGII | Digi International | Communications Equipment | $3.06B | moderate | 9.6% | 29.0% |
| 17 | PLXS | Plexus Corp. | Electronic Manufacturing Services | $6.59B | moderate | 4.0% | 28.1% |
| 18 | KN | Knowles Corporation | Electronic Components | $3.05B | moderate | 10.6% | 14.3% |
| 19 | NTCT | NetScout Systems | Communications Equipment | $2.81B | moderate | 13.7% | 12.7% |
| 20 | ACIW | ACI Worldwide | Application Software | $5.33B | moderate | 12.4% | 7.3% |
| 21 | VNT | Vontier Corporation | Electronic Equipment & Instruments | $4.43B | moderate | 11.3% | −2.2% |
| 22 | CTS | CTS Corporation | Electronic Manufacturing Services | $1.71B | moderate | 12.4% | 7.0% |
| 23 | BMI | Badger Meter | Electronic Equipment & Instruments | $3.73B | moderate | 14.3% | −6.6% |
| 24 | CALX | Calix | Application Software | $2.46B | moderate | 4.6% | 21.3% |
| 25 | OSIS | OSI Systems | Electronic Equipment & Instruments | $3.65B | moderate | 8.4% | 2.0% |
| 26 | ITRI | Itron | Electronic Equipment & Instruments | $4.27B | moderate | 11.9% | −7.2% |
| 27 | DLB | Dolby Laboratories | Application Software | $5.79B | moderate | 16.7% | −3.3% |
| 28 | CNXN | PC Connection | Technology Distributors | $2.00B | moderate | 3.2% | 12.4% |
| 29 | SPSC | SPS Commerce | Application Software | $2.86B | moderate | 10.1% | 5.6% |
| 30 | FIVN | Five9 | Application Software | $2.47B | moderate | 4.9% | 10.3% |

### FCF-positive, GAAP-unprofitable (6) — where the exemption actually mattered

| Ticker | Company | Sub-Industry | Market Cap | Rev. growth | Why GAAP-unprofitable |
|---|---|---|---:|---:|---|
| HLIT | Harmonic Inc. | Communications Equipment | $1.39B | +53.5% | Fastest revenue growth in the entire longlist; video/broadband infrastructure equipment maker scaling hard |
| RAL | Ralliant Corporation | Electronic Equipment & Instruments | $7.65B | +12.8% | Recent spin-off (from Fortive) — spin-off transition costs are a common, temporary source of GAAP losses, not a quality signal either way |
| PI | Impinj, Inc. | Electronic Equipment & Instruments | $5.16B | +10.7% | RFID chip/reader maker; investing through a growth phase |
| RNG | RingCentral, Inc. | Application Software | $5.54B | +5.9% | Cloud communications platform; stock-based-comp-heavy cost structure is a common driver of GAAP losses in scaled SaaS despite real FCF |
| DBX | Dropbox, Inc. | Application Software | $7.49B | +0.9% | Mature, FCF-generative business; GAAP profitability distorted by historical items, worth checking directly at Mini QBM rather than assumed from this pass |
| CLSK | CleanSpark, Inc. | Internet Services & Infrastructure | $2.93B | −30.5% | Bitcoin mining — **flag for Mini QBM:** this is a fundamentally different business model (crypto-mining economics, not enterprise tech), swept in by GICS classification rather than genuine sector fit; worth a specific Eligibility check before treating as a normal candidate |

## Known limitations, disclosed

- **The AI-exposure screen on this pass is Discovery-stage business-description judgment**, not the full Evidence Verification Standard — only PATH was excluded; if Mini/Full QBM research on any surviving name surfaces a different picture (e.g. a company pivoting toward AI-infrastructure supply chains that wasn't obvious from a sector-level read), that should be re-verified and could result in exclusion at that later stage.
- **CLSK (CleanSpark)** is a crypto-mining company that cleared the mechanical filters only because of its GICS classification — flagged explicitly rather than silently treated as a normal Electronic Technology candidate.
- **RAL (Ralliant)** is a very recent spin-off; its GAAP-unprofitability likely reflects one-time separation costs rather than an ongoing characteristic — worth confirming directly rather than assuming either way.
- As with the Health Care scan, this pass covers the S&P 1500 constituent universe only — genuinely small, recently-IPO'd, or index-ineligible Electronic Technology/Tech Services companies below this scan's radar are not claimed to be covered.

## What happens next

This 36-company longlist is Discovery-stage output — an input to Mini QBM, not a conclusion. No Company Quality, moat or valuation judgment has been applied. The investor's stated interest (non-AI Electronic Technology and Technology Services) points to this whole longlist as the starting point; nothing in it stands out yet as more or less oncology-flagged the way the Health Care scan had a clear sub-theme — it's a broader, more heterogeneous sector than biotech.
