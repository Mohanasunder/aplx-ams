---
id: FEAT-003
id_prefix: FEAT
title: "FEAT-003: S-19: Delivery Manager Sets Up a Client Organization Contract — Acceptance Criteria"
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
# FEAT-003: S-19: Delivery Manager Sets Up a Client Organization Contract — Acceptance Criteria

## Input References
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-19
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-003 (REQ S-19). Criteria are copied verbatim from REQ-001 v0.3 § S-19.

## Acceptance Criteria
REQ-019 AC-1 REQ S-19 AC-1: Given client organization A with no active contract, when the delivery manager creates an active hours bank contract of 100 contracted hours, then organization A's hours bank balance shows 100 hours.
REQ-019 AC-2 REQ S-19 AC-2: Given client organization A already has an active contract, when the delivery manager tries to make a second contract active for organization A, then it is refused and organization A keeps one active contract (BR B-15).
REQ-019 AC-3 REQ S-19 AC-3: Given the delivery manager creates a fixed fee contract, when it is saved, then no contracted hours or hours bank balance is held for it.
REQ-019 AC-4 REQ S-19 AC-4: Given a user who is not a delivery manager, when they try to create or change a contract, then the change is refused.

## Test Scenarios
REQ-019 AC-1 REQ S-19 AC-1: Given client organization A with no active contract... — verify Given/When/Then conditions as stated above.
REQ-019 AC-2 REQ S-19 AC-2: Given client organization A already has an active contract... — verify Given/When/Then conditions as stated above.
REQ-019 AC-3 REQ S-19 AC-3: Given the delivery manager creates a fixed fee contract... — verify Given/When/Then conditions as stated above.
REQ-019 AC-4 REQ S-19 AC-4: Given a user who is not a delivery manager... — verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 § S-19; PIB-005 v0.1
- Downstream: FEAT-003-TASKS (builder task list); Phase 6 test set FEAT-003-TESTS

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
