---
id: FEAT-029-ACC
id_prefix: FEAT
title: "FEAT-029: S-17: Delivery Manager Produces the Monthly Finance Export â€” Acceptance Criteria"
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
# FEAT-029: S-17: Delivery Manager Produces the Monthly Finance Export â€” Acceptance Criteria

## Input References
- REQ-001 v0.3 â€” APLX AMS: User Stories (Approved 2026-10-17) Â§ S-17
- PIB-005 v0.1 â€” Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-029 (REQ S-17). Criteria are copied verbatim from REQ-001 v0.3 Â§ S-17.

## Acceptance Criteria
REQ-017 AC-1 REQ S-17 AC-1: Given effort entries recorded in October 2026, when the delivery manager produces the October 2026 finance export, then it holds one row per effort entry recorded in October 2026 with client organization, contract, ticket, engineer, date, hours and remaining hours bank balance (BR B-18).
REQ-017 AC-2 REQ S-17 AC-2: Given an effort entry on a fixed fee contract, when it appears in the finance export, then its hours are shown and its remaining hours bank balance field is blank (BR B-17).
REQ-017 AC-3 REQ S-17 AC-3: Given client organization A's hours bank balance at the end of October 2026 is 70 hours, when the October 2026 finance export is produced, then every row of organization A shows 70 in the remaining hours bank balance field (BR B-18, OQ-043).
REQ-017 AC-4 REQ S-17 AC-4: Given the finance export is produced, when the delivery manager downloads it as Excel or as CSV, then the downloaded file is in the chosen format with the same rows, and APLX AMS sends nothing to finance (BR B-18, OQ-038).

## Test Scenarios
REQ-017 AC-1 REQ S-17 AC-1: Given effort entries recorded in October 2026, when the delivery manager produce... â€” verify Given/When/Then conditions as stated above.
REQ-017 AC-2 REQ S-17 AC-2: Given an effort entry on a fixed fee contract, when it appears in the finance ex... â€” verify Given/When/Then conditions as stated above.
REQ-017 AC-3 REQ S-17 AC-3: Given client organization A's hours bank balance at the end of October 2026 is 7... â€” verify Given/When/Then conditions as stated above.
REQ-017 AC-4 REQ S-17 AC-4: Given the finance export is produced, when the delivery manager downloads it as ... â€” verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 Â§ S-17; PIB-005 v0.1
- Downstream: FEAT-029-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
