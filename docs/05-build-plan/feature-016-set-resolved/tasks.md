---
id: FEAT-016-TASKS
id_prefix: FEAT
title: "FEAT-016: S-6: Support Engineer Sets a Ticket to Resolved â€” Tasks"
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
# FEAT-016: S-6: Support Engineer Sets a Ticket to Resolved â€” Tasks

## Input References
- FEAT-016 plan.md â€” implementation steps and file list
- REQ-001 v0.3 Â§ S-6 â€” acceptance criteria
- API-001 v0.1 â€” endpoint contracts
- DBD-001 v0.1 â€” table definitions
- STD-001 v0.1 â€” coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-016. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Add `set_resolved(ticket_id, engineer_user, action_time)` to `tickets/services.py`: validates user is assigned engineer or L1; sets status=Resolved, records resolution_stopped_at=action_time.
- [ ] T-2: Add POST `/api/tickets/{id}/resolve/` to `tickets/views.py`; L1 or L2/L3 only.
- [ ] T-3: Update `tickets/serializers.py` with `resolution_stopped_at` field.
- [ ] T-4: Add `set_ticket_resolved` to `tickets/dal.py`.
- [ ] T-5: Update `tickets/urls.py`.
- [ ] T-6: Update `TicketDetail.tsx` with Resolve button (L1 and L2/L3 only).
- [ ] T-7: Run all gate commands locally; confirm each exits 0.
- [ ] T-8: Verify `python3 scripts/check_feature_size.py size FEAT-016` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-016 plan.md; REQ-001 v0.3 Â§ S-6; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
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
