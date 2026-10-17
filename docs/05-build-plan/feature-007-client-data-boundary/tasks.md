---
id: FEAT-007
id_prefix: FEAT
title: "FEAT-007: S-22: Client Data Boundary Holds Across Two Client Organizations — Tasks"
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
# FEAT-007: S-22: Client Data Boundary Holds Across Two Client Organizations — Tasks

## Input References
- FEAT-007 plan.md — implementation steps and file list
- REQ-001 v0.3 § S-22 — acceptance criteria
- API-001 v0.1 — endpoint contracts
- DBD-001 v0.1 — table definitions
- STD-001 v0.1 — coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-007. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Write `audit/migrations/0002_roles_and_rls.py` as a Django migration with `RunSQL`: create PostgreSQL roles (`aplx_app`, `aplx_readonly`), GRANT privileges on all tables, enable RLS on `organizations_clientorg`, `organizations_sapapplication`, `organizations_contract`, `tickets_ticket`, `tickets_comment`, `effort_effortentry`, `reports_monthlyclientreport`, `audit_auditentry` per DBD-001 § Migration Approach.
- [ ] T-2: Update `permissions.py` with `OrgScopedPermission` that filters querysets to the request user's org for client users, and allows full access for internal roles.
- [ ] T-3: Apply `OrgScopedPermission` to `organizations/views.py`, `tickets/views.py`, `reports/views.py`, `accounts/views.py`.
- [ ] T-4: Add `set_rls_session()` call in `settings/base.py` DATABASE configuration to set `app.current_org_id` and `app.current_role` on each connection.
- [ ] T-5: Write boundary tests: create two orgs, two client users, one ticket each; assert each client user sees only their own org's tickets and reports.
- [ ] T-6: Run all gate commands locally (`ruff`, `mypy`, `pytest --cov`, `bandit`, `pip-audit`, `detect-secrets`); confirm each exits 0.
- [ ] T-7: Verify `python3 scripts/check_feature_size.py size FEAT-007` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-007 plan.md; REQ-001 v0.3 § S-22; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
- Downstream: FEAT-007-TESTS (Phase 6 test set)

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
