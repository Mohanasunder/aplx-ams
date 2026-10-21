---
id: FEAT-037-ACC
title: "FEAT-037: S-34: Delivery Manager Edits User Account - Acceptance Criteria"
phase: 5
version: 0.1
template: feature-acceptance
template_version: 1.1
status: Approved
author_agent: build-planner
approver: Mohanasunder
date: 2026-10-21
validation: Pass
---
# FEAT-037: S-34: Delivery Manager Edits User Account - Acceptance Criteria

## Input References
- REQ-001 v0.4 — APLX AMS: User Stories (Approved 2026-10-21, SCR S-19) § S-34
- API-001 v0.3 — APLX AMS: API Specification (Approved 2026-10-21, SCR S-20) § PATCH /api/accounts/users/{id}/ (endpoint #7)
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-037 (REQ S-34). Criteria are copied verbatim from REQ-001 v0.4 § S-34.

## Acceptance Criteria
REQ-034 AC-1 REQ S-34 AC-1: Given a delivery manager and an existing user account, when the delivery manager submits a PATCH /api/accounts/users/{id}/ request with one or more of the fields name, email, role, client_organization_id, or is_active, then only the supplied fields are updated on the account, the endpoint returns HTTP 200 with the UserAccount schema, and one audit trail entry recording old value, new value, actor identity, and UTC timestamp is created for each field whose value changed.
REQ-034 AC-2 REQ S-34 AC-2: Given a delivery manager, when they submit a PATCH /api/accounts/users/{id}/ request that sets role to client_user and neither the request nor the existing account provides a client_organization_id, then the account is not modified and the endpoint returns HTTP 400 with a ValidationError body.
REQ-034 AC-3 REQ S-34 AC-3: Given a delivery manager, when they submit a PATCH /api/accounts/users/{id}/ request that sets role to any value other than client_user, then the account's client_organization_id is set to null automatically and the endpoint returns HTTP 200 with the updated UserAccount schema.
REQ-034 AC-4 REQ S-34 AC-4: Given a user whose role is not delivery_manager, when they submit a PATCH /api/accounts/users/{id}/ request, then the endpoint returns HTTP 403 with a SimpleError body and the account is not modified.

## Test Scenarios
REQ-034 AC-1 REQ S-34 AC-1: Send PATCH as delivery_manager with changed name and email; assert 200, DB fields updated, two AuditEntry rows with correct old/new values, actor, and timestamp.
REQ-034 AC-2 REQ S-34 AC-2: Send PATCH as delivery_manager setting role to client_user on an account with no client_organization_id; assert 400 ValidationError body, no DB change, no AuditEntry created.
REQ-034 AC-3 REQ S-34 AC-3: Send PATCH as delivery_manager setting role to l2l3_support on an account with a non-null client_organization_id; assert 200, client_organization_id is null in DB, AuditEntry rows for role and client_organization_id changes.
REQ-034 AC-4 REQ S-34 AC-4: Send PATCH as l2l3_support user; assert 403 SimpleError body, no DB change.

## Assumptions
- A-050: AuditEntry model field names (entity_type, entity_id, field_name, old_value, new_value, actor, created_at) are as documented in DBD-001 v0.1 § audit_auditentry. If the actual schema differs, an SCR is required. Logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.4 § S-34; API-001 v0.3 § endpoint #7; PIB-005 v0.1; SCR-001 § S-19 (REQ S-34 added); SCR-001 § S-20 (API-001 v0.3)
- Downstream: FEAT-037-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
| Comments | FEAT-037 acceptance criteria AC-1 through AC-4 approved as written. |
| Timestamp | 2026-10-21 16:43 UTC |
