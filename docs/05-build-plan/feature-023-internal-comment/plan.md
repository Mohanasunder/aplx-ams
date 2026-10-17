---
id: FEAT-023
id_prefix: FEAT
title: "FEAT-023: S-29: Internal User Adds a Comment on a Ticket"
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
# FEAT-023: S-29: Internal User Adds a Comment on a Ticket

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-29
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-29: S-29: Internal User Adds a Comment on a Ticket. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-29 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-022

## Inputs And Contracts
- REQ-001 v0.3 § S-29 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-29
- API-001 v0.1 § Ticket management (F-1)
- DBD-001 v0.1 § Module: tickets
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Ticket management (F-1)
- UIS-001 v0.1 § REQ S-29 — Internal user adds a comment on a ticket

## Files To Create Or Modify
- `src/aplx_ams_django/tickets/services.py`
- `src/aplx_ams_django/tickets/views.py`
- `src/aplx_ams_django/tickets/serializers.py`
- `src/aplx_ams_django/tickets/urls.py`
- `src/frontend/src/pages/TicketDetail.tsx`

## New Packages
- None

## Out Of Scope
Client comment — FEAT-022. Audit trail for comment — FEAT-032.

## Risk Tier
Tier: Standard
Internal comments must not clear awaiting client and must count as L1 action; incorrect logic corrupts SLA state.

## Implementation Steps
1. Add `add_internal_comment(ticket_id, internal_user, text, action_time)` to `tickets/services.py`: saves comment with `is_internal=True`; if user is L1 and first L1 action, stops response clock (A-017); does NOT clear awaiting_client.
2. Add POST `/api/tickets/{id}/comments/` (internal variant) to `tickets/views.py`; L1, L2/L3, DM only.
3. Update `tickets/serializers.py` with internal comment visibility rules.
4. Update `tickets/urls.py`.
5. Update `TicketDetail.tsx` with internal comment form (internal users only); show all comments to internal users, no internal indicator to client.

## Test Plan
REQ-029 AC-1 REQ S-29 AC-1: Given a ticket of client organization A, when a support engineer or the delivery manager adds a comm...
REQ-029 AC-2 REQ S-29 AC-2: Given a ticket of organization A in awaiting client with resolution elapsed time 2 business hours, w...
REQ-029 AC-3 REQ S-29 AC-3: Given an internal user's comment on a ticket of organization A, when a client user of organization B...
REQ-029 AC-4 REQ S-29 AC-4: Given a new P2 ticket raised at 10:00 IST with no L1 action yet, when an L1 support engineer adds a ...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 5 | 10 |

Expected test runtime: 4 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-023` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: Standard` and references FEAT-023-ACC.

## Risks
- AC-4: L1 comment counts as first L1 action (A-017); call `acknowledge_ticket` from FEAT-013.
- AC-2: internal comment must NOT call `clear_awaiting_client`.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-29; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-023-TASKS; FEAT-023-ACC; FEAT-023-STATUS; Phase 6 PR

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
