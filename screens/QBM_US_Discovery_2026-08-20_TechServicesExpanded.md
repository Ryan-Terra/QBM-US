# QBM-US Discovery Scan Revisit — Small/Mid-Cap Electronic Technology & Technology Services, Expanded Depth — 20 August 2026

Methodology version: **1.9**, first application of the new **1.5x longlist depth rule**. This document does not change or replace [QBM_US_Discovery_2026-08-19_TechServices.md](QBM_US_Discovery_2026-08-19_TechServices.md) — the original 36-company longlist stands exactly as published. This is an *additive* pass: same source universe, same Universe Filter, same Quantitative Pre-Screen, same composite ranking, carried one tier deeper.

## Why this document exists

The investor approved a new standing rule: when a Discovery scan is revisited, widen the longlist depth to 1.5x its original size — the next-ranked tier by the same composite ranking — rather than treating the original cutoff as permanent. The stated purpose is to catch genuine candidates that a rough quantitative ranking placed just outside the original cutoff, not to re-run the scan with different criteria.

Original longlist size: 36. 1.5x depth: 54. This document identifies and ranks the companies that would occupy that next tier — approximately positions 37 through 54 of the original ranking.

**This is a Discovery-only pass.** No Mini QBM or Full QBM work has been done on any name below. That is a separate, later step pending investor review, exactly as the original scan's output was.

## Source universe — unchanged from 19 August

Same S&P 400 (MidCap) + S&P 600 (SmallCap) constituents, GICS Sector = Information Technology, restricted to the same in-scope sub-industries, excluding Semiconductors and Semiconductor Materials & Equipment. This is a static, index-membership-based universe (84 companies) — it was not re-fetched, since index constituent lists do not change day to day and re-fetching would risk introducing an inconsistency with the already-published 19 Aug universe rather than a genuine update. See the original scan for full sourcing detail: [QBM_US_TechServices_2026-08-19_universe.csv](QBM_US_TechServices_2026-08-19_universe.csv).

## Universe Filter and Quantitative Pre-Screen — same criteria, re-confirmed against fresh data

The 19 Aug scan already carried 64 companies through the Universe Filter and 54 through the Quantitative Pre-Screen (net margin/ROE gates dropped for this sub-industry set; free cash flow > $0 and current ratio ≥ 1.0 still applied) — see [QBM_US_TechServices_2026-08-19_prescreened.csv](QBM_US_TechServices_2026-08-19_prescreened.csv). Rather than re-run the full 84-company funnel (which would risk reshuffling the already-published top-36 against a different data snapshot and breaking the "next tier below the existing cutoff" premise the investor asked for), this pass:

1. Takes the fixed set of 54 companies that cleared both filters on 19 Aug.
2. Subtracts the 36 already on the published longlist.
3. **Result: exactly 18 companies remain** — BHE, BILL, BL, CRSR, CXM, DBD, DXC, EFOR, EPAM, IPGP, MIR, NOVT, PATH, PLUS, ROG, SCSC, VSH, VYX.
4. Re-pulled live via yfinance on 20 August 2026 to confirm market cap, price, and average dollar volume still clear the Universe Filter thresholds (≥$300M and <$10B market cap, ≥$5 price, ≥$5M avg dollar volume) as of today, not just as of 19 Aug. **All 18 still clear.** Fundamental ratios (ROE, net margin, revenue growth, current ratio, free cash flow) are unchanged from the 19 Aug pull, as expected — these come from the same most-recently-reported quarter and would not differ regardless of which day they were pulled.

| | Count |
|---|---:|
| Cleared Universe Filter + Quantitative Pre-Screen (19 Aug, unchanged) | 54 |
| Less: already on published 36-company longlist | −36 |
| **Next-tier candidates (this pass)** | **18** |
| Re-confirmed against fresh 20 Aug market data (price, market cap, volume) | 18 of 18 |

One data-quality note: **EFOR** returned a blank company name from yfinance (`info.get('longName')` is `None`) on both the 19 Aug and 20 Aug pulls. Web search confirms this is a real, currently-listed NYSE ticker: **Everforth, Inc.**, formerly ASGN Incorporated (IT staffing/consulting — Apex Systems, ECS Federal), which appears to have renamed recently enough that yfinance's cached profile field hasn't caught up. Financial figures pulled for EFOR are populated and plausible (FY2025 revenue ~$4.0B against the ~$1.3B market cap here is consistent with a low-margin staffing business), so it is retained, but this is flagged as exactly the kind of "stale API metadata" issue this project's standards ask to disclose rather than paper over.

## Ranking methodology — same composite, extended one tier

Same two-cohort approach as the original scan. The Quantitative Pre-Screen's 54 survivors split into 48 GAAP-profitable companies and 6 FCF-positive-but-GAAP-unprofitable companies (HLIT, RAL, PI, RNG, DBX, CLSK — all 6 already fully absorbed into the original 36-company longlist, so this cohort has no further tier to surface). The profitable cohort is ranked by Discovery Score = average percentile rank across ROE, net margin, and revenue growth.

To preserve exact consistency with the already-published top-36, the ranking was reconstructed on the **same 47-company population the original scan actually ranked** (48 profitable companies minus PATH, which the original document excluded via the AI Thematic Exclusion *before* the Ranking Methodology step). Re-running the percentile computation on this 47-company set reproduces the original top-30 profitable names **exactly** (verified programmatically — zero difference). The next 17 companies by this same ranking (positions 31–47 of the profitable cohort) are the organic "next tier" — continuing the original document's implicit numbering (1–30 profitable + 31–36 the six-company unprofitable cohort), these land at **overall positions 37–53**.

**PATH (UiPath) does not organically belong in this 37–53 band.** Re-inserting it into the ranking population to see where it would fall: its Discovery Score (ROE 18.2%, net margin 19.6%, revenue growth 17.3% — all strong) places it at **rank 6 of 48** — comfortably inside what would have been the original top-36 on quantitative merit alone. Its absence from the original longlist was purely a Thematic Exclusion outcome, not a quantitative one. Per the task's explicit instruction to mirror the original PATH exclusion, it is revisited and re-flagged below rather than silently omitted — bringing the total names examined in this pass to 18, even though only 17 are a genuine "next rank tier" in the strict quantitative sense.

## Next-tier candidates (17, ranks 37–53) + PATH revisited

| Rank | Ticker | Company | Sub-Industry | Market Cap (20 Aug) | ROE | Net margin | Rev. growth | AI/crypto screen |
|---:|---|---|---|---:|---:|---:|---:|---|
| 37 | EPAM | EPAM Systems | IT Consulting & Other Services | $5.54B | 11.2% | 7.2% | 4.5% | **EXCLUDED — AI-infrastructure** |
| 38 | NOVT | Novanta Inc. | Electronic Equipment & Instruments | $5.52B | 5.1% | 6.0% | 10.3% | Eligible |
| 39 | PLUS | ePlus inc. | Technology Distributors | $2.26B | 11.7% | 4.9% | 1.0% | **EXCLUDED — AI-infrastructure** |
| 40 | BL | BlackLine, Inc. | Application Software | $1.83B | 7.0% | 4.7% | 9.2% | Eligible |
| 41 | MIR | Mirion Technologies | Electronic Equipment & Instruments | $3.88B | 1.5% | 2.4% | 19.7% | Eligible |
| 42 | BHE | Benchmark Electronics | Electronic Manufacturing Services | $2.64B | 4.8% | 1.9% | 17.7% | Eligible, flagged for context |
| 43 | DBD | Diebold Nixdorf | Electronic Equipment & Instruments | $2.29B | 10.9% | 2.9% | 1.7% | Eligible |
| 44 | SCSC | ScanSource, Inc. | Technology Distributors | $1.05B | 8.1% | 2.4% | 8.8% | Eligible |
| 45 | VSH | Vishay Intertechnology | Electronic Components | $4.90B | 1.1% | 0.9% | 16.6% | Eligible |
| 46 | IPGP | IPG Photonics | Electronic Manufacturing Services | $3.25B | 1.3% | 2.6% | 11.1% | Eligible, flagged for context |
| 47 | CXM | Sprinklr, Inc. | Application Software | $1.67B | 5.1% | 3.3% | 6.8% | Eligible |
| 48 | BILL | BILL Holdings | Application Software | $4.75B | 0.0% | 0.0% | 13.5% | Eligible |
| 49 | ROG | Rogers Corporation | Electronic Components | $2.31B | 2.6% | 3.7% | 6.9% | Eligible |
| 50 | CRSR | Corsair Gaming | Technology Hardware, Storage & Peripherals | $1.23B | 5.8% | 2.5% | −1.8% | Eligible |
| 51 | VYX | NCR Voyix | IT Consulting & Other Services | $1.05B | 5.3% | 3.0% | −20.8% | Eligible |
| 52 | EFOR | Everforth, Inc. (fka ASGN Inc.) | IT Consulting & Other Services | $1.31B | 4.6% | 2.1% | −1.3% | Eligible, data-quality flag (see above) |
| 53 | DXC | DXC Technology | IT Consulting & Other Services | $1.73B | 4.0% | 1.0% | −5.1% | Eligible, flagged for context |
| — | **PATH** | **UiPath, Inc.** | Systems Software | $8.18B | 18.2% | 19.6% | 17.3% | **RE-EXCLUDED — AI-infrastructure (mirrors original)** |

**Eligible after this pass: 15** (17 ranked minus EPAM and PLUS; PATH separately re-affirmed excluded, not counted toward the 17).

## AI-exposure and crypto screening (Thematic Exclusion) applied to this tier

Two new exclusions found, at the same Discovery-stage depth (business-description-level judgment, current public disclosures — not the full Evidence Verification Standard, and not the deeper quarterly-earnings-call-level research that later caught ATEN/ADEA at Mini QBM):

- **EPAM (EPAM Systems)** — the company's own current strategy is explicitly built around "AI-native enterprise transformation": a dedicated go-to-market motion (AI/RUN), a stated $600M AI-native revenue target for 2026 growing roughly 10x faster than overall reported revenue, and management commentary framing the whole business around operating "in the AI era." This is a genuine, current, disclosed core-strategy shift toward AI, not incidental use — same standard that excluded PATH originally.
- **PLUS (ePlus inc.)** — launched a "Private AI Infrastructure Managed Service" in May 2026 built on NVIDIA-accelerated computing clusters, and describes recent growth as driven by "AI-linked... data center wins" across multiple verticals including Neocloud. This is direct AI-infrastructure resale/integration exposure, not a peripheral product line.
- **PATH (UiPath)** — re-affirmed excluded, consistent with the original scan's finding (Agentic Automation / AI-orchestration repositioning). Included here per the task instruction to explicitly revisit and mirror this exclusion in the expanded pass, not because it organically ranks in this tier (see note above — it would rank 6th on quantitative merit).

**Three names reviewed and explicitly kept eligible, flagged for context rather than excluded** (to show this wasn't an automatic keyword trigger, mirroring how the original Mini QBM distinguished CALX/FIVN's "AI-as-feature" language from ATEN/ADEA's AI-infrastructure dependency):

- **BHE (Benchmark Electronics)** — recent commentary attributes part of its raised outlook to "AI and semi-cap demand," but this is contract-manufacturing exposure to AI-adjacent *customers* (the same supply-chain relationship several already-longlisted EMS names — PLXS, FN, TTMI — have without being excluded), not a company-level strategic pivot to AI.
- **IPGP (IPG Photonics)** — some coverage describes its laser/photonics expertise "quietly finding its way into next-generation datacenter photonics roadmaps," but its reported Q1 2026 growth is attributed primarily to industrial/EV-battery applications; the AI-datacenter angle reads as forward-looking and not yet a material, disclosed current revenue driver. Worth re-checking if this name ever advances further.
- **DXC (DXC Technology)** — heavy AI messaging (an AI-enabled service-delivery platform, an "agent-based operations" cost-reduction push), but this is AI used internally to cut DXC's own delivery costs and modestly offset core-business decline (organic revenue guidance is still −3% to −5%), not a business whose revenue/earnings depend on selling AI infrastructure. Different in kind from EPAM and PLUS above.

No crypto exposure (mining, exchanges, brokerages, treasury holdings) was found in any of the 18 names in this tier.

## Known limitations, disclosed

- **This pass reuses the 19 August 2026 fundamentals** (ROE, net margin, revenue growth, current ratio, free cash flow) rather than re-pulling them, specifically so the ranking is computed against the exact same numbers that produced the already-published top-36 — a fresh full re-pull risked reshuffling the original longlist itself, which would have broken the "next tier below the existing cutoff" premise. Only price, market cap, and volume were refreshed live for 20 August, and used solely to re-confirm the Universe Filter still holds — the underlying fundamentals were not stale in any way that would move the ranking (quarterly-reported figures do not change day to day).
- **EFOR (Everforth, Inc.)** returned no company name from the yfinance API on either pull date — confirmed as real via independent web search rather than assumed. Flagged rather than silently accepted.
- **The AI-exposure screen here is Discovery-stage business-description judgment**, the same depth and same caveat as the original scan — not the full Evidence Verification Standard, and shallower than the quarterly-earnings-level research that caught ATEN and ADEA at the Mini QBM stage in this same project. If any of the 15 eligible names here ever advances to Mini/Full QBM, its AI exposure should be re-verified properly at that point, not assumed settled by this pass.
- As with the original scan, this covers the S&P 1500 constituent universe only.

## What happens next

This produces 15 additional Discovery-eligible names (17 ranked minus EPAM and PLUS), plus a re-affirmed exclusion for PATH. **No Mini QBM or Full QBM work has been performed on any of them.** Whether and how to fold this expanded tier into the existing Mini QBM / Full QBM pipeline (which has already run on the original 36) is a decision for investor review, not something this Discovery-stage pass presumes.

**Raw data:** [QBM_US_TechServices_2026-08-20_expanded_longlist.csv](QBM_US_TechServices_2026-08-20_expanded_longlist.csv) — the 17 ranked next-tier companies plus computed Discovery Scores and AI/crypto screening notes. (PATH's re-flag detail is documented in this file's prose rather than a separate row in that CSV, since it isn't part of the organic 37–53 ranked set — its figures are already fully disclosed in the original scan's [QBM_US_TechServices_2026-08-19_prescreened.csv](QBM_US_TechServices_2026-08-19_prescreened.csv).)
