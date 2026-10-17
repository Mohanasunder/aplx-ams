---
id: FEAT-022-TASKS
id_prefix: FEAT
title: "FEAT-022: S-28: Client User Adds a Comment on Their Ticket â€” Tasks"
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
# FEAT-022: S-28: Client User Adds a Comment on Their Ticket â€” Tasks

## Input References
- FEAT-022 plan.md â€” implementation steps and file list
- REQ-001 v0.3 Â§ S-28 â€” acceptance criteria
- API-001 v0.1 â€” endpoint contracts
- DBD-001 v0.1 â€” table definitions
- STD-001 v0.1 â€” coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-022. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Add `Comment` model to `tickets/models.py` (ticket FK, author FK, text, created_at, is_internal bool) per DBD-001.
- [ ] T-2: Generate `tickets/migrations/0003_comment.py`.
- [ ] T-3: Add `CommentSerializer` to `tickets/serializers.py`.
- [ ] T-4: Add `add_client_comment(ticket_id, client_user, text, created_at)` to `tickets/services.py`: validates client user org matches ticket org; if awaiting_client, calls `clear_awaiting_client`.
- [ ] T-5: Add comment DAL queries to `tickets/dal.py`.
- [ ] T-6: Add POST `/api/tickets/{id}/comments/` to `tickets/views.py`; client users of ticket's org only.
- [ ] T-7: Update `tickets/urls.py`.
- [ ] T-8: Update `TicketDetail.tsx` with comment list and client comment form.
- [ ] T-9: Run all gate commands locally; confirm each exits 0.
- [ ] T-10: Verify `python3 scripts/check_feature_size.py size FEAT-022` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-022 plan.md; REQ-001 v0.3 Â§ S-28; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
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
