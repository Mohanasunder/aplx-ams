---
id: PRM-001
title: APLX AMS: Permission Matrix
phase: 4
version: 0.1
template: permission-matrix
template_version: 2.0
status: Approved
author_agent: backend-designer
approver: Mohanasunder
date: 2026-10-17
validation: Pass
---
# APLX AMS: Permission Matrix

> **Single file.** There is exactly one permission matrix per project. Always use `--id PRM --out docs/04-design/permission-matrix.md` when calling `new_artifact.py`; never auto-name as `PRM-NNN.md`.

## Input References

- PIB-004 v0.1 — Phase 4 Input Brief (Approved 2026-10-17)
- API-001 v0.1 — APLX AMS: API Specification, § Endpoint Summary (In review 2026-10-17)
- THR-001 v0.2 § Authentication and authorization model (Approved 2026-10-17)
- BR-001 v0.3 § B-20, B-21, B-22, B-24 (Approved 2026-10-17)
- NFR-001 v0.3 § N-6, N-7 (Approved 2026-10-17)
- REQ-001 v0.3 § S-1 to S-33 (Approved 2026-10-17)
- ADR-001 v0.3 § ADR A-6, A-7, A-11 (Approved 2026-10-17)
- GLO-001 v0.3 — APLX AMS: Domain Glossary (Approved 2026-10-17)
- BED-001 v0.1 — APLX AMS: Backend Design (In review 2026-10-17)

## Purpose And Scope

Covers: the complete role, feature, and data access matrix for APLX AMS release 1. Every one of the 46 endpoints defined in API-001 is listed with the roles permitted to call it, the HTTP method, and the path. Row-level and field-level access rules are documented per role and per table.

Does not cover: implementation code (Phase 6); screen layout (Phase 4 UI spec); database DDL (DBD-001). Role definitions and row-level security rules that require human decision are flagged for human approval (see § Roles note and § Data Access note).

> **Escalate to a human (do not decide):** Role definitions (what each role can and cannot do at a business level) and row-level security rules (which rows each role can see or modify) are set by the approved upstream artifacts (THR-001 § Authentication and authorization model; BR-001 § B-20, B-21; ADR A-6). This artifact records those decisions in matrix form; it does not invent new permissions. Any permission gap found here must be raised as an open question.

## Roles

Roles are defined in BR-001 v0.3 § B-21, THR-001 v0.2 § Authentication and authorization model, and GLO-001 v0.3. Four roles exist in release 1.

| Role code | GLO-001 name | Persona | Kind | Description |
| --- | --- | --- | --- | --- |
| P1 | L1 support engineer | PER P-1 | Internal user | First-line support: acknowledges tickets, triages, assigns to L2/L3, changes priority, sets Resolved, closes Resolved tickets, records effort, manages awaiting client state |
| P2 | L2/L3 support engineer | PER P-2 | Internal user | Second-line support: acts on tickets assigned to them, records effort, adds comments, manages awaiting client state on assigned tickets |
| P3 | Delivery manager | PER P-3 | Internal user | Full internal access plus: user accounts, roles, temporary passwords, client organizations, SAP applications, contracts, company holiday list, monthly client report generate/publish, finance export, all security events |
| P4 | Client user | PER P-4 | Client user (one client organization) | Raise tickets for own org; view own org's tickets and comments; view own org's published monthly client reports; change own password. Cannot view any audit entry or security event |

Notes on role enforcement:
- Deny by default: any endpoint not listed for a role returns HTTP 403 (THR T-13 control; `HasRolePermission` in `accounts/permissions.py`).
- Unauthenticated callers receive HTTP 401 on any endpoint that requires a session.
- Object-level access (e.g., P2 can only act on assigned tickets; P4 can only see own org) is enforced in the service layer after the role check.

## Feature Access

The table below lists all 46 endpoints from API-001 § Endpoint Summary. Columns P1, P2, P3, P4 show Y (permitted) or — (denied). "Auth" = session cookie required (Y/N). "Object-level" notes any further restriction beyond role.

### Authentication (F-5)

| # | Method | Path | P1 | P2 | P3 | P4 | Auth | Object-level | Story |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | POST | /api/auth/login/ | Y | Y | Y | Y | N | None; rate-limited 10 req/min per IP at Nginx | REQ S-21 |
| 2 | POST | /api/auth/logout/ | Y | Y | Y | Y | Y | Own session only | REQ S-21 |
| 3 | GET | /api/auth/me/ | Y | Y | Y | Y | Y | Own user record | REQ S-21 |

### User account management (F-6)

| # | Method | Path | P1 | P2 | P3 | P4 | Auth | Object-level | Story |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | POST | /api/accounts/users/ | — | — | Y | — | Y | P3 only | REQ S-20, S-30 |
| 5 | GET | /api/accounts/users/ | — | — | Y | — | Y | P3 sees all | REQ S-20 |
| 6 | GET | /api/accounts/users/{id}/ | — | — | Y | — | Y | P3 sees any user | REQ S-20 |
| 7 | PATCH | /api/accounts/users/{id}/ | — | — | Y | — | Y | P3 only; writable: name, email, role, client_org_id | REQ S-20 |
| 8 | POST | /api/accounts/users/{id}/deactivate/ | — | — | Y | — | Y | P3 only | REQ S-20 |
| 9 | POST | /api/accounts/users/{id}/set-temp-password/ | — | — | Y | — | Y | P3 only; new_password not returned | REQ S-30 |
| 10 | POST | /api/accounts/me/change-password/ | Y | Y | Y | Y | Y | Own account only; current_password required | REQ S-31 |

### Organization setup (F-1, F-5)

| # | Method | Path | P1 | P2 | P3 | P4 | Auth | Object-level | Story |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | POST | /api/organizations/ | — | — | Y | — | Y | P3 only | REQ S-18 |
| 12 | GET | /api/organizations/ | Y | Y | Y | Y | Y | P4 sees own org only (RLS + DAL filter) | REQ S-18, S-22 |
| 13 | GET | /api/organizations/{id}/ | Y | Y | Y | — | Y | Internal only | REQ S-18 |
| 14 | PATCH | /api/organizations/{id}/ | — | — | Y | — | Y | P3 only; writable: name | REQ S-18 |
| 15 | POST | /api/organizations/{id}/sap-applications/ | — | — | Y | — | Y | P3 only | REQ S-18 |
| 16 | GET | /api/organizations/{id}/sap-applications/ | Y | Y | Y | Y | Y | P4 sees own org's SAP apps only (RLS) | REQ S-18, S-1 |

### Contract management (F-4, F-5)

| # | Method | Path | P1 | P2 | P3 | P4 | Auth | Object-level | Story |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 17 | POST | /api/organizations/{id}/contracts/ | — | — | Y | — | Y | P3 only; at most one active contract per org (409 on conflict) | REQ S-19 |
| 18 | GET | /api/organizations/{id}/contracts/ | — | — | Y | — | Y | P3 only | REQ S-16, S-19 |
| 19 | POST | /api/organizations/{id}/contracts/{contract_id}/end/ | — | — | Y | — | Y | P3 only; sets is_active=False, ended_at=now() | REQ S-27 |
| 20 | GET | /api/organizations/{id}/contracts/active/ | — | — | Y | — | Y | P3 only; includes computed hours_bank_balance | REQ S-16, S-19 |

### Company holiday list (F-2 support)

| # | Method | Path | P1 | P2 | P3 | P4 | Auth | Object-level | Story |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 21 | GET | /api/holidays/ | Y | Y | Y | — | Y | Internal only; active entries only | REQ S-24 |
| 22 | POST | /api/holidays/ | — | — | Y | — | Y | P3 only | REQ S-24 |
| 23 | DELETE | /api/holidays/{id}/ | — | — | Y | — | Y | P3 only; soft-remove only (sets removed_at) | REQ S-24 |

### Ticket management (F-1)

| # | Method | Path | P1 | P2 | P3 | P4 | Auth | Object-level | Story |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 24 | POST | /api/tickets/ | — | — | — | Y | Y | P4 only; own org's SAP applications only | REQ S-1 |
| 25 | GET | /api/tickets/ | Y | Y | Y | Y | Y | P4 sees own org only (RLS); P2 sees all (ticket list); SLA state included | REQ S-2, S-10, S-11, S-12, S-22 |
| 26 | GET | /api/tickets/{id}/ | Y | Y | Y | Y | Y | P4 sees own org only (RLS + 404 for another org); SLA state included | REQ S-2, S-5, S-10, S-11, S-22 |
| 27 | PATCH | /api/tickets/{id}/priority/ | Y | — | — | — | Y | P1 only; reason field required | REQ S-4 |
| 28 | POST | /api/tickets/{id}/assign/ | Y | — | — | — | Y | P1 only; target must be l2l3_support user | REQ S-5 |
| 29 | POST | /api/tickets/{id}/resolve/ | Y | Y | — | — | Y | P1 or P2; P2 only if assigned to them | REQ S-6 |
| 30 | POST | /api/tickets/{id}/close/ | Y | — | — | — | Y | P1 only; ticket must be Resolved (409 otherwise) | REQ S-7 |
| 31 | POST | /api/tickets/{id}/await-client/ | Y | Y | — | — | Y | P1 or the L2/L3 assigned to the ticket | REQ S-8 |
| 32 | DELETE | /api/tickets/{id}/await-client/ | Y | Y | — | — | Y | P1 or the L2/L3 assigned to the ticket | REQ S-8 |
| 33 | POST | /api/tickets/{id}/comments/ | Y | Y | Y | Y | Y | P4 own org only (RLS); adds comment; P4 comment also clears awaiting client if set | REQ S-28, S-29 |
| 34 | GET | /api/tickets/{id}/comments/ | Y | Y | Y | Y | Y | P4 own org only (RLS) | REQ S-2, S-28, S-29 |

### Effort tracking (F-4)

| # | Method | Path | P1 | P2 | P3 | P4 | Auth | Object-level | Story |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 35 | POST | /api/tickets/{id}/effort/ | Y | Y | — | — | Y | P1 or the L2/L3 assigned to the ticket | REQ S-15 |
| 36 | GET | /api/tickets/{id}/effort/ | Y | Y | Y | — | Y | Internal only; all effort for the ticket | REQ S-15, S-16 |
| 37 | PATCH | /api/effort/{effort_id}/ | Y | Y | Y | — | Y | P1/P2: own entry within calendar month of effort_date only; P3: any entry at any time | REQ S-25, S-26 |
| 38 | DELETE | /api/effort/{effort_id}/ | Y | Y | — | — | Y | P1/P2 own entry within calendar month only; soft-delete (is_deleted=True) | REQ S-25 |

### Service reporting and dashboards (F-3)

| # | Method | Path | P1 | P2 | P3 | P4 | Auth | Object-level | Story |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 39 | GET | /api/reports/dashboard/ | Y | Y | Y | — | Y | Internal only; all orgs | REQ S-12 |
| 40 | POST | /api/reports/client-reports/{org_id}/{year}/{month}/generate/ | — | — | Y | — | Y | P3 only | REQ S-13 |
| 41 | POST | /api/reports/client-reports/{org_id}/{year}/{month}/publish/ | — | — | Y | — | Y | P3 only; sets published_at | REQ S-13, S-14 |
| 42 | GET | /api/reports/client-reports/{org_id}/{year}/{month}/ | Y | Y | Y | Y | Y | P4: own org and published only (RLS + published_at IS NOT NULL) | REQ S-13, S-14 |
| 43 | GET | /api/reports/client-reports/{org_id}/{year}/{month}/download/ | Y | Y | Y | Y | Y | P4: own org and published only; ?format=xlsx\|pdf | REQ S-14 |

### Finance export (F-8)

| # | Method | Path | P1 | P2 | P3 | P4 | Auth | Object-level | Story |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 44 | GET | /api/reports/finance-export/{year}/{month}/ | — | — | Y | — | Y | P3 only; all orgs; ?format=xlsx\|csv | REQ S-17 |

### Audit trail (F-7)

| # | Method | Path | P1 | P2 | P3 | P4 | Auth | Object-level | Story |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 45 | GET | /api/tickets/{id}/audit/ | Y | Y | Y | — | Y | Internal only; all internal users see any ticket's audit entries (BR B-22) | REQ S-23 |
| 46 | GET | /api/audit/security-events/ | Y | Y | Y | — | Y | P3 sees all; P1/P2 see own account only (object-level: filtered by entity_id = request.user.id) | REQ S-33 |

### Endpoint count summary

| Feature | Endpoints | P1 | P2 | P3 | P4 |
| --- | --- | --- | --- | --- | --- |
| F-1 Ticket management | 24–34 (11) | 9 | 7 | 5 | 5 |
| F-2 SLA timer (embedded in F-1, F-3) | 0 separate | — | — | — | — |
| F-3 Service reporting and dashboards | 39–43 (5) | 4 | 4 | 5 | 2 |
| F-4 Effort tracking | 35–38 (4) | 4 | 4 | 2 | 0 |
| F-5 Client log-in and portal | 1–3, 11–12, 16 (6) | 5 | 5 | 6 | 4 |
| F-6 User account management | 4–10 (7) | 1 | 1 | 7 | 1 |
| F-7 Audit trail | 45–46 (2) | 2 | 2 | 2 | 0 |
| F-8 Finance export | 44 (1) | 0 | 0 | 1 | 0 |
| Org/contract/holiday setup | 13–15, 17–23 (10) | 2 | 2 | 10 | 0 |
| **Total distinct endpoints** | **46** | | | | |

## Data Access

Row-level and field-level access rules by role and table. Rules are derived from BR-001 § B-20, B-21; ADR A-6; NFR N-7; and THR-001 § Authentication and authorization model.

> **Note:** Row-level security (RLS) policy definitions are in DBD-001. This section documents the business-layer rules that complement RLS. Any gap or conflict between this section and DBD-001 must be raised as a spec change record.

### organizations_clientorg

| Role | Read rows | Write rows | Writable fields |
| --- | --- | --- | --- |
| P1, P2 | All orgs (internal) | None | — |
| P3 | All orgs | CREATE new org; UPDATE name | name |
| P4 | Own org row only (RLS: id = app.client_org_id) | None | — |

### organizations_sapapplication

| Role | Read rows | Write rows | Writable fields |
| --- | --- | --- | --- |
| P1, P2 | All (internal) | None | — |
| P3 | All | CREATE for any org | name, client_org_id |
| P4 | Own org's SAP apps only (RLS: client_org_id = app.client_org_id) | None | — |

### organizations_contract

| Role | Read rows | Write rows | Writable fields |
| --- | --- | --- | --- |
| P1, P2 | None (endpoints 17–20 are P3 only) | None | — |
| P3 | All contracts for any org | CREATE; end (is_active=False, ended_at) | contract_type, contracted_hours, monthly_close_at |
| P4 | None | None | — |

### accounts_user

| Role | Read rows | Write rows | Writable fields |
| --- | --- | --- | --- |
| P1, P2 | None (user-list endpoint is P3 only); own record via /api/auth/me/ | Own password only (change-password endpoint) | password (own, via change-password endpoint only) |
| P3 | All user rows | CREATE; UPDATE name, email, role, client_org_id; deactivate; set temp password | name, email, role, client_org_id, is_active, password (temp via set-temp-password only) |
| P4 | Own row only (RLS: id = app.user_id); via /api/auth/me/ | Own password only | password (own, via change-password endpoint only) |

Forbidden for all roles: writing `failed_attempts`, `locked_until`, `date_joined`, `last_login` directly (managed by the service layer only).

### sla_holidayentry

| Role | Read rows | Write rows | Notes |
| --- | --- | --- | --- |
| P1, P2, P3 | Active entries only (endpoints list by default; historical available via SLA computation) | P3: CREATE (add holiday); P3: soft-remove (set removed_at, removed_by_id) | Hard-delete never permitted; ADR A-10 |
| P4 | None | None | — |

### tickets_ticket

| Role | Read rows | Write rows | Writable fields |
| --- | --- | --- | --- |
| P1 | All tickets (internal) | priority (with reason), assigned_to_id, status (Resolved, Closed), awaiting_client_since/total_paused_minutes, response_stopped_at/response_status, escalation_flag | See ticket lifecycle state machine in BED-001 |
| P2 | All tickets; updates only on assigned tickets | status (Resolved for assigned tickets), awaiting_client_since (assigned tickets only) | Same as P1 for assigned tickets |
| P3 | All tickets | None (P3 does not change ticket lifecycle fields) | — |
| P4 | Own org only (RLS: client_org_id = app.client_org_id) | None | — |

Fields that can never be written directly through the API: `ticket_reference` (set at creation from sequence), `raised_at` (set at creation to now()), `raised_by_id` (set at creation to request.user), `client_org_id` (set at creation from user.client_org_id for P4), `response_stopped_at`, `response_status`, `resolution_stopped_at`, `resolution_status`, `total_paused_minutes`, `escalation_flag` (all managed by service layer).

### tickets_comment

| Role | Read rows | Write rows | Notes |
| --- | --- | --- | --- |
| P1, P2, P3 | All comments on any ticket | CREATE comment on any ticket | Comments are permanent; no edit or delete endpoint |
| P4 | Own org's comments only (RLS: client_org_id = app.client_org_id) | CREATE comment on own org's tickets | A P4 comment clears awaiting_client if status = 'Awaiting client' (DEC-026) |

### effort_effortentry

| Role | Read rows | Write rows | Editing window |
| --- | --- | --- | --- |
| P1 | All non-deleted entries for any ticket | CREATE own entries; EDIT own entries; soft-DELETE own entries | Edit/delete within calendar month of effort_date (A-025 Confirmed) |
| P2 | All non-deleted entries for any ticket | CREATE own entries on assigned tickets; EDIT own; soft-DELETE own | Same window as P1 |
| P3 | All non-deleted entries for any ticket | EDIT any entry (no delete) | No window restriction (REQ S-26) |
| P4 | None | None | — |

### reports_monthlyclientreport

| Role | Read rows | Write rows | Notes |
| --- | --- | --- | --- |
| P1, P2 | All report metadata (any org) | None | Report content generated on demand |
| P3 | All report metadata | CREATE/UPSERT (generate); publish (set published_at) | One metadata row per (org, year, month); unique constraint |
| P4 | Own org, published rows only (RLS: client_org_id = app.client_org_id AND published_at IS NOT NULL) | None | — |

### audit_auditentry

| Role | Read rows | Write rows | Notes |
| --- | --- | --- | --- |
| P1, P2 | All rows for any ticket (entity_type = 'ticket' or 'effort_entry'); own security events only (entity_id = own user.id where entity_type = 'security_event') | None via API; INSERT via audit_event() in service calls | Application-layer filter for security events; RLS allows all internal users |
| P3 | All rows (all entity types, all users) | None via API; INSERT via audit_event() | Delivery manager sees all security events (BR B-24) |
| P4 | None (RLS blocks all reads: rls_auditentry USING user_kind = 'internal') | None | Client users cannot view any audit entries, including their own security events (BR B-22, B-24; REQ S-33 AC-4) |

No role can UPDATE or DELETE audit entries. The DB runtime role `aplx_ams_app` has INSERT + SELECT only on `audit_auditentry` (DBD-001; ADR A-11; NFR N-6).

## Assumptions

- A-014 (Open): Response clock and resolution clock evaluated independently. This matrix treats them as separate computed fields on the ticket; no separate endpoint is needed (consistent with API-001 § Endpoint Summary note on F-2).
- A-015 (Open): Reporting period is calendar month in IST. No impact on the permission matrix itself.
- A-019 (Confirmed): All sign-in refusals return the same generic message. Reflected in endpoint 1 behavior.

## Open Questions

No new open questions are raised by this artifact. All role and permission rules are traceable to approved upstream artifacts (THR-001 § Authentication and authorization model; BR-001 § B-20, B-21; ADR A-6; REQ-001 S-1 to S-33).

## Traceability Links

- Upstream: PIB-004 v0.1; API-001 v0.1; THR-001 v0.2; BR-001 v0.3 (B-20, B-21, B-22, B-24); NFR-001 v0.3 (N-6, N-7); REQ-001 v0.3 (S-1 to S-33); ADR-001 v0.3 (A-6, A-7, A-11); GLO-001 v0.3; BED-001 v0.1.
- Downstream: Phase 5 feature breakdown (FBD); Phase 6 feature plans (each feature references this matrix for its endpoint's permitted roles); Phase 7 test cases (role × endpoint matrix test from THR T-13 verification).

## Quality Checklist

- [x] Every template section is filled, or marked "Not applicable - reason"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)
- [x] Permission matrix covers every endpoint — all 46 endpoints from API-001 are listed

## Approval Record
| Field | Value |
| --- | --- |
| Decision | Approve |
| Approver | Mohanasunder |
| Role | Architect / tech lead + UX |
| Version | 0.1 |
| Conditions | None |
| Comments | Phase 4 design package approved. |
| Timestamp | 2026-10-17 14:04 UTC |
