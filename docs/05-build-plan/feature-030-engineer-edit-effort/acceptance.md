---
id: FEAT-030-ACC
id_prefix: FEAT
title: "FEAT-030: S-25: Support Engineer Changes or Deletes Their Own Effort Entry â€” Acceptance Criteria"
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
# FEAT-030: S-25: Support Engineer Changes or Deletes Their Own Effort Entry â€” Acceptance Criteria

## Input References
- REQ-001 v0.3 â€” APLX AMS: User Stories (Approved 2026-10-17) Â§ S-25
- PIB-005 v0.1 â€” Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-030 (REQ S-25). Criteria are copied verbatim from REQ-001 v0.3 Â§ S-25.

## Acceptance Criteria
REQ-025 AC-1 REQ S-25 AC-1: Given support engineer X recorded an effort entry of 1.5 hours dated 2026-11-02, when X changes it to 2 hours on 2026-11-20, then the change is saved and the audit trail holds old value 1.5, new value 2, user X and the time (BR B-15, BR B-22).
REQ-025 AC-2 REQ S-25 AC-2: Given support engineer X recorded an effort entry of 1.5 hours dated 2026-11-02, when X deletes it on 2026-11-25, then it no longer counts against the contract and the audit trail holds the deletion with old value 1.5, user X and the time (BR B-15, BR B-22).
REQ-025 AC-3 REQ S-25 AC-3: Given an effort entry of X dated 2026-11-02, when X tries to change or delete it on 2026-12-01, then the change is refused and the entry keeps its values (BR B-15, A-025).
REQ-025 AC-4 REQ S-25 AC-4: Given an effort entry recorded by support engineer X, when support engineer Y tries to change or delete it, then the change is refused (BR B-15).

## Test Scenarios
REQ-025 AC-1 REQ S-25 AC-1: Given support engineer X recorded an effort entry of 1.5 hours dated 2026-11-02,... â€” verify Given/When/Then conditions as stated above.
REQ-025 AC-2 REQ S-25 AC-2: Given support engineer X recorded an effort entry of 1.5 hours dated 2026-11-02,... â€” verify Given/When/Then conditions as stated above.
REQ-025 AC-3 REQ S-25 AC-3: Given an effort entry of X dated 2026-11-02, when X tries to change or delete it... â€” verify Given/When/Then conditions as stated above.
REQ-025 AC-4 REQ S-25 AC-4: Given an effort entry recorded by support engineer X, when support engineer Y tr... â€” verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 Â§ S-25; PIB-005 v0.1
- Downstream: FEAT-030-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
