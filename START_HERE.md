# Start Here — QBM-US Investment Operating System

## Purpose

This document is the entry point for any person or AI assistant using the Quality Before Momentum — US (QBM-US) Investment Operating System.

It explains what to read, in what order, how authority is determined, and how to begin a fresh market scan. It is a navigation and execution guide only. It does not amend the QBM-US methodology or override any governing document.

## Independence from QBM

QBM-US is a separate system from the original QBM Investment Operating System (ASX-focused). Separate git repository, separate git history, separate holdings, separate methodology version. Nothing here amends QBM, and nothing in QBM amends this. QBM-US carries forward QBM's process, gates, scoring and decision framework as a starting point (v1.0, 13 August 2026) but is free to diverge — see the [QBM-US Methodology Changelog](framework/QBM_US_Methodology.md#changelog) for what has already changed.

## Source of truth

This repository is the authoritative source for QBM-US.

Do not rely on remembered versions, copied prompts, prior chat summaries or earlier recommendations when they conflict with the current repository.

## Governing hierarchy

Read and apply the governing documents in this order:

1. `framework/QBM_US_Investment_Charter.md`
2. `framework/QBM_US_Methodology.md`
3. `framework/QBM_US_Operating_Standard.md`

If two instructions conflict, the higher document in this hierarchy prevails.

Unlike QBM, the Methodology here is **versioned, not frozen**. Amendments are made directly by investor instruction and recorded in its Changelog — no formal Operational Change Register is required.

## Investor-specific preferences

After reading the governing documents, read:

4. `UserProfile.md`

`UserProfile.md` records investor preferences and ethical exclusions. It guides how QBM-US is applied but does not override the governing hierarchy.

## Live operating documents

Before assessing an existing portfolio, watchlist, company or current QBM-US operating state, read the relevant live documents:

- `live/QBM_US_Dashboard.md`
- `live/QBM_US_Company_Database.md`
- `live/QBM_US_Investment_Universe.md`
- `live/QBM_US_Standing_CMEA.md`
- `live/QBM_US_Review_Calendar.md`

As of 13 August 2026 these are all freshly created and empty — no scan has been run yet. Do not assume these documents are current merely because they exist. Check their dates, status and supporting evidence.

## Historical records

Use the following documents for audit history and prior reasoning only:

- `history/QBM_US_Decision_Journals.md`
- `history/QBM_US_Investment_Committee_Minutes.md`
- `history/QBM_US_Portfolio_Timeline.md`
- `history/QBM_US_CMEA_Archive.md`

Historical records must not be treated as current recommendations. They are append-only and should not be rewritten to reflect later outcomes.

## Fresh market scan procedure

When instructed to perform a completely fresh market scan:

1. Read this file.
2. Read the three governing documents in hierarchy order.
3. Read `UserProfile.md`.
4. Treat the current scan as a new decision cycle.
5. Assume no portfolio, watchlist, preferred company or prior recommendation unless the investor explicitly supplies current information.
6. Use current market prices, company announcements, SEC filings and other reliable current evidence.
7. Apply every QBM-US gatekeeper, scoring rule, evidence standard and decision rule exactly as defined in the authoritative documents.
8. Do not lower standards to produce a minimum number of candidates.
9. Clearly distinguish verified facts, estimates, judgement and unresolved uncertainty.
10. Return **No Buy** when no company genuinely qualifies.

Note: no Standing CMEA exists yet (see `live/QBM_US_Standing_CMEA.md`). Research and adopt one before or alongside the first Full QBM-US scan — do not invent a macro view to fill the gap.

## Existing portfolio or company review procedure

When reviewing an existing holding, watchlist or named company:

1. Read the governing documents and `UserProfile.md` first.
2. Read the relevant live operating documents.
3. Confirm the investor's current units, available cash, capital ceiling and any other portfolio constraints rather than assuming old figures remain valid.
4. Obtain current market and company information.
5. Reassess from current evidence rather than repeating a previous score or recommendation.
6. Record any formal QBM-US decision in the authoritative location required by the operating standard.

## Evidence and data rules

- Never invent missing figures, prices, dates, filings or scores.
- Use current sources for live market decisions.
- Identify stale, incomplete or conflicting evidence.
- Separate fact from inference and opinion.
- Explain why a company fails as clearly as why another passes.
- Do not present historical QBM-US material as live evidence without revalidation.

## Repository discipline

- Every category of information has one authoritative location.
- Do not duplicate methodology in onboarding prompts or new files.
- Do not create new permanent documents unless the information cannot logically reside in an existing authoritative document.
- Preserve append-only historical records.
- Keep investor preferences in `UserProfile.md` rather than embedding them in the methodology.
- Amend the Methodology directly when the investor requests a rule change — record it as a new version with a one-line Changelog reason. This is the entire amendment process; there is no register to fill out.

## Minimal onboarding prompt

A future AI session can begin with:

> Read `START_HERE.md` in my QBM-US repository and follow it exactly. Then perform a completely fresh US market scan using current data. Assume I have no portfolio or watchlist unless I provide one.
