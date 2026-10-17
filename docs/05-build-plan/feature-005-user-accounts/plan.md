---
id: FEAT-005
id_prefix: FEAT
title: "FEAT-005: S-20: Delivery Manager Manages User Accounts"
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
# FEAT-005: S-20: Delivery Manager Manages User Accounts

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-20
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-20: S-20: Delivery Manager Manages User Accounts. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-20 end-to-end: backend models, migrations, serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-002

## Inputs And Contracts
- REQ-001 v0.3 § S-20 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-20
- API-001 v0.1 § User account management (F-6)
- DBD-001 v0.1 § Module: accounts
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § User account management (F-6)
- UIS-001 v0.1 § REQ S-20 — Delivery manager manages user accounts

## Files To Create Or Modify
- `src/aplx_ams_django/accounts/models.py`
- `src/aplx_ams_django/accounts/migrations/0001_initial.py`
- `src/aplx_ams_django/accounts/serializers.py`
- `src/aplx_ams_django/accounts/services.py`
- `src/aplx_ams_django/accounts/dal.py`
- `src/aplx_ams_django/accounts/views.py`
- `src/aplx_ams_django/accounts/urls.py`
- `src/aplx_ams_django/urls.py`
- `src/frontend/src/pages/UserManagement.tsx`
- `src/frontend/src/api/users.ts`

## New Packages
- None

## Out Of Scope
Sign-in and authentication — FEAT-006. Temporary password — FEAT-008. Change own password — FEAT-009. Security event recording — FEAT-033.

## Risk Tier
Tier: High
Personal data (names, emails, roles); incorrect role assignment grants unauthorized access.

## Implementation Steps
1. Create `src/aplx_ams_django/accounts/` app with `models.py` defining `User` model (extends AbstractBaseUser) with `role`, `org` FK (nullable for internal roles), `is_active` per DBD-001.
2. Generate `migrations/0001_initial.py`.
3. Write `serializers.py` with `UserCreateSerializer`, `UserUpdateSerializer`, `UserDetailSerializer`.
4. Write `services.py` with `create_user`, `deactivate_user` functions enforcing DM role.
5. Write `dal.py` with `get_user_by_id`, `list_users`, `get_active_users_by_org` queries.
6. Write `views.py` with `UserViewSet` (DM-only write).
7. Write `urls.py` registering user account endpoints.
8. Register `accounts.urls` in root `urls.py`.
9. Write `src/frontend/src/pages/UserManagement.tsx` with MUI DataGrid; DM-only create/deactivate.
10. Write `src/frontend/src/api/users.ts` with typed API calls.

## Test Plan
REQ-020 AC-1 REQ S-20 AC-1: Given the delivery manager, when they create a user account with role L1 support...
REQ-020 AC-2 REQ S-20 AC-2: Given the delivery manager creates a client user account, when no client organiz...
REQ-020 AC-3 REQ S-20 AC-3: Given an active user account, when the delivery manager deactivates it, then tha...
REQ-020 AC-4 REQ S-20 AC-4: Given a user who is not a delivery manager, when they try to create, change or d...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 10 | 10 |

Expected test runtime: 5 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-005` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in `requirements.txt` or `package.json` at the stated version spec.
- [ ] PR description states `Tier: High` and references FEAT-005-ACC.

## Risks
- Client user accounts MUST link to a client organization (AC-2); the serializer must enforce this.
- Deactivated accounts must be rejected at sign-in (AC-3); the sign-in auth view (FEAT-006) must check `is_active`.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-20; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-005-TASKS; FEAT-005-ACC; FEAT-005-STATUS; Phase 6 PR

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
