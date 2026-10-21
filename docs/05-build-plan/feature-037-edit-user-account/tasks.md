---
id: FEAT-037-TASKS
title: "FEAT-037: S-34: Delivery Manager Edits User Account - Tasks"
phase: 5
version: 0.1
template: feature-tasks
template_version: 1.0
status: Draft
author_agent: build-planner
approver: Tech lead
date: 2026-10-21
validation: Pending
---
# FEAT-037: S-34: Delivery Manager Edits User Account - Tasks

## Input References
- FEAT-037 plan.md — implementation steps and file list
- REQ-001 v0.4 § S-34 — acceptance criteria
- API-001 v0.3 § PATCH /api/accounts/users/{id}/ (endpoint #7) — request and response schemas
- DBD-001 v0.1 § audit_auditentry — AuditEntry model fields
- STD-001 v0.1 — coding standards

## Purpose And Scope
Ordered task checklist for the builder of FEAT-037. Each task names the file(s) it produces or modifies. Backend tasks come first to establish the API contract, then frontend tasks consume it.

## Task Checklist

**Mode A (tests first — run before any implementation code)**
- [ ] T-1: Write `src/aplx_ams_django/accounts/tests/test_edit_user.py` with four failing test functions:
  - `test_dm_can_edit_user_fields_and_creates_audit_entries` (REQ S-34 AC-1)
  - `test_role_client_user_without_org_returns_400` (REQ S-34 AC-2)
  - `test_role_change_away_from_client_user_clears_org` (REQ S-34 AC-3)
  - `test_non_dm_patch_returns_403` (REQ S-34 AC-4)
  Each test sends HTTP to PATCH /api/accounts/users/{id}/ and asserts the response code, DB state, and (where applicable) AuditEntry rows. Confirm all four tests fail (red) before proceeding to Mode B.
- [ ] T-2: Write `src/frontend/src/pages/UserManagement.test.tsx` with:
  - `test_edit_button_visible_for_dm_and_opens_dialog` (REQ S-34 AC-1 UI path)
  - `test_edit_button_absent_for_non_dm` (REQ S-34 AC-4 UI path)
  Confirm both tests fail (red) before proceeding to Mode B.

**Mode B (implementation)**
- [ ] T-3: In `src/aplx_ams_django/accounts/serializers.py` add `UpdateUserAccountSerializer(ModelSerializer, partial=True)` for the User model with fields name, email, role, client_organization_id, is_active; add `validate()` method enforcing the client_user + client_organization_id rule (AC-2) and auto-clearing client_organization_id when role is not client_user (AC-3).
- [ ] T-4: In `src/aplx_ams_django/accounts/services.py` add `update_user(user_id: int, payload: dict, actor: User) -> User`: fetch instance via `dal.get_user_by_id(user_id)`; instantiate `UpdateUserAccountSerializer(instance, data=payload, partial=True)`; on valid data capture per-field diffs, call `instance.save()`, create one `AuditEntry` per changed field; return the updated instance.
- [ ] T-5: In `src/aplx_ams_django/accounts/views.py` add `patch(self, request, pk)` to `UserDetailView`: return HTTP 403 if `request.user.role != 'delivery_manager'`; call `services.update_user(pk, request.data, request.user)`; return 200 with `UserAccountSerializer(result).data` or 400 with serializer errors.
- [ ] T-6: In `src/frontend/src/api/users.ts` add `updateUser(id: number, data: Partial<UpdateUserAccountRequest>): Promise<UserAccount>` using the configured Axios instance to call `PATCH /api/accounts/users/${id}/`.
- [ ] T-7: In `src/frontend/src/pages/UserManagement.tsx` add:
  - An "Edit" icon button in the DataGrid actions column, rendered only when `user.role === 'delivery_manager'`.
  - A MUI Dialog containing a form pre-populated with the selected user's name, email, role, client_organization_id, and is_active fields.
  - On submit: call `updateUser(id, changedFields)`; on 200 show MuiSnackbar "User updated"; on 400 show field-level validation errors; on either path refresh the user list.
- [ ] T-8: Run all gate commands locally (`ruff check src/ && ruff format --check src/`, `mypy src/ --strict`, `npx eslint src/frontend/src/ && npx tsc --noEmit`, `pytest --cov`, `npm run test -- --run --coverage`, `bandit -r src/ -ll`, `pip-audit`, `detect-secrets scan`); confirm each exits 0.
- [ ] T-9: Verify `py -3 scripts/check_feature_size.py size FEAT-037` exits 0.

## Assumptions
- A-050: AuditEntry model field names (entity_type, entity_id, field_name, old_value, new_value, actor, created_at) match DBD-001 v0.1 § audit_auditentry. If the actual field names differ in the codebase, raise an OQ before writing T-4. Logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-037 plan.md; REQ-001 v0.4 § S-34; API-001 v0.3 § endpoint #7; DBD-001 v0.1 § audit_auditentry; STD-001 v0.1
- Downstream: Phase 6 test set (created in Phase 6)

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
