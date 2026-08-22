# QBM-US Dashboard

Assessment evidence current through: 21 August 2026 Full QBM (Tech Services depth-widening tier) + 8-holding Portfolio Concentration expansion  
Current macro evidence through: 14 August 2026 (CMEA-US-2026-08-14-001)  
Methodology updated: 22 August 2026 (v1.22 — Primary Price Data Source requirement, after a systematic re-check found four bench companies' Implementation Readiness was wrong due to inconsistent web-search-sourced price data)  
Investment Charter updated: 20 August 2026 (v1.6 — ATH Proximity Rule + Valuation Ceiling; Portfolio Concentration expanded to 8 holdings 21 Aug under the existing v1.3 rule)  
Full-system synchronisation confirmed: 21 August 2026 — this reconciliation pass  

**Systematic price data re-verification (22 Aug 2026, Methodology v1.22).** Investor spot-checked one bench name (VCYT) after noticing its price had shown a $17 spread across different web searches on different days, then asked directly whether every company should get the same check. It should have, and now has — every ATH-proximity figure for all 24 then-standing Add/bench companies was re-pulled from a single reproducible source (`yfinance`) rather than general web search. **Found four genuine Implementation Readiness errors, not just imprecision:** DGII (was wrongly recorded as trading *above* its 52-week high — actually 13.7% below, clears), KN (was "fails at ~3% below" — actually 22.4% below, clears), CTS (was "fails at ~4-6% below" — actually 16.9% below, clears), and NTCT (was "fails at 7.1% below" — actually 15.0% below, clears; **now the second fully clean bench candidate alongside BDC**). One reversal the other way: KRYS was believed to clear the ATH rule (15.8% below) but actually fails it (9.4% below) — its bench placement is unaffected since that was never the reason it was benched. No target-portfolio holding's readiness changed, and no funded capital was affected (all four upgraded names were unfunded bench candidates). Full detail: [screens/QBM_US_PriceDataReverification_2026-08-22.md](../screens/QBM_US_PriceDataReverification_2026-08-22.md). Going forward, all mechanical price checks (ATH Proximity Rule, Valuation Ceiling, momentum figures) must use this same reproducible-source standard — see [Methodology v1.22](../framework/QBM_US_Methodology.md#primary-price-data-source-added-v122).

**Target Holding Period amendment (19 Aug 2026):** Charter now targets 6-18 months per position, not indefinite hold — see [Investment Charter](../framework/QBM_US_Investment_Charter.md#target-holding-period). LLY and MA re-examined: both remain **Add** ([detail](../screens/QBM_US_Review_2026-08-19_LLY_MA_TargetHorizon.md)) — LLY's litigation risk found to have grown (new NAION MDL, new Texas AG complaint), confidence lowered to Medium; MA's case strengthened with two dated near-term catalysts identified (BVNK close, swipe-fee settlement court progress).

**Full QBM completed on the 11-company small/mid-cap Health Care queue (19 Aug 2026)** — [full record](../screens/QBM_US_FullQBM_2026-08-19_SmallMidHealthCare.md). **8 Add: VCYT, NEO, PTCT, XNCR, ACAD, HRMY, KRYS, HQY. 3 Continue Monitoring: LGND, CON, INVA** (all three cleared Mini QBM/horizon review but were pulled back by Full QBM's dedicated verification pass — LGND on valuation, CON on a newly-found data breach plus open CA DOI investigation and thin valuation margin, INVA on a genuine bull/bear analyst split). The verification pass also surfaced a confirmed data breach at HQY (4.3M records, active class action) — HQY's Add was retained but downgraded to Tier 3 with a reduced allocation range given this. QBM-US now has **10 standing Add recommendations** (LLY, MA + 8 new), still 100% cash pending investor-specified deployable capital.

**Portfolio Concentration instruction (19 Aug 2026, Charter v1.3)** — [full construction](../screens/QBM_US_ConcentratedPortfolio_2026-08-19.md). Investor overrode the market-cap-tier position-sizing framework from earlier the same day with a direct instruction: 5-8 holdings, no position below 10%, sized in 10/15/20% tiers — "go hard or go home." This required selecting which of the 10 standing Adds actually get a slot, since Add no longer implies a funded position at this size. Result: **MA 20%, LLY/VCYT/PTCT/XNCR 15% each, ACAD 10% — 6 holdings, 100% invested.** NEO, HRMY, KRYS and HQY remain Add-rated but sit on the bench. XNCR and ACAD (25% combined) each carry a disclosed binary near-term catalyst. Sector concentration sharpened, not reduced: 5 of 6 holdings (85%) are Health Care/pharma-biotech.

**Electronic Technology / Technology Services scan added and Mini QBM completed (19-20 Aug 2026, Methodology v1.9)** — [Discovery](../screens/QBM_US_Discovery_2026-08-19_TechServices.md), [Mini QBM](../screens/QBM_US_MiniQBM_2026-08-19_TechServices.md). Investor asked to relax the screen for these sectors "like we did with biotech." Only partly granted: net margin/ROE gates dropped, but FCF-positive and liquidity gates kept — unlike biotech, most tech companies at this size are profitable by choice, not structurally barred from it (only 6 of 54 pre-screen survivors actually needed the exemption). Discovery produced a 36-company longlist; Mini QBM then found **two more AI-infrastructure-exposed names Discovery's sector-level screen missed** — CleanSpark (CLSK, an explicit pivot to AI/HPC data-center buildout) and A10 Networks (ATEN, growth explicitly tied to AI-driven network demand) — plus Adeia (ADEA, long-term guidance tied to AI-chip hybrid-bonding IP). **15 of the remaining 33 Advance to Full QBM**: ARLO, AGYS, CVLT, BDC, DGII, PLXS, KN, NTCT, ACIW, CTS, DLB, CNXN, HLIT, RAL, PI.

**Entry-Point Discipline added (19 Aug 2026, Charter v1.2, folded into v1.3 same day) — CORRECTED 20 August 2026.** [Full review](../screens/QBM_US_EntryPointReview_2026-08-19.md). Investor asked that QBM-US find quality before it breaks out, not after. Checking each of the 10 Adds against its own 52-week range and trailing return found **8 have already run hard and sit near their 52-week highs: LLY +61%/1yr, NEO +170%/1yr, XNCR +178.71%/1yr (within 1% of its 52-week high), ACAD/HRMY at/near their highs, KRYS/HQY/VCYT substantially elevated** — all moved to **Await Better Entry**. **Correction, 20 Aug 2026:** XNCR was originally recorded as "Ready" based on an incorrect −18.3%/yr figure — an analysis error, not new information (the underlying data conflict was noted at the time and not resolved before publishing). Re-verified: XNCR is one of the most extended names in the portfolio, not one of the least. **Only MA is genuinely "before the move"** and remains Ready; PTCT is Ready with Considerations. Investment Decision (Add) is unchanged for all 10 — this affects Implementation Readiness only.

**Crypto Exposure Thematic Exclusion added (19-20 Aug 2026, Methodology v1.10)** — investor stated directly: not interested in any crypto-related stocks. Applied broadly, matching the AI exclusion's structure (miners/mining infrastructure, exchanges/brokerages, material treasury holdings), at Discovery stage going forward. Not a permanent ethical exclusion — a revisable risk-view preference. Applied retroactively to CLSK (CleanSpark), already excluded on AI-infrastructure grounds — crypto exposure is now a second, independent reason. **Full QBM on the 15 Tech Services Advance names is deliberately on hold — investor asked to wait until directed.**

**Full QBM run on the 15 Tech Services names (20 Aug 2026) — final result after four update passes: 11 of 15 Add.** [Full record](../screens/QBM_US_FullQBM_2026-08-20_TechServices.md). Insider Ownership & Net Buying Screen went through three iterations: net buying required (v1.13, 0/15) → "no material net selling" as a hard gate (v1.14, 2/15) → **net selling demoted to a disclosed factor moving Decision Confidence/Priority Tier, ownership kept as the only hard gate (v1.15)**. The six-name ownership data gap (KN, DLB, CNXN, DGII, PI, ARLO) was then closed: **DLB (~35% via the Dolby family's Class B stake), CNXN (Gallup alone owns 10%+), DGII (2.6-5.78%) and PI (2.5%) all clear the ownership gate and now Advance.** A fourth update (20 Aug, Methodology v1.16) then added a near-miss provision to the ownership gate itself (≥80% of the tier threshold passes, disclosed and discounted) — **KN (1.7%), ARLO (4.03%) and PLXS (1.78%) all now clear it too.** Final 11 Adds: **BDC (Ready, no discount — the cleanest of the eleven), CNXN/DLB/ARLO/PI/AGYS (Ready with Considerations), NTCT/DGII/KN (Await Better Entry — all three fail the ATH rule), CTS (Await Better Entry, Medium-Low confidence).** None has a target-portfolio slot — all 11 join the bench (15 total, with NEO, HRMY, KRYS, HQY). Only 4 remain Not Advanced: ACIW and HLIT (confirmed-failing ownership even under the near-miss band), and RAL/CVLT (independent securities-litigation findings).

**Four new methodology rules built 20 Aug 2026, on investor request for both relax- and raise-the-bar recommendations.** Relax: (1) the Insider Ownership near-miss provision above (Methodology v1.16, applied and complete — see the Fourth update in the Full QBM record); (2) a Discovery longlist depth-widening rule — 1.5x the original cutoff on revisit (v1.17), first applied to Tech Services (36→54 candidates): 15 new eligible names found at Discovery stage (NOVT, BL, MIR, BHE, DBD, SCSC, VSH, IPGP, CXM, BILL, ROG, CRSR, VYX, EFOR, DXC — ranks 37-53), 2 more excluded on AI-infrastructure grounds (EPAM, PLUS), and PATH's original AI-exposure exclusion re-affirmed (it would otherwise rank 6th on quantitative merit alone). Full detail: [screens/QBM_US_Discovery_2026-08-20_TechServicesExpanded.md](../screens/QBM_US_Discovery_2026-08-20_TechServicesExpanded.md).

**Mini QBM then run on all 15 (20 Aug 2026)** — [full record](../screens/QBM_US_MiniQBM_2026-08-20_TechServicesExpanded.md). Company-level research caught one more AI-infrastructure exclusion the Discovery screen missed — **NOVT**, with 17% of revenue (growing 25%) disclosed by management as AI-datacenter-tied — stronger evidence than either of the original ATEN/ADEA exclusions had. **3 of the remaining 14 Advance to Full QBM: BHE, SCSC, ROG.** 11 Continue Monitoring, 0 Not Advanced. This was also the first live use of the new Mini QBM Red-Flag Adverse-Event Scan (v1.18) — it directly drove 5 of the 11 Continue Monitoring calls (DBD, VSH, IPGP, EFOR, DXC), each on a confirmed large single-day price drop and/or an active shareholder/securities investigation surfaced by the dedicated scan step. The rule worked exactly as designed on real evidence in its first application.

**Full QBM completed 21 Aug 2026 on BHE, SCSC, ROG** — [full record](../screens/QBM_US_FullQBM_2026-08-21_TechServicesExpanded.md). All three Add. **BHE and ROG both Ready** — clean insider-ownership, insider-selling, ATH, and Valuation Ceiling pictures across the board (ROG's CEO notably chose not to sell beyond mandatory tax withholding). **SCSC is Add but Await Better Entry — the new Valuation Ceiling's first real Implementation Readiness consequence.** It clears the ATH Proximity Rule (pulled back to 14.4% below a 52-week high set the day before) and carries a near-miss ownership pass (4.20% vs. 5%) plus material insider selling ($10.59M/12mo, zero buying), but fails the Valuation Ceiling against the only analyst target found (+24% above, though that target is thin — 1-2 analysts — and possibly stale, disclosed explicitly rather than quietly waived).

**Two more methodology rules built 21 Aug 2026, on investor request for further relax/raise-the-bar recommendations.** Relax: **Insider Buying** (Methodology v1.20) — genuine net insider buying now raises Decision Confidence/Priority, the symmetric counterpart to how net selling has been treated since v1.15. A retroactive check of already-gathered transaction data (no new research) found exactly one genuine buy among the 24 standing Adds: **KN's ~$423K purchase**, disclosed as a partial offset to its much larger ~$9M in selling — doesn't change KN's Confidence rating, but is now named explicitly rather than left invisible. Raise the bar: **Evidence Staleness Re-verification** (Methodology v1.21) — any target-portfolio holding whose Full QBM evidence exceeds 30 days old now requires a lightweight re-verification pass (price, adverse-event, analyst-sentiment, ATH rule, Valuation Ceiling) before any resizing or renewed readiness claim is trusted, motivated directly by this session's own findings (SCSC's overnight price swing, VSH/IPGP's crashes found only because a scan happened to run that day). **No holding currently exceeds the 30-day threshold** — the first trigger falls in mid-to-late September 2026.

**Target portfolio expanded to 8 holdings (21 Aug 2026)** — [full construction](../screens/QBM_US_ConcentratedPortfolio_2026-08-21.md), superseding [the 19 Aug construction](../screens/QBM_US_ConcentratedPortfolio_2026-08-19.md). Investor directed expansion to 7-8 holdings; exactly three standing Adds cleared every check with no confidence discount (BDC, BHE, ROG) for two remaining slots at the Charter's 8-holding ceiling — **BDC and BHE selected** (already-executing catalysts, cleaner data) **over ROG** (pre-revenue catalyst, largest already-realized run of the three; remains the top bench candidate). Funded by trimming **PTCT and XNCR from 15% to 10%** — PTCT already carried two disclosed open items under "Ready with Considerations," and XNCR's own binary-catalyst disclosure fits the 10% floor tier more precisely than the 15% tier it held before. **New construction: MA 20%, LLY 15%, VCYT 15%, PTCT 10%, XNCR 10%, ACAD 10%, BDC 10%, BHE 10%.** Health Care concentration falls from 85% to **62.5%** (5 of 8) as a direct result of selecting both new slots from a different sector. Binary-catalyst exposure falls from 25% to **20%** (XNCR+ACAD, both now at the 10% floor). **3 of 8 holdings are Ready or Ready with Considerations** (PTCT, BDC, BHE) — up from 1 of 6. 16 companies remain on the bench.

**Four new methodology rules built 20 Aug 2026, on investor request for both relax- and raise-the-bar recommendations** (recapped here since two of them — the Insider Ownership near-miss provision and the Valuation Ceiling — directly shaped the portfolio expansion above). Relax: (1) the Insider Ownership near-miss provision (Methodology v1.16); (2) a Discovery longlist depth-widening rule (v1.17). Raise the bar: (3) a Mini QBM Red-Flag Adverse-Event Scan (v1.18) — a lightweight litigation/investigation search before recommending Advance, motivated directly by RAL and CVLT, whose adverse events predated the 19 Aug Mini QBM pass but were only caught the next day at Full QBM; (4) a **Valuation Ceiling** (Charter v1.6, Methodology v1.19) — no Ready/Ready with Considerations rating when price sits more than 20% above the average analyst consensus target, checked directly and independently of the ATH Proximity Rule. **Applied to all 21 standing Adds: 20 pass, 0 fail** — every name with a computable consensus trades at a *discount* to its average analyst target (widest: ARLO -35.4%, VCYT -27.0%, PTCT -25.8%; tightest: LLY -2.3%, XNCR -5.1%, PI -6.3%). **CTS is a disclosed data gap, not a pass or fail** — no reliable consensus target exists (2 analysts, no numeric target published). This rule changes no current outcome, but is now a standing, mechanical check going forward, independent of the ATH Proximity Rule. Full detail, sourcing and dates: [screens/QBM_US_ValuationCeiling_2026-08-20.md](../screens/QBM_US_ValuationCeiling_2026-08-20.md).

**Insider Ownership & Net Buying Screen added (20 Aug 2026, Methodology v1.13)** — two new required gates for every future Full QBM Add: (1) minimum combined officer/director ownership, tiered by market-cap tier (≥0.5% mega/large-cap, ≥2% mid-cap, ≥5% small-cap — tiered specifically so a flat bar doesn't silently exclude every mega-cap); (2) net insider buying (dollar value bought > sold) over the trailing 6 months, not a rigid ownership-percentage-increase target. **Not yet applied retroactively** — the current 6-holding target portfolio and the 15 Tech Services Advance names were all assessed before this gate existed. This is a disclosed, open verification gap, not an assumption they'd pass.

**ATH Proximity Rule added, then widened (20 Aug 2026, Charter v1.5)** — [full record](../screens/QBM_US_ATHRule_2026-08-20.md). Triggered by a real error: XNCR was rated Ready on 19 Aug based on an incorrect trailing-return figure (the underlying data conflict was noticed at the time and not resolved before publishing). New hard rule: **no Ready/Ready with Considerations rating within 10% of a position's 52-week high or all-time high** (set at 5% initially, widened to 10% same day on investor instruction), checked directly, regardless of confidence or catalyst strength. Applied to all 6 target holdings: **MA also fails it** (4.26% below its all-time high, $601.77 set 22 Aug 2025) — **no current target-portfolio holding is rated Ready as of 20 Aug 2026; only PTCT retains Ready with Considerations.** Target weights unchanged — this affects Implementation Readiness only.

Governing authority: [QBM-US Investment Charter](../framework/QBM_US_Investment_Charter.md) — Version 1.6; permanent; amended 20 August 2026.

## 1. System Health

| Control | Current status |
|---|---|
| Operating Status | **Healthy** |
| QBM-US Methodology Version | 1.22 |
| Investment Charter Status | **Permanent and controlling** — Version 1.6 (amended 20 Aug 2026: Valuation Ceiling added alongside the ATH Proximity Rule) |
| Operating-System Release | **QBM-US Version 1.22** |
| Methodology Status | Versioned — see [Changelog](../framework/QBM_US_Methodology.md#changelog) |
| Database Status | Synchronised |
| Database Integrity | **Complete** |
| Duplicate Records | 0 |
| Broken Links | 0 |
| Missing Identifiers | 0 |
| Synchronisation Failures | 0 |
| Corrupted References | 0 |
| Last Full-Market Scan | 14 Aug 2026 (general funnel) + 19 Aug 2026 (Small/Mid-Cap Health Care supplemental: Discovery 41, Mini QBM 41, Full QBM 11) |
| Last Full-System Synchronisation | 19 August 2026 |

**Status explanation:** QBM-US completed its first full Discovery→Mini QBM→Full QBM funnel on 14 Aug 2026, then the investor added a Thematic Exclusion (avoid AI-industry exposure — personal bubble-risk view) the same day, applied retroactively. On 19 Aug 2026 the investor flagged that the 14 Aug outcome under-represented small/mid-cap and oncology opportunity; root-cause analysis found the Universe Filter's $2B floor and the Quantitative Pre-Screen's profitability gate were structurally excluding that category before research could even begin. Methodology v1.4 fixed both; a dedicated Small/Mid-Cap Health Care scan ran the full Discovery→Mini QBM→Full QBM funnel, producing 8 further Add decisions. The same day, the investor also directed a Charter amendment (v1.1): QBM-US now targets a 6-18 month holding period per position rather than an indefinite hold, which triggered a re-examination of the existing LLY/MA Add decisions (both confirmed) and is now a standing requirement of every Full QBM conclusion (Methodology v1.5). **Ten Investment Decisions now stand as Add** (LLY, MA, VCYT, NEO, PTCT, XNCR, ACAD, HRMY, KRYS, HQY). No capital has been deployed — deployable cash amount not yet specified by the investor.

## 2. Current Macro Environment

| Standing CMEA control | Current assessment |
|---|---|
| Current Standing CMEA | **CMEA-US-2026-08-14-001 — Active official view** |
| Current Macro Regime | **Late-cycle expansion with elevated valuation and contested AI-capex sustainability** |
| Standing CMEA Version | **CMEA-US-2026-08-14-001** |
| Assessment Date | **14 August 2026** |
| Current Portfolio Macro Exposure | Not applicable — no holdings yet |
| Companies Most Exposed | NVDA, LRCX, AVGO, GOOGL, KLAC — all now excluded from the active portfolio candidate set on investor preference, which happens to directly address this exact macro exposure |
| Companies Least Exposed | LLY, HALO, MA (macro-insensitive), AAPL (company-specific issues currently dominate over macro factors) |
| Current Decision Impact Summary | Largely superseded by the Thematic Exclusion — the semiconductor/AI-infrastructure names this CMEA flagged as most macro-exposed are the same names now excluded on investor preference |

**Executive Committee Comment:** Genuinely researched and adopted 14 Aug 2026, alongside the first Full QBM pass. Several source conflicts were disclosed rather than resolved arbitrarily (Fed rate-path direction, oil-price direction) — see the full CMEA for detail. Worth noting explicitly: the investor's new AI-exclusion preference and this CMEA's own risk flagging point in the same direction (semiconductor/AI-infrastructure names carry the most current macro risk) — the exclusion isn't contradicted by anything in this CMEA.

Current detail: [QBM-US Standing CMEA](QBM_US_Standing_CMEA.md) · Historical records: [Standing CMEA Archive](../history/QBM_US_CMEA_Archive.md) · Governance: [QBM-US Operating Standard](../framework/QBM_US_Operating_Standard.md)

## 3. Investment Committee Summary

| Item | Current status |
|---|---|
| Current Committee Position | Full QBM complete on 9 general-funnel finalists (14 Aug), 11 small/mid-cap Health Care finalists (19 Aug), 15 Tech Services finalists (20 Aug, 11 Add after all four update passes) and 3 Tech Services depth-widening finalists (21 Aug, 3 Add); **24 Add decisions stand**, of which **8 hold a slot in the expanded target portfolio** (MA, LLY, VCYT, PTCT, XNCR, ACAD, BDC, BHE) and **16 sit on the bench** (NEO, HRMY, KRYS, HQY, ROG, NTCT, CTS, AGYS, DLB, CNXN, DGII, PI, KN, ARLO, PLXS, SCSC); no capital deployed yet |
| Current Committee Action | **None — cash** (8-holding target portfolio constructed but awaits investor-specified deployable capital) |
| Investment Decision | **Add — in target portfolio:** MA 20% · LLY 15% · VCYT 15% · PTCT 10% · XNCR 10% · ACAD 10% · BDC 10% · BHE 10%. **Add — benched:** NEO, HRMY, KRYS, HQY, ROG, NTCT, CTS, AGYS, DLB, CNXN, DGII, PI, KN, ARLO, PLXS, SCSC. **Continue Monitoring:** HALO, AAPL, LGND, CON, INVA + 11 from the Tech Services depth-widening tier. **Excluded — investor preference (AI exposure):** NVDA/LRCX/AVGO/GOOGL/KLAC + NOVT, EPAM, PLUS, PATH |
| Implementation Readiness | **Ready:** BDC, BHE. **Ready with Considerations:** PTCT. **Await Better Entry:** MA, LLY, VCYT, XNCR, ACAD, plus 16 benched names. **3 of 8 target-portfolio holdings are Ready or Ready with Considerations** — up from 1 of 6 before the 21 Aug expansion, a direct result of selecting both new slots specifically for clean entry points. See [ATH Rule](../screens/QBM_US_ATHRule_2026-08-20.md), [Entry-Point Review](../screens/QBM_US_EntryPointReview_2026-08-19.md), and the [8-holding construction](../screens/QBM_US_ConcentratedPortfolio_2026-08-21.md) |
| Implementation Notes | 14 Aug Full QBM referenced Standing CMEA CMEA-US-2026-08-14-001; same-day Thematic Exclusion removed NVDA/LRCX/AVGO/GOOGL/KLAC. 19 Aug: Charter amended for Target Holding Period, Entry-Point Discipline, then **Portfolio Concentration** (v1.3) — 6 of 10 standing Adds selected into a 100%-invested target book. **21 Aug: expanded to 8 holdings** — BDC and BHE added (clean Full QBM records, no confidence discount); PTCT and XNCR trimmed 15%→10% to fund the two new slots; see [8-holding construction](../screens/QBM_US_ConcentratedPortfolio_2026-08-21.md). Still 100% cash; no purchase has occurred. |
| Tier 1 Companies | 5 (LLY, MA, VCYT, PTCT — in the target portfolio; NEO — benched) |
| Tier 2 Companies | 8 (HALO, AAPL — Continue Monitoring; XNCR, ACAD, BDC, BHE — in target portfolio; HRMY, KRYS — benched) |
| Tier 3 Companies | 4 (HQY — benched; LGND, CON, INVA — Continue Monitoring) |
| On Probation | 0 |
| Current Holdings | 0 |
| Cash Position | **100% — deployable capital not yet specified by the investor** |
| Highest Ranked Company | Not applicable — QBM-US does not yet maintain a cross-company ranking |
| Weakest Holding | Not applicable — no current holdings |
| Most Attractive Opportunity | VCYT — highest identified expected-return range (15-35%) of the 10 Add decisions, Tier 1 |
| Highest Risk Holding | Not applicable — no current holdings |
| Highest Confidence Assessment | MA, VCYT, XNCR — Medium-High |
| Lowest Confidence Assessment | LLY — Medium (GLP-1 litigation growing — new NAION MDL, new Texas AG complaint; Sept 2026 Rule 702 hearing is the key watch date) |

### Recent Investment Committee Minutes

| Meeting Date | Committee Minute | Company | Committee Action |
|---|---|---|---|
| 19 Aug 2026 | QBM-US-MINUTE-VCYT-2026-08-19-001 | VCYT | Add |
| 19 Aug 2026 | QBM-US-MINUTE-NEO-2026-08-19-001 | NEO | Add |
| 19 Aug 2026 | QBM-US-MINUTE-PTCT-2026-08-19-001 | PTCT | Add |
| 14 Aug 2026 | QBM-US-MINUTE-LLY-2026-08-14-001 | LLY | Add |
| 14 Aug 2026 | QBM-US-MINUTE-MA-2026-08-14-001 | MA | Add |

16 further minutes (XNCR, ACAD, HRMY, KRYS, HQY — Add; LGND, CON, INVA — Continue Monitoring; HALO, AAPL — Continue Monitoring; NVDA, LRCX, AVGO, GOOGL, KLAC — superseded by exclusion) preserved in the [QBM-US Investment Committee Minutes Register](../history/QBM_US_Investment_Committee_Minutes.md).

### Portfolio Challenge Summary

Every Full QBM finalist was challenged against cash (the only holding QBM-US has, being 100% cash). 14 Aug: 3 of 9 cleared (NVDA, LLY, MA); Thematic Exclusion then removed NVDA. 19 Aug: 8 of 11 small/mid-cap Health Care finalists cleared (VCYT, NEO, PTCT, XNCR, ACAD, HRMY, KRYS, HQY); 3 did not (LGND, CON, INVA — each pulled back specifically by Full QBM's dedicated verification pass, not by Mini QBM). **10 of 20 total Full QBM finalists assessed to date stand as Add.** Full detail: [screens/QBM_US_FullQBM_2026-08-14.md](../screens/QBM_US_FullQBM_2026-08-14.md), [screens/QBM_US_FullQBM_2026-08-19_SmallMidHealthCare.md](../screens/QBM_US_FullQBM_2026-08-19_SmallMidHealthCare.md).

### Tier Distribution

| Classification | Count |
|---|---:|
| Tier 1 | 4 |
| Tier 2 | 6 |
| Tier 3 | 4 |
| Probation | 0 |
| Discovery (unresearched) | 12 |
| Mini QBM (not advanced, quality reasons) | 10 + 9 (19 Aug: AHCO, QDEL, TNDM, ADMA, ALHC, CRVL, DOCS, LQDA, TGTX) = 19 |
| Full QBM | 9 + 11 (19 Aug) = 20 |
| Excluded — ethical policy | 6 |
| Excluded — investor preference (AI exposure) | 14 |
| Not applicable — pending M&A | 3 (LNTH, BLFS, SUPN) |
| Current Holdings | 0 |

## 4. Research Completeness

| Research control | Current status |
|---|---:|
| Companies tracked | 85 unique (40 general Discovery longlist + 39 net-new from the 19 Aug Small/Mid-Cap Health Care supplemental scan + 6 permanently excluded on ethical grounds; ADMA and LGND Company IDs reused across both scans; GOOG tracked as GOOGL's duplicate, not separately) |
| Full QBM completed | 20 (9 on 14 Aug — 2 Add, 2 Continue Monitoring, 5 excluded post-assessment on investor preference; 11 on 19 Aug — 8 Add, 3 Continue Monitoring) |
| Mini QBM completed | 66 assessments across both scans (25 on 14 Aug, of which 1 — GOOG — was a duplicate of GOOGL and not separately assessed; 41 on 19 Aug) |
| Discovery completed | 81 gross across both scans (40 + 41, 2 IDs reused) |
| Companies awaiting Full QBM | 0 — all Mini QBM Advance decisions from both scans have now completed Full QBM |
| Historical records requiring reconstruction | 0 |
| Outstanding metadata items | 0 |

## 5. Research Coverage

| Coverage Level | Active Count | Current | Review Due | Incomplete | Archived |
|---|---:|---:|---:|---:|---:|
| Full QBM — Add | 10 | 10 | 0 | 0 | 0 |
| Full QBM / Mini QBM — Continue Monitoring | 23 | 23 | 0 | 0 | 0 |
| Mini QBM — not advanced (quality reasons) | 17 | 17 | 0 | 0 | 0 |
| Discovery (unresearched) | 12 | 12 | 0 | 0 | 0 |
| Rejected — ethical policy | 6 | 6 | 0 | 0 | 0 |
| Excluded — investor preference (AI exposure) | 14 | — | — | — | — |
| Not applicable — pending M&A | 3 | — | — | — | — |
| Archived | 0 | 0 | 0 | 0 | 0 |
| **Total Investment Universe** | **85** | **68** | **0** | **0** | **0** |

Breakdown of the two consolidated rows — **Add (10):** LLY, MA (14 Aug); VCYT, NEO, PTCT, XNCR, ACAD, HRMY, KRYS, HQY (19 Aug). **Continue Monitoring (23):** HALO, AAPL (14 Aug); SDGR, RCUS, RDNT, AORT, PAHC, AZTA, ENOV, VIR, ANIP, LMAT, VCEL, UFPT, TFX, LIVN, SHC, TMDX, AMRX, BRKR, LGND, CON, INVA (19 Aug — the last three were pulled back specifically at Full QBM, not Mini QBM). "Excluded — investor preference" and "Not applicable — pending M&A" have no Current/Review Due/Incomplete/Archived breakdown since these are out of consideration entirely, not pending review.

## 6. Coverage Funnel

| Funnel stage | Companies entering stage | Advancement percentage | Current count | Last updated | Coverage context |
|---|---:|---:|---:|---|---|
| S&P 1500 source universe | 1,506 | Not applicable | 1,506 | 14 Aug 2026 | Wikipedia constituent lists, S&P 500+400+600 |
| Universe Filter (v1.1) | 1,313 | 87.2% of source | 1,313 | 14 Aug 2026 | Market cap/price/liquidity/listing/security-type |
| Quantitative Pre-Screen (v1.2) | 454 | 34.6% of Universe Filter | 454 | 14 Aug 2026 | Profitability/FCF/ROE/growth/liquidity |
| Ethical exclusion | 448 | 98.7% of pre-screen | 448 | 14 Aug 2026 | 6 excluded (weapons/gambling); 10 flagged, not excluded |
| Discovery longlist | 40 | 8.9% of eligible pool | 40 | 14 Aug 2026 | Quantitative Discovery ranking (ROE/margin/growth) |
| Mini QBM | 25 | 62.5% of Discovery longlist (top 25 taken in) | 25 | 14 Aug 2026 | Real per-company evidence research |
| Full QBM | 9 | 36% of Mini QBM assessed | 9 | 14 Aug 2026 | Evidence Verification Standard applied to all 9 |
| Thematic Exclusion (v1.3) | 14 | Not a funnel-advancement stage | 14 excluded across Full QBM (5), Mini QBM (6) and Discovery-only (3: META, MSFT, GOOG) | 14 Aug 2026 | Investor AI-exposure preference, applied broadly and retroactively |
| Universe Filter + Pre-Screen (v1.4, Health Care band) | 104 | 78.8% (82 cleared cap/liquidity band; 78 cleared liquidity gate) | 78 | 19 Aug 2026 | $300M-$10B small/mid-cap band; Health Care exempted from the profitability/FCF/ROE gates |
| Discovery — Small/Mid-Cap Health Care | 78 | 52.6% | 41 | 19 Aug 2026 | Ranked longlist, 7 oncology/cancer-flagged |
| Mini QBM — Small/Mid-Cap Health Care | 41 | 26.8% | 11 | 19 Aug 2026 | 11 advanced to Full QBM (4 after a further Target Holding Period re-examination moved names between Continue Monitoring and Advance) |
| Full QBM — Small/Mid-Cap Health Care | 11 | 72.7% | 8 | 19 Aug 2026 | Evidence Verification Standard applied to all 11; surfaced two material adverse-event findings (HQY, CON) not known at Mini QBM |
| Target Holding Period amendment (Charter v1.1) | Not a funnel-advancement stage | Applied to all 22 companies reaching an Investment Decision across both scans (LLY, MA + 20 small/mid-cap Health Care Full QBM finalists) | 22 | 19 Aug 2026 | Every Add now requires a specific, dated 6-18 month convergence reason, not just durable quality |
| Current Holdings | Not applicable | Not meaningful | 0 | 19 Aug 2026 | 10 Add decisions exist; no capital deployed |

Full detail: [screens/QBM_US_Discovery_2026-08-14.md](../screens/QBM_US_Discovery_2026-08-14.md), [screens/QBM_US_MiniQBM_2026-08-14.md](../screens/QBM_US_MiniQBM_2026-08-14.md), [screens/QBM_US_FullQBM_2026-08-14.md](../screens/QBM_US_FullQBM_2026-08-14.md), [screens/QBM_US_Discovery_2026-08-19_SmallMidHealthCare.md](../screens/QBM_US_Discovery_2026-08-19_SmallMidHealthCare.md), [screens/QBM_US_MiniQBM_2026-08-19_OncologySmallMid.md](../screens/QBM_US_MiniQBM_2026-08-19_OncologySmallMid.md), [screens/QBM_US_MiniQBM_2026-08-19_SmallMidHealthCareRemaining.md](../screens/QBM_US_MiniQBM_2026-08-19_SmallMidHealthCareRemaining.md), [screens/QBM_US_FullQBM_2026-08-19_SmallMidHealthCare.md](../screens/QBM_US_FullQBM_2026-08-19_SmallMidHealthCare.md).

### Current Watchlist Movements

| Date | Company | Movement | Current stage |
|---|---|---|---|
| 19 Aug 2026 | VCYT, NEO, PTCT, XNCR, ACAD, HRMY, KRYS, HQY | Discovery → Mini QBM → (Target Holding Period review for HRMY/KRYS) → Full QBM | **Add** — awaiting capital deployment |
| 14 Aug 2026 | LLY, MA | Discovery → Mini QBM → Full QBM → Target Holding Period re-examination (19 Aug) | **Add** (confirmed) — awaiting capital deployment |
| 19 Aug 2026 | LGND, CON, INVA | Discovery → Mini QBM → (Target Holding Period review for CON/INVA) → Full QBM → **pulled back** | Continue Monitoring — each cleared Mini QBM/horizon review but was pulled back specifically by Full QBM's dedicated verification pass |
| 19 Aug 2026 | SDGR, RCUS, RDNT, AORT, PAHC, AZTA, ENOV, VIR, ANIP, LMAT, VCEL, UFPT, TFX, LIVN, SHC, TMDX, AMRX, BRKR | Discovery → Mini QBM | Continue Monitoring (did not advance to Full QBM) |
| 14 Aug 2026 | HALO, AAPL | Discovery → Mini QBM → Full QBM | Continue Monitoring (non-AI reasons) |
| 19 Aug 2026 | LNTH, BLFS, SUPN | Discovery → Mini QBM → **pending acquisition** | Not applicable — mid-merger, not a quality finding |
| 19 Aug 2026 | AHCO, QDEL, TNDM, ADMA, ALHC, CRVL, DOCS | Discovery → Mini QBM | Not advanced (quality reasons) |
| 14 Aug 2026 | NVDA, LRCX, AVGO, GOOGL, KLAC | Discovery → Mini QBM → Full QBM → **Excluded** | Investor preference (AI exposure) — was Add/Continue Monitoring on the merits |
| 14 Aug 2026 | APP, MU, WDC, PLTR, TER, ANET | Discovery → Mini QBM → **Excluded** | Investor preference (AI exposure) — was Continue Monitoring on the merits |
| 14 Aug 2026 | SNDK, TGTX, LQDA, INSW, SEZL, STX, DAVE, FTNT, HLNE, AAMI | Discovery → Mini QBM | Not advanced (quality reasons, unaffected by exclusion) — TGTX and LQDA re-confirmed Not advanced at the 19 Aug Target Holding Period review |
| 14 Aug 2026 | META, MSFT, GOOG | Discovery only → **Excluded** | Investor preference (AI exposure) — excluded without needing dedicated research |
| 14 Aug 2026 | 12 companies (remaining Discovery-only) | Discovery only | Not yet at Mini QBM |

Company lifecycle detail is maintained in the [QBM-US Investment Universe](QBM_US_Investment_Universe.md).

## 7. Portfolio Summary

No current holdings. **24** Full QBM Add decisions stand, but no capital has been deployed — the investor has not yet specified deployable cash. NVDA's original Add decision was superseded by the Thematic Exclusion, not by any quality finding.

| Company ID | Holding | Units | Decision | Implementation Readiness | Allocation range | Current weight | Alignment |
|---|---|---:|---|---|---:|---:|---|
| QBM-US-COMP-MA | — (recommended, not held) | 0 | Add | Await Better Entry (corrected 20 Aug — ATH rule) | **20%** | 0.00% | Underweight |
| QBM-US-COMP-LLY | — (recommended, not held) | 0 | Add | Await Better Entry | **15%** | 0.00% | Underweight |
| QBM-US-COMP-VCYT | — (recommended, not held) | 0 | Add | Await Better Entry | **15%** | 0.00% | Underweight |
| QBM-US-COMP-BDC | — (recommended, not held) | 0 | Add | **Ready** *(new 21 Aug)* | **10%** | 0.00% | Underweight |
| QBM-US-COMP-BHE | — (recommended, not held) | 0 | Add | **Ready** *(new 21 Aug)* | **10%** | 0.00% | Underweight |
| QBM-US-COMP-PTCT | — (recommended, not held) | 0 | Add | Ready with Considerations | **10%** *(trimmed)* | 0.00% | Underweight |
| QBM-US-COMP-XNCR | — (recommended, not held) | 0 | Add | Await Better Entry | **10%** *(trimmed)* † | 0.00% | Underweight |
| QBM-US-COMP-ACAD | — (recommended, not held) | 0 | Add | Await Better Entry | **10%** † | 0.00% | Underweight |
| QBM-US-COMP-NEO, HRMY, KRYS, HQY, ROG + 11 more | Bench — not in the 8 | 0 | Add | Mixed — see Section 8 | Not applicable | 0.00% | — |
| — | Deployable cash | — | — | — | — | 100.00% | — |

† XNCR and ACAD each carry a **binary near-term catalyst** (a single Phase 3 dose readout and a single Phase 2 readout respectively) — disclosed explicitly, not netted into the tier assignment. Together they're 20% of the target portfolio (down from 25% at 6 holdings, since XNCR's trim to 10% now matches its own binary-catalyst disclosure).

**Portfolio expanded to 8 holdings (21 Aug 2026), per direct investor instruction** — [full construction](../screens/QBM_US_ConcentratedPortfolio_2026-08-21.md), superseding [the 19 Aug 6-holding construction](../screens/QBM_US_ConcentratedPortfolio_2026-08-19.md). **BDC and BHE added** — the two cleanest Full QBM records available (no ownership/selling/ATH/valuation-ceiling caveat), selected over ROG on catalyst concreteness and entry timing. Funded by trimming **PTCT and XNCR from 15% to 10%**. 16 standing Adds remain on the bench, with ROG now at the top of that list.

**Sector concentration meaningfully improved, not just diluted:** 5 of 8 holdings (**62.5%**) are Health Care/pharma-biotech, down from 85% at 6 holdings — MA, BDC and BHE now sit outside the sector. This is a direct result of both new slots coming from Tech Services rather than the next-best Health Care bench names.

Target portfolio sums to exactly **100%** — fully invested across 8 names once capital is deployed. **3 of 8 holdings are now Ready or Ready with Considerations (BDC, BHE, PTCT)** — up from 1 of 6 before the expansion, a direct consequence of selecting both new additions specifically for clean entry points, not a coincidence.

**Portfolio Investment Decision:** Add LLY, MA, VCYT, BDC, BHE, PTCT, XNCR, ACAD (target portfolio) + 16 benched Adds (once deployable capital is specified).  
**Implementation Readiness:** **Ready — BDC, BHE.** **Ready with Considerations — PTCT.** **Await Better Entry — MA, LLY, VCYT, XNCR, ACAD**, plus most of the bench. See [ATH Rule](../screens/QBM_US_ATHRule_2026-08-20.md), [Entry-Point Review](../screens/QBM_US_EntryPointReview_2026-08-19.md), and the [8-holding construction](../screens/QBM_US_ConcentratedPortfolio_2026-08-21.md).  
**Implementation Notes:** Portfolio is 100% cash. Deployable capital amount not yet specified by the investor — no unit quantities, weights or execution timing can be set until it is. **Sector concentration disclosed:** 5 of 8 target-portfolio Adds are Health Care (62.5%, down from 85%); MA, BDC, BHE sit outside the sector — a real, correlated exposure, somewhat reduced by this expansion, to weigh at sizing time.

### Current Thesis Status

| Thesis Status | Companies | Count |
|---|---|---:|
| Unchanged | VCYT, NEO, XNCR, ACAD, HRMY, KRYS, HQY, LGND, CON, INVA (assessments dated 19 Aug 2026, no elapsed time yet to judge drift) | 10 |
| Strengthening | MA (two dated near-term catalysts identified at 19 Aug re-examination that the 14 Aug record lacked) | 1 |
| Weakening | LLY (GLP-1 litigation demonstrably expanding since 14 Aug — new NAION MDL, new Texas AG complaint; confidence lowered) | 1 |
| Broken | None | 0 |

### Recent Portfolio Timeline

| Date | Event | Current effect |
|---|---|---|
| 19 Aug 2026 | Full QBM — small/mid-cap Health Care completed | Evidence Verification Standard applied to 11 candidates. 8 Add, 3 Continue Monitoring. Surfaced confirmed data breaches at HQY and CON not known at Mini QBM. |
| 19 Aug 2026 | Target Holding Period reviews (LLY/MA; five flagged Mini QBM names) | LLY/MA re-examined and confirmed Add. Four names (HRMY, KRYS, CON, INVA) moved Continue Monitoring → Advance; LQDA's rejection confirmed. |
| 19 Aug 2026 | Investment Charter amended to v1.1 | 6-18 month Target Holding Period added, replacing the prior implicit indefinite hold. |
| 19 Aug 2026 | Mini QBM + Discovery — Small/Mid-Cap Health Care completed | Methodology v1.4 (lowered Universe Filter floor to $300M; exempted Health Care from the Quantitative Pre-Screen profitability gates) applied to a dedicated scan. 41 companies assessed; 11 advanced toward Full QBM. |
| 14 Aug 2026 | Thematic Exclusion added (AI-industry exposure) | Investor stated a personal AI-bubble-risk view; applied broadly and retroactively. 14 companies excluded across Full QBM, Mini QBM and Discovery-only. NVDA's original Add withdrawn on preference, not quality. LLY and MA unaffected. |
| 14 Aug 2026 | Full QBM completed | Evidence Verification Standard applied to all 9 Mini QBM finalists. Originally 3 Add (NVDA, LLY, MA), 6 Continue Monitoring — see Thematic Exclusion entry above for what changed same day. |
| 14 Aug 2026 | Mini QBM completed | 25 companies assessed; 9 advanced to Full QBM, 6 Continue Monitoring, 10 not advanced. |
| 14 Aug 2026 | Discovery scan completed | 40-company longlist from 1,506 S&P 1500 source, via Universe Filter, Quantitative Pre-Screen and ethical exclusion. |
| 13 Aug 2026 | QBM-US created | Independent system created, mirroring QBM's document architecture, targeting US-listed equities. 100% cash, no companies tracked. |

Permanent history: [QBM-US Portfolio Timeline](../history/QBM_US_Portfolio_Timeline.md).

## 8. Current Rankings

**Rankings are now the 8-holding target portfolio itself** (Portfolio Concentration, Charter v1.6, expanded 21 Aug 2026) — 5-8 holdings, 10-20% each, "go hard or go home." Ranked by target weight; within the target portfolio, Implementation Readiness still governs execution order (Ready first).

### Target portfolio (8 holdings, 100% invested)

| Rank | Company ID | Company | Weight | Implementation Readiness | Reason for position |
|---:|---|---|---:|---|---|
| 1 | QBM-US-COMP-MA | Mastercard (MA) | **20%** | Await Better Entry (corrected 20 Aug — 4.26% below its all-time high) | Durable duopoly moat; two dated near-term catalysts (BVNK close, settlement progress) still ahead of it, not behind it — Core conviction on quality, but the ATH Proximity Rule (10% threshold) means the entry itself must wait |
| 2 | QBM-US-COMP-LLY | Eli Lilly (LLY) | **15%** | Await Better Entry | Evidenced GLP-1 leadership, but +61% over the trailing year and ~97% up its own 52-week range; confidence lowered to Medium on expanding litigation. Quality earns the slot; the caveats cap it below Core. |
| 3 | QBM-US-COMP-VCYT | Veracyte (VCYT) | **15%** | Await Better Entry | Strongest moat evidence of the batch (>60% guideline-embedded share), but +62.8% in the trailing 90 days alone — too sharp and recent a run to call pre-breakout. |
| 4 | QBM-US-COMP-BDC | Belden (BDC) | **10%** *(new 21 Aug)* | **Ready** | Cleanest Full QBM record across all three scans — no ownership, selling, ATH, or valuation-ceiling caveat. RUCKUS Networks integration and order momentum (book-to-bill 1.11) already executing. Sized at the floor as a new addition, not for any disclosed weakness. |
| 5 | QBM-US-COMP-BHE | Benchmark Electronics (BHE) | **10%** *(new 21 Aug)* | **Ready** | Equally clean record — 27.0% below its 52-week high (most room in the book), immaterial selling, dated HPC/AI production-ramp catalyst (management-guided late Q4 2026 into 2027). |
| 6 | QBM-US-COMP-PTCT | PTC Therapeutics (PTCT) | **10%** *(trimmed from 15%)* | Ready with Considerations | Three independent revenue sources — real diversification within one name; litigation status and a conflicting analyst target still need confirming. Trimmed to fund the two new slots — the one 15% holding already carrying two disclosed open items. |
| 7 | QBM-US-COMP-XNCR | Xencor (XNCR) | **10%** *(trimmed from 15%)* † | Await Better Entry | Validated multi-partner platform and diversified royalty income, but the Add catalyst is a single Phase 3 dose readout (2H 2026) — binary, disclosed. Trimmed to the floor tier that its own binary-catalyst disclosure fits more precisely than 15% ever did. |
| 8 | QBM-US-COMP-ACAD | ACADIA Pharmaceuticals (ACAD) | **10%** † | Await Better Entry | Two approved, growing products provide a real base, but the Add catalyst is a single Phase 2 readout (Sept-Oct 2026) — binary, sized at the floor because of it. |

† XNCR + ACAD = 20% of the portfolio riding partly on a single binary event each (down from 25% at 6 holdings). Disclosed explicitly per Charter, not averaged into the Add rating. Full construction, sector-concentration note (62.5% Health Care, down from 85%) and selection rationale (BDC/BHE over ROG): [8-holding Concentrated Portfolio construction](../screens/QBM_US_ConcentratedPortfolio_2026-08-21.md), superseding [the 19 Aug 6-holding construction](../screens/QBM_US_ConcentratedPortfolio_2026-08-19.md).

### Bench (Add-rated, no slot — rotation candidates)

| Company ID | Company | Why benched | Rotation trigger |
|---|---|---|---|
| QBM-US-COMP-NTCT | NetScout Systems (NTCT) | **Ready, no discount** (corrected 22 Aug — re-verified 15.0% below its 52-week high, was wrongly recorded as failing at 7.1%). Ownership and selling already clean. One of two fully clean bench candidates, alongside BDC. | Next open slot |
| QBM-US-COMP-ROG | Rogers Corporation (ROG) | Full QBM Ready — clean across every check, but a weaker (pre-revenue) catalyst than BDC/BHE and the largest already-realized run (+92%/yr) of the three clean candidates. **Top of the bench** — first considered if a slot opens. | A closed slot opens (replacement) |
| QBM-US-COMP-DGII | Digi International (DGII) | **Ready with Considerations** (corrected 22 Aug — re-verified 13.7% below its 52-week high; the original claim it was trading *above* its high was wrong). Material CFO selling ($6.9M) remains the live caveat. | Selling pattern normalizes |
| QBM-US-COMP-KN | Knowles (KN) | **Ready with Considerations** (corrected 22 Aug — re-verified 22.4% below its 52-week high, was wrongly recorded as failing at ~3%). Near-miss ownership (1.7% vs. 2%); ~$9M selling partially offset by a genuine ~$423K insider buy (v1.20). | Selling pattern normalizes |
| QBM-US-COMP-CTS | CTS Corporation (CTS) | **Ready with Considerations** (corrected 22 Aug — re-verified 16.9% below its 52-week high, was wrongly recorded as failing at ~4-6%). Material CEO-only selling ($8.48M, zero buys) remains the live caveat. | Selling pattern normalizes |
| QBM-US-COMP-AGYS | Agilysys (AGYS) | Multi-officer concentrated selling. Re-verified 22 Aug at 21.7% below its 52-week high, cleanly resolving the earlier disclosed price conflict ($65-$108). | Selling pattern normalizes |
| QBM-US-COMP-CNXN | Connection (CNXN) | Multi-officer material selling; narrow (11.5%, re-verified 22 Aug) ATH clearance | Wider ATH clearance |
| QBM-US-COMP-DLB | Dolby Laboratories (DLB) | ~35% ownership via the Dolby family, selling from non-family executives only. Re-verified 22 Aug: only 11.7% below its 52-week high — clears, but far more narrowly than the original ~21% estimate. | Wider ATH clearance |
| QBM-US-COMP-PI | Impinj (PI) | Most severe insider selling found across either scan ($49.4M/3mo, zero buying) | Selling pattern must genuinely improve |
| QBM-US-COMP-PLXS | Plexus (PLXS) | Near-miss ownership (1.78% vs. 2%); severe recent selling ($5.4M/90 days). Re-verified 22 Aug: 21.8% below its 52-week high — comfortably clear, not the "narrow" clearance originally recorded | Selling pattern normalizes |
| QBM-US-COMP-ARLO | Arlo Technologies (ARLO) | Near-miss ownership (4.03% vs. 5%); all-sell pattern with unconfirmed dollar magnitude | Ownership/selling data gap closes further |
| QBM-US-COMP-SCSC | ScanSource, Inc. (SCSC) | Full QBM Add but Await Better Entry — fails the new Valuation Ceiling on a thin, possibly-stale single-analyst target | Broader analyst coverage confirms the ceiling result either way |
| QBM-US-COMP-NEO | NeoGenomics (NEO) | +170%/yr (most extreme extension in the batch) plus an unresolved older shareholder-litigation status | Litigation status confirmed immaterial, and/or a meaningful pullback |
| QBM-US-COMP-HRMY | Harmony Biosciences (HRMY) | Single-product (WAKIX) concentration plus a binary Apr 2027 PDUFA catalyst | Pitolisant GR approval, or real pipeline diversification |
| QBM-US-COMP-KRYS | Krystal Biotech (KRYS) | Single-product (VYJUVEK) concentration plus a binary early-2027 readout. Re-verified 22 Aug: now also 9.4% below its 52-week high — genuinely fails the ATH Proximity Rule too (an earlier estimate had wrongly shown it clearing) | A positive EMERALD-1 readout |
| QBM-US-COMP-HQY | HealthEquity (HQY) | Confirmed, currently unresolved data breach with active litigation | Breach litigation resolves / regulatory response clarifies |

QBM-US-COMP-NVDA (Nvidia) — Add on the merits, **Excluded — investor preference (AI exposure)** as of 14 Aug 2026. Preserved for audit in [screens/QBM_US_FullQBM_2026-08-14.md](../screens/QBM_US_FullQBM_2026-08-14.md), not treated as a current ranking entry.

**Continue Monitoring, not ranked:** LGND, CON, INVA (each cleared Mini QBM and were pulled back only at Full QBM's dedicated verification pass), SDGR, RCUS, RDNT (oncology-flagged), plus AORT, ENOV, VCEL, TMDX from the broader batch. Full list in [Investment Universe](QBM_US_Investment_Universe.md).

## 9. Committee Actions

| Scope | Company ID | Investment Decision | Implementation Readiness | Existing assessment preserved |
|---|---|---|---|---|
| Portfolio | Not applicable | **No current holdings — 100% cash; 8-holding target portfolio constructed, pending capital** | **Not Applicable** | — |
| Target portfolio | QBM-US-COMP-MA | Add — 20% | Await Better Entry (corrected 20 Aug — ATH rule) | Add |
| Target portfolio | QBM-US-COMP-LLY | Add — 15% | Await Better Entry | Add |
| Target portfolio | QBM-US-COMP-VCYT | Add — 15% | Await Better Entry | Add |
| Target portfolio | QBM-US-COMP-BDC | Add — 10% *(new 21 Aug)* | **Ready** | Add |
| Target portfolio | QBM-US-COMP-BHE | Add — 10% *(new 21 Aug)* | **Ready** | Add |
| Target portfolio | QBM-US-COMP-PTCT | Add — 10% *(trimmed 21 Aug)* | Ready with Considerations | Add |
| Target portfolio | QBM-US-COMP-XNCR | Add — 10% *(trimmed 21 Aug, binary catalyst)* | Await Better Entry | Add |
| Target portfolio | QBM-US-COMP-ACAD | Add — 10% (binary catalyst) | Await Better Entry | Add |
| Bench (Add, no slot) | QBM-US-COMP-NEO, HRMY, KRYS, HQY, ROG + 11 more Tech Services names | Add — not applicable (see rotation triggers, Section 8) | Mixed — see Section 8 | Add |
| Full QBM watchlist | QBM-US-COMP-HALO, AAPL | Continue Monitoring | Not Applicable | Continue Monitoring |
| Full QBM watchlist | QBM-US-COMP-LGND, CON, INVA | Continue Monitoring | Not Applicable | Continue Monitoring (pulled back from an Advance lean by Full QBM's verification pass) |
| Full QBM — excluded | QBM-US-COMP-NVDA, LRCX, AVGO, GOOGL, KLAC | Excluded — investor preference (AI exposure) | Not Applicable | Original decision (Add/Continue Monitoring) preserved in screens/QBM_US_FullQBM_2026-08-14.md |
| Full QBM — not applicable | QBM-US-COMP-LNTH, BLFS, SUPN | Not applicable — pending acquisition | Not Applicable | Mid-merger; not a quality finding |

### Current Portfolio Actions

| Company ID | Company | Investment Decision | Target weight | Implementation Readiness |
|---|---|---|---:|---|
| QBM-US-COMP-MA | Mastercard | Add | 20% | Await Better Entry (corrected 20 Aug — ATH rule) |
| QBM-US-COMP-LLY | Eli Lilly | Add | 15% | Await Better Entry |
| QBM-US-COMP-VCYT | Veracyte | Add | 15% | Await Better Entry |
| QBM-US-COMP-BDC | Belden | Add | 10% | **Ready** |
| QBM-US-COMP-BHE | Benchmark Electronics | Add | 10% | **Ready** |
| QBM-US-COMP-PTCT | PTC Therapeutics | Add | 10% | Ready with Considerations |
| QBM-US-COMP-XNCR | Xencor | Add | 10% | Await Better Entry |
| QBM-US-COMP-ACAD | ACADIA Pharmaceuticals | Add | 10% | Await Better Entry |
| — | Deployable cash | Not Applicable | — | Not Applicable |

No equity positions are currently held — the 8-holding target portfolio (expanded 21 Aug 2026) awaits investor-specified deployable capital. 16 companies remain Add-rated but hold no target weight (benched — see Section 8).

## 10. Risk Dashboard

| Risk view | Current status |
|---|---|
| Highest Risk Holding | Not applicable — no current holdings |
| Highest Permanent-Loss Risk | Not applicable — no current holdings |
| Concentration Risk | **Deliberately high, by investor instruction (Charter v1.3), moderately eased by the 21 Aug expansion:** the target portfolio is now 8 holdings at 10-20% each. **5 of 8 (62.5%) are Health Care/pharma-biotech** — down from 85% at 6 holdings — with MA, BDC and BHE now outside the sector. **2 of 8 (XNCR 10%, ACAD 10% — 20% combined, down from 25%) carry a single binary near-term catalyst.** A sector-wide shock or one failed binary readout each still has materially more effect on total portfolio outcome than in a diffuse portfolio — the trade-off is explicit, just somewhat smaller than before. |
| Implementation Notes | No open positions; 8-holding target portfolio (100% invested, expanded 21 Aug 2026) awaits investor-specified deployable capital; **3 of 8 holdings are now Ready or Ready with Considerations (BDC, BHE, PTCT) — up from 1 of 6** |
| Near-Term Evidence Risk | LLY (litigation genuinely expanding — new NAION MDL, new Texas AG complaint); HQY (confirmed 4.3M-record data breach, active class action); CON (open California DOI investigation — Continue Monitoring, not an Add, but tracked given proximity to the bar) |
| Metadata Risk | None |
| Cash Alternative | 100.00% of the portfolio |

### Latest Evidence Changes

| Evidence date | Company | Material evidence | Decision impact |
|---|---|---|---|
| 19 Aug 2026 | HQY | Confirmed data breach exposing 4.3M individuals' PII; active class action (negligence, breach of contract) | Add retained (moat evidence intact) but downgraded to Tier 3 with reduced allocation range (2-4%) and Ready with Considerations |
| 19 Aug 2026 | CON | Separate ~4M-patient data breach via vendor Perry Johnson & Associates; open, unresolved California DOI investigation | Moved from an Advance lean (Target Holding Period review) to Continue Monitoring at Full QBM |
| 19 Aug 2026 | LLY | GLP-1 MDL case count rose 3,763→3,848 in one month; new NAION-specific MDL (No. 3163, 86+ cases) formally created; previously-untracked Texas AG kickback complaint found | Add retained; Decision Confidence lowered Medium-High → Medium; Sept 2026 Rule 702 hearing now the key watch date |
| 19 Aug 2026 | MA | $38B swipe-fee settlement confirmed progressing through court (preliminary-approval hearing held 27 Apr 2026); BVNK acquisition dated to close before year-end 2026 | Add retained and strengthened — the 14 Aug record's missing near-term-catalyst gap addressed |
| 19 Aug 2026 | LGND | Average analyst consensus target ($245.86) found to sit below current price ($287.59); Viking Therapeutics TR-Beta program terminated (Apr 2026) | Moved from an Advance lean to Continue Monitoring at Full QBM |
| 14 Aug 2026 | NVDA, LRCX, AVGO, GOOGL, KLAC, APP, MU, WDC, PLTR, TER, ANET, META, MSFT, GOOG | Investor added a broad Thematic Exclusion for AI-industry exposure (personal bubble-risk view) | All 14 excluded from active consideration, regardless of individual quality findings |
| 14 Aug 2026 | HALO | PTAB found several core patents unpatentable (2025 rulings, confirmed at verification) | Continue Monitoring (non-AI reason, unaffected by exclusion) |
| 14 Aug 2026 | AAPL | App Store legal posture corrected from "paused" to actively adverse; Jefferies Underperform downgrade | Continue Monitoring (non-AI reason, unaffected by exclusion) |

### Review Priority and Decision Drift

| Operational control | Current status |
|---|---|
| Critical review items | 0 |
| High-priority review items | 4 (LLY litigation/Sept 2026 hearing; HQY breach monitoring; NEO/PTCT older-litigation-status checks; ACAD pretrial-hearing status) |
| Most urgent operational review | LLY — September 2026 Rule 702 (Daubert) hearing, GLP-1 MDL (identified 19 Aug 2026) |
| Earliest dated review | LLY — September 2026 |
| Decision Drift — Current | 15 companies (LLY, MA, HALO, AAPL — 14 Aug assessments, re-examined 19 Aug; VCYT, NEO, PTCT, XNCR, ACAD, HRMY, KRYS, HQY, LGND, CON, INVA — all 19 Aug Full QBM assessments) |
| Decision Drift — Review Soon | None yet |
| Decision Drift — Review Required / Stale | 0 / 0 |

## 11. Portfolio Health

**Portfolio Health Score: Not applicable — no current holdings (recommendations exist, not positions)**

| Contributing factor | Current status |
|---|---|
| Diversification | Not applicable while 100% cash; **if funded as recommended, the 8 target-portfolio positions span 3 sectors, 5 of them (62.5%) Health Care** — down from 85% before the 21 Aug expansion to 8 holdings, still a real, disclosed concentration for the investor to weigh, not resolved by QBM-US itself |
| Average Company Quality | Medium-High to High across the 10 Add decisions — genuinely evidenced in each case, but two (HQY, and to a lesser extent CON among the Continue Monitoring names) carry a confirmed adverse event (data breach) that a pure moat/balance-sheet view would miss |
| Average Evidence Confidence | Medium to Medium-High across the 10 Add decisions; Medium is the modal rating — reflects genuine, disclosed open items (litigation status, breach follow-up) rather than uniformly settled evidence |
| Cash Position | 100% — deployable amount not yet specified |
| Speculative Exposure | None outright, but note: 6 of the 10 Adds are development-/growth-stage small/mid-cap biotech or biotech-adjacent names whose theses depend on binary, dated catalysts (FDA decisions, trial readouts) rather than steady-state compounding — a materially different risk character than LLY/MA |
| Portfolio Alignment | Not applicable — 100% cash |
| Concentration Risk | **None realised (100% cash), but real if funded** — see Diversification and Section 10 above |
| Review Currency | LLY, MA, HALO, AAPL dated 14 Aug 2026 (re-examined 19 Aug); VCYT, NEO, PTCT, XNCR, ACAD, HRMY, KRYS, HQY, LGND, CON, INVA dated 19 Aug 2026 — all current |
| Expected Return | Not estimated for LLY/MA (pre-dates the Target Holding Period's expected-return requirement); 9-40% ranges estimated for the 8 new small/mid-cap Adds — QBM-US still does not assign single-point figures |
| Downside Protection | Full — 100% cash |

## 12. Review Calendar

4 dated reviews scheduled: LLY (Sept 2026 Rule 702 hearing — now the earliest dated review, displacing AAPL), XNCR/HRMY (2H2026-Apr2027 binary catalysts), KRYS (early 2027 EMERALD-1 readout), AAPL (October 2026, exact date not specified). 6 open reviews without a confirmed date (MA, HALO, ACAD, PTCT/NEO litigation-status checks, HQY breach monitoring). 3 Continue Monitoring revisit triggers (LGND, CON, INVA). 5 review triggers removed following the Thematic Exclusion (NVDA, AVGO, LRCX, GOOGL, KLAC) — preserved in the Review Calendar's "Removed" section, not deleted. See [QBM-US Review Calendar](QBM_US_Review_Calendar.md) for full detail.

Permanent record: [QBM-US Review Calendar](QBM_US_Review_Calendar.md).

### Recent Review Outcomes

None yet — these are newly scheduled, not completed reviews.

## 13. QBM-US Performance Dashboard

| Prospective validation measure | Current status |
|---|---|
| Portfolio Return | Not yet available. |
| Benchmark Return | Not yet available. |
| Outperformance | Not yet available. |
| Decision Accuracy | Not yet available. |
| Expected vs Actual Return | Not yet available. |
| Replacement Success Rate | Not yet available. |
| Review Compliance | Not yet available. |
| Average Holding Period | Not yet available. |
| Forecast Calibration | Not yet available. |
| Thesis Success Rate | Not yet available. |

## 14. Metadata Completion Register

None open.

## Synchronisation Control

- Governance: Investment Charter (v1.3, amended 19 Aug — Target Holding Period, Entry-Point Discipline, Portfolio Concentration), Methodology (v1.9 — discrete Position Sizing tiers replacing the earlier continuous bands, plus the Electronic Technology/Technology Services partial pre-screen exemption) and Operating Standard reconciled
- Live operating records: Dashboard, Company Database, Investment Universe, Standing CMEA and Review Calendar all populated and reconciled through the 19 Aug Full QBM and Target Holding Period reviews
- Historical records: Decision Journals (20 entries: 9 from 14 Aug + 11 from 19 Aug), Investment Committee Minutes (20 entries: 9 + 11), Portfolio Timeline (Charter amendment, both Target Holding Period reviews, and 19 Aug Full QBM entries appended) and Standing CMEA Archive (empty — CMEA-US-2026-08-14-001 is still active, nothing superseded yet) reconciled
- Company IDs: 85 unique (40 general Discovery longlist + 39 net-new from 19 Aug Small/Mid-Cap Health Care supplemental scan + 6 ethically excluded; GOOG shares no separate research from GOOGL; ADMA and LGND IDs reused across both Discovery scans); duplicates 0
- Assessment IDs: 20 unique (QBM-US-ASSESS-[TICKER]-2026-08-14-001 series, 9; QBM-US-ASSESS-[TICKER]-2026-08-19-001 series, 11); duplicates 0; unlinked 0
- Journal IDs: 20 unique (QBM-US-JOURNAL-[TICKER]-2026-08-14-001 series, 9; QBM-US-JOURNAL-[TICKER]-2026-08-19-001 series, 11); duplicates 0; unlinked 0
- Historical assessments overwritten: none — NVDA's original Add preserved with a correction notice, not deleted; LLY/MA's 14 Aug Full QBM records preserved, with the 19 Aug Target Holding Period re-examination recorded as a separate, linked review rather than an edit to the original
- Methodology version: 1.19
- Investment Charter version: 1.6
- Investment Charter compliance: confirmed; no conflict identified
- Current Investment Decision: **Add** (LLY, MA, VCYT, NEO, PTCT, XNCR, ACAD, HRMY, KRYS, HQY — 10 total); **Continue Monitoring** (HALO, AAPL, LGND, CON, INVA, plus 18 further names from the 19 Aug Mini QBM batch that never reached Full QBM); **Not advanced** (17 total across both scans); **Excluded — investor preference** (NVDA, LRCX, AVGO, GOOGL, KLAC, plus 9 more from Mini QBM/Discovery — 14 total); **Not applicable — pending M&A** (LNTH, BLFS, SUPN); no current holdings, portfolio is 100% cash
- Current Implementation Readiness (revised 20 Aug 2026 — ATH Proximity Rule, Charter v1.5, 10% threshold): Ready with Considerations (PTCT only); Await Better Entry (MA, LLY, VCYT, XNCR, NEO, ACAD, HRMY, KRYS, HQY). No holding is currently Ready — MA and XNCR both corrected 20 Aug after a real error (XNCR rated Ready on an incorrect trailing-return figure) prompted a hard ATH/52-week-high proximity floor (5% initially, widened to 10% same day), which MA also failed on re-check.
- Standing CMEA: CMEA-US-2026-08-14-001; "Late-cycle expansion with elevated valuation and contested AI-capex sustainability"; active until formally replaced; none of the 19 Aug small/mid-cap Health Care finalists carry material AI-capex exposure
- Current controlled committee action: None — cash (10 Add decisions await investor-specified deployable capital)
- Operating-system release: QBM-US Version 1.19
- **This reconciliation (22 Aug 2026, systematic price data re-verification):** Primary Price Data Source requirement built (v1.22) after a full re-check of all 24 then-standing companies' ATH-proximity figures against a single reproducible source (`yfinance`) found four genuine Implementation Readiness errors (DGII, KN, CTS upgraded Await Better Entry → Ready with Considerations; NTCT upgraded to fully Ready) and one reversal (KRYS now fails the ATH rule, bench placement unaffected). Full detail: [screens/QBM_US_PriceDataReverification_2026-08-22.md](../screens/QBM_US_PriceDataReverification_2026-08-22.md). Dashboard bench table re-ordered (cleanest candidates first) and Investment Universe updated for every affected company. Also closed several pre-existing sync gaps found in passing: AGYS, DGII, PLXS, CTS and DLB's Investment Universe records still said "Discovery only" despite having completed Full QBM weeks ago.
- **Prior reconciliation (21 Aug 2026, two more methodology rules):** Insider Buying positive factor (v1.20) and Evidence Staleness Re-verification Requirement (v1.21) built on investor request. Insider Buying applied retroactively using already-gathered data (no new research): one genuine buy found (KN, ~$423K, disclosed as a partial offset). Evidence Staleness sets a 30-day re-verification trigger for target-portfolio holdings — none currently exceed it. Dashboard, Investment Universe and the Tech Services Full QBM record updated; no Charter change required (both are Methodology-only numeric/process proxies for existing principles, the same pattern as the Insider Ownership Screen itself). In closing this out, also fixed a pre-existing gap found in passing: KN's Investment Universe record still said "Discovery only" despite having completed Full QBM on 20 Aug.
- **Prior reconciliation (21 Aug 2026, portfolio expansion):** Target portfolio expanded from 6 to 8 holdings per direct investor instruction, under the Charter's existing Portfolio Concentration rule (no new amendment required — 8 is within the pre-existing 5-8 range). BDC and BHE added at 10% each (both Full QBM Ready, no confidence discount); PTCT and XNCR trimmed 15%→10% to fund the two new slots. Health Care concentration falls from 85% to 62.5%; binary-catalyst exposure falls from 25% to 20%. Full construction: [screens/QBM_US_ConcentratedPortfolio_2026-08-21.md](../screens/QBM_US_ConcentratedPortfolio_2026-08-21.md), superseding the 19 Aug 6-holding construction (preserved for history). Dashboard, Investment Universe and Portfolio Timeline updated; Charter and Methodology required no version change since the rule already permitted this.
- **Prior reconciliation (20 Aug 2026, methodology-recommendations pass, complete):** Four new rules built and all four fully applied — Insider Ownership near-miss provision (v1.16: KN/ARLO/PLXS now Advance), Discovery longlist depth-widening (v1.17: Tech Services widened 36→54, 15 new Discovery-eligible names found), Mini QBM Red-Flag Adverse-Event Scan (v1.18: first live application, run on all 15 depth-widening candidates — drove 5 of 11 Continue Monitoring calls directly), Valuation Ceiling (v1.19/Charter v1.6: applied to all 21 standing Adds, 20 pass, 0 fail, CTS a disclosed data gap). Tech Services Full QBM final tally revised to 11 of 15 Add; bench now 18 candidates after Full QBM completed 21 Aug on BHE, SCSC, ROG (all three Add — BHE/ROG Ready, SCSC Await Better Entry on the new Valuation Ceiling's first real fail). Mini QBM on the 15 depth-widening candidates found these 3 Advance candidates and one more AI-infrastructure exclusion (NOVT) the Discovery screen missed. Also closed a pre-existing gap found in passing: 11 Investment Committee Minutes from the 20 Aug Tech Services Full QBM had never been appended to the register — added now, alongside the 3 new ones from today. Not yet reconciled: Sections 4-6's detailed coverage-funnel counts (companies tracked, Full QBM completed, Discovery longlist totals) still reflect the pre-Tech-Services state — flagged here as a known gap rather than silently left inconsistent.
- Permanent documents: 12 total — 3 governance, 5 live operating, 4 historical
- Historical information lost: none
- **This reconciliation (19 Aug 2026):** completes the full-system synchronisation flagged as outstanding after the 19 Aug Full QBM — all 14 Dashboard sections, the Investment Universe, Review Calendar, Portfolio Timeline, Investment Committee Minutes and the Company Database (LLY/MA re-examination recorded as new dated sub-entries per the append-only principle; all 11 new 19 Aug Full QBM companies added) are now consistent with the Target Holding Period amendment and the 19 Aug Full QBM results.
- **Entry-Point Discipline pass (19 Aug 2026, same day):** Charter amended to v1.2 (folded into v1.3); all 10 Adds checked against 52-week range position and trailing return; Implementation Readiness revised for 7 of 10 (moved to Await Better Entry); Investment Decision unchanged for all 10.
- **Portfolio Concentration pass (19 Aug 2026, same day):** Charter amended to v1.3; investor directed 5-8 holdings, 10-20% each, in 10/15/20% tiers. Selected 6 of the 10 standing Adds (MA 20%, LLY/VCYT/PTCT/XNCR 15% each, ACAD 10%); NEO, HRMY, KRYS, HQY benched with rotation triggers. Dashboard, Investment Universe, Company Database and Portfolio Timeline updated.
- Last full-system synchronisation: 19 August 2026 — confirmed complete, no outstanding sections.
