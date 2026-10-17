---
id: FEAT-009
id_prefix: FEAT
title: "FEAT-009: S-31: User Changes Their Own Password"
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
# FEAT-009: S-31: User Changes Their Own Password

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-31
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-31: S-31: User Changes Their Own Password. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-31 end-to-end: backend models, migrations, serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-006

## Inputs And Contracts
- REQ-001 v0.3 § S-31 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-31
- API-001 v0.1 § Authentication (F-5)
- DBD-001 v0.1 § Module: accounts
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Authentication (F-5)
- UIS-001 v0.1 § REQ S-31 — Change own password

## Files To Create Or Modify
- `src/aplx_ams_django/accounts/services.py`
- `src/aplx_ams_django/accounts/views.py`
- `src/aplx_ams_django/accounts/urls.py`
- `src/aplx_ams_django/accounts/serializers.py`
- `src/frontend/src/pages/ChangePassword.tsx`
- `src/frontend/src/api/auth.ts`

## New Packages
- None

## Out Of Scope
Temporary password (DM sets another user's password) — FEAT-008. Security event recording of password changes — FEAT-033.

## Risk Tier
Tier: High
Password change; wrong-current-password check prevents unauthorized password replacement.

## Implementation Steps
1. Add `change_own_password(user_id, current_password, new_password)` to `accounts/services.py`: verifies current password, validates new password policy, hashes and saves.
2. Add POST `/api/auth/change-password/` to `accounts/views.py` (any authenticated user, own account only).
3. Register in `accounts/urls.py`.
4. Add `ChangePasswordSerializer` to `serializers.py` with `current_password` and `new_password` fields.
5. Write `src/frontend/src/pages/ChangePassword.tsx` with MUI form; current + new + confirm password.
6. Add `changePassword(current, newPwd)` to `src/frontend/src/api/auth.ts`.

## Test Plan
REQ-031 AC-1 REQ S-31 AC-1: Given signed-in user X (an internal user or a client user), when X enters their ...
REQ-031 AC-2 REQ S-31 AC-2: Given signed-in user X, when the new password has fewer than 8 characters or lac...
REQ-031 AC-3 REQ S-31 AC-3: Given signed-in user X who is not a delivery manager, when X tries to change the...
REQ-031 AC-4 REQ S-31 AC-4: Given signed-in user X, when X enters a wrong current password while changing th...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 6 | 10 |

Expected test runtime: 4 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-009` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in `requirements.txt` or `package.json` at the stated version spec.
- [ ] PR description states `Tier: High` and references FEAT-009-ACC.

## Risks
- The current-password check must use constant-time comparison (Argon2 verify) to prevent timing attacks.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-31; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-009-TASKS; FEAT-009-ACC; FEAT-009-STATUS; Phase 6 PR

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
