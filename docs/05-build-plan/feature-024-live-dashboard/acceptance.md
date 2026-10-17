---
id: FEAT-024-ACC
id_prefix: FEAT
title: "FEAT-024: S-12: Delivery Manager Monitors the Live Dashboard â€” Acceptance Criteria"
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
# FEAT-024: S-12: Delivery Manager Monitors the Live Dashboard â€” Acceptance Criteria

## Input References
- REQ-001 v0.3 â€” APLX AMS: User Stories (Approved 2026-10-17) Â§ S-12
- PIB-005 v0.1 â€” Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-024 (REQ S-12). Criteria are copied verbatim from REQ-001 v0.3 Â§ S-12.

## Acceptance Criteria
REQ-012 AC-1 REQ S-12 AC-1: Given open tickets in client organizations A and B, when the delivery manager views the live dashboard, then it shows, per client organization and per SAP application, the count of open tickets, at-risk tickets, breached tickets and tickets with the escalation flag.
REQ-012 AC-2 REQ S-12 AC-2: Given a ticket's SLA timer changes from on track to at risk, when the delivery manager next views the live dashboard, then the at-risk count includes that ticket.
REQ-012 AC-3 REQ S-12 AC-3: Given client organization A has an hours bank contract, when the delivery manager views the live dashboard, then it shows organization A's hours bank balance (BR B-16).
REQ-012 AC-4 REQ S-12 AC-4: Given a client user, when they try to view the live dashboard, then access is refused.

## Test Scenarios
REQ-012 AC-1 REQ S-12 AC-1: Given open tickets in client organizations A and B, when the delivery manager vi... â€” verify Given/When/Then conditions as stated above.
REQ-012 AC-2 REQ S-12 AC-2: Given a ticket's SLA timer changes from on track to at risk, when the delivery m... â€” verify Given/When/Then conditions as stated above.
REQ-012 AC-3 REQ S-12 AC-3: Given client organization A has an hours bank contract, when the delivery manage... â€” verify Given/When/Then conditions as stated above.
REQ-012 AC-4 REQ S-12 AC-4: Given a client user, when they try to view the live dashboard, then access is re... â€” verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 Â§ S-12; PIB-005 v0.1
- Downstream: FEAT-024-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
