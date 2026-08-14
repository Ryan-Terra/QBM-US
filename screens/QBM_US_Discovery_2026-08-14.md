# QBM-US Discovery Scan — 14 August 2026

Methodology version: **1.2** — first Discovery-stage pass, per [QBM_US_Methodology.md](../framework/QBM_US_Methodology.md)

This is a Discovery-stage scan: preliminary Eligibility filters applied to produce a ranked longlist, without full reports on every candidate (per Methodology). It is not Mini QBM or Full QBM — no individual company has been deeply researched yet, except the 16 ethics-flagged names below.

## Funnel so far

| Stage | Count | Reference |
|---|---:|---|
| S&P 1500 source universe | 1,506 | [QBM_US_Universe_Filter_2026-08-13.md](QBM_US_Universe_Filter_2026-08-13.md) |
| Cleared Universe Filter (v1.1) | 1,313 | same |
| Cleared Quantitative Pre-Screen (v1.2) | 454 | same |
| **Cleared ethical exclusion (this scan)** | **448** | this report |
| **Discovery longlist (ranked, top 40)** | **40** | this report |

## Ethical exclusion — weapons manufacturing / gambling / tobacco

Sub-industry data (GICS) flagged 16 of the 454 for individual review — sub-industry alone isn't precise enough to exclude on (the same lesson QBM learned from over-broadly excluding Codan on "defence" grounds). Each of the 16 was individually assessed on whether weapons manufacturing (or gambling) is genuinely the *principal* activity, not just an adjacent exposure:

**Excluded (6):**

| Ticker | Company | Reason |
|---|---|---|
| LMT | Lockheed Martin | Weapons manufacturing — fighter jets, missiles, combat systems are the defining business |
| NOC | Northrop Grumman | Weapons manufacturing — bombers, missiles |
| RTX | RTX Corporation | Weapons manufacturing — missiles, missile defense |
| MGM | MGM Resorts | Gambling — casino operator |
| MCRI | Monarch Casino & Resort | Gambling — casino operator |
| RSI | Rush Street Interactive | Gambling — sports betting/casino operator |

**Flagged but not excluded (10)** — defense-adjacent, but weapons manufacturing is not the principal activity:

| Ticker | Company | Reason |
|---|---|---|
| GD | General Dynamics | Combat Systems (tanks) is one of four segments; Gulfstream/Marine/Technologies are the majority |
| BA | Boeing | Boeing Defense includes weapons systems; Boeing Commercial Airplanes is the larger part of the business |
| TXT | Textron | Bell military/Textron Systems exist; general aviation (Cessna) and industrial products are the majority |
| HWM | Howmet Aerospace | Aerospace/defense materials supplier, not a weapons manufacturer |
| ATI | ATI Inc. | Aerospace/defense materials supplier, not a weapons manufacturer |
| CW | Curtiss-Wright | Aerospace/defense components supplier, not a weapons manufacturer |
| HXL | Hexcel | Aerospace/defense composites supplier, not a weapons manufacturer |
| MOG-A | Moog Inc. | Aerospace/defense actuation components supplier, not a weapons manufacturer |
| BWXT | BWX Technologies | Naval nuclear propulsion components, not a weapons manufacturer |
| SARO | StandardAero | Aircraft MRO services, not a weapons manufacturer |

**Caveat, disclosed rather than hidden:** this is Discovery-stage judgment based on well-established knowledge of these companies' business mix, not the full Evidence Verification Standard search pass. If any of the 10 flagged-but-eligible names advance to Full QBM, their defense-segment revenue share should be verified properly at that point, not assumed from this pass.

Full detail: [QBM_US_Discovery_2026-08-14_ethics_screened.csv](QBM_US_Discovery_2026-08-14_ethics_screened.csv) (all 454, with ethics_status and ethics_note columns).

## Discovery ranking methodology

448 eligible companies ranked by a composite **Discovery Score** = average of percentile rank across three metrics already gathered at the Quantitative Pre-Screen stage:

- Return on equity (capital-allocation proxy)
- Net profit margin (cash-generation-quality proxy)
- Revenue growth, year-over-year (not-shrinking proxy)

This directly operationalizes three of QBM's own Investment Principles (excellent capital allocation, strong cash generation, durability) as a ranking, not a pass/fail gate — nothing here is Investment Attractiveness or valuation, which are Mini/Full QBM questions, not Discovery ones.

Full ranked list of all 448: [QBM_US_Discovery_2026-08-14_ranked_448.csv](QBM_US_Discovery_2026-08-14_ranked_448.csv).

## Discovery longlist (top 40)

Within the Methodology's specified 30–50 range. Full list: [QBM_US_Discovery_2026-08-14_longlist_40.csv](QBM_US_Discovery_2026-08-14_longlist_40.csv).

| Rank | Ticker | Company | Sector | ROE | Net margin | Rev. growth |
|---:|---|---|---|---:|---:|---:|
| 1 | NVDA | Nvidia | Information Technology | 114% | 63% | 85% |
| 2 | SNDK | Sandisk | Information Technology | 92% | 56% | 372% |
| 3 | APP | AppLovin | Communication Services | 204% | 65% | 53% |
| 4 | TGTX | TG Therapeutics | Health Care | 100% | 55% | 70% |
| 5 | MU | Micron Technology | Information Technology | 67% | 56% | 346% |
| 6 | LQDA | Liquidia Corporation | Health Care | 132% | 31% | 1843% |
| 7 | WDC | Western Digital | Information Technology | 131% | 73% | 44% |
| 8 | LLY | Eli Lilly | Health Care | 102% | 34% | 48% |
| 9 | INSW | International Seaways | Energy | 37% | 62% | 140% |
| 10 | SEZL | Sezzle | Financials | 89% | 30% | 52% |
| 11 | STX | Seagate Technology | Information Technology | 372% | 26% | 49% |
| 12 | PLTR | Palantir Technologies | Information Technology | 38% | 49% | 93% |
| 13 | HALO | Halozyme | Health Care | 174% | 25% | 48% |
| 14 | DAVE | Dave, Inc. | Financials | 105% | 35% | 30% |
| 15 | LRCX | Lam Research | Information Technology | 65% | 31% | 30% |
| 16 | AVGO | Broadcom | Information Technology | 37% | 39% | 48% |
| 17 | GOOGL | Alphabet (Class A) | Communication Services | 49% | 55% | 24% |
| 18 | GOOG | Alphabet (Class C) | Communication Services | 49% | 55% | 24% |
| 19 | FTNT | Fortinet | Information Technology | 117% | 28% | 26% |
| 20 | TER | Teradyne | Information Technology | 36% | 26% | 104% |
| 21 | HLNE | Hamilton Lane | Financials | 32% | 32% | 57% |
| 22 | ANET | Arista Networks | Information Technology | 31% | 38% | 38% |
| 23 | MA | Mastercard | Financials | 241% | 46% | 14% |
| 24 | KLAC | KLA Corporation | Information Technology | 87% | 36% | 15% |
| 25 | AAPL | Apple Inc. | Information Technology | 149% | 28% | 16% |
| 26 | AAMI | Acadian Asset Management | Financials | 107% | 15% | 45% |
| 27 | MCO | Moody's Corporation | Financials | 77% | 34% | 15% |
| 28 | APH | Amphenol | Information Technology | 38% | 18% | 55% |
| 29 | INCY | Incyte | Health Care | 31% | 28% | 38% |
| 30 | TXN | Texas Instruments | Information Technology | 35% | 31% | 23% |
| 31 | LIF | Life360 | Information Technology | 30% | 26% | 38% |
| 32 | DUOL | Duolingo | Consumer Discretionary | 34% | 36% | 18% |
| 33 | ADMA | ADMA Biologics | Health Care | 42% | 33% | 16% |
| 34 | META | Meta Platforms | Communication Services | 30% | 30% | 28% |
| 35 | LGND | Ligand Pharmaceuticals | Health Care | 22% | 68% | 34% |
| 36 | MSFT | Microsoft | Information Technology | 34% | 40% | 18% |
| 37 | YOU | Clear Secure | Information Technology | 119% | 15% | 27% |
| 38 | EOG | EOG Resources | Energy | 23% | 26% | 59% |
| 39 | AMG | Affiliated Managers Group | Financials | 24% | 38% | 30% |
| 40 | AGX | Argan, Inc. | Industrials | 39% | 15% | 50% |

## Known limitation, disclosed

**Sector concentration:** 18 of the 40 longlist names (45%) are Information Technology. A purely quantitative ranking on ROE/margin/growth mechanically favors high-margin tech and pharma businesses — this is a real property of the ranking, not a bug, but it means genuinely good businesses in lower-margin sectors (industrials, consumer staples, utilities) are systematically under-represented in this longlist. Worth keeping in mind before treating this 40 as a complete picture of opportunity — QBM's own Investment Principles don't require any sector diversification at Discovery stage, but Portfolio Fit at Mini/Full QBM will need to consider it.

## What happens next

This longlist of 40 is the input to Mini QBM — the next stage requires real, evidence-based research per company (Eligibility, preliminary Company Quality, Investment Attractiveness, Portfolio Fit), not mechanical ranking. Nothing here constitutes a Mini QBM or Full QBM conclusion, and no Investment Decision has been made on any of these 40 companies.
