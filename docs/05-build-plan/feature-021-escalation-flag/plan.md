---
id: FEAT-021
id_prefix: FEAT
title: "FEAT-021: S-11: Ticket Is Flagged for Escalation at L1 Target"
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
# FEAT-021: S-11: Ticket Is Flagged for Escalation at L1 Target

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-11
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-11: S-11: Ticket Is Flagged for Escalation at L1 Target. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-11 end-to-end: backend models, migrations (where applicable), serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-019

## Inputs And Contracts
- REQ-001 v0.3 § S-11 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-11
- API-001 v0.1 § Ticket management (F-1)
- DBD-001 v0.1 § Module: sla
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Ticket management (F-1)
- UIS-001 v0.1 § REQ S-11 — Ticket is flagged for escalation at L1's target

## Files To Create Or Modify
- `src/aplx_ams_django/sla/services.py`
- `src/aplx_ams_django/tickets/serializers.py`
- `src/aplx_ams_django/tickets/views.py`
- `src/frontend/src/pages/TicketList.tsx`
- `src/frontend/src/pages/TicketDetail.tsx`

## New Packages
- None

## Out Of Scope
Escalation to L2/L3 — FEAT-015. Dashboard escalation counts — FEAT-024.

## Risk Tier
Tier: Standard
Escalation flag drives proactive L1 escalation; incorrect flag timing delays resolution.

## Implementation Steps
1. Add `compute_escalation_flag(ticket)` to `sla/services.py`: returns True if assigned_to is None or L1 (ticket still with L1) AND resolution_elapsed >= 50% of resolution_target.
2. Update `tickets/serializers.py` to include `escalation_flag` (on-read, computed).
3. Update `tickets/views.py`.
4. Update `TicketList.tsx` with escalation flag indicator.
5. Update `TicketDetail.tsx` with escalation flag badge.

## Test Plan
REQ-011 AC-1 REQ S-11 AC-1: Given a P1 ticket still with L1, when its resolution elapsed time reaches 2 business hours (50% of 4...
REQ-011 AC-2 REQ S-11 AC-2: Given a P2 ticket still with L1 at 3 business hours of resolution elapsed time (escalation point 4.5...
REQ-011 AC-3 REQ S-11 AC-3: Given a P1 ticket assigned to an L2/L3 support engineer at 1 business hour, when its resolution elap...
REQ-011 AC-4 REQ S-11 AC-4: Given a P1 ticket still with L1 showing the escalation flag at 2.5 business hours of resolution elap...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 5 | 10 |

Expected test runtime: 5 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-021` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in requirements.txt or package.json at the stated version spec.
- [ ] PR description states `Tier: Standard` and references FEAT-021-ACC.

## Risks
- BR B-10: the flag clears when a priority change moves the escalation point; `change_priority` in FEAT-014's service must trigger flag recomputation.
- The flag is computed on-read (ADR A-10); it is not stored.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-11; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-021-TASKS; FEAT-021-ACC; FEAT-021-STATUS; Phase 6 PR

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
