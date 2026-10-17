---
id: FEAT-022
id_prefix: FEAT
title: "FEAT-022: S-28: Client User Adds a Comment on Their Ticket — Acceptance Criteria"
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
# FEAT-022: S-28: Client User Adds a Comment on Their Ticket — Acceptance Criteria

## Input References
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-28
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-022 (REQ S-28). Criteria are copied verbatim from REQ-001 v0.3 § S-28.

## Acceptance Criteria
REQ-028 AC-1 REQ S-28 AC-1: Given a client user of client organization A, when they add a comment on a ticket of organization A, then the comment is saved on the ticket with the client user and the time, and internal users viewing the ticket see it.
REQ-028 AC-2 REQ S-28 AC-2: Given a ticket of organization A in awaiting client with resolution elapsed time 2 business hours, when a client user of organization A adds a comment, then awaiting client is cleared automatically and the paused SLA timers resume from 2 business hours (BR B-6).
REQ-028 AC-3 REQ S-28 AC-3: Given a ticket of organization A that is not in awaiting client, when a client user of organization A adds a comment, then the ticket status does not change.
REQ-028 AC-4 REQ S-28 AC-4: Given a client user of organization A, when they try to add a comment on a ticket of organization B, then it is refused and no comment is saved (BR B-20).

## Test Scenarios
REQ-028 AC-1 REQ S-28 AC-1: Given a client user of client organization A, when they add a comment on a ticke... — verify Given/When/Then conditions as stated above.
REQ-028 AC-2 REQ S-28 AC-2: Given a ticket of organization A in awaiting client with resolution elapsed time... — verify Given/When/Then conditions as stated above.
REQ-028 AC-3 REQ S-28 AC-3: Given a ticket of organization A that is not in awaiting client, when a client u... — verify Given/When/Then conditions as stated above.
REQ-028 AC-4 REQ S-28 AC-4: Given a client user of organization A, when they try to add a comment on a ticke... — verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 § S-28; PIB-005 v0.1
- Downstream: FEAT-022-TASKS (builder task list); Phase 6 test set FEAT-022-TESTS

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
