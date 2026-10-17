---
id: FEAT-011
id_prefix: FEAT
title: "FEAT-011: S-1: Client User Raises a Ticket in the Portal"
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
# FEAT-011: S-1: Client User Raises a Ticket in the Portal

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-1
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-1: S-1: Client User Raises a Ticket in the Portal. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-1 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-010

## Inputs And Contracts
- REQ-001 v0.3 § S-1 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-1
- API-001 v0.1 § Ticket management (F-1)
- DBD-001 v0.1 § Module: tickets
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Ticket management (F-1)
- UIS-001 v0.1 § REQ S-1 — Client user raises a ticket

## Files To Create Or Modify
- `src/aplx_ams_django/tickets/models.py`
- `src/aplx_ams_django/tickets/migrations/0001_initial.py`
- `src/aplx_ams_django/tickets/serializers.py`
- `src/aplx_ams_django/tickets/services.py`
- `src/aplx_ams_django/tickets/dal.py`
- `src/aplx_ams_django/tickets/views.py`
- `src/aplx_ams_django/tickets/urls.py`
- `src/aplx_ams_django/urls.py`
- `src/frontend/src/pages/RaiseTicket.tsx`
- `src/frontend/src/api/tickets.ts`

## New Packages
- None

## Out Of Scope
Follow/view tickets — FEAT-012. L1 acknowledge — FEAT-013. Priority change — FEAT-014. Full SLA computation — FEAT-019. Comments — FEAT-022, FEAT-023. Audit trail for ticket events — FEAT-032.

## Risk Tier
Tier: Standard
Ticket creation; no personal data beyond org membership; SLA timer initialization tested by AC-4.

## Implementation Steps
1. Create `src/aplx_ams_django/tickets/` app with `models.py` defining `Ticket` model (org FK, sap_app FK, type, priority, description, raise_time, status, response_due, resolution_due, response_stopped_at, resolution_stopped_at, assigned_to FK nullable, awaiting_client bool) per DBD-001.
2. Generate `tickets/migrations/0001_initial.py`.
3. Write `serializers.py` with `TicketCreateSerializer` (client user write) and `TicketDetailSerializer`.
4. Write `services.py` with `raise_ticket(user, org, sap_app, type, priority, description)`: validates org membership, computes response/resolution targets from BR B-1 (per priority), records raise_time.
5. Write `dal.py` with `get_tickets_for_org`, `get_l1_queue`, `get_ticket_by_id` queries.
6. Write `views.py` with `TicketViewSet`; POST restricted to client users of the correct org.
7. Write `urls.py`; register in root `urls.py`.
8. Write `src/frontend/src/pages/RaiseTicket.tsx` with MUI form (type, SAP app, priority, description).
9. Write `src/frontend/src/api/tickets.ts` with typed API calls.
10. Write test with `freezegun` for AC-4: raise at 18:30 IST; assert SLA elapsed = 0 until next 09:00.

## Test Plan
REQ-001 AC-1 REQ S-1 AC-1: Given a signed-in client user of client organization A, when they raise a ticket with a type (incide...
REQ-001 AC-2 REQ S-1 AC-2: Given a client user raising a ticket, when the type, SAP application, priority or description is mis...
REQ-001 AC-3 REQ S-1 AC-3: Given a client user of client organization A, when they try to raise a ticket for an SAP application...
REQ-001 AC-4 REQ S-1 AC-4: Given a client user raises a ticket at 18:30 IST on a business day, when the SLA timers start, then ...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 10 | 10 |

Expected test runtime: 5 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-011` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: Standard` and references FEAT-011-ACC.

## Risks
- SLA target values (BR B-1) must be encoded exactly: P1 1h/4h, P2 4h/9h, P3 9h/27h, P4 18h/45h.
- Business hours (09:00–18:00 IST, Mon–Fri) and the holiday list from FEAT-010 must be used by `services.py`.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-1; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-011-TASKS; FEAT-011-ACC; FEAT-011-STATUS; Phase 6 PR

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
