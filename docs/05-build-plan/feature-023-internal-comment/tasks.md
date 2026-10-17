---
id: FEAT-023
id_prefix: FEAT
title: "FEAT-023: S-29: Internal User Adds a Comment on a Ticket — Tasks"
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
# FEAT-023: S-29: Internal User Adds a Comment on a Ticket — Tasks

## Input References
- FEAT-023 plan.md — implementation steps and file list
- REQ-001 v0.3 § S-29 — acceptance criteria
- API-001 v0.1 — endpoint contracts
- DBD-001 v0.1 — table definitions
- STD-001 v0.1 — coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-023. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Add `add_internal_comment(ticket_id, internal_user, text, action_time)` to `tickets/services.py`: saves comment with `is_internal=True`; if user is L1 and first L1 action, stops response clock (A-017); does NOT clear awaiting_client.
- [ ] T-2: Add POST `/api/tickets/{id}/comments/` (internal variant) to `tickets/views.py`; L1, L2/L3, DM only.
- [ ] T-3: Update `tickets/serializers.py` with internal comment visibility rules.
- [ ] T-4: Update `tickets/urls.py`.
- [ ] T-5: Update `TicketDetail.tsx` with internal comment form (internal users only); show all comments to internal users, no internal indicator to client.
- [ ] T-6: Run all gate commands locally; confirm each exits 0.
- [ ] T-7: Verify `python3 scripts/check_feature_size.py size FEAT-023` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-023 plan.md; REQ-001 v0.3 § S-29; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
- Downstream: FEAT-023-TESTS (Phase 6 test set)

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
