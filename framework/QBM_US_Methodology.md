# QBM-US Methodology

**Version:** 1.3  
Adopted: 13 August 2026  
Status: **Versioned** — amendments are made directly by investor instruction and recorded in the Changelog below. No formal Operational Change Register is required (see [QBM-US Investment Charter](QBM_US_Investment_Charter.md#governance-philosophy) for why this differs from QBM).

Governing authority: This methodology is subordinate to the [QBM-US Investment Charter](QBM_US_Investment_Charter.md). If a future instruction conflicts with the Investment Charter, the Investment Charter prevails unless intentionally amended.

Starting ruleset: v1.0 carries forward the process, gates, scoring approach, allocation logic and decision framework of QBM's frozen methodology (as it stood 13 August 2026), adapted only where the ASX-specific target market, benchmark holdings and amendment history do not apply to a fresh US-market system. It is not a fork of QBM's document — it is a new document that starts from the same rules.

## Default commands

The following commands trigger the complete US QBM-US funnel:

- Run QBM-US Full Scan
- Run the complete US QBM-US funnel
- Find the best overlooked US QBM-US candidates
- Run Discovery, Mini QBM and Full QBM on the US market

## Target market

Default universe: US-listed equities (NYSE and NASDAQ), subject to the Universe Filter below. The first scan should still state its actual source list (e.g. S&P 500, Russell 1000, a broader screener) explicitly rather than implying full-market coverage.

## Universe Filter (added v1.1)

Applied before Discovery, to keep low-quality, untradeable and data-poor tickers out of the funnel rather than filtering them out one-by-one during research. This mirrors what QBM itself does in practice on the ASX side (it scans a "top-300 liquid proxy," not the full exchange) rather than trying to genuinely cover the entire market.

A candidate must clear all of the following to enter Discovery:

- **Market capitalisation:** ≥ US$2 billion. Excludes micro/nano-caps, where data quality, audit rigor and public disclosure are typically weakest.
- **Average daily dollar volume:** ≥ US$5 million. Ensures a position could realistically be entered and exited.
- **Share price:** ≥ US$5. Excludes penny-stock-adjacent names, which carry disproportionate manipulation and data-quality risk.
- **Primary listing:** NYSE or NASDAQ. Excludes OTC/pink-sheet tickers.
- **Security type:** common stock only. Excludes SPACs (pre- and post-merger shells), warrants, rights, units and preferred shares. Foreign private issuers with an NYSE/NASDAQ-listed ADR are included, since the ADR itself trades as an ordinary listed share.

This is a mechanical, objective pre-filter — it does not judge business quality. Business quality, moat, valuation and all other Company Quality questions are still decided at Discovery/Mini/Full QBM as usual; this filter only keeps genuinely untradeable or data-poor tickers from consuming research effort.

Every scan must disclose how many tickers were excluded by this filter and why, the same as any other coverage limitation.

## Quantitative Pre-Screen (added v1.2)

Applied after the Universe Filter and before genuine Discovery-stage research begins. It exists because clearing the Universe Filter still leaves far more tickers (e.g. 1,313 from the first S&P 1500 pass) than can be genuinely, evidence-based researched in one Discovery pass — QBM's own ASX Discovery scan covered roughly 300. Rather than cutting the source universe arbitrarily or pretending to review companies that were never actually looked at, this step applies QBM's own Investment Principles (durable cash generation, high returns on capital, conservative balance sheets, a business that isn't shrinking) as numeric, mechanical proxies.

A candidate must clear all of the following to advance into Discovery:

- **Profitability:** trailing net margin > 0%.
- **Free cash flow:** positive (> $0).
- **Return on equity:** ≥ 10%.
- **Revenue growth (year-over-year):** ≥ 0% — not shrinking.
- **Liquidity:** current ratio ≥ 1.0.

This is coarse and imperfect by design — it will miss genuine turnaround stories with temporarily weak numbers, and it cannot see moat, management quality or recurring-revenue character, which remain qualitative Discovery/Mini/Full QBM questions. It is a pre-screen, not a substitute for Company Quality assessment.

Every scan must disclose how many tickers were excluded by this pre-screen and why, the same as the Universe Filter.

## Required workflow

1. Reference the active Standing CMEA; create an Event Brief only when material new macro evidence warrants testing whether a replacement version is required
2. US Discovery Scan
3. Mini QBM on candidates that genuinely warrant advancement
4. Full QBM on the strongest finalists
5. Portfolio Challenge Test against current holdings and cash (no fixed benchmark companies — QBM-US starts with no holdings; compare finalists against whatever is actually held or, while the portfolio is 100% cash, against cash itself)
6. Full downstream synchronisation: Company Database, Investment Committee Dashboard, Investment Universe, Master Dashboard, Relative Rankings, Review Calendar, Decision Journals, CMEA Register and Archive, Record Integrity Register, Metadata Completion Register and all operational-intelligence registers

## Discovery requirements

- Start with the broadest verifiable investable US source universe available, then apply the Universe Filter and Quantitative Pre-Screen above.
- Disclose the source universe, number considered, data date, filters (including the Universe Filter's and Quantitative Pre-Screen's exclusion counts), exclusions and coverage limitations.
- Never claim complete US-market coverage unless every relevant listed security was genuinely reviewed.
- Permanently exclude new discovery candidates principally involved in weapons manufacturing, gambling, or tobacco.
- Do not exclude unfamiliar, unfashionable or out-of-portfolio sectors merely for those reasons.
- Apply preliminary Eligibility filters without producing full reports at Discovery stage.
- Produce a ranked longlist of approximately 30–50 companies, or fewer when evidence does not support that many.

## Mini QBM requirements

- Normally review approximately 15–30 candidates, determined by evidence rather than quota.
- Assess Eligibility, preliminary Company Quality, Investment Attractiveness and Portfolio Fit.
- Record decision, priority, confidence, expected-return range, allocation range, strongest evidence, contradicting evidence and advancement decision.
- Rank candidates by likelihood of improving the portfolio without implying precision unsupported by evidence.
- Reference the active Standing CMEA as a separate evidence overlay to Investment Attractiveness, Portfolio Fit, Review Priority, Implementation Readiness and Monitoring Priorities. Display Current Macro Reference, Decision Impact and Executive Committee Comment without reproducing the complete CMEA. Do not let it directly change Company Quality or independently create a recommendation.

## Full QBM finalist requirements

- Select approximately 3–10 finalists only when quality and evidence justify advancement.
- Apply the permanent Executive Committee Summary and complete Research Appendix.
- Compare every finalist directly with current holdings (or cash, while none are held).
- Preserve the decision process and record methodological difficulties only as Validation Observations.
- Display Current Macro Reference, Decision Impact and Executive Committee Comment. Link to the Standing CMEA for Current Macro Impact, reason, time horizon, confidence and detailed portfolio effects rather than reproducing the full assessment.

## Portfolio Challenge Test

- Compare current holdings, finalists and cash on Company Quality, Investment Attractiveness, Portfolio Fit, confidence, expected return, allocation range, decision and relative rank.
- Identify the strongest and weakest holdings, strongest outside candidate, best diversifier, best expected return, best downside protection, expensive quality companies and insufficiently proven opportunities.
- Require a demonstrably superior, evidence-supported and downside-aware expected return before recommending replacement.
- Determine the Investment Decision from Company Quality, Investment Attractiveness, Portfolio Fit, concentration, correlation, evidence confidence and downside-aware expected return.
- Record tax, brokerage, transaction costs, current weights, liquidity, cash, sizing and execution timing separately under Implementation Readiness and Implementation Notes; these inputs must not dilute the ownership conclusion.
- When no candidate clearly passes the hurdle, conclude: **No replacement justified.**

## Recordkeeping

- Update the internal QBM-US Investment Universe after each completed scan.
- Update relative rankings and the Investment Committee Dashboard.
- Update the Company Database, Master Dashboard and Review Calendar.
- Append every completed Decision Journal to the Decision Journal index.
- Preserve all Decision Journals and historical assessments.
- Distinguish Discovery-only, Mini-QBM and Full-QBM coverage.
- Record evidence and review dates.
- Assign a permanent Company ID to every newly tracked company.
- Assign unique Assessment and Journal IDs to every completed Full QBM and link both to the Company ID.
- Reconcile identifier uniqueness, coverage counts, review dates, active-assessment status, duplicates and missing metadata through the Record Integrity Register.
- Record unresolved metadata only in the Metadata Completion Register.
- Express the Investment Decision using only Add, Hold, Hold but Do Not Add, Trim, Exit, Replace, Probation or Continue Monitoring.
- Display Implementation Readiness separately using Ready, Ready with Considerations, Await Better Entry, Await Better Evidence, Await Tax Window, Await Liquidity, Await Portfolio Weights or Not Applicable.
- Place weights, tax, brokerage, spread, liquidity, cash, sizing and timing only in concise Implementation Notes; never use them to weaken the Investment Decision.
- Append one Investment Committee Minute for every completed Full QBM.
- Append each Discovery, Mini QBM, Full QBM and portfolio transition to Portfolio Timeline and Watchlist Evolution.
- Create or update the immutable original entry in the Thesis Tracker and Portfolio Memory without overwriting earlier evidence.
- Record only material new evidence in the Evidence Change Log.
- Update Decision Stability and create a Review Outcome when a scheduled review is completed.
- Compare every new Full QBM company with every current holding through the Portfolio Challenge Engine.
- Update the Portfolio Replacement Table, Review Priority Queue, Morning Brief, Heat Map, Decision Drift Monitor and Executive Snapshot.
- Reference the active Standing CMEA before the scan. Routine volatility does not create a new version. If an Event Brief concludes Create new Standing CMEA, assign a unique CMEA-YYYY-MM-DD-### identifier, preserve the superseded version append-only and update all required dashboard references.
- Leave every challenge comparison advisory; never change a recommendation automatically. When the committee evidence supports a replacement, state the Investment Decision directly and separately state Implementation Readiness.
- Update or export the master workbook only when explicitly requested with "Update the QBM-US Database" or "Export the QBM-US Database."

## Accuracy and progressive coverage

- Prioritise audited accounts (10-K/10-Q), SEC filings, earnings releases, and independently verifiable operating data.
- Grade secondary evidence and never invent missing data.
- When the workload exceeds what can be properly evidenced in one pass, complete and report each stage progressively rather than implying false completeness.

## Evidence Verification Standard

QBM-US has no live market-data feed or financial-terminal connection. All evidence comes from web search, which is sensitive to how a query is phrased and does not self-verify. General evidence-gathering searches can miss a more severe or more current characterisation of a known issue even when that information is publicly available and indexed at the time.

Before any Full QBM finalist conclusion is finalised, run a dedicated final-verification search pass, separate from general evidence-gathering, consisting of at minimum:

1. A direct current-price query (e.g. "[ticker] share price today"). Where sources disagree and cannot be reconciled, disclose the range rather than asserting a single figure, and prefer an investor-supplied live quote over search-derived figures when one is available.
2. A direct adverse-event query (e.g. "[ticker] recall", "[ticker] lawsuit", "[ticker] SEC investigation", "[ticker] safety"), aimed explicitly at surfacing the most severe available characterisation of any known issue rather than stopping at the first plausible result.
3. A direct analyst-sentiment query (e.g. "[ticker] analyst downgrade", "[ticker] price target cut", "[ticker] rating change"), covering at minimum the trailing 6 months — not just since the prior scan's evidence cut-off.

Disclose the verification search timestamp — not just the calendar date — in the output. If verification could not be completed before publishing, state this explicitly rather than implying completeness.

*(Carried forward from QBM's Operating Standard, where this control was added 8 August 2026 after a real evidence gap on ResMed. Applying it here from the start rather than waiting to rediscover the same gap.)*

## Ethical exclusions

Permanently exclude new discovery candidates principally involved in:

- weapons manufacturing;
- gambling; or
- tobacco.

Where exposure is indirect, incidental or ambiguous, identify it clearly before treating the company as eligible.

## Thematic exclusions (added v1.3)

Distinct from the ethical exclusions above — see [UserProfile.md](../UserProfile.md#thematic-exclusions-distinct-from-ethical-exclusions) for the full statement and rationale.

Exclude candidates with material revenue or earnings exposure to the AI-infrastructure buildout — applied broadly (AI chip/software companies, semiconductor-equipment suppliers to AI chipmakers, and hyperscalers whose capex or cloud revenue is substantially AI-driven), not narrowly to pure-play AI companies only.

This is an investor risk-view preference, not a permanent ethical exclusion — it may be revisited if the investor's view on AI-sector risk changes, unlike the ethical exclusions above. Apply it at Discovery stage going forward so AI-exposed candidates are screened out before consuming Mini/Full QBM research effort, the same way the Universe Filter and Quantitative Pre-Screen already narrow the funnel mechanically.

## Operational maturity control

Do not propose methodology additions because they appear theoretically attractive. Every future change should arise from a real investment decision, validation finding, recurring operational weakness or demonstrated data-quality issue — but unlike QBM, it does not need a formal Operational Change Register entry to take effect. Record it as a new version below with a one-line reason.

## Open Items

- No position-sizing or order-execution logic defined.
- Universe Filter thresholds (v1.1) are a starting point, not validated against real results yet — revisit once the first scan shows how much they actually cut and whether anything worth keeping got excluded.
- Quantitative Pre-Screen thresholds (v1.2) are a starting point too, and will systematically miss turnaround-story candidates by design — revisit once the first scan shows the resulting longlist size and quality.
- The Thematic Exclusion (v1.3) has not yet been applied at Discovery stage in a live scan — it was applied retroactively to the 14 Aug 2026 results. First real test is the next fresh Discovery scan.

## Changelog

- **v1.3 (14 August 2026):** Added a Thematic Exclusion for AI-industry exposure, applied broadly (see UserProfile.md). Investor stated a personal view that AI-infrastructure spending may be a bubble and asked to avoid the theme entirely, distinct from the permanent ethical exclusions — applied retroactively to the 14 Aug 2026 Full QBM/Mini QBM results (see history/QBM_US_Portfolio_Timeline.md) and going forward at Discovery stage.
- **v1.2 (13 August 2026):** Added a Quantitative Pre-Screen (profitable, positive free cash flow, ROE ≥ 10%, revenue growth ≥ 0%, current ratio ≥ 1.0) applied after the Universe Filter and before Discovery. Investor asked how to narrow the 1,313-ticker Universe-Filter result further rather than either running Discovery on all of it or cutting the source index arbitrarily; agreed a numeric proxy for QBM's own Investment Principles was more defensible than either.
- **v1.1 (13 August 2026):** Added a Universe Filter (market cap ≥ $2B, avg daily dollar volume ≥ $5M, price ≥ $5, NYSE/NASDAQ primary listing, common stock only) applied before Discovery. Investor asked whether junk should be filtered out before the first full scan rather than handled later; agreed doing it up front is cheaper than filtering noise out ticker-by-ticker during research, at the cost of a somewhat arbitrary cutoff that could exclude a genuine small-cap.
- **v1.0 (13 August 2026):** QBM-US created as an independent system, carrying forward QBM's process, gates, scoring and decision framework as of 13 Aug 2026. Target market changed from ASX to US-listed equities (NYSE/NASDAQ). Fixed ASX benchmark holdings (CSL, RMD, TNE, CDA, CU6) removed from the Portfolio Challenge Test — QBM-US starts with no holdings and compares against whatever is actually held. Governance changed from frozen (Operational Change Register required) to versioned (investor can authorise a change directly, recorded here). ASX-specific amendment history not carried over — QBM-US has none of its own yet.
