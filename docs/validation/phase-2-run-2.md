---
id: VAL-009
title: Phase 2 validation run 2
phase: 2
version: 0.1
template: validation-report
template_version: 2.0
status: Draft
author_agent: checker
approver: Tech lead
date: 2026-10-17
validation: Pending
---
> **One file per validation run per phase.** Each phase validation run produces one `phase-N-run-M.md` in `docs/validation/`. Use `--out docs/validation/phase-N-run-M.md` when calling `new_artifact.py`; never auto-name as `VAL-NNN.md`. M increments with each re-run of the same phase.

# Phase 2 validation run 2

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
Under validation (all Draft v0.1, `docs/02-requirements/`): PRS-001, EPC-001, REQ-001 (23 stories, 87 ACs), NFR-001, BR-001, BKL-001, GLO-001, RSK-002, SUM-002; log rows OQ-037 to OQ-045, A-009 to A-016, RSK-002 R-1 and R-2, R-4 to R-6 updates, DEC-024, DEC-025, 23 traceability-matrix rows. Evidence: PIB-002 v0.1, INT-002 v0.1 (Approved), SUM-001 v0.3 and the Approved Phase 1 artifacts.

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
First run on the Phase 2 requirements deliverables (loop count 0). Rules: `.ai/checker-rules/phase-2.md` in full, `.ai/standards/checker-and-fail-decision.md`. Scripts: `validate_artifact.py --check-links` Pass (all 12 files 0/0/0); `glossary_check.py check` skipped (no Approved glossary; manual scan found no avoided terms); `traceability.py check --phase 2` 4 goals, 5 epics, 0 gaps; `context_pack.py summaries 2` 0 problems.

## Verdict
<!-- guidance: Pass | Pass with warnings | Fail -->
Fail

## Scorecard
<!-- guidance: Result per validation layer (structural, input conformance, completeness, consistency, traceability, content quality) -->
| Layer | Result |
| --- | --- |
| Structural | Pass |
| Input conformance | Pass with notes; no design content; post-run answers reflected |
| Completeness | Minor gaps (M-6, M-7, M-8, M-11) |
| Consistency | Fail (M-1, M-3) |
| Traceability | Pass with warnings (M-10) |
| Content quality | Fail (M-2) |
| Producer self-check | 2 of 4 spot-checked claims do not fully hold (M-6, M-7) |

## Findings
<!-- guidance: Table: ID, location, description, severity (Blocker/Major/Minor), suggested fix -->
Blocker 0, Major 3, Minor 16. None non-overridable.

| ID | Location | Description | Severity | Suggested fix |
| --- | --- | --- | --- | --- |
| M-1 | BR-001 B-4, B-5 vs B-8; GLO-001 | Clock stopping exactly at target is met under B-4/B-5, breached under B-8 and the glossary | Major | One boundary everywhere; add an AC at exactly 100% |
| M-2 | BR-001 B-7; GLO-001 | "Open target" wording lets stopped (breached) clocks recalculate; priority change after Resolved and effect on escalation flag undefined | Major | Define open = clock still running; raise OQ or ask |
| M-3 | GLO-001 Acknowledgement vs B-4, S-3, S-5 | Acknowledgement = any first L1 action (glossary) vs explicit act (rules, stories) | Major | Align to one meaning; add AC for action before acknowledgement |
| M-4 | REQ S-4 AC-1 | Says response target 1 business hour after change though response already met | Minor | Reword per B-7 |
| M-5 | REQ S-4 AC-4 | Two cases in one AC | Minor | Split or drop audit part |
| M-6 | REQ S-21 AC-2, S-15 AC-2, S-13 AC-2; BR-001 | Unsourced criteria (generic sign-in error, refuse 0/negative hours, zero-denominator display) | Minor | Label as assumptions or confirm |
| M-7 | GLO-001 | Missing terms (ticket statuses, ticket reference, assignee, user account, role); SLA clock/timer synonyms | Minor | Add terms; pick one name |
| M-8 | PRS-001 F-2; EPC-001 E-1 | Say L1 marks awaiting client; S-8, B-6, A-013 say assigned engineer | Minor | Align; cite A-013 |
| M-9 | REQ S-8, S-2 | No story lets a client reply; S-2 "act on" vs view only | Minor | Fold into OQ-045 or reword |
| M-10 | traceability-matrix; EPC-001 E-5 | Inconsistent goal-link derivation; S-23 to G-4 weak | Minor | One rule; move S-23 to G-3 or justify |
| M-11 | REQ S-19 | No AC to end or replace a contract | Minor | Add AC or OQ |
| M-12 | REQ S-13, S-14 | Monthly report trigger and availability not stated | Minor | State or raise OQ |
| M-13 | REQ S-15 AC-3 | "Changed" effort entry without a criterion; who may record effort | Minor | Add criterion or OQ |
| M-14 | NFR-001 | Names-and-emails data limit not carried; "quickly" in N-2 | Minor | Add NFR or note; remove "quickly" |
| M-15 | PRS-001, EPC-001 | Goals cited "BRF-001 G-n" vs rule format "BRF G-N" | Minor | Use BRF G-N (check traceability script accepts it) |
| M-16 | PRS-001 G-2 | MTTR unit vs 3-day baseline not decided | Minor | Resolve in OQ-039 or note under R-4 |
| M-17 | RSK-002 R-1 | Overall rating text does not follow the RSK-001 method | Minor | Restate rating |
| M-18 | risk-register R-2, R-3, R-8 | Last reviewed Phase 1; R-2 MoSCoW outcome not recorded | Minor | Update R-2; confirm at gate risk review |
| M-19 | BR-001 B-12 | Formula wording proposed for confirmation at the gate | Minor | Approver confirms at review |

## Top Issues
<!-- guidance: Three to five most important findings in plain language -->
1. Met/breached boundary at exactly 100% is inconsistent (M-1).
2. B-7 "open target" goes beyond the human's answer (M-2).
3. "Acknowledgement" has two meanings (M-3).
4. Unsourced criteria and missing glossary terms (M-6, M-7).

## Unresolved From Earlier Runs
<!-- guidance: Findings still open from previous loops -->
None - run 1 covered only the intake artifacts, now Approved.

## Recommendation
<!-- guidance: The checker's advice (send back or proceed) with reasoning -->
Option C: send back with modified instructions, after asking the human short questions for M-1 to M-3; fix the Minors in the same pass.

## Decision Record
<!-- guidance: Options offered, option chosen, decided by, timestamp, reason (required when proceeding on a Fail) -->
Options A, B, C offered to Mohanasunder (Product owner / BA) on 2026-10-17. Chosen: C (send back with modified instructions). Answers: M-1 a clock stopped at exactly 100% of target is breached (met only if stopped before 100%); M-2 only running clocks recalculate on a priority change, stopped clocks keep their result, no priority change after Resolved, and the 50% escalation point moves with the new resolution target; M-3 any first L1 action on the ticket counts as acknowledgement and stops the response clock. Fix all 19 findings. Loop count becomes 1.

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
None.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
None.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: PRS-001, EPC-001, REQ-001, NFR-001, BR-001, BKL-001, GLO-001, RSK-002, SUM-002 (v0.1).
- Downstream: Not applicable - report feeds the Fail decision and human review only.

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)

## Approval Record
| Field | Value |
| --- | --- |
| Decision | Pending |
| Approver | Pending |
| Role | Pending |
| Conditions | None |
| Comments | None |
| Timestamp | Pending |
