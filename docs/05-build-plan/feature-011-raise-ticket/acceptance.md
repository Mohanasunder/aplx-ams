---
id: FEAT-011
id_prefix: FEAT
title: "FEAT-011: S-1: Client User Raises a Ticket in the Portal — Acceptance Criteria"
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
# FEAT-011: S-1: Client User Raises a Ticket in the Portal — Acceptance Criteria

## Input References
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-1
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-011 (REQ S-1). Criteria are copied verbatim from REQ-001 v0.3 § S-1.

## Acceptance Criteria
REQ-001 AC-1 REQ S-1 AC-1: Given a signed-in client user of client organization A, when they raise a ticket with a type (incident or service request), one of organization A's SAP applications, a priority P1 to P4 and a description, then the ticket is created with the raise time, the response and resolution targets of that priority (BR B-1), and appears in the L1 queue.
REQ-001 AC-2 REQ S-1 AC-2: Given a client user raising a ticket, when the type, SAP application, priority or description is missing, then no ticket is created and the client user is told which field is missing.
REQ-001 AC-3 REQ S-1 AC-3: Given a client user of client organization A, when they try to raise a ticket for an SAP application of client organization B, then the ticket is refused and no ticket is created.
REQ-001 AC-4 REQ S-1 AC-4: Given a client user raises a ticket at 18:30 IST on a business day, when the SLA timers start, then elapsed business time stays 0 until 09:00 IST on the next business day (BR B-3).

## Test Scenarios
REQ-001 AC-1 REQ S-1 AC-1: Given a signed-in client user of client organization A, when they raise a ticket... — verify Given/When/Then conditions as stated above.
REQ-001 AC-2 REQ S-1 AC-2: Given a client user raising a ticket, when the type, SAP application, priority o... — verify Given/When/Then conditions as stated above.
REQ-001 AC-3 REQ S-1 AC-3: Given a client user of client organization A, when they try to raise a ticket fo... — verify Given/When/Then conditions as stated above.
REQ-001 AC-4 REQ S-1 AC-4: Given a client user raises a ticket at 18:30 IST on a business day, when the SLA... — verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 § S-1; PIB-005 v0.1
- Downstream: FEAT-011-TASKS (builder task list); Phase 6 test set FEAT-011-TESTS

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
