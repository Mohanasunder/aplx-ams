---
id: FEAT-017
id_prefix: FEAT
title: "FEAT-017: S-7: L1 Support Engineer Closes a Resolved Ticket"
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
# FEAT-017: S-7: L1 Support Engineer Closes a Resolved Ticket

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-7
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-7: S-7: L1 Support Engineer Closes a Resolved Ticket. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-7 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-016

## Inputs And Contracts
- REQ-001 v0.3 § S-7 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-7
- API-001 v0.1 § Ticket management (F-1)
- DBD-001 v0.1 § Module: tickets
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Ticket management (F-1)
- UIS-001 v0.1 § REQ S-7 — L1 support engineer closes a Resolved ticket

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
No email notifications — by design (OQ-037 answered; no email service exists in release 1). Audit trail for Close event — FEAT-032.

## Risk Tier
Tier: Standard
Close is L1-only; incorrect status guard allows L2/L3 to close or non-Resolved tickets to be closed.

## Implementation Steps
1. Add `close_ticket(ticket_id, l1_user)` to `tickets/services.py`: validates status=Resolved; sets status=Closed; does NOT change resolution_stopped_at.
2. Add POST `/api/tickets/{id}/close/` to `tickets/views.py`; L1-only.
3. Update `tickets/serializers.py` (no new fields needed beyond status).
4. Add `set_ticket_closed` to `tickets/dal.py`.
5. Update `tickets/urls.py`.
6. Update `TicketDetail.tsx` with Close button (L1-only, visible for Resolved tickets).

## Test Plan
REQ-007 AC-1 REQ S-7 AC-1: Given a Resolved ticket in the L1 queue, when an L1 support engineer closes it, then its status is C...
REQ-007 AC-2 REQ S-7 AC-2: Given a ticket that is not Resolved, when an L1 support engineer tries to close it, then the close i...
REQ-007 AC-3 REQ S-7 AC-3: Given a Resolved ticket, when it is closed, then the resolution clock stop time does not change (the...
REQ-007 AC-4 REQ S-7 AC-4: Given a Resolved ticket of client organization A, when an L1 support engineer closes it, then APLX A...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 6 | 10 |

Expected test runtime: 4 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-017` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: Standard` and references FEAT-017-ACC.

## Risks
- AC-4: assert no email is sent; the service must not call any email utility. APLX AMS has no email service in release 1.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-7; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-017-TASKS; FEAT-017-ACC; FEAT-017-STATUS; Phase 6 PR

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
