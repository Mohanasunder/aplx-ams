---
id: FEAT-034
id_prefix: FEAT
title: "FEAT-034: S-33: Users View Security Events — Tasks"
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
# FEAT-034: S-33: Users View Security Events — Tasks

## Input References
- FEAT-034 plan.md — implementation steps and file list
- REQ-001 v0.3 § S-33 — acceptance criteria
- API-001 v0.1 — endpoint contracts
- DBD-001 v0.1 — table definitions
- STD-001 v0.1 — coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-034. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Add `get_security_events_for_user(user_id)` and `get_all_security_events()` to `audit/dal.py` filtering on security event_types.
- [ ] T-2: Add `SecurityEventSerializer` to `audit/serializers.py` (read-only; event, account_name, occurred_at).
- [ ] T-3: Add GET `/api/audit/security-events/` to `audit/views.py`: DM: sees all security events with optional `account_name` filter; L1/L2/L3: sees own security events only; client user: 403.
- [ ] T-4: Update `audit/urls.py`.
- [ ] T-5: Write `src/frontend/src/pages/SecurityEvents.tsx` with MUI DataGrid; DM shows account filter; L1/L2/L3 shows own events only.
- [ ] T-6: Update `src/frontend/src/api/audit.ts` with `getSecurityEvents(accountName?)` call.
- [ ] T-7: Run all gate commands locally; confirm each exits 0.
- [ ] T-8: Verify `python3 scripts/check_feature_size.py size FEAT-034` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-034 plan.md; REQ-001 v0.3 § S-33; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
- Downstream: FEAT-034-TESTS (Phase 6 test set)

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
