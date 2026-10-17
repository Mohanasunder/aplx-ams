---
id: VAL-003
title: Phase 1 validation run 2
phase: 1
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

# Phase 1 validation run 2

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
Artifacts under validation (all Draft v0.1): BRF-001 `business-brief.md`, PER-001 `personas.md`, SCP-001 `scope-statement.md`, RSK-001 `risks.md`, PRC-001 `process-maps.md`, SUM-001 `SUMMARY.md` (all in `docs/01-discovery/`); log rows OQ-015 to OQ-022, A-004 to A-007, RSK R-1 to R-8. Evidence base: INT-001 v0.1, PIB-001 v0.1, IRC-002 v0.1 (Approved), `project.md`.

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Run 2 of Phase 1 validation; first run for the discovery deliverables (loop count 0). Rules: `.ai/checker-rules/phase-1.md` in full, `.ai/standards/checker-and-fail-decision.md`. Validator patch for collection headings authorized by DEC-019 (not scored). Script results: `validate_artifact.py --check-links` Fail (BRF-001 1 Major, all others Pass); `context_pack.py summaries 1` 0 problems; `spec_impact.py records` and `stale` 0.

## Verdict
<!-- guidance: Pass | Pass with warnings | Fail -->
Fail

## Scorecard
<!-- guidance: Result per validation layer (structural, input conformance, completeness, consistency, traceability, content quality) -->
| Layer | Result |
| --- | --- |
| Structural | Fail (F-01) |
| Input conformance | Pass: all inputs cited as Approved v0.1; nothing invented; inferences labelled A-005 to A-007; within the Phase 1 boundary |
| Completeness | Pass with warnings (F-03, F-04) |
| Consistency | Pass with warnings (F-02, F-04, F-07) |
| Traceability | Pass |
| Content quality | Fail (F-01); warnings F-05, F-06, F-08; every risk has owner, mitigation, register row |
| Collection-file checks | Pass: P-1 to P-3, R-1 to R-8, M-1 to M-3 numbered in order; register rows match |
| Producer self-check | Pass with warnings |

## Findings
<!-- guidance: Table: ID, location, description, severity (Blocker/Major/Minor), suggested fix -->
Blocker 0, Major 1, Minor 7. All overridable. No OQ or A ID collisions.

| ID | Location | Description | Severity | Suggested fix |
| --- | --- | --- | --- | --- |
| F-01 | BRF-001 § Quality Checklist; § Business Goals And KPIs | Goals not measurable: G-1 to G-3 have no baseline or target (OQ-001); G-4 has no KPI (OQ-020). Box correctly left unticked; producer cannot fix without inventing numbers | Major | Human answers OQ-001 and OQ-020 (then option C), or records a decision on how and when baselines are set and proceeds (option B) |
| F-02 | PRC-001 PP-1.2, PP-2.3, PP-3.2 vs BRF-001 G-4 | "No single view" pain points mapped to G-3 in process maps but to G-4 in the brief | Minor | Map them to G-4 (KPI pending OQ-020) or record that G-3 covers them |
| F-03 | SUM-001 Open Items; BRF-001 § Open Questions; RSK-001 R-4 | High OQ-016 (SLA compliance baseline) not in the High list or cited by BRF/R-4 | Minor | Add OQ-016 to those places |
| F-04 | assumptions-log A-001 to A-007 | A-001 still says "about 2027-01-17"; "Artifact(s) affected" lists incomplete | Minor | Remove "about"; complete the lists |
| F-05 | risk-register "Last reviewed" | Shows `2026-10-17`; required format `Phase 1, 2026-10-17` (becomes Major at the gate) | Minor | Set during the gate risk review |
| F-06 | SCP-001 OS-3, IS-6 | OS-3 is a process choice, not a product exclusion; IS-6 lists users, not a capability | Minor | Remove OS-3; recast IS-6 |
| F-07 | PRC-001 diagram labels M-1.3, M-1.4, M-2.4 | System labels omit "(unconfirmed)" shown in the step table | Minor | Add "unconfirmed" |
| F-08 | open-questions-log OQ-005, OQ-015, OQ-017, OQ-018 | Partial overlap; same person asked the same thing twice | Minor | Cross-reference or narrow OQ-018 |

Notes (not scored): SUM-001 `approver` front matter is a template default; risk-register header states ID format `RSK-NNN R-N` while the standard and rows use `RSK R-N` (human-owned).

## Top Issues
<!-- guidance: Three to five most important findings in plain language -->
1. The only Major is missing KPI numbers (F-01); only a human answer or recorded decision closes it.
2. The brief and process maps disagree on which goal the "one view" problem affects (F-02).
3. High OQ-016 is missing from the gate list (F-03).
4. Log fixes needed (F-04, F-05); F-05 becomes Major at the gate.
5. Scope items OS-3 and IS-6 are not product scope (F-06).

## Unresolved From Earlier Runs
<!-- guidance: Findings still open from previous loops -->
- Run 1 F-03 (accepted): OQ-002 answer, PIB-001 and IRC-002 still say "client contact names and emails"; deliverables correctly say "names and emails". Approved artifacts need an SCR to align.
- Run 1 F-04 (accepted): A-001 "about"; rescored as part of F-04.
- Run 1 F-01, F-02: resolved.

## Recommendation
<!-- guidance: The checker's advice (send back or proceed) with reasoning -->
Do not send back as-is: the Major needs human information. Option C if OQ-001 and OQ-020 can be answered now (send back with answers plus F-02 to F-08); otherwise option B with F-01 accepted, a reason in `fail-decisions-log.md`, and ideally a decision on how and when baselines are measured (RSK R-4 mitigation).

## Decision Record
<!-- guidance: Options offered, option chosen, decided by, timestamp, reason (required when proceeding on a Fail) -->
Options A, B, C offered to Mohanasunder (Business owner / BA) on 2026-10-17. Chosen: C (send back with modified instructions), by Mohanasunder, 2026-10-17. Instructions: KPI values supplied (OQ-001: SLA compliance 80% to 95%; MTTR 3 days to 1 day; admin and reporting 40 to 10 hours per month. OQ-020: G-4 KPI is % of clients on the dashboard, target 100%); fix F-01 to F-04 and F-06 to F-08; F-05 deferred to the gate risk review. Loop count becomes 1.

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
None.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
None.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: BRF-001, PER-001, SCP-001, RSK-001, PRC-001, SUM-001 (v0.1).
- Downstream: Not applicable - report feeds the human review of these artifacts only.

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
