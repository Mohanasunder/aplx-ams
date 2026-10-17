---
id: FEAT-007
id_prefix: FEAT
title: "FEAT-007: S-22: Client Data Boundary Holds Across Two Client Organizations — Acceptance Criteria"
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
# FEAT-007: S-22: Client Data Boundary Holds Across Two Client Organizations — Acceptance Criteria

## Input References
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-22
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-007 (REQ S-22). Criteria are copied verbatim from REQ-001 v0.3 § S-22.

## Acceptance Criteria
REQ-022 AC-1 REQ S-22 AC-1: Given client organizations A and B each have tickets, when a client user of organization A lists tickets, then only organization A's tickets are listed.
REQ-022 AC-2 REQ S-22 AC-2: Given a ticket of organization B, when a client user of organization A opens it by its ticket reference, then access is refused and no detail of the ticket is shown.
REQ-022 AC-3 REQ S-22 AC-3: Given organization B's monthly client report and SAP applications, when a client user of organization A tries to view or use them, then access is refused.
REQ-022 AC-4 REQ S-22 AC-4: Given an L1 support engineer, an L2/L3 support engineer or a delivery manager, when they list tickets, then tickets of organizations A and B are both listed.

## Test Scenarios
REQ-022 AC-1 REQ S-22 AC-1: Given client organizations A and B each have tickets... — verify Given/When/Then conditions as stated above.
REQ-022 AC-2 REQ S-22 AC-2: Given a ticket of organization B... — verify Given/When/Then conditions as stated above.
REQ-022 AC-3 REQ S-22 AC-3: Given organization B's monthly client report and SAP applica... — verify Given/When/Then conditions as stated above.
REQ-022 AC-4 REQ S-22 AC-4: Given an L1 support engineer... — verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 § S-22; PIB-005 v0.1
- Downstream: FEAT-007-TASKS (builder task list); Phase 6 test set FEAT-007-TESTS

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
