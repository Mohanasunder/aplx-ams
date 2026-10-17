---
id: FEAT-002
id_prefix: FEAT
title: "FEAT-002: S-18: Delivery Manager Sets Up Client Organizations and SAP Applications"
phase: 5
version: 0.1
template: feature-plan
template_version: 1.6
status: Approved
author_agent: build-planner
approver: Mohanasunder
default_approver: Tech lead
default_folder: docs/05-build-plan
date: 2026-10-17
validation: Pass
---
# FEAT-002: S-18: Delivery Manager Sets Up Client Organizations and SAP Applications

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-18
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-18: S-18: Delivery Manager Sets Up Client Organizations and SAP Applications. Delivers end-to-end behavior (data, API, UI) for 3 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 3 acceptance criteria of REQ S-18 end-to-end: backend models, migrations, serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-001

## Inputs And Contracts
- REQ-001 v0.3 § S-18 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-18
- API-001 v0.1 § Organization setup (F-1, F-5 portal, setup)
- DBD-001 v0.1 § Module: organizations
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Organization setup (F-1, F-5)
- UIS-001 v0.1 § REQ S-18 — Delivery manager sets up client organizations and SAP applications

## Files To Create Or Modify
- `src/aplx_ams_django/organizations/models.py`
- `src/aplx_ams_django/organizations/migrations/0001_initial.py`
- `src/aplx_ams_django/organizations/serializers.py`
- `src/aplx_ams_django/organizations/services.py`
- `src/aplx_ams_django/organizations/dal.py`
- `src/aplx_ams_django/organizations/views.py`
- `src/aplx_ams_django/organizations/urls.py`
- `src/aplx_ams_django/urls.py`
- `src/frontend/src/pages/OrgManagement.tsx`
- `src/frontend/src/api/organizations.ts`

## New Packages
- None

## Out Of Scope
Contract setup — FEAT-003. User accounts — FEAT-005. Holiday list — FEAT-010. Ticket raising — FEAT-011. Row-level security and RLS policies — FEAT-007.

## Risk Tier
Tier: Standard
Organization and SAP application setup is internal DM data; no personal data; no payment data.

## Implementation Steps
1. Create `src/aplx_ams_django/organizations/` app with `models.py` defining `ClientOrg` and `SAPApplication` models per DBD-001.
2. Generate `migrations/0001_initial.py` with `makemigrations organizations`.
3. Write `serializers.py` for `ClientOrg` and `SAPApplication` with DM-only write permission.
4. Write `services.py` with `create_org`, `add_sap_application` functions enforcing DM role check.
5. Write `dal.py` with `get_org_by_id`, `list_orgs`, `get_sap_apps_for_org` queries.
6. Write `views.py` with `OrgViewSet` and `SAPApplicationViewSet` restricted by `HasRolePermission`.
7. Write `urls.py` registering organization and SAP application endpoints.
8. Register `organizations.urls` in `src/aplx_ams_django/urls.py`.
9. Write `src/frontend/src/pages/OrgManagement.tsx` with MUI DataGrid listing orgs and SAP apps; DM-only create/edit controls.
10. Write `src/frontend/src/api/organizations.ts` with typed axios/fetch calls for org and SAP endpoints.

## Test Plan
REQ-018 AC-1 REQ S-18 AC-1: Given the delivery manager, when they create client organization Applexus and ad...
REQ-018 AC-2 REQ S-18 AC-2: Given two client organizations A and B, when the delivery manager adds an SAP ap...
REQ-018 AC-3 REQ S-18 AC-3: Given an L1 support engineer, an L2/L3 support engineer or a client user, when t...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 3 | 4 |
| Source files (non-test) | 10 | 10 |

Expected test runtime: 5 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-002` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in `requirements.txt` or `package.json` at the stated version spec.
- [ ] PR description states `Tier: Standard` and references FEAT-002-ACC.

## Risks
- Migration 0001_initial must be the FIRST migration in the organizations app; later features add Contract in 0002_contract.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-18; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-002-TASKS; FEAT-002-ACC; FEAT-002-STATUS; Phase 6 PR

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
| Comments | Phase 5 validation passed (VAL-023). |
| Timestamp | 2026-10-17 16:50 UTC |
