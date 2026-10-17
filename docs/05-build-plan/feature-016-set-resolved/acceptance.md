---
id: FEAT-016-ACC
id_prefix: FEAT
title: "FEAT-016: S-6: Support Engineer Sets a Ticket to Resolved â€” Acceptance Criteria"
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
# FEAT-016: S-6: Support Engineer Sets a Ticket to Resolved â€” Acceptance Criteria

## Input References
- REQ-001 v0.3 â€” APLX AMS: User Stories (Approved 2026-10-17) Â§ S-6
- PIB-005 v0.1 â€” Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-016 (REQ S-6). Criteria are copied verbatim from REQ-001 v0.3 Â§ S-6.

## Acceptance Criteria
REQ-006 AC-1 REQ S-6 AC-1: Given a P2 ticket raised at 10:00 IST Monday, assigned to an L2/L3 support engineer, when they set it to Resolved at 15:00 IST Monday, then the resolution clock stops at 5 business hours and the resolution target (9 business hours) is met (BR B-5).
REQ-006 AC-2 REQ S-6 AC-2: Given an L2/L3 support engineer sets a ticket to Resolved, when an L1 support engineer views the L1 queue, then the ticket appears there for closure (BR B-11).
REQ-006 AC-3 REQ S-6 AC-3: Given an L1 support engineer resolves a ticket themselves, when they set it to Resolved, then the resolution clock stops and the ticket is in the L1 queue for closure.
REQ-006 AC-4 REQ S-6 AC-4: Given an L2/L3 support engineer, when they try to close a Resolved ticket, then the close is refused and the status stays Resolved.

## Test Scenarios
REQ-006 AC-1 REQ S-6 AC-1: Given a P2 ticket raised at 10:00 IST Monday, assigned to an L2/L3 support engin... â€” verify Given/When/Then conditions as stated above.
REQ-006 AC-2 REQ S-6 AC-2: Given an L2/L3 support engineer sets a ticket to Resolved, when an L1 support en... â€” verify Given/When/Then conditions as stated above.
REQ-006 AC-3 REQ S-6 AC-3: Given an L1 support engineer resolves a ticket themselves, when they set it to R... â€” verify Given/When/Then conditions as stated above.
REQ-006 AC-4 REQ S-6 AC-4: Given an L2/L3 support engineer, when they try to close a Resolved ticket, then ... â€” verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 Â§ S-6; PIB-005 v0.1
- Downstream: FEAT-016-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
