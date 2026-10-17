---
id: FEAT-021
id_prefix: FEAT
title: "FEAT-021: S-11: Ticket Is Flagged for Escalation at L1 Target — Acceptance Criteria"
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
# FEAT-021: S-11: Ticket Is Flagged for Escalation at L1 Target — Acceptance Criteria

## Input References
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-11
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-021 (REQ S-11). Criteria are copied verbatim from REQ-001 v0.3 § S-11.

## Acceptance Criteria
REQ-011 AC-1 REQ S-11 AC-1: Given a P1 ticket still with L1, when its resolution elapsed time reaches 2 business hours (50% of 4), then the ticket shows the escalation flag.
REQ-011 AC-2 REQ S-11 AC-2: Given a P2 ticket still with L1 at 3 business hours of resolution elapsed time (escalation point 4.5 business hours, 50% of 9), when an L1 support engineer changes the priority to P1 with a reason, then the escalation point moves to 2 business hours (50% of the new 4-hour resolution target) and the ticket shows the escalation flag at the change (BR B-7, BR B-10).
REQ-011 AC-3 REQ S-11 AC-3: Given a P1 ticket assigned to an L2/L3 support engineer at 1 business hour, when its resolution elapsed time reaches 2 business hours, then no escalation flag is shown.
REQ-011 AC-4 REQ S-11 AC-4: Given a P1 ticket still with L1 showing the escalation flag at 2.5 business hours of resolution elapsed time, when an L1 support engineer changes the priority to P2 with a reason, then the escalation point moves to 4.5 business hours (50% of 9), the flag clears at the change, and the flag shows again when the resolution elapsed time reaches 4.5 business hours (BR B-7, BR B-10).

## Test Scenarios
REQ-011 AC-1 REQ S-11 AC-1: Given a P1 ticket still with L1, when its resolution elapsed time reaches 2 busi... — verify Given/When/Then conditions as stated above.
REQ-011 AC-2 REQ S-11 AC-2: Given a P2 ticket still with L1 at 3 business hours of resolution elapsed time (... — verify Given/When/Then conditions as stated above.
REQ-011 AC-3 REQ S-11 AC-3: Given a P1 ticket assigned to an L2/L3 support engineer at 1 business hour, when... — verify Given/When/Then conditions as stated above.
REQ-011 AC-4 REQ S-11 AC-4: Given a P1 ticket still with L1 showing the escalation flag at 2.5 business hour... — verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 § S-11; PIB-005 v0.1
- Downstream: FEAT-021-TASKS (builder task list); Phase 6 test set FEAT-021-TESTS

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
