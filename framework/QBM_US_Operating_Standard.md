# QBM-US Operating Standard

Adopted: 13 August 2026

Governing authority: This standard is subordinate to the [QBM-US Investment Charter](QBM_US_Investment_Charter.md). If a future instruction conflicts with the Investment Charter, the Investment Charter prevails unless intentionally amended.

This is the single authoritative operating standard for QBM-US. It governs synchronisation, reporting, monitoring, record integrity, decision intelligence, dashboard operation and document maintenance without changing the Investment Charter, Methodology, company assessments, gates, scores, rankings, allocations or decisions.

## Permanent document architecture

QBM-US maintains exactly twelve permanent documents:

### Governance — 3

1. QBM-US Investment Charter
2. QBM-US Methodology
3. QBM-US Operating Standard

### Live operating records — 5

1. QBM-US Dashboard
2. QBM-US Company Database
3. QBM-US Investment Universe
4. QBM-US Standing Current Macro Environment Assessment
5. QBM-US Review Calendar

### Historical records — 4

1. QBM-US Decision Journals
2. QBM-US Investment Committee Minutes
3. QBM-US Portfolio Timeline
4. QBM-US Standing CMEA Archive

Only one current version of each live document exists. Updates replace the current version while preserving its file identity and version history. Historical records are append-only.

QBM-US adopts this twelve-document architecture from inception — there is no legacy document set to retire and no retired-source appendix to preserve, unlike QBM (which consolidated from 24 prior documents).

## Single-source controls

- Current holdings: Company Database
- Current rankings and executive reporting: Dashboard
- Current universe and coverage stage: Investment Universe
- Current review schedule: Review Calendar
- Current macro assessment: Standing CMEA
- Historical decisions: Decision Journals
- Historical portfolio actions and operating-system events: Portfolio Timeline
- Historical committee deliberations: Investment Committee Minutes
- Superseded macro regimes: Standing CMEA Archive

No standalone dashboard, queue, monitor, validation placeholder, development register or duplicate report may be created. New capability must normally be implemented as a section of an existing authoritative document.

## Required Dashboard sections

1. System Health
2. Current Macro Environment
3. Investment Committee Summary
4. Research Completeness
5. Research Coverage
6. Coverage Funnel
7. Portfolio Summary
8. Current Rankings
9. Committee Actions
10. Risk Dashboard
11. Portfolio Health
12. Review Calendar
13. Performance Dashboard
14. Metadata Completion Register

Operating Status measures whether QBM-US is functioning and uses only: Healthy, Healthy with Minor Exceptions, Requires Maintenance or Degraded. It must never be reduced solely because historical metadata or research records are incomplete.

Database Integrity measures only duplicates, broken links, missing identifiers, synchronisation failures and corrupted references. It uses only: Complete, Complete with Minor Exceptions, Partial or Out of Sync. Research completeness must be reported separately.

The Coverage Funnel must distinguish the Current Investment Universe, latest Discovery Scan and historical coverage. The Performance Dashboard remains prospective and displays "Not yet available." until auditable data exists.

## Refresh triggers

Refresh automatically after a Full QBM, database rebuild, universe or holding change, Discovery Scan, Mini QBM, review-date change or material evidence change. Do not change rankings for ordinary daily price movements.

Every refresh must reconcile all core records, operational-intelligence registers and decision-intelligence controls, including the Portfolio Challenge Engine, Replacement Table, Review Priority Queue, Morning Brief, Portfolio Heat Map, Decision Drift Monitor, Executive Snapshot and Validation Dashboard. All historical registers are append-only and must never be overwritten.

Every company row must carry its permanent Company ID. Every Full QBM assessment and Decision Journal must carry unique, linked Assessment and Journal IDs.

## Evidence Verification Standard

See [QBM-US Methodology](QBM_US_Methodology.md#evidence-verification-standard) — carried forward from the start rather than treated as a separate reporting-rigor control layered on later.

## Operational maturity

Future development prioritises better research, evidence, monitoring, historical records and validation over additional methodological complexity. Every proposed change should originate from a real investment decision, validation finding, recurring operational weakness or demonstrated data-quality issue and should be recorded as a new version in the [QBM-US Methodology](QBM_US_Methodology.md) Changelog.

Unlike QBM, no formal Operational Change Register (Problem observed / Evidence / Materiality / Proposed solution / Expected benefit / Complexity cost / Recommendation) is required — a one-line Changelog entry with the reason is sufficient. See [QBM-US Investment Charter — Governance Philosophy](QBM_US_Investment_Charter.md#governance-philosophy).

Decision Intelligence is governed by this Operating Standard and may only highlight, prioritise, summarise, compare, monitor and challenge.

Every portfolio recommendation must display Investment Decision and Implementation Readiness as separate fields under the consolidated decision rules in this Operating Standard.

Before every qualifying scan, assessment or review, reference the active [QBM-US Standing CMEA](../live/QBM_US_Standing_CMEA.md) under the consolidated CMEA rules in this Operating Standard. The active version remains official until formally replaced after a material change. Routine volatility may trigger an Event Brief but not a new Standing CMEA. The dashboard macro section is contextual evidence only and must not independently change Company Quality or create a recommendation.

## Architectural Stability

The QBM-US permanent architecture (twelve documents) is intentionally stable, even though the Methodology inside it is expected to change more often than QBM's.

New permanent documents should be created only when they contain unique information that cannot logically exist within an existing permanent document.

### Guiding Principle

Every proposed enhancement should first answer:

> "Will this improve the quality of long-term investment decisions?"

If the answer cannot be demonstrated with reasonable evidence, the operating system should remain unchanged.

## Default commands

The following display the latest Dashboard:

- Show QBM-US Dashboard
- Open QBM-US Dashboard
- QBM-US Dashboard
- Dashboard
- Investment Committee Dashboard
- Portfolio Dashboard
- Update Dashboard

## Decision and Implementation Readiness rules

### A. Investment Decision

Investment Decision answers: **What should the portfolio own based solely on current QBM-US evidence?**

Permitted decisions:

- Add
- Hold
- Hold but Do Not Add
- Trim
- Exit
- Replace
- Probation
- Continue Monitoring

The Investment Decision is direct and must not be weakened by tax, brokerage, costs, weights, liquidity or execution wording.

### B. Implementation Readiness

Implementation Readiness answers: **Is the recommended Investment Decision ready to be executed now?**

Permitted statuses:

- Ready
- Ready with Considerations
- Await Better Entry
- Await Better Evidence
- Await Tax Window
- Await Liquidity
- Await Portfolio Weights
- Not Applicable

Implementation Readiness never reverses, dilutes or obscures the Investment Decision.

### Implementation Notes

Notes may briefly cover weights, tax, gains or losses, transaction costs, brokerage, spread, liquidity, sizing, cash and timing. They appear after the decision and readiness fields and affect only how or when execution occurs.

### Replacement output

Every replacement conclusion displays Candidate, Holding to Replace, Investment Decision, Replacement Status, Implementation Readiness, Evidence Strength, Decision Confidence and Reason.

Replacement Status remains Strong Replacement, Possible Replacement, No Improvement or Insufficient Evidence.

## Permanent identifiers and integrity

- Company ID format: **QBM-US-COMP-[TICKER]**. It remains permanent through ticker or name changes.
- Assessment ID format: **QBM-US-ASSESS-[TICKER]-[YYYY-MM-DD]-[SEQUENCE]**.
- Journal ID format: **QBM-US-JOURNAL-[TICKER]-[YYYY-MM-DD]-[SEQUENCE]**.
- Committee Minute ID format: **QBM-US-MINUTE-[TICKER]-[YYYY-MM-DD]-[SEQUENCE]**.
- Assessment, Journal and Minute IDs are unique, append-only and never reused.
- Every journal links to exactly one Assessment ID and one Company ID.
- The Record Integrity Register must be refreshed during every full-system synchronisation.
- Do not mark coverage complete unless all mandatory fields for that coverage level are present and verifiable.

## System health, integrity and research completeness

- Operating Status measures whether QBM-US itself functions and uses Healthy, Healthy with Minor Exceptions, Requires Maintenance or Degraded.
- Database Integrity measures only duplicates, broken links, missing identifiers, synchronisation failures and corrupted references and uses Complete, Complete with Minor Exceptions, Partial or Out of Sync.
- Research Completeness separately reports tracked companies, completed coverage, companies awaiting Full QBM, historical reconstruction and outstanding metadata.
- Historical metadata and research completeness must never reduce Operating Status by themselves.
- Unresolved metadata is maintained centrally in the Metadata Completion Register.

## Performance Dashboard

Maintain prospective placeholders for Portfolio Return, Benchmark Return, Outperformance, Decision Accuracy, Expected vs Actual Return, Replacement Success Rate, Review Compliance, Average Holding Period, Forecast Calibration and Thesis Success Rate. State **Not yet available.** until auditable prospective data exists.

## Operational intelligence registers

- Every completed Full QBM automatically appends one Investment Committee Minute and updates the Thesis Tracker, Decision Stability Register and applicable Portfolio Memory comparison.
- Every portfolio or coverage-lifecycle event appends to the Portfolio Timeline and Watchlist Evolution Register.
- Only material evidence appends to the Evidence Change Log; daily price movements, minor news, analyst opinions and rumours are excluded.
- Every completed scheduled review appends one Review Outcome and updates Decision Stability, Thesis Tracker, Committee Minutes, Portfolio Timeline and Review Calendar.
- Original theses, purchase evidence, Committee Minutes, timeline entries, lifecycle histories, evidence entries and review outcomes are never overwritten or deleted.
- A falling share price alone never changes Thesis Status. Only evidence affecting Company Quality, Investment Attractiveness or Portfolio Fit may do so.

## Ranking stability

Do not change rankings for small return differences, minor valuation movements, price action or sentiment. Change them only for material changes in fundamentals, Portfolio Fit, Company Quality, Investment Attractiveness or evidence confidence.

## Company research-record status fields

Every company displays:

- Assessment Status: Discovery Only, Mini QBM, Full QBM or Archived
- Current Assessment Status: Current, Review Due or Update Required
- Research Record Completeness: Complete, Partial or Awaiting Review

Company-level research completeness must not be described as structural Database Integrity.
