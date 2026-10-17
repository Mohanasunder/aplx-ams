---
id: FEAT-019
id_prefix: FEAT
title: "FEAT-019: S-9: SLA Timers Count Business Hours Against the Standard SLA — Acceptance Criteria"
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
# FEAT-019: S-9: SLA Timers Count Business Hours Against the Standard SLA — Acceptance Criteria

## Input References
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-9
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-019 (REQ S-9). Criteria are copied verbatim from REQ-001 v0.3 § S-9.

## Acceptance Criteria
REQ-009 AC-1 REQ S-9 AC-1: Given a P1 ticket raised at 17:30 IST on Friday, when the next business day starts, then the response target falls due at 09:30 IST on Monday (0.5 business hours on Friday and 0.5 on Monday).
REQ-009 AC-2 REQ S-9 AC-2: Given a P3 ticket raised at 10:00 IST on the business day before a date on the company holiday list, when elapsed business time is counted, then the holiday contributes 0 business hours.
REQ-009 AC-3 REQ S-9 AC-3: Given tickets of P1, P2, P3 and P4, when they are raised, then their response and resolution targets are 1 and 4, 4 and 9, 9 and 27, and 18 and 45 business hours (BR B-1).
REQ-009 AC-4 REQ S-9 AC-4: Given a ticket raised at 08:00 IST on a business day, when the clocks start, then elapsed business time is 0 until 09:00 IST the same day.

## Test Scenarios
REQ-009 AC-1 REQ S-9 AC-1: Given a P1 ticket raised at 17:30 IST on Friday, when the next business day star... — verify Given/When/Then conditions as stated above.
REQ-009 AC-2 REQ S-9 AC-2: Given a P3 ticket raised at 10:00 IST on the business day before a date on the c... — verify Given/When/Then conditions as stated above.
REQ-009 AC-3 REQ S-9 AC-3: Given tickets of P1, P2, P3 and P4, when they are raised, then their response an... — verify Given/When/Then conditions as stated above.
REQ-009 AC-4 REQ S-9 AC-4: Given a ticket raised at 08:00 IST on a business day, when the clocks start, the... — verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 § S-9; PIB-005 v0.1
- Downstream: FEAT-019-TASKS (builder task list); Phase 6 test set FEAT-019-TESTS

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
