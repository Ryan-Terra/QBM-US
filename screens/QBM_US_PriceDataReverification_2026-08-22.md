# QBM-US Systematic Price Data Re-verification — 22 August 2026

Triggered directly by investor question ("won't we need to do the same thing for all of the stocks in Target Portfolio and on the bench?") after a spot-check on Veracyte (VCYT) surfaced a $17 spread across three different price readings pulled on different days via general web search. Rather than fix VCYT alone, every ATH-proximity figure for every company then Add-rated (target portfolio or bench) was re-pulled from a single, reproducible source — Yahoo Finance historical data via `yfinance` — in one pass, on 22 August 2026. See [Methodology v1.22, Primary Price Data Source](../framework/QBM_US_Methodology.md#primary-price-data-source-added-v122) for the standing rule this prompted.

**Method:** for each ticker, pulled the most recent close (as "current price") and the max High over the trailing 1 year (as "52-week high") via `yfinance`, computed % of high and % below high directly. This is the same mechanical calculation the ATH Proximity Rule always specified — the fix is the *source*, not the formula.

## Target portfolio (8 holdings)

| Ticker | Old figure (source: mixed web search) | New figure (yfinance, 22 Aug) | Change |
|---|---|---|---|
| MA | 4.26% below all-time high ($601.77) | 2.9% below 52-week high ($598.04) | Immaterial — still clears comfortably either way. Note: $598.04 is the 52-week high, not necessarily the all-time high if that was set >1yr ago; the two were already known to be very close. |
| LLY | 2.8% below 52-week high | 2.9% below 52-week high | Immaterial, effectively identical |
| VCYT | 25.0% below (the figure that prompted this whole re-check) | 30.5% below ($42.31 vs. $60.91) | Still clears the 10% floor comfortably either way — the number was off, but not the conclusion |
| PTCT | 17.0% below | 23.2% below ($69.82 vs. $90.87) | Still clears comfortably, more room than believed |
| XNCR | ~1% below (within 1%) | 1.3% below ($27.80 vs. $28.16) | Immaterial, confirms the near-the-high finding that triggered the original ATH Rule build |
| ACAD | 3.6% below | 4.7% below ($29.50 vs. $30.96) | Immaterial, still fails the 10% floor either way |
| BDC | 19.9% below | 23.4% below ($122.46 vs. $159.86) | Still clears comfortably, more room than believed |
| BHE | 27.0% below | 27.7% below ($72.64 vs. $100.41) | Immaterial |

**No Implementation Readiness changes in the target portfolio.** All eight were already directionally correct; only precision improved.

## Bench (16 candidates)

| Ticker | Old figure | New figure (yfinance, 22 Aug) | Change |
|---|---|---|---|
| ROG | ~20-25% below (disclosed price conflict) | 25.1% below ($126.55 vs. $169.00) | **Resolves the disclosed conflict cleanly** — no change to Ready status |
| NEO | 2.9% below | 0.6% below ($16.98 vs. $17.08) | Tightened — still fails the ATH floor, now even closer to its high than believed |
| HRMY | 6.7% below | 6.7% below ($38.15 vs. $40.87) | Exact match, no change |
| **KRYS** | **15.8% below — believed to clear the ATH rule with real room** | **9.4% below ($346.58 vs. $382.54) — now inside the 10% band** | **Reversal.** KRYS now fails the ATH Proximity Rule. Its bench placement doesn't change (already benched for single-product concentration + binary catalyst, unrelated to ATH), but the earlier claim that "entry timing was never actually the blocker for it" is now false and has been corrected in the Dashboard and portfolio-construction record. |
| HQY | 1.8% below | 2.1% below ($105.41 vs. $107.62) | Immaterial |
| CNXN | 11.1% below | 11.5% below ($77.93 vs. $88.10) | Immaterial, still clears narrowly |
| DLB | ~21% below (estimate) | 11.7% below ($65.27 vs. $73.95) | **Materially tightened.** Still clears the 10% floor, but far more narrowly than the original estimate implied — the "Medium confidence, pending live-price confirmation" framing undersold how close this one actually is |
| AGYS | ~26% below (disclosed price conflict) | 21.7% below ($113.80 vs. $145.25) | **Resolves the disclosed conflict cleanly** — still clears comfortably |
| PI | ~25% below (estimate) | 33.0% below ($165.54 vs. $247.06) | More room than estimated, no change |
| **NTCT** | **7.1% below — believed to fail the ATH rule** | **15.0% below ($38.49 vs. $45.28) — clears** | **Reversal.** Ownership (3.82%) and selling (immaterial, ~$324K) were already clean — with the ATH rule now also clearing, **NTCT upgrades to fully Ready, no discount**, the second completely clean name in the batch alongside BDC. |
| **DGII** | **Claimed to be trading *above* its own 52-week high — failing the ATH rule outright** | **13.7% below ($74.91 vs. $86.84) — clears** | **Reversal, and the most striking one.** The "trading above its high" claim was simply wrong. DGII upgrades from Await Better Entry to Ready with Considerations (material CFO selling of $6.9M remains the live caveat). |
| **CTS** | **~4-6% below — believed to fail the ATH rule** | **16.9% below ($57.74 vs. $69.51) — clears** | **Reversal.** CTS upgrades from Await Better Entry to Ready with Considerations (material CEO selling of $8.48M remains the live caveat). |
| ARLO | 31.9% below | 34.3% below ($13.10 vs. $19.94) | Immaterial |
| PLXS | 10.85% below — "clears narrowly, watch closely" | 21.8% below ($240.14 vs. $307.06) | **Materially tightened in the other direction** — this one was believed to be a narrow, watch-closely clearance; it is actually comfortably clear. The "watch closely" framing was overcautious. |
| **KN** | **~3% below — believed to fail the ATH rule decisively** | **22.4% below ($33.32 vs. $42.93) — clears comfortably** | **Reversal, the largest swing found.** KN upgrades from Await Better Entry to Ready with Considerations (near-miss ownership and selling, partially offset by the disclosed insider buy, remain the live caveats). |
| SCSC | 14.4% below | 18.6% below ($54.35 vs. $66.78) | Immaterial — still clears the ATH rule; still fails the Valuation Ceiling on separate grounds (unaffected by this re-check) |

## Summary of consequential changes

**Four Implementation Readiness upgrades**, all within the bench (none currently funded, so no capital was misallocated by the errors):

| Ticker | Was | Now |
|---|---|---|
| NTCT | Await Better Entry | **Ready** (no discount) |
| DGII | Await Better Entry | Ready with Considerations |
| CTS | Await Better Entry | Ready with Considerations |
| KN | Await Better Entry | Ready with Considerations |

**One reversal in the other direction:**

| Ticker | Was | Now |
|---|---|---|
| KRYS | Believed to clear ATH rule | Now fails the ATH rule (bench placement unaffected — already benched for unrelated reasons) |

**No standing Add/Not-Advanced decision changed.** No target-portfolio holding's readiness changed. The corrections are confined to Implementation Readiness within the bench, plus general precision improvements across the board that didn't change any conclusion.

## What this means going forward

NTCT and BDC are now the two cleanest bench candidates — both fully Ready, no confidence discount of any kind. If the target portfolio is ever expanded again or a holding rotated, NTCT should be weighed alongside ROG as a top candidate, not overlooked on the strength of a since-corrected "fails the ATH rule" record.

This was a one-time full re-check, not a recurring process — the Evidence Staleness Re-verification Requirement (Methodology v1.21) already governs when target-portfolio holdings get re-checked going forward (30-day trigger), and the Primary Price Data Source rule (v1.22) governs how any future mechanical price check should be sourced.
