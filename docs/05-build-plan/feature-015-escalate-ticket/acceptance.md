---
id: FEAT-015-ACC
id_prefix: FEAT
title: "FEAT-015: S-5: L1 Support Engineer Escalates a Ticket to L2/L3 â€” Acceptance Criteria"
phase: 5
version: 0.1
template: feature-acceptance
template_version: 1.1
status: Approved
author_agent: build-planner
approver: Mohanasunder
default_approver: Tech lead
default_folder: docs/05-build-plan
date: 2026-10-17
validation: Pass
---
# FEAT-015: S-5: L1 Support Engineer Escalates a Ticket to L2/L3 â€” Acceptance Criteria

## Input References
- REQ-001 v0.3 â€” APLX AMS: User Stories (Approved 2026-10-17) Â§ S-5
- PIB-005 v0.1 â€” Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-015 (REQ S-5). Criteria are copied verbatim from REQ-001 v0.3 Â§ S-5.

## Acceptance Criteria
REQ-005 AC-1 REQ S-5 AC-1: Given a P2 ticket raised at 10:00 IST in the L1 queue with no L1 action yet, when an L1 support engineer assigns it to an L2/L3 support engineer at 11:00 IST, then the ticket appears in that L2/L3 support engineer's assigned tickets, leaves the L1 queue, and the response clock stops at 1 business hour because the assignment is the first L1 action (BR B-4).
REQ-005 AC-2 REQ S-5 AC-2: Given a ticket with the escalation flag, when an L1 support engineer assigns it to an L2/L3 support engineer, then the escalation flag is removed (BR B-10).
REQ-005 AC-3 REQ S-5 AC-3: Given a ticket is assigned to an L2/L3 support engineer, when the assignment is saved, then the audit trail holds the old and new assigned support engineer, the user and the time (BR B-22).
REQ-005 AC-4 REQ S-5 AC-4: Given a client user, when they view their organization's ticket, then they cannot change its assignment.

## Test Scenarios
REQ-005 AC-1 REQ S-5 AC-1: Given a P2 ticket raised at 10:00 IST in the L1 queue with no L1 action yet, whe... â€” verify Given/When/Then conditions as stated above.
REQ-005 AC-2 REQ S-5 AC-2: Given a ticket with the escalation flag, when an L1 support engineer assigns it ... â€” verify Given/When/Then conditions as stated above.
REQ-005 AC-3 REQ S-5 AC-3: Given a ticket is assigned to an L2/L3 support engineer, when the assignment is ... â€” verify Given/When/Then conditions as stated above.
REQ-005 AC-4 REQ S-5 AC-4: Given a client user, when they view their organization's ticket, then they canno... â€” verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 Â§ S-5; PIB-005 v0.1
- Downstream: FEAT-015-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
| Decision | Approve |
| Approver | Mohanasunder |
| Role | Architect / tech lead |
| Version | 0.1 |
| Conditions | None |
| Comments | None |
| Timestamp | 2026-10-17 18:47 UTC |
