---
id: FEAT-012
id_prefix: FEAT
title: "FEAT-012: S-2: Client User Follows Their Client Organization Tickets — Acceptance Criteria"
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
# FEAT-012: S-2: Client User Follows Their Client Organization Tickets — Acceptance Criteria

## Input References
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-2
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-012 (REQ S-2). Criteria are copied verbatim from REQ-001 v0.3 § S-2.

## Acceptance Criteria
REQ-002 AC-1 REQ S-2 AC-1: Given client organization A has 3 tickets and client organization B has 2 tickets, when a client user of organization A views tickets, then they see the 3 tickets of organization A, each with its status and priority, and none of organization B's tickets.
REQ-002 AC-2 REQ S-2 AC-2: Given a ticket of organization A is set to Resolved or Closed, when a client user of organization A views that ticket, then it shows the status Resolved or Closed.
REQ-002 AC-3 REQ S-2 AC-3: Given a client user of organization A, when they view one of their organization's tickets, then the audit trail is not shown (BR B-22).
REQ-002 AC-4 REQ S-2 AC-4: Given a client user of organization A viewing one of their organization's tickets after it is raised, when they try to change its priority, then the change is refused and the priority stays as it was (BR B-7).

## Test Scenarios
REQ-002 AC-1 REQ S-2 AC-1: Given client organization A has 3 tickets and client organization B has 2 ticket... — verify Given/When/Then conditions as stated above.
REQ-002 AC-2 REQ S-2 AC-2: Given a ticket of organization A is set to Resolved or Closed, when a client use... — verify Given/When/Then conditions as stated above.
REQ-002 AC-3 REQ S-2 AC-3: Given a client user of organization A, when they view one of their organization'... — verify Given/When/Then conditions as stated above.
REQ-002 AC-4 REQ S-2 AC-4: Given a client user of organization A viewing one of their organization's ticket... — verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 § S-2; PIB-005 v0.1
- Downstream: FEAT-012-TASKS (builder task list); Phase 6 test set FEAT-012-TESTS

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
