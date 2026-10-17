---
id: FEAT-014-ACC
id_prefix: FEAT
title: "FEAT-014: S-4: L1 Support Engineer Changes a Ticket Priority â€” Acceptance Criteria"
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
# FEAT-014: S-4: L1 Support Engineer Changes a Ticket Priority â€” Acceptance Criteria

## Input References
- REQ-001 v0.3 â€” APLX AMS: User Stories (Approved 2026-10-17) Â§ S-4
- PIB-005 v0.1 â€” Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-014 (REQ S-4). Criteria are copied verbatim from REQ-001 v0.3 Â§ S-4.

## Acceptance Criteria
REQ-004 AC-1 REQ S-4 AC-1: Given a P3 ticket raised at 10:00 IST Monday with no L1 action yet, when an L1 support engineer changes the priority to P1 at 12:00 IST with a reason, then the change is the first L1 action, so the response clock stops at 2 business hours and is judged against the new P1 response target of 1 business hour: breached, not met (BR B-4, OQ-046); and the running resolution clock recalculates to 4 business hours from 10:00 IST (resolution due 14:00 IST Monday) (BR B-7).
REQ-004 AC-2 REQ S-4 AC-2: Given a P1 ticket raised at 09:00 IST Monday whose response clock stopped at 10:30 IST (1.5 business hours, response target breached), when an L1 support engineer changes the priority to P3 at 11:00 IST with a reason, then the response clock stays breached and only the running resolution clock recalculates to 27 business hours from 09:00 IST (BR B-7, BR B-8).
REQ-004 AC-3 REQ S-4 AC-3: Given an L1 support engineer changing a priority, when no reason is entered, then the priority does not change.
REQ-004 AC-4 REQ S-4 AC-4: Given a ticket set to Resolved, when an L1 support engineer tries to change its priority, then the change is refused and the priority and both stopped clocks keep their values (BR B-7).

## Test Scenarios
REQ-004 AC-1 REQ S-4 AC-1: Given a P3 ticket raised at 10:00 IST Monday with no L1 action yet, when an L1 s... â€” verify Given/When/Then conditions as stated above.
REQ-004 AC-2 REQ S-4 AC-2: Given a P1 ticket raised at 09:00 IST Monday whose response clock stopped at 10:... â€” verify Given/When/Then conditions as stated above.
REQ-004 AC-3 REQ S-4 AC-3: Given an L1 support engineer changing a priority, when no reason is entered, the... â€” verify Given/When/Then conditions as stated above.
REQ-004 AC-4 REQ S-4 AC-4: Given a ticket set to Resolved, when an L1 support engineer tries to change its ... â€” verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 Â§ S-4; PIB-005 v0.1
- Downstream: FEAT-014-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
