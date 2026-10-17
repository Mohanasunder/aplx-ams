---
id: FEAT-018
id_prefix: FEAT
title: "FEAT-018: S-8: Support Engineer Marks a Ticket as Awaiting Client"
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
# FEAT-018: S-8: Support Engineer Marks a Ticket as Awaiting Client

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-8
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-8: S-8: Support Engineer Marks a Ticket as Awaiting Client. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-8 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-011

## Inputs And Contracts
- REQ-001 v0.3 § S-8 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-8
- API-001 v0.1 § Ticket management (F-1)
- DBD-001 v0.1 § Module: tickets
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Ticket management (F-1)
- UIS-001 v0.1 § REQ S-8 — Support engineer marks a ticket as awaiting client

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
Client comment clearing awaiting client — FEAT-022 AC-2. SLA state display — FEAT-020. Audit trail — FEAT-032.

## Risk Tier
Tier: Standard
SLA timer pause; incorrect pause/resume causes wrong elapsed time and distorted SLA metrics.

## Implementation Steps
1. Add `awaiting_client_paused_at` and `awaiting_client_elapsed_snapshot` fields to `Ticket` model in `tickets/models.py`; add migration `tickets/migrations/0002_awaiting_client_fields.py`.
2. Add `set_awaiting_client(ticket_id, assigned_engineer, pause_time)` and `clear_awaiting_client(ticket_id, clear_time)` to `tickets/services.py`: snapshot elapsed time at pause; resume from snapshot on clear.
3. Add PATCH `/api/tickets/{id}/awaiting-client/` to `tickets/views.py`; assigned engineer only.
4. Update `tickets/serializers.py` with awaiting_client field.
5. Update `tickets/dal.py` with awaiting client update queries.
6. Update `tickets/urls.py`.
7. Update `TicketDetail.tsx` with Awaiting Client toggle (assigned engineer only).

## Test Plan
REQ-008 AC-1 REQ S-8 AC-1: Given a P3 ticket with its resolution clock running at 2 business hours, when the assigned support e...
REQ-008 AC-2 REQ S-8 AC-2: Given a ticket in awaiting client, when business hours pass, then neither SLA timer changes state.
REQ-008 AC-3 REQ S-8 AC-3: Given a ticket in awaiting client, when the status is cleared, then the paused SLA timers resume fro...
REQ-008 AC-4 REQ S-8 AC-4: Given a client user or a support engineer who is not the assigned support engineer, when they view a...
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
- [ ] `python3 scripts/check_feature_size.py size FEAT-018` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: Standard` and references FEAT-018-ACC.

## Risks
- A-024 (Confirmed): a ticket not assigned to L2/L3 is assigned to ALL L1 engineers; the assigned-engineer check must handle this case.
- `awaiting_client_paused_at` and `awaiting_client_elapsed_snapshot` add two DB columns; builder lists the new migration in plan.md files.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-8; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-018-TASKS; FEAT-018-ACC; FEAT-018-STATUS; Phase 6 PR

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
