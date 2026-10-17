---
id: FEAT-002-ACC
id_prefix: FEAT
title: "FEAT-002: S-18: Delivery Manager Sets Up Client Organizations and SAP Applications â€” Acceptance Criteria"
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
# FEAT-002: S-18: Delivery Manager Sets Up Client Organizations and SAP Applications â€” Acceptance Criteria

## Input References
- REQ-001 v0.3 â€” APLX AMS: User Stories (Approved 2026-10-17) Â§ S-18
- PIB-005 v0.1 â€” Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 3 acceptance criteria for FEAT-002 (REQ S-18). Criteria are copied verbatim from REQ-001 v0.3 Â§ S-18.

## Acceptance Criteria
REQ-018 AC-1 REQ S-18 AC-1: Given the delivery manager, when they create client organization Applexus and add an SAP application to it, then client users of Applexus can choose that SAP application when raising a ticket.
REQ-018 AC-2 REQ S-18 AC-2: Given two client organizations A and B, when the delivery manager adds an SAP application to organization A, then client users of organization B cannot choose it.
REQ-018 AC-3 REQ S-18 AC-3: Given an L1 support engineer, an L2/L3 support engineer or a client user, when they try to create or change a client organization or SAP application, then the change is refused.

## Test Scenarios
REQ-018 AC-1 REQ S-18 AC-1: Given the delivery manager... â€” verify Given/When/Then conditions as stated above.
REQ-018 AC-2 REQ S-18 AC-2: Given two client organizations A and B... â€” verify Given/When/Then conditions as stated above.
REQ-018 AC-3 REQ S-18 AC-3: Given an L1 support engineer... â€” verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 Â§ S-18; PIB-005 v0.1
- Downstream: FEAT-002-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
