---
id: FEAT-037
title: "FEAT-037: S-34: Delivery Manager Edits User Account"
phase: 5
version: 0.1
template: feature-plan
template_version: 1.6
status: Approved
author_agent: build-planner
approver: Mohanasunder
date: 2026-10-21
validation: Pass
---
# FEAT-037: S-34: Delivery Manager Edits User Account

## Input References
- REQ-001 v0.4 — APLX AMS: User Stories (Approved 2026-10-21, SCR S-19) § S-34
- API-001 v0.3 — APLX AMS: API Specification (Approved 2026-10-21, SCR S-20) § PATCH /api/accounts/users/{id}/ (endpoint #7)
- DBD-001 v0.1 — APLX AMS: Database Design (Approved 2026-10-17) § accounts_user, audit_auditentry
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (Approved 2026-10-17)
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17) § User Management
- PRM-001 v0.1 — APLX AMS: Permission Matrix (Approved 2026-10-17) § User account management
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- OQ-075 — Edit user account capability approved: DEC-089 (2026-10-21, Mohanasunder)

## Purpose And Scope
Implements REQ S-34: delivery manager edits any field on a user account (name, email, role, client_organization_id, is_active) with one audit trail entry per changed field. Extends the existing PATCH /api/accounts/users/{id}/ endpoint (endpoint #7, introduced in FEAT-005) and the UserManagement.tsx page to add an edit button and form.

## Feature Type
Type: Feature

## Objective
Deliver all 4 acceptance criteria of REQ S-34 end-to-end: backend PATCH handler in UserDetailView, UpdateUserAccountSerializer for partial update, update_user() service function with per-field audit trail creation, and a frontend edit button with modal form on UserManagement.tsx.

## Dependencies
- Depends on: FEAT-005

## Inputs And Contracts
- REQ-001 v0.4 § S-34 — acceptance criteria (copied verbatim into acceptance.md)
- API-001 v0.3 § PATCH /api/accounts/users/{id}/ — UpdateUserAccountRequest schema (name, email, role, client_organization_id, is_active — all optional); 200 UserAccount, 400 ValidationError, 403/404 SimpleError; delivery_manager only; role→client_user without client_organization_id → 400; role away from client_user → auto-clears client_organization_id; each changed field → one AuditEntry (old value, new value, actor, timestamp)
- PRM-001 v0.1 § User account management — delivery_manager role only for PATCH
- DBD-001 v0.1 § audit_auditentry — AuditEntry model fields: entity_type, entity_id, field_name, old_value, new_value, actor, created_at

## Context Pack
- REQ-001 v0.4 § S-34
- API-001 v0.3 § PATCH /api/accounts/users/{id}/ (endpoint #7)
- PRM-001 v0.1 § User account management (F-6)
- DBD-001 v0.1 § accounts_user
- DBD-001 v0.1 § audit_auditentry
- STD-001 v0.1 § Naming And Structure
- UIS-001 v0.1 § User Management
- src/aplx_ams_django/accounts/models.py
- src/aplx_ams_django/accounts/serializers.py
- src/aplx_ams_django/accounts/services.py
- src/aplx_ams_django/accounts/dal.py
- src/aplx_ams_django/accounts/views.py
- src/aplx_ams_django/audit/models.py
- docs/04-design/openapi.yaml § /api/accounts/users/{id}

## Files To Create Or Modify

**Backend (source files — modify existing)**
- `src/aplx_ams_django/accounts/views.py`
- `src/aplx_ams_django/accounts/serializers.py`
- `src/aplx_ams_django/accounts/services.py`

**Frontend (source files — modify existing)**
- `src/frontend/src/pages/UserManagement.tsx`
- `src/frontend/src/api/users.ts`

**Tests**
- `src/aplx_ams_django/accounts/tests/test_edit_user.py` (new — pytest tests for AC-1, AC-2, AC-3, AC-4)
- `src/frontend/src/pages/UserManagement.test.tsx` (new — Vitest tests for AC-1 and AC-4 UI paths)

## New Packages
None

## Out Of Scope
- Creating new user accounts (FEAT-005).
- Deactivating/reactivating accounts via is_active without the full edit form (FEAT-005 handled this via a dedicated toggle; FEAT-037 includes is_active as one editable field in the edit form only).
- Temporary password reset (FEAT-008).
- Changing own password (FEAT-009).
- Audit trail model definition or migration (already exists from FEAT-032).
- Any endpoint other than PATCH /api/accounts/users/{id}/ (endpoint #7).
- Any model migration — the accounts_user and audit_auditentry tables already exist; no schema change is required.
- Client organization management (FEAT-002, FEAT-003, FEAT-004).

## Risk Tier
Tier: High
This feature modifies existing user account data with role changes that affect authorization boundaries (for example, promoting a user to delivery_manager or assigning a client_user to a different client organization), and the audit trail provides the tamper-evident record required by BR B-22 and NFR N-6; an error in the role-change or audit logic could silently grant or revoke access.

## Implementation Steps
1. In `src/aplx_ams_django/accounts/serializers.py` add `UpdateUserAccountSerializer` (ModelSerializer on the User model, all five fields optional, `partial=True`): validate that if `role` is being set to `client_user` and neither the incoming data nor the existing record provides a `client_organization_id`, raise a `ValidationError`; if `role` is being set to any value other than `client_user`, force `client_organization_id` to `None` in `validated_data`.
2. In `src/aplx_ams_django/accounts/services.py` add `update_user(user_id, payload, actor)`: retrieve the User instance via `dal.get_user_by_id`; call `UpdateUserAccountSerializer(instance, data=payload, partial=True)`; on valid data, record changed fields (compare each supplied field's current value to the incoming value), call `instance.save()`, then create one `AuditEntry` per changed field via `AuditEntry.objects.create(entity_type='user', entity_id=user_id, field_name=field, old_value=str(old), new_value=str(new), actor=actor, created_at=datetime.utcnow())`.
3. In `src/aplx_ams_django/accounts/views.py` add a `patch` method to `UserDetailView` (or the existing class-based view that handles GET /api/accounts/users/{id}/): enforce `delivery_manager` role (return 403 otherwise); call `services.update_user(id, request.data, request.user)`; return 200 with `UserAccountSerializer(updated_instance).data` or forward the 400 ValidationError.
4. Write `src/aplx_ams_django/accounts/tests/test_edit_user.py`: four test functions, one per AC, using pytest-django fixtures; each test verifies the full backend behavior end-to-end (request → response → database state → audit entries).
5. In `src/frontend/src/api/users.ts` add `updateUser(id: number, data: Partial<UpdateUserAccountRequest>): Promise<UserAccount>` that calls `PATCH /api/accounts/users/{id}/` and returns the typed response.
6. In `src/frontend/src/pages/UserManagement.tsx` add an "Edit" icon button in the DataGrid actions column (delivery_manager only); clicking it opens a MUI Dialog with a form pre-populated from the row data; on submit calls `updateUser(id, changedFields)`, shows a success snackbar on 200, shows a field-level error on 400, and refreshes the user list.
7. Write `src/frontend/src/pages/UserManagement.test.tsx`: Vitest tests for the edit dialog renders (AC-1 happy path mock) and the 403 / non-DM path (AC-4) where the Edit button is absent.

## Test Plan
- REQ S-34 AC-1: Send PATCH /api/accounts/users/{id}/ as delivery_manager with `{"name": "New Name", "email": "new@example.com"}`; assert HTTP 200; assert account fields updated in DB; assert two AuditEntry rows created (one for name, one for email), each with old value, new value, actor=delivery_manager user ID, and a UTC timestamp.
- REQ S-34 AC-2: Send PATCH /api/accounts/users/{id}/ as delivery_manager with `{"role": "client_user"}` on a user who has no client_organization_id; assert HTTP 400; assert ValidationError body; assert no change in DB and no AuditEntry created.
- REQ S-34 AC-3: Send PATCH /api/accounts/users/{id}/ as delivery_manager with `{"role": "l2l3_support"}` on a user who has a client_organization_id; assert HTTP 200; assert client_organization_id is null in DB; assert AuditEntry rows for role (changed) and client_organization_id (changed to null).
- REQ S-34 AC-4: Send PATCH /api/accounts/users/{id}/ as l2l3_support user; assert HTTP 403; assert SimpleError body; assert no change in DB.
- Frontend AC-1: Mount UserManagement with delivery_manager context; assert Edit button is present in first row actions; open dialog; assert form fields are pre-populated; submit with one changed field; assert `updateUser` is called with the correct payload.
- Frontend AC-4: Mount UserManagement with l2l3_support context; assert no Edit button is rendered in the actions column.

## Size Check
| Metric | Count | Limit |
|---|---|---|
| Acceptance criteria | 4 | 4 |
| Source files (non-test) | 5 | 30 |

Expected test runtime: 5 minutes
Open design decisions: None

## Definition Of Done
- [ ] All 4 acceptance criteria pass (verified by test_edit_user.py and UserManagement.test.tsx per the test plan above).
- [ ] All CI gates listed in `.ai/standards/automated-gates.md` exit 0 on the feature branch.
- [ ] No file listed under Production Configuration paths is changed (STD-001 v0.1).
- [ ] `py -3 scripts/check_feature_size.py size FEAT-037` exits 0.
- [ ] No `<fill:` placeholders remain in any artifact in this folder.
- [ ] All new packages listed under New Packages appear in the manifests at the stated version spec (None for this feature).
- [ ] PR description states `Tier: High` and references FEAT-037-ACC.
- [ ] AI code review (`ai-code-reviewer` agent) report saved; no Major or Critical finding unresolved.
- [ ] AI security scan (`security-scanner` agent) report saved.
- [ ] Human developer reviewer has approved the PR via `/approve`.
- [ ] Tech lead has reviewed the risk sections before merge (High tier).

## Risks
- `UserDetailView` in views.py is shared with GET /api/accounts/users/{id}/; adding `patch()` must not break the existing GET handler or the UserAccountSerializer used there.
- The per-field audit trail loop in `update_user()` must compare the current DB value (not the serializer representation) to the incoming value to avoid spurious entries when a field is supplied in the request but matches the existing value.
- The auto-clear of `client_organization_id` when role changes away from `client_user` must happen in the serializer (before save), not the view, so it appears in the audit diff correctly.
- The frontend edit form shows all five fields; the builder must ensure the DM cannot accidentally submit unchanged fields (only send fields the user actually edited) to avoid spurious audit entries.

## Assumptions
- A-050: The AuditEntry model (from FEAT-032) has fields: entity_type (CharField), entity_id (PositiveIntegerField), field_name (CharField), old_value (TextField), new_value (TextField), actor (ForeignKey to User), created_at (DateTimeField). If the actual field names differ, an SCR is required before building. Logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.4 § S-34; API-001 v0.3 § endpoint #7; DBD-001 v0.1 § accounts_user, audit_auditentry; STD-001 v0.1; BED-001 v0.1; UIS-001 v0.1 § User Management; PRM-001 v0.1; PIB-005 v0.1; SCR-001 § S-19 (REQ S-34 added); SCR-001 § S-20 (API-001 v0.3)
- Downstream: FEAT-037-TASKS; FEAT-037-ACC; FEAT-037-STATUS; Phase 6 PR

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
| Comments | FEAT-037 plan approved. Wave 30, Tier High, 5 source files, 4 ACs from REQ S-34. |
| Timestamp | 2026-10-21 16:43 UTC |
