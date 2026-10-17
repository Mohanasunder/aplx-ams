---
id: FEAT-033
id_prefix: FEAT
title: "FEAT-033: S-32: Security Events Are Recorded in the Audit Trail — Tasks"
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
# FEAT-033: S-32: Security Events Are Recorded in the Audit Trail — Tasks

## Input References
- FEAT-033 plan.md — implementation steps and file list
- REQ-001 v0.3 § S-32 — acceptance criteria
- API-001 v0.1 — endpoint contracts
- DBD-001 v0.1 — table definitions
- STD-001 v0.1 — coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-033. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Add security event types (sign_in_success, sign_in_failure, account_lockout, temp_password_set, own_password_change) to `AuditEntry.event_type` choices in `audit/models.py`.
- [ ] T-2: Generate `audit/migrations/0002_security_event_type.py`.
- [ ] T-3: Update `audit/services.py` with `write_security_event(event_type, account_name_or_user, occurred_at)`: append-only; assert no password value in new_value or old_value fields.
- [ ] T-4: Update `accounts/authentication.py` to call `write_security_event` on every sign-in success, failure, and lockout (AC-1, AC-2, AC-3); record account name as typed for unknown accounts (OQ-065).
- [ ] T-5: Update `accounts/services.py` `set_temporary_password` and `change_own_password` to call `write_security_event` (AC-4); assert no password values written.
- [ ] T-6: Run all gate commands locally; confirm each exits 0.
- [ ] T-7: Verify `python3 scripts/check_feature_size.py size FEAT-033` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-033 plan.md; REQ-001 v0.3 § S-32; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
- Downstream: FEAT-033-TESTS (Phase 6 test set)

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
