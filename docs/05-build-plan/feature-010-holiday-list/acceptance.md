---
id: FEAT-010
id_prefix: FEAT
title: "FEAT-010: S-24: Delivery Manager Maintains the Company Holiday List — Acceptance Criteria"
phase: 5
version: 0.1
template: feature-acceptance
template_version: 1.1
status: In review
author_agent: build-planner
approver: Tech lead
default_approver: Tech lead
default_folder: docs/05-build-plan
date: 2026-10-17
validation: Pending
---
# FEAT-010: S-24: Delivery Manager Maintains the Company Holiday List — Acceptance Criteria

## Input References
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-24
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-010 (REQ S-24). Criteria are copied verbatim from REQ-001 v0.3 § S-24.

## Acceptance Criteria
REQ-024 AC-1 REQ S-24 AC-1: Given the delivery manager adds 2027-01-26 (a Tuesday) to the company holiday list before that date, when a P3 ticket raised at 10:00 IST on Monday 2027-01-25 has its elapsed business time counted, then 2027-01-26 contributes 0 business hours (BR B-2).
REQ-024 AC-2 REQ S-24 AC-2: Given 2027-03-15 (a Monday) was on the company holiday list, when the delivery manager removes it before that date, then 2027-03-15 counts as a business day of 9 business hours (BR B-2).
REQ-024 AC-3 REQ S-24 AC-3: Given an L1 support engineer, an L2/L3 support engineer or a client user, when they try to add or remove a date on the company holiday list, then the change is refused (BR B-21).
REQ-024 AC-4 REQ S-24 AC-4: Given a P3 ticket raised at 09:00 IST on Monday 2027-02-01 whose resolution clock has counted 3 business hours by 12:00 IST, when the delivery manager adds 2027-02-01 to the company holiday list at 12:00 IST, then the 3 business hours stay counted and no further business time is counted on 2027-02-01 after 12:00 IST (BR B-2, OQ-050).

## Test Scenarios
REQ-024 AC-1 REQ S-24 AC-1: Given the delivery manager adds 2027-01-26 (a Tuesday) to th... — verify Given/When/Then conditions as stated above.
REQ-024 AC-2 REQ S-24 AC-2: Given 2027-03-15 (a Monday) was on the company holiday list... — verify Given/When/Then conditions as stated above.
REQ-024 AC-3 REQ S-24 AC-3: Given an L1 support engineer... — verify Given/When/Then conditions as stated above.
REQ-024 AC-4 REQ S-24 AC-4: Given a P3 ticket raised at 09:00 IST on Monday 2027-02-01 w... — verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 § S-24; PIB-005 v0.1
- Downstream: FEAT-010-TASKS (builder task list); Phase 6 test set FEAT-010-TESTS

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
