---
id: FEAT-022
id_prefix: FEAT
title: "FEAT-022: S-28: Client User Adds a Comment on Their Ticket"
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
# FEAT-022: S-28: Client User Adds a Comment on Their Ticket

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-28
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-28: S-28: Client User Adds a Comment on Their Ticket. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-28 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-018

## Inputs And Contracts
- REQ-001 v0.3 § S-28 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-28
- API-001 v0.1 § Ticket management (F-1)
- DBD-001 v0.1 § Module: tickets
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Ticket management (F-1)
- UIS-001 v0.1 § REQ S-28 — Client user adds a comment on their client organization's ticket

## Files To Create Or Modify
- `src/aplx_ams_django/tickets/models.py`
- `src/aplx_ams_django/tickets/migrations/0003_comment.py`
- `src/aplx_ams_django/tickets/serializers.py`
- `src/aplx_ams_django/tickets/services.py`
- `src/aplx_ams_django/tickets/dal.py`
- `src/aplx_ams_django/tickets/views.py`
- `src/aplx_ams_django/tickets/urls.py`
- `src/frontend/src/pages/TicketDetail.tsx`

## New Packages
- None

## Out Of Scope
Internal user comments — FEAT-023. Audit trail for comment events — FEAT-032.

## Risk Tier
Tier: Standard
Client comment clears awaiting client; incorrect auto-clear corrupts SLA timer state.

## Implementation Steps
1. Add `Comment` model to `tickets/models.py` (ticket FK, author FK, text, created_at, is_internal bool) per DBD-001.
2. Generate `tickets/migrations/0003_comment.py`.
3. Add `CommentSerializer` to `tickets/serializers.py`.
4. Add `add_client_comment(ticket_id, client_user, text, created_at)` to `tickets/services.py`: validates client user org matches ticket org; if awaiting_client, calls `clear_awaiting_client`.
5. Add comment DAL queries to `tickets/dal.py`.
6. Add POST `/api/tickets/{id}/comments/` to `tickets/views.py`; client users of ticket's org only.
7. Update `tickets/urls.py`.
8. Update `TicketDetail.tsx` with comment list and client comment form.

## Test Plan
REQ-028 AC-1 REQ S-28 AC-1: Given a client user of client organization A, when they add a comment on a ticket of organization A,...
REQ-028 AC-2 REQ S-28 AC-2: Given a ticket of organization A in awaiting client with resolution elapsed time 2 business hours, w...
REQ-028 AC-3 REQ S-28 AC-3: Given a ticket of organization A that is not in awaiting client, when a client user of organization ...
REQ-028 AC-4 REQ S-28 AC-4: Given a client user of organization A, when they try to add a comment on a ticket of organization B,...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 8 | 10 |

Expected test runtime: 5 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-022` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: Standard` and references FEAT-022-ACC.

## Risks
- AC-2: auto-clear of awaiting_client must call the same `clear_awaiting_client` service as FEAT-018; do not duplicate the logic.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-28; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-022-TASKS; FEAT-022-ACC; FEAT-022-STATUS; Phase 6 PR

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
