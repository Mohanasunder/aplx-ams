---
id: FEAT-021
id_prefix: FEAT
title: "FEAT-021: S-11: Ticket Is Flagged for Escalation at L1 Target — Tasks"
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
# FEAT-021: S-11: Ticket Is Flagged for Escalation at L1 Target — Tasks

## Input References
- FEAT-021 plan.md — implementation steps and file list
- REQ-001 v0.3 § S-11 — acceptance criteria
- API-001 v0.1 — endpoint contracts
- DBD-001 v0.1 — table definitions
- STD-001 v0.1 — coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-021. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Add `compute_escalation_flag(ticket)` to `sla/services.py`: returns True if assigned_to is None or L1 (ticket still with L1) AND resolution_elapsed >= 50% of resolution_target.
- [ ] T-2: Update `tickets/serializers.py` to include `escalation_flag` (on-read, computed).
- [ ] T-3: Update `tickets/views.py`.
- [ ] T-4: Update `TicketList.tsx` with escalation flag indicator.
- [ ] T-5: Update `TicketDetail.tsx` with escalation flag badge.
- [ ] T-6: Run all gate commands locally; confirm each exits 0.
- [ ] T-7: Verify `python3 scripts/check_feature_size.py size FEAT-021` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-021 plan.md; REQ-001 v0.3 § S-11; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
- Downstream: FEAT-021-TESTS (Phase 6 test set)

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
