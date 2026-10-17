---
id: FEAT-031
id_prefix: FEAT
title: "FEAT-031: S-26: Delivery Manager Corrects an Effort Entry — Acceptance Criteria"
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
# FEAT-031: S-26: Delivery Manager Corrects an Effort Entry — Acceptance Criteria

## Input References
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-26
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-031 (REQ S-26). Criteria are copied verbatim from REQ-001 v0.3 § S-26.

## Acceptance Criteria
REQ-026 AC-1 REQ S-26 AC-1: Given support engineer X recorded an effort entry of 2 hours dated 2026-10-15 on an hours bank contract with balance 70 hours, when the delivery manager changes it to 1.5 hours on 2026-11-10, then the change is saved, the hours bank balance is 70.5 hours, and the audit trail holds old value 2, new value 1.5, the delivery manager and the time (BR B-15, BR B-16, BR B-22).
REQ-026 AC-2 REQ S-26 AC-2: Given the delivery manager correcting an effort entry, when the hours are 0 or negative, then the change is not saved (A-020).
REQ-026 AC-3 REQ S-26 AC-3: Given a client user, when they try to change any effort entry, then the change is refused (BR B-15).
REQ-026 AC-4 REQ S-26 AC-4: Given an effort entry recorded by support engineer X, when the delivery manager tries to delete it, then the deletion is refused and the entry keeps its values (BR B-15; Phase 2 review answers, 2026-10-17).

## Test Scenarios
REQ-026 AC-1 REQ S-26 AC-1: Given support engineer X recorded an effort entry of 2 hours dated 2026-10-15 on... — verify Given/When/Then conditions as stated above.
REQ-026 AC-2 REQ S-26 AC-2: Given the delivery manager correcting an effort entry, when the hours are 0 or n... — verify Given/When/Then conditions as stated above.
REQ-026 AC-3 REQ S-26 AC-3: Given a client user, when they try to change any effort entry, then the change i... — verify Given/When/Then conditions as stated above.
REQ-026 AC-4 REQ S-26 AC-4: Given an effort entry recorded by support engineer X, when the delivery manager ... — verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 § S-26; PIB-005 v0.1
- Downstream: FEAT-031-TASKS (builder task list); Phase 6 test set FEAT-031-TESTS

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
