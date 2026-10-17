---
id: FEAT-002
id_prefix: FEAT
title: "FEAT-002: S-18: Delivery Manager Sets Up Client Organizations and SAP Applications — Tasks"
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
# FEAT-002: S-18: Delivery Manager Sets Up Client Organizations and SAP Applications — Tasks

## Input References
- FEAT-002 plan.md — implementation steps and file list
- REQ-001 v0.3 § S-18 — acceptance criteria
- API-001 v0.1 — endpoint contracts
- DBD-001 v0.1 — table definitions
- STD-001 v0.1 — coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-002. Each task names the file(s) it produces.

## Task Checklist
- [ ] T-1: Create `src/aplx_ams_django/organizations/` app with `models.py` defining `ClientOrg` and `SAPApplication` models per DBD-001.
- [ ] T-2: Generate `migrations/0001_initial.py` with `makemigrations organizations`.
- [ ] T-3: Write `serializers.py` for `ClientOrg` and `SAPApplication` with DM-only write permission.
- [ ] T-4: Write `services.py` with `create_org`, `add_sap_application` functions enforcing DM role check.
- [ ] T-5: Write `dal.py` with `get_org_by_id`, `list_orgs`, `get_sap_apps_for_org` queries.
- [ ] T-6: Write `views.py` with `OrgViewSet` and `SAPApplicationViewSet` restricted by `HasRolePermission`.
- [ ] T-7: Write `urls.py` registering organization and SAP application endpoints.
- [ ] T-8: Register `organizations.urls` in `src/aplx_ams_django/urls.py`.
- [ ] T-9: Write `src/frontend/src/pages/OrgManagement.tsx` with MUI DataGrid listing orgs and SAP apps; DM-only create/edit controls.
- [ ] T-10: Write `src/frontend/src/api/organizations.ts` with typed axios/fetch calls for org and SAP endpoints.
- [ ] T-11: Run all gate commands locally (`ruff`, `mypy`, `pytest --cov`, `bandit`, `pip-audit`, `detect-secrets`); confirm each exits 0.
- [ ] T-12: Verify `python3 scripts/check_feature_size.py size FEAT-002` exits 0.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-002 plan.md; REQ-001 v0.3 § S-18; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1
- Downstream: FEAT-002-TESTS (Phase 6 test set)

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
