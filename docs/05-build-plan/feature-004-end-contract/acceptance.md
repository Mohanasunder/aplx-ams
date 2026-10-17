---
id: FEAT-004
id_prefix: FEAT
title: "FEAT-004: S-27: Delivery Manager Ends a Contract and Sets Up a New One — Acceptance Criteria"
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
# FEAT-004: S-27: Delivery Manager Ends a Contract and Sets Up a New One — Acceptance Criteria

## Input References
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-27
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-004 (REQ S-27). Criteria are copied verbatim from REQ-001 v0.3 § S-27.

## Acceptance Criteria
REQ-027 AC-1 REQ S-27 AC-1: Given client organization A has an active hours bank contract with hours bank balance 10 hours, when the delivery manager ends it, then organization A has no active contract and the ended contract keeps its effort entries and its balance of 10 hours (BR B-15, A-023).
REQ-027 AC-2 REQ S-27 AC-2: Given client organization A has no active contract, when a support engineer tries to record effort on a ticket of organization A assigned to them, then no effort entry is saved (BR B-15, OQ-042).
REQ-027 AC-3 REQ S-27 AC-3: Given organization A's contract has ended, when the delivery manager sets up a new active hours bank contract of 50 contracted hours, then organization A's hours bank balance shows 50 hours and effort entries saved after that count against the new contract (BR B-15, BR B-16, A-023).
REQ-027 AC-4 REQ S-27 AC-4: Given a user who is not a delivery manager, when they try to end a contract, then the change is refused (BR B-21).

## Test Scenarios
REQ-027 AC-1 REQ S-27 AC-1: Given client organization A has an active hours bank contrac... — verify Given/When/Then conditions as stated above.
REQ-027 AC-2 REQ S-27 AC-2: Given client organization A has no active contract... — verify Given/When/Then conditions as stated above.
REQ-027 AC-3 REQ S-27 AC-3: Given organization A's contract has ended... — verify Given/When/Then conditions as stated above.
REQ-027 AC-4 REQ S-27 AC-4: Given a user who is not a delivery manager... — verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 § S-27; PIB-005 v0.1
- Downstream: FEAT-004-TASKS (builder task list); Phase 6 test set FEAT-004-TESTS

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
