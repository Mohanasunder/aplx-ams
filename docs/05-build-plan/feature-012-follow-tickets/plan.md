---
id: FEAT-012
id_prefix: FEAT
title: "FEAT-012: S-2: Client User Follows Their Client Organization Tickets"
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
# FEAT-012: S-2: Client User Follows Their Client Organization Tickets

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-2
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-2: S-2: Client User Follows Their Client Organization Tickets. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-2 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-011

## Inputs And Contracts
- REQ-001 v0.3 § S-2 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-2
- API-001 v0.1 § Ticket management (F-1)
- DBD-001 v0.1 § Module: tickets
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Ticket management (F-1)
- UIS-001 v0.1 § REQ S-2 — Client user follows their client organization's tickets

## Files To Create Or Modify
- `src/aplx_ams_django/tickets/views.py`
- `src/aplx_ams_django/tickets/serializers.py`
- `src/aplx_ams_django/tickets/urls.py`
- `src/frontend/src/pages/TicketList.tsx`
- `src/frontend/src/pages/TicketDetail.tsx`

## New Packages
- None

## Out Of Scope
Internal user ticket list — included in FEAT-013 (L1 queue). Audit trail display — FEAT-032. Comments display — FEAT-022. Priority change — FEAT-014 (which explicitly refuses the client user).

## Risk Tier
Tier: Standard
Read-only view for client users; org isolation enforced by permission class.

## Implementation Steps
1. Update `tickets/views.py`: add `GET /api/tickets/` for client users filtering by their org; add `GET /api/tickets/{id}/` showing status, priority (no audit trail).
2. Update `tickets/serializers.py`: add `TicketListSerializer` (status, priority, raise_time, type, sap_app).
3. Update `tickets/urls.py` with read-only ticket endpoints.
4. Write `src/frontend/src/pages/TicketList.tsx` with MUI DataGrid showing org tickets.
5. Write `src/frontend/src/pages/TicketDetail.tsx` showing ticket details without audit trail.

## Test Plan
REQ-002 AC-1 REQ S-2 AC-1: Given client organization A has 3 tickets and client organization B has 2 tickets, when a client use...
REQ-002 AC-2 REQ S-2 AC-2: Given a ticket of organization A is set to Resolved or Closed, when a client user of organization A ...
REQ-002 AC-3 REQ S-2 AC-3: Given a client user of organization A, when they view one of their organization's tickets, then the ...
REQ-002 AC-4 REQ S-2 AC-4: Given a client user of organization A viewing one of their organization's tickets after it is raised...
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
- [ ] `python3 scripts/check_feature_size.py size FEAT-012` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: Standard` and references FEAT-012-ACC.

## Risks
- AC-1: the org filter must be applied server-side; the client must not rely on client-side filtering.
- AC-3: the TicketDetail response must not include audit trail entries even if they exist.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-2; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-012-TASKS; FEAT-012-ACC; FEAT-012-STATUS; Phase 6 PR

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
