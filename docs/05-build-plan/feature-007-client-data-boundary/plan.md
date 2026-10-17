---
id: FEAT-007
id_prefix: FEAT
title: "FEAT-007: S-22: Client Data Boundary Holds Across Two Client Organizations"
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
# FEAT-007: S-22: Client Data Boundary Holds Across Two Client Organizations

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-22
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-22: S-22: Client Data Boundary Holds Across Two Client Organizations. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-22 end-to-end: backend models, migrations, serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-025
- Depends on: FEAT-032

## Inputs And Contracts
- REQ-001 v0.3 § S-22 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-22
- API-001 v0.1 § Client organization scoping (ADR A-6)
- DBD-001 v0.1 § Row-Level Security Policies
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Data Access
- UIS-001 v0.1 § REQ S-22 — Client data boundary

## Files To Create Or Modify
- `src/aplx_ams_django/audit/migrations/0003_roles_and_rls.py`
- `src/aplx_ams_django/permissions.py`
- `src/aplx_ams_django/organizations/views.py`
- `src/aplx_ams_django/tickets/views.py`
- `src/aplx_ams_django/reports/views.py`
- `src/aplx_ams_django/accounts/views.py`
- `src/aplx_ams_django/settings/base.py`

## New Packages
- None

## Out Of Scope
Ticket creation — FEAT-011. Report generation — FEAT-025. Audit trail — FEAT-032. Security event viewing — FEAT-034. This feature adds no new API endpoints; it enforces boundaries on existing endpoints.

## Risk Tier
Tier: Critical
Data isolation between client organizations; failure exposes one client's data to another; RLS policies are applied at the PostgreSQL level (ADR A-6).

## Implementation Steps
1. Write `audit/migrations/0003_roles_and_rls.py` as a Django migration with `RunSQL`: create PostgreSQL roles (`aplx_app`, `aplx_readonly`), GRANT privileges on all tables, enable RLS on `organizations_clientorg`, `organizations_sapapplication`, `organizations_contract`, `tickets_ticket`, `tickets_comment`, `effort_effortentry`, `reports_monthlyclientreport`, `audit_auditentry` per DBD-001 § Migration Approach.
2. Update `permissions.py` with `OrgScopedPermission` that filters querysets to the request user's org for client users, and allows full access for internal roles.
3. Apply `OrgScopedPermission` to `organizations/views.py`, `tickets/views.py`, `reports/views.py`, `accounts/views.py`.
4. Add `set_rls_session()` call in `settings/base.py` DATABASE configuration to set `app.current_org_id` and `app.current_role` on each connection.
5. Write boundary tests: create two orgs, two client users, one ticket each; assert each client user sees only their own org's tickets and reports.

## Test Plan
REQ-022 AC-1 REQ S-22 AC-1: Given client organizations A and B each have tickets, when a client user of orga...
REQ-022 AC-2 REQ S-22 AC-2: Given a ticket of organization B, when a client user of organization A opens it ...
REQ-022 AC-3 REQ S-22 AC-3: Given organization B's monthly client report and SAP applications, when a client...
REQ-022 AC-4 REQ S-22 AC-4: Given an L1 support engineer, an L2/L3 support engineer or a delivery manager, w...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 7 | 10 |

Expected test runtime: 6 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-007` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in `requirements.txt` or `package.json` at the stated version spec.
- [ ] PR description states `Tier: Critical` and references FEAT-007-ACC.

## Risks
- This feature depends on FEAT-025 (reports table) and FEAT-032 (audit table); the RLS migration must run AFTER all app tables exist.
- The boundary tests must use factory-boy to create test data directly; they do not depend on any UI flow.
- RSK R-6: boundary tests must be re-run before the first external client goes live.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-22; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-007-TASKS; FEAT-007-ACC; FEAT-007-STATUS; Phase 6 PR

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
