---
id: FEAT-013
id_prefix: FEAT
title: "FEAT-013: S-3: L1 Support Engineer Acknowledges a New Ticket"
phase: 5
version: 0.1
template: feature-plan
template_version: 1.6
status: Approved
author_agent: build-planner
approver: Mohanasunder
default_approver: Tech lead
default_folder: docs/05-build-plan
date: 2026-10-17
validation: Pass
---
# FEAT-013: S-3: L1 Support Engineer Acknowledges a New Ticket

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-3
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-3: S-3: L1 Support Engineer Acknowledges a New Ticket. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-3 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-011

## Inputs And Contracts
- REQ-001 v0.3 § S-3 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-3
- API-001 v0.1 § Ticket management (F-1)
- DBD-001 v0.1 § Module: tickets
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Ticket management (F-1)
- UIS-001 v0.1 § REQ S-3 — L1 support engineer acknowledges a new ticket

## Files To Create Or Modify
- `src/aplx_ams_django/tickets/services.py`
- `src/aplx_ams_django/tickets/views.py`
- `src/aplx_ams_django/tickets/serializers.py`
- `src/aplx_ams_django/tickets/dal.py`
- `src/aplx_ams_django/tickets/urls.py`
- `src/frontend/src/pages/TicketDetail.tsx`

## New Packages
- None

## Out Of Scope
Priority change — FEAT-014. Escalation — FEAT-015. Set resolved — FEAT-016. Close — FEAT-017. SLA state display — FEAT-020. Audit trail — FEAT-032.

## Risk Tier
Tier: Standard
Response clock stop logic; incorrect implementation causes wrong SLA response % at month end.

## Implementation Steps
1. Add `acknowledge_ticket(ticket_id, l1_user, action_time)` to `tickets/services.py`: sets `response_stopped_at` to `action_time` only if it is None (first L1 action, BR B-4).
2. Add POST `/api/tickets/{id}/acknowledge/` to `tickets/views.py`; L1-only.
3. Update `tickets/serializers.py` with `response_stopped_at` field.
4. Add `has_l1_action(ticket_id)` check to `tickets/dal.py`.
5. Update `tickets/urls.py`.
6. Update `TicketDetail.tsx`: show Acknowledge button for L1 only; disabled once acknowledged.

## Test Plan
REQ-003 AC-1 REQ S-3 AC-1: Given a P2 ticket raised at 10:00 IST, when an L1 support engineer acknowledges it at 12:00 IST the ...
REQ-003 AC-2 REQ S-3 AC-2: Given a ticket whose first L1 action was at 12:00 IST, when another L1 support engineer acknowledges...
REQ-003 AC-3 REQ S-3 AC-3: Given a P1 ticket raised at 10:00 IST, when the first L1 action on it is at 11:00 IST, then the resp...
REQ-003 AC-4 REQ S-3 AC-4: Given a client user, an L2/L3 support engineer or a delivery manager, when they view a new ticket, t...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 6 | 10 |

Expected test runtime: 5 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-013` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: Standard` and references FEAT-013-ACC.

## Risks
- A-017 (Confirmed): any first L1 action (priority change, escalation, comment, acknowledge) stops the response clock. Services for FEAT-014, FEAT-015, FEAT-023 must call the same `acknowledge_ticket` helper.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-3; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-013-TASKS; FEAT-013-ACC; FEAT-013-STATUS; Phase 6 PR

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
| Comments | Phase 5 validation passed (VAL-023). |
| Timestamp | 2026-10-17 16:50 UTC |
