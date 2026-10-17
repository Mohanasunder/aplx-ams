---
id: VAL-016
title: Phase 3 validation run 4
phase: 3
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

# Phase 3 validation run 4

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
Part A: SCR S-4 (Draft); NFR-001, REQ-001, BR-001, GLO-001, EPC-001, BKL-001, PRS-001 v0.3; SUM-002 v0.4. Part B: PIB-003, INT-003, IRC-004 v0.2 (citation-only revision of Approved v0.1). Part C: ARC-001 v0.2, TEC-001 v0.2, ADR-001 v0.2 (A-1 to A-17), THR-001, TOP-001, CST-001, RSK-003 v0.2, SUM-003; log rows OQ-052 to OQ-066, A-030 to A-038, RSK-003 R-1 to R-10; DEC-027 to DEC-029.

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Run 4 of Phase 3 validation (failed rounds so far: 2 of 3). Scripts: `validate_artifact.py --check-links` all 23 artifacts Pass (only the Approved S-1 template "etc." warning); `spec_impact.py records` 0 unrecorded; `stale` 0; `spike.py check` 0 problems (non-overridable check passes); `context_pack.py summaries 3` 0 problems; `traceability.py check --phase 2` 0 gaps; glossary skipped (no Approved glossary). Simulation with all Drafts Approved: glossary 65 terms 0 problems; stale 47.

## Verdict
<!-- guidance: Pass | Pass with warnings | Fail -->
Fail (Part A Pass with warnings; Part B Fail; Part C Fail)

## Scorecard
<!-- guidance: Result per validation layer (structural, input conformance, completeness, consistency, traceability, content quality) -->
| Layer | A | B | C |
| --- | --- | --- | --- |
| Structural | Pass | Pass | Pass |
| Input conformance | Pass | Fail (B-1) | Fail (C-1) |
| Completeness | Pass | Pass with warnings | Pass |
| Consistency | Pass with warnings | Pass with warnings | Fail (C-2, C-3) |
| Traceability | Pass | Pass | Pass with warnings |
| Content quality | Pass with warnings | Pass | Fail (C-4) |

## Findings
<!-- guidance: Table: ID, location, description, severity (Blocker/Major/Minor), suggested fix -->
Part A: 0 Blocker, 0 Major, 7 Minor. Part B: 1 Major, 3 Minor. Part C: 4 Major, 7 Minor. None non-overridable.

| ID | Location | Description | Severity | Suggested fix |
| --- | --- | --- | --- | --- |
| A-1 | REQ S-32 AC-4 | Refers to password values not given in AC-1 to AC-3 | Minor | Give values or generalise |
| A-2 | NFR N-6 | "0 password values" unverifiable for unknown names (OQ-065) | Minor | Narrow wording or leave to R-10 |
| A-3 | GLO Security event | Definition excludes unknown names; "Account name" undefined | Minor | Reword; add term |
| A-4 | BR B-22 | No pointer to B-24 replacement | Minor | Add pointer |
| A-5 | NFR N-6 | Counts types, not events | Minor | Reword |
| A-6 | SCR S-4 Work Stopped / Impact | Does not match what happened | Minor | Update |
| A-7 | SUM-002 | "Phase 3 input brief (not yet created)"; preamble becomes false | Minor | Update |
| B-1 | PIB-003, IRC-004 | Cite INT-003 v0.1 (now v0.2) | Major | Cite v0.2 |
| B-2 | PIB-003, IRC-004 verdicts | Misstate when producers started | Minor | Reword |
| B-3 | PIB-003, IRC-004 | OQ-052 still "Open" | Minor | Update |
| B-4 | PIB-003 | No pointer to S-32, S-33, B-24, N-6 change | Minor | Add if allowed |
| C-1 | All Phase 3 deliverables | Mixed and superseded citations; 47 stale at approval | Major | After S-4 and Part B are Approved, refresh all citations |
| C-2 | THR-001 | Not updated for OQ-056, OQ-066 (T-30 still undecided) | Major | Revise |
| C-3 | THR vs ADR A-14, A-17, TOP | Contradiction on TLS key recovery copy vs new certificate | Major | Architect decides one approach |
| C-4 | risk-register | Inherited Open/Mitigating rows not reviewed in Phase 3 | Major | Gate risk review |
| C-5 | TOP, CST | Out-of-date status text; OQ-066 missing | Minor | Update |
| C-6 | TOP, THR | Unsourced Applexus facts (package source; Windows machines) | Minor | Assumption/OQ or remove |
| C-7 | SUM-003 | Incomplete S-4 list and open-risks list | Minor | Complete |
| C-8 | THR, ADR A-16, TOP | Ambiguous audit view wording; Uptime Kuma access mismatch | Minor | Align |
| C-9 | ADR A-17, THR | Compose file secrets ownership may not apply | Minor | Verify in Phase 4/8 |
| C-10 | ADR A-7, THR T-7 | Session limits have no Phase 2 source | Minor | Record a DEC |
| C-11 | ADR-001 checklist | Approved-inputs claim without exception note | Minor | Note exception |

## Top Issues
<!-- guidance: Three to five most important findings in plain language -->
1. 47 citations go stale at approval (C-1, B-1); order: S-4 approved, Part B approved, then refresh.
2. THR-001 not updated for answered OQs (C-2).
3. TLS key recovery contradiction affecting RTO (C-3).
4. Inherited risks not reviewed in Phase 3 (C-4).

## Unresolved From Earlier Runs
<!-- guidance: Findings still open from previous loops -->
None; VAL-013 to VAL-015 items closed.

## Recommendation
<!-- guidance: The checker's advice (send back or proceed) with reasoning -->
Part A proceed; Part B send back (B-1); Part C send back after A and B are approved. Near the loop limit: the human should decide C-3 and run the C-4 risk review directly.

## Decision Record
<!-- guidance: Options offered, option chosen, decided by, timestamp, reason (required when proceeding on a Fail) -->
Mohanasunder (Architect / tech lead; also Product owner / BA) on 2026-10-17 chose option C (send back with modified instructions) for Parts B and C, and agreed the order: fix Part A minors, approve SCR S-4 and its revisions, fix Part B, approve PIB-003/INT-003/IRC-004 v0.2, then producers fix C-1 to C-11, then a final check. Human answers: C-3 keep a protected recovery copy of the production certificate and key (root-only, on the test server) and restore it, so users' trust survives within the RTO; C-4 inherited risks confirmed as stated, RSK R-3 closed (server capacity recorded by OQ-055), Last reviewed "Phase 3, 2026-10-17"; C-10 session limits recorded as DEC-030. Loop count becomes 3 of 3 (limit reached); the human resolved the open decisions directly per the loop-limit rule.

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
None.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
None.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: ARC-001, TEC-001, ADR-001, RSK-003 (v0.2); THR-001, TOP-001, CST-001, SUM-003 (v0.1); VAL-015.
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
