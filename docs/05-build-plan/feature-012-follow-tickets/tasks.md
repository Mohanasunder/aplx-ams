---
id: FEAT-012
id_prefix: FEAT
title: "FEAT-012: S-2: Client User Follows Their Client Organization Tickets — Tasks"
phase: 5
version: 0.1
template: feature-tasks
template_version: 1.0
status: In review
author_agent: build-planner
approver: Tech lead
default_approver: Tech lead
default_folder: docs/05-build-plan
date: 2026-10-17
validation: Pending
---
# FEAT-012: S-2: Client User Follows Their Client Organization Tickets — Tasks

## Input References
- FEAT-012 plan.md — implementation steps and file list
- REQ-001 v0.3 § S-2 — acceptance criteria
- API-001 v0.1 — endpoint contracts
- DBD-001 v0.1 — table definitions
- STD-001 v0.1 — coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-012. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Update `tickets/views.py`: add `GET /api/tickets/` for client users filtering by their org; add `GET /api/tickets/{id}/` showing status, priority (no audit trail).
- [ ] T-2: Update `tickets/serializers.py`: add `TicketListSerializer` (status, priority, raise_time, type, sap_app).
- [ ] T-3: Update `tickets/urls.py` with read-only ticket endpoints.
- [ ] T-4: Write `src/frontend/src/pages/TicketList.tsx` with MUI DataGrid showing org tickets.
- [ ] T-5: Write `src/frontend/src/pages/TicketDetail.tsx` showing ticket details without audit trail.
- [ ] T-6: Run all gate commands locally; confirm each exits 0.
- [ ] T-7: Verify `python3 scripts/check_feature_size.py size FEAT-012` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-012 plan.md; REQ-001 v0.3 § S-2; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
- Downstream: FEAT-012-TESTS (Phase 6 test set)

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
| Decision | Pending |
| Approver | Pending |
| Role | Pending |
| Conditions | None |
| Comments | None |
| Timestamp | Pending |
