---
id: FEAT-026-ACC
id_prefix: FEAT
title: "FEAT-026: S-14: Client User Views and Downloads the Monthly Client Report â€” Acceptance Criteria"
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
# FEAT-026: S-14: Client User Views and Downloads the Monthly Client Report â€” Acceptance Criteria

## Input References
- REQ-001 v0.3 â€” APLX AMS: User Stories (Approved 2026-10-17) Â§ S-14
- PIB-005 v0.1 â€” Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-026 (REQ S-14). Criteria are copied verbatim from REQ-001 v0.3 Â§ S-14.

## Acceptance Criteria
REQ-014 AC-1 REQ S-14 AC-1: Given the monthly client report for September 2026 is published for client organization A, when a client user of organization A opens it, then they see its response %, resolution %, breached tickets, MTTR and ticket counts.
REQ-014 AC-2 REQ S-14 AC-2: Given that report, when the client user downloads it as Excel and as PDF, then each file holds the same figures as the report viewed in APLX AMS.
REQ-014 AC-3 REQ S-14 AC-3: Given a client user of client organization A, when they try to open client organization B's monthly client report, then access is refused.
REQ-014 AC-4 REQ S-14 AC-4: Given the September 2026 report for organization A is generated but not yet published, when a client user of organization A looks for it, then it is not shown; when the delivery manager then publishes it, the client user can open it (BR B-14, OQ-047).

## Test Scenarios
REQ-014 AC-1 REQ S-14 AC-1: Given the monthly client report for September 2026 is published for client organ... â€” verify Given/When/Then conditions as stated above.
REQ-014 AC-2 REQ S-14 AC-2: Given that report, when the client user downloads it as Excel and as PDF, then e... â€” verify Given/When/Then conditions as stated above.
REQ-014 AC-3 REQ S-14 AC-3: Given a client user of client organization A, when they try to open client organ... â€” verify Given/When/Then conditions as stated above.
REQ-014 AC-4 REQ S-14 AC-4: Given the September 2026 report for organization A is generated but not yet publ... â€” verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 Â§ S-14; PIB-005 v0.1
- Downstream: FEAT-026-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
