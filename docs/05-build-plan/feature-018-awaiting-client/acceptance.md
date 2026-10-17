---
id: FEAT-018
id_prefix: FEAT
title: "FEAT-018: S-8: Support Engineer Marks a Ticket as Awaiting Client — Acceptance Criteria"
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
# FEAT-018: S-8: Support Engineer Marks a Ticket as Awaiting Client — Acceptance Criteria

## Input References
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-8
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-018 (REQ S-8). Criteria are copied verbatim from REQ-001 v0.3 § S-8.

## Acceptance Criteria
REQ-008 AC-1 REQ S-8 AC-1: Given a P3 ticket with its resolution clock running at 2 business hours, when the assigned support engineer sets awaiting client and clears it 4 business hours later, then the resolution elapsed time is still 2 business hours at the moment it is cleared.
REQ-008 AC-2 REQ S-8 AC-2: Given a ticket in awaiting client, when business hours pass, then neither SLA timer changes state.
REQ-008 AC-3 REQ S-8 AC-3: Given a ticket in awaiting client, when the status is cleared, then the paused SLA timers resume from the elapsed time at the pause.
REQ-008 AC-4 REQ S-8 AC-4: Given a client user or a support engineer who is not the assigned support engineer, when they view a ticket that is not awaiting client, then they cannot set awaiting client (BR B-6, OQ-045).

## Test Scenarios
REQ-008 AC-1 REQ S-8 AC-1: Given a P3 ticket with its resolution clock running at 2 business hours, when th... — verify Given/When/Then conditions as stated above.
REQ-008 AC-2 REQ S-8 AC-2: Given a ticket in awaiting client, when business hours pass, then neither SLA ti... — verify Given/When/Then conditions as stated above.
REQ-008 AC-3 REQ S-8 AC-3: Given a ticket in awaiting client, when the status is cleared, then the paused S... — verify Given/When/Then conditions as stated above.
REQ-008 AC-4 REQ S-8 AC-4: Given a client user or a support engineer who is not the assigned support engine... — verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 § S-8; PIB-005 v0.1
- Downstream: FEAT-018-TASKS (builder task list); Phase 6 test set FEAT-018-TESTS

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
