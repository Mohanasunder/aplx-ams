---
id: FEAT-008
id_prefix: FEAT
title: "FEAT-008: S-30: Delivery Manager Sets a Temporary Password"
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
# FEAT-008: S-30: Delivery Manager Sets a Temporary Password

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- REQ-001 v0.3 — APLX AMS: User Stories (Approved 2026-10-17) § S-30
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17)
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17)

## Purpose And Scope
Implements REQ S-30: S-30: Delivery Manager Sets a Temporary Password. Delivers end-to-end behavior (data, API, UI) for 4 acceptance criteria.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-30 end-to-end: backend models, migrations, serializers, services, DAL, views, URLs, and frontend pages.

## Dependencies
- Depends on: FEAT-006

## Inputs And Contracts
- REQ-001 v0.3 § S-30 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.1 — endpoint contracts for this feature
- DBD-001 v0.1 — table definitions and migration order
- PRM-001 v0.1 — role-based permission matrix

## Context Pack
- REQ-001 v0.3 § S-30
- API-001 v0.1 § Authentication (F-5)
- DBD-001 v0.1 § Module: accounts
- STD-001 v0.1 § Naming And Structure
- PRM-001 v0.1 § Authentication (F-5)
- UIS-001 v0.1 § REQ S-30 — Delivery manager sets a temporary password

## Files To Create Or Modify
- `src/aplx_ams_django/accounts/services.py`
- `src/aplx_ams_django/accounts/views.py`
- `src/aplx_ams_django/accounts/serializers.py`
- `src/aplx_ams_django/accounts/dal.py`
- `src/aplx_ams_django/accounts/urls.py`
- `src/frontend/src/pages/UserManagement.tsx`
- `src/frontend/src/api/users.ts`

## New Packages
- None

## Out Of Scope
Change own password — FEAT-009. Security event recording of password changes — FEAT-033. Self-service password reset — out of scope for release 1 (PRS NG-4).

## Risk Tier
Tier: High
Temporary password bypasses normal credential flow; incorrect lockout-clear logic allows reuse of a locked account.

## Implementation Steps
1. Add `set_temporary_password(user_id, password, acting_user)` to `accounts/services.py`: validates password policy, hashes with Argon2id, clears lockout counter, saves.
2. Add PATCH `/api/users/{id}/set-temp-password/` action to `accounts/views.py` (DM-only).
3. Add `TempPasswordSerializer` to `serializers.py` with password policy validation.
4. Add `clear_lockout(user_id)` to `accounts/dal.py`.
5. Register temp-password URL in `accounts/urls.py`.
6. Update `UserManagement.tsx` with 'Set temporary password' dialog (DM-only).
7. Update `users.ts` with `setTempPassword(id, password)` call.

## Test Plan
REQ-030 AC-1 REQ S-30 AC-1: Given the delivery manager creates a user account with temporary password "Abcde...
REQ-030 AC-2 REQ S-30 AC-2: Given the delivery manager sets a temporary password, when it has fewer than 8 c...
REQ-030 AC-3 REQ S-30 AC-3: Given user X told the delivery manager outside APLX AMS that they forgot their p...
REQ-030 AC-4 REQ S-30 AC-4: Given a user who is not a delivery manager, when they try to set a temporary pas...
See acceptance.md for the full Given/When/Then text of each criterion above.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 7 | 10 |

Expected test runtime: 4 minutes
Open design decisions: None

## Definition Of Done
- [ ] All acceptance criteria pass (verified by the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `python3 scripts/check_feature_size.py size FEAT-008` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in `requirements.txt` or `package.json` at the stated version spec.
- [ ] PR description states `Tier: High` and references FEAT-008-ACC.

## Risks
- The lockout clear (AC-3) must happen atomically with the password change to avoid a race condition.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; REQ-001 v0.3 § S-30; API-001 v0.1; DBD-001 v0.1; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1
- Downstream: FEAT-008-TASKS; FEAT-008-ACC; FEAT-008-STATUS; Phase 6 PR

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
