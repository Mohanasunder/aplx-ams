---
id: FEAT-023-ACC
id_prefix: FEAT
title: "FEAT-023: S-29: Internal User Adds a Comment on a Ticket â€” Acceptance Criteria"
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
# FEAT-023: S-29: Internal User Adds a Comment on a Ticket â€” Acceptance Criteria

## Input References
- REQ-001 v0.3 â€” APLX AMS: User Stories (Approved 2026-10-17) Â§ S-29
- PIB-005 v0.1 â€” Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-023 (REQ S-29). Criteria are copied verbatim from REQ-001 v0.3 Â§ S-29.

## Acceptance Criteria
REQ-029 AC-1 REQ S-29 AC-1: Given a ticket of client organization A, when a support engineer or the delivery manager adds a comment on it, then the comment is saved on the ticket with the user and the time, and client users of organization A viewing the ticket see it (BR B-6).
REQ-029 AC-2 REQ S-29 AC-2: Given a ticket of organization A in awaiting client with resolution elapsed time 2 business hours, when an internal user adds a comment, then the ticket stays in awaiting client and its SLA timers stay paused at 2 business hours (BR B-6).
REQ-029 AC-3 REQ S-29 AC-3: Given an internal user's comment on a ticket of organization A, when a client user of organization B lists or opens tickets, then the comment is not shown to them (BR B-20).
REQ-029 AC-4 REQ S-29 AC-4: Given a new P2 ticket raised at 10:00 IST with no L1 action yet, when an L1 support engineer adds a comment on it at 11:00 IST, then the comment is the acknowledgement: the response clock stops at 1 business hour and the response target is met (BR B-4).

## Test Scenarios
REQ-029 AC-1 REQ S-29 AC-1: Given a ticket of client organization A, when a support engineer or the delivery... â€” verify Given/When/Then conditions as stated above.
REQ-029 AC-2 REQ S-29 AC-2: Given a ticket of organization A in awaiting client with resolution elapsed time... â€” verify Given/When/Then conditions as stated above.
REQ-029 AC-3 REQ S-29 AC-3: Given an internal user's comment on a ticket of organization A, when a client us... â€” verify Given/When/Then conditions as stated above.
REQ-029 AC-4 REQ S-29 AC-4: Given a new P2 ticket raised at 10:00 IST with no L1 action yet, when an L1 supp... â€” verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 Â§ S-29; PIB-005 v0.1
- Downstream: FEAT-023-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
