---
id: FEAT-020
id_prefix: FEAT
title: "FEAT-020: S-10: Support Engineer Sees SLA Timer States"
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
# FEAT-020: S-10: Support Engineer Sees SLA Timer States

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-10
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-10: S-10: Support Engineer Sees SLA Timer States. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-10 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-019

## Inputs And Contracts
- REQ-001 v0.3 § S-10 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-10
- API-001 v0.1 § Ticket management (F-1)
- DBD-001 v0.1 § Module: sla
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Ticket management (F-1)
- UIS-001 v0.1 § REQ S-10 — Support engineer sees SLA timer states

## Files To Create Or Modify
- `src/aplx_ams_django/sla/services.py`
- `src/aplx_ams_django/tickets/serializers.py`
- `src/aplx_ams_django/tickets/views.py`
- `src/frontend/src/pages/TicketList.tsx`
- `src/frontend/src/pages/TicketDetail.tsx`

## New Packages
- None

## Out Of Scope
Escalation flag — FEAT-021. Email notifications — none in release 1 (BR B-9). Dashboard SLA counts — FEAT-024.

## Risk Tier
Tier: Standard
SLA state display drives engineer action; incorrect states cause delayed escalation.

## Implementation Steps
1. Add `compute_sla_state(elapsed_hours, target_hours, stopped)` to `sla/services.py`: returns 'on_track', 'at_risk' (>=90%), 'breached' (>=100%), or 'met' (stopped and within target).
2. Update `tickets/serializers.py` to include `response_state` and `resolution_state` (on-read, computed).
3. Update `tickets/views.py` list and detail endpoints.
4. Update `TicketList.tsx` with color-coded SLA state chips.
5. Update `TicketDetail.tsx` with SLA timer state badges.

## Test Plan
REQ-010 AC-1 REQ S-10 AC-1: Given a P1 ticket not yet acknowledged, when its response elapsed time reaches 54 business minutes (...
REQ-010 AC-2 REQ S-10 AC-2: Given a P1 ticket not yet Resolved, when its resolution elapsed time reaches 4 business hours, then ...
REQ-010 AC-3 REQ S-10 AC-3: Given a ticket whose response clock stopped at 50% of the response target, when its resolution clock...
REQ-010 AC-4 REQ S-10 AC-4: Given any ticket reaches at risk or breached, when the state changes, then no email is sent for it (...
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
- [ ] `python3 scripts/check_feature_size.py size FEAT-020` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: Standard` and references FEAT-020-ACC.

## Risks
- A-014 (Open): each clock has its own state independently; response clock 'met' does not affect resolution clock state.
- AC-4: assert no email utility is called when state changes; no email service exists in release 1.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-10; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-020-TASKS; FEAT-020-ACC; FEAT-020-STATUS; Phase 6 PR

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
