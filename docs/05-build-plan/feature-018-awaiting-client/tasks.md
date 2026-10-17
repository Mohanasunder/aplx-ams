---
id: FEAT-018-TASKS
id_prefix: FEAT
title: "FEAT-018: S-8: Support Engineer Marks a Ticket as Awaiting Client â€” Tasks"
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
# FEAT-018: S-8: Support Engineer Marks a Ticket as Awaiting Client â€” Tasks

## Input References
- FEAT-018 plan.md â€” implementation steps and file list
- REQ-001 v0.3 Â§ S-8 â€” acceptance criteria
- API-001 v0.1 â€” endpoint contracts
- DBD-001 v0.1 â€” table definitions
- STD-001 v0.1 â€” coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-018. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Add `awaiting_client_paused_at` and `awaiting_client_elapsed_snapshot` fields to `Ticket` model in `tickets/models.py`; add migration `tickets/migrations/0002_awaiting_client_fields.py`.
- [ ] T-2: Add `set_awaiting_client(ticket_id, assigned_engineer, pause_time)` and `clear_awaiting_client(ticket_id, clear_time)` to `tickets/services.py`: snapshot elapsed time at pause; resume from snapshot on clear.
- [ ] T-3: Add PATCH `/api/tickets/{id}/awaiting-client/` to `tickets/views.py`; assigned engineer only.
- [ ] T-4: Update `tickets/serializers.py` with awaiting_client field.
- [ ] T-5: Update `tickets/dal.py` with awaiting client update queries.
- [ ] T-6: Update `tickets/urls.py`.
- [ ] T-7: Update `TicketDetail.tsx` with Awaiting Client toggle (assigned engineer only).
- [ ] T-8: Run all gate commands locally; confirm each exits 0.
- [ ] T-9: Verify `python3 scripts/check_feature_size.py size FEAT-018` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-018 plan.md; REQ-001 v0.3 Â§ S-8; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
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
