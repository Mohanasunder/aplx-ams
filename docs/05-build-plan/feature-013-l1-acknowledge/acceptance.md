---
id: FEAT-013
id_prefix: FEAT
title: "FEAT-013: S-3: L1 Support Engineer Acknowledges a New Ticket — Acceptance Criteria"
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
# FEAT-013: S-3: L1 Support Engineer Acknowledges a New Ticket — Acceptance Criteria

## Input References
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-3
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-013 (REQ S-3). Criteria are copied verbatim from REQ-001 v0.3 § S-3.

## Acceptance Criteria
REQ-003 AC-1 REQ S-3 AC-1: Given a P2 ticket raised at 10:00 IST, when an L1 support engineer acknowledges it at 12:00 IST the same business day, then the response clock stops at 2 business hours and the response target is met (BR B-4).
REQ-003 AC-2 REQ S-3 AC-2: Given a ticket whose first L1 action was at 12:00 IST, when another L1 support engineer acknowledges it or acts on it at 13:00 IST, then the response clock stop time stays 12:00 IST (BR B-4).
REQ-003 AC-3 REQ S-3 AC-3: Given a P1 ticket raised at 10:00 IST, when the first L1 action on it is at 11:00 IST, then the response clock stops at exactly 1 business hour (100% of the response target) and the response target is breached, not met (BR B-4, BR B-8).
REQ-003 AC-4 REQ S-3 AC-4: Given a client user, an L2/L3 support engineer or a delivery manager, when they view a new ticket, then they cannot acknowledge it and the response clock keeps running (BR B-4).

## Test Scenarios
REQ-003 AC-1 REQ S-3 AC-1: Given a P2 ticket raised at 10:00 IST, when an L1 support engineer acknowledges ... — verify Given/When/Then conditions as stated above.
REQ-003 AC-2 REQ S-3 AC-2: Given a ticket whose first L1 action was at 12:00 IST, when another L1 support e... — verify Given/When/Then conditions as stated above.
REQ-003 AC-3 REQ S-3 AC-3: Given a P1 ticket raised at 10:00 IST, when the first L1 action on it is at 11:0... — verify Given/When/Then conditions as stated above.
REQ-003 AC-4 REQ S-3 AC-4: Given a client user, an L2/L3 support engineer or a delivery manager, when they ... — verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 § S-3; PIB-005 v0.1
- Downstream: FEAT-013-TASKS (builder task list); Phase 6 test set FEAT-013-TESTS

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
