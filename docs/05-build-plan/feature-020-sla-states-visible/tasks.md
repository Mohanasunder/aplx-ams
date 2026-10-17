---
id: FEAT-020-TASKS
id_prefix: FEAT
title: "FEAT-020: S-10: Support Engineer Sees SLA Timer States â€” Tasks"
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
# FEAT-020: S-10: Support Engineer Sees SLA Timer States â€” Tasks

## Input References
- FEAT-020 plan.md â€” implementation steps and file list
- REQ-001 v0.3 Â§ S-10 â€” acceptance criteria
- API-001 v0.1 â€” endpoint contracts
- DBD-001 v0.1 â€” table definitions
- STD-001 v0.1 â€” coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-020. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Add `compute_sla_state(elapsed_hours, target_hours, stopped)` to `sla/services.py`: returns 'on_track', 'at_risk' (>=90%), 'breached' (>=100%), or 'met' (stopped and within target).
- [ ] T-2: Update `tickets/serializers.py` to include `response_state` and `resolution_state` (on-read, computed).
- [ ] T-3: Update `tickets/views.py` list and detail endpoints.
- [ ] T-4: Update `TicketList.tsx` with color-coded SLA state chips.
- [ ] T-5: Update `TicketDetail.tsx` with SLA timer state badges.
- [ ] T-6: Run all gate commands locally; confirm each exits 0.
- [ ] T-7: Verify `python3 scripts/check_feature_size.py size FEAT-020` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-020 plan.md; REQ-001 v0.3 Â§ S-10; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
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
