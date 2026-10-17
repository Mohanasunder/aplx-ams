---
id: FEAT-020-ACC
id_prefix: FEAT
title: "FEAT-020: S-10: Support Engineer Sees SLA Timer States â€” Acceptance Criteria"
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
# FEAT-020: S-10: Support Engineer Sees SLA Timer States â€” Acceptance Criteria

## Input References
- REQ-001 v0.3 â€” APLX AMS: User Stories (Approved 2026-10-17) Â§ S-10
- PIB-005 v0.1 â€” Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-020 (REQ S-10). Criteria are copied verbatim from REQ-001 v0.3 Â§ S-10.

## Acceptance Criteria
REQ-010 AC-1 REQ S-10 AC-1: Given a P1 ticket not yet acknowledged, when its response elapsed time reaches 54 business minutes (90% of 1 business hour), then its response clock shows at risk.
REQ-010 AC-2 REQ S-10 AC-2: Given a P1 ticket not yet Resolved, when its resolution elapsed time reaches 4 business hours, then its resolution clock shows breached.
REQ-010 AC-3 REQ S-10 AC-3: Given a ticket whose response clock stopped at 50% of the response target, when its resolution clock is at risk, then the response clock shows met and the resolution clock shows at risk (A-014).
REQ-010 AC-4 REQ S-10 AC-4: Given any ticket reaches at risk or breached, when the state changes, then no email is sent for it (BR B-9).

## Test Scenarios
REQ-010 AC-1 REQ S-10 AC-1: Given a P1 ticket not yet acknowledged, when its response elapsed time reaches 5... â€” verify Given/When/Then conditions as stated above.
REQ-010 AC-2 REQ S-10 AC-2: Given a P1 ticket not yet Resolved, when its resolution elapsed time reaches 4 b... â€” verify Given/When/Then conditions as stated above.
REQ-010 AC-3 REQ S-10 AC-3: Given a ticket whose response clock stopped at 50% of the response target, when ... â€” verify Given/When/Then conditions as stated above.
REQ-010 AC-4 REQ S-10 AC-4: Given any ticket reaches at risk or breached, when the state changes, then no em... â€” verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 Â§ S-10; PIB-005 v0.1
- Downstream: FEAT-020-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
