---
id: FEAT-012-TASKS
id_prefix: FEAT
title: "FEAT-012: S-2: Client User Follows Their Client Organization Tickets â€” Tasks"
phase: 5
version: 0.1
template: feature-tasks
template_version: 1.0
status: Approved
author_agent: build-planner
approver: Mohanasunder
default_approver: Tech lead
default_folder: docs/05-build-plan
date: 2026-10-17
validation: Pass
---
# FEAT-012: S-2: Client User Follows Their Client Organization Tickets â€” Tasks

## Input References
- FEAT-012 plan.md â€” implementation steps and file list
- REQ-001 v0.3 Â§ S-2 â€” acceptance criteria
- API-001 v0.1 â€” endpoint contracts
- DBD-001 v0.1 â€” table definitions
- STD-001 v0.1 â€” coding standards

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
- Upstream: FEAT-012 plan.md; REQ-001 v0.3 Â§ S-2; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
- Downstream: Phase 6 test set (created in Phase 6)

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
| Comments | None |
| Timestamp | 2026-10-17 18:47 UTC |
