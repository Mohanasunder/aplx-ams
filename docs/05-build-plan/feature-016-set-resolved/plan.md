---
id: FEAT-016
id_prefix: FEAT
title: "FEAT-016: S-6: Support Engineer Sets a Ticket to Resolved"
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
# FEAT-016: S-6: Support Engineer Sets a Ticket to Resolved

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-6
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-6: S-6: Support Engineer Sets a Ticket to Resolved. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-6 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-011

## Inputs And Contracts
- REQ-001 v0.3 § S-6 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-6
- API-001 v0.1 § Ticket management (F-1)
- DBD-001 v0.1 § Module: tickets
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Ticket management (F-1)
- UIS-001 v0.1 § REQ S-6 — Support engineer sets a ticket to Resolved

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
Close ticket (L1 action) — FEAT-017. Audit trail for Resolved event — FEAT-032.

## Risk Tier
Tier: Standard
Resolution clock stop time drives resolution % and MTTR; incorrect logic corrupts monthly report metrics.

## Implementation Steps
1. Add `set_resolved(ticket_id, engineer_user, action_time)` to `tickets/services.py`: validates user is assigned engineer or L1; sets status=Resolved, records resolution_stopped_at=action_time.
2. Add POST `/api/tickets/{id}/resolve/` to `tickets/views.py`; L1 or L2/L3 only.
3. Update `tickets/serializers.py` with `resolution_stopped_at` field.
4. Add `set_ticket_resolved` to `tickets/dal.py`.
5. Update `tickets/urls.py`.
6. Update `TicketDetail.tsx` with Resolve button (L1 and L2/L3 only).

## Test Plan
REQ-006 AC-1 REQ S-6 AC-1: Given a P2 ticket raised at 10:00 IST Monday, assigned to an L2/L3 support engineer, when they set i...
REQ-006 AC-2 REQ S-6 AC-2: Given an L2/L3 support engineer sets a ticket to Resolved, when an L1 support engineer views the L1 ...
REQ-006 AC-3 REQ S-6 AC-3: Given an L1 support engineer resolves a ticket themselves, when they set it to Resolved, then the re...
REQ-006 AC-4 REQ S-6 AC-4: Given an L2/L3 support engineer, when they try to close a Resolved ticket, then the close is refused...
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
- [ ] `python3 scripts/check_feature_size.py size FEAT-016` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: Standard` and references FEAT-016-ACC.

## Risks
- BR B-5: the resolution clock stop time is the exact moment `set_resolved` is called; use `freezegun` in tests to control this.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-6; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-016-TASKS; FEAT-016-ACC; FEAT-016-STATUS; Phase 6 PR

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
