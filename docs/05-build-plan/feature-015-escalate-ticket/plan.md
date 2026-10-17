---
id: FEAT-015
id_prefix: FEAT
title: "FEAT-015: S-5: L1 Support Engineer Escalates a Ticket to L2/L3"
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
# FEAT-015: S-5: L1 Support Engineer Escalates a Ticket to L2/L3

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-5
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-5: S-5: L1 Support Engineer Escalates a Ticket to L2/L3. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-5 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-011

## Inputs And Contracts
- REQ-001 v0.3 § S-5 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-5
- API-001 v0.1 § Ticket management (F-1)
- DBD-001 v0.1 § Module: tickets
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Ticket management (F-1)
- UIS-001 v0.1 § REQ S-5 — L1 support engineer escalates a ticket to L2/L3

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
Escalation flag display — FEAT-021. Full audit trail — FEAT-032 (AC-3 will be verified by FEAT-032's audit service).

## Risk Tier
Tier: Standard
Escalation removes the hand-off email step; incorrect assignment logic leaves tickets in the wrong queue.

## Implementation Steps
1. Add `escalate_ticket(ticket_id, l2l3_user_id, l1_user, action_time)` to `tickets/services.py`: assigns ticket to L2/L3, removes escalation_flag, stops response clock if first L1 action, creates audit entry.
2. Add PATCH `/api/tickets/{id}/assign/` to `tickets/views.py`; L1-only.
3. Update `tickets/serializers.py` with `AssignSerializer` (assigned_to_id).
4. Add `assign_ticket` to `tickets/dal.py`.
5. Update `tickets/urls.py`.
6. Update `TicketDetail.tsx` with Assign/Escalate dialog (L1-only, L2/L3 user picker).

## Test Plan
REQ-005 AC-1 REQ S-5 AC-1: Given a P2 ticket raised at 10:00 IST in the L1 queue with no L1 action yet, when an L1 support engi...
REQ-005 AC-2 REQ S-5 AC-2: Given a ticket with the escalation flag, when an L1 support engineer assigns it to an L2/L3 support ...
REQ-005 AC-3 REQ S-5 AC-3: Given a ticket is assigned to an L2/L3 support engineer, when the assignment is saved, then the audi...
REQ-005 AC-4 REQ S-5 AC-4: Given a client user, when they view their organization's ticket, then they cannot change its assignm...
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
- [ ] `python3 scripts/check_feature_size.py size FEAT-015` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: Standard` and references FEAT-015-ACC.

## Risks
- AC-3 writes an audit entry; the audit app (FEAT-032) must be installed for this test to pass. Builder may stub the audit write and mark AC-3 as pending until FEAT-032 is merged.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-5; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-015-TASKS; FEAT-015-ACC; FEAT-015-STATUS; Phase 6 PR

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
