---
id: API-001
title: APLX AMS: API Specification
phase: 4
version: 0.1
template: api-spec
template_version: 2.0
status: Approved
author_agent: api-designer
approver: Mohanasunder
date: 2026-10-17
validation: Pass
---
# APLX AMS: API Specification

> **Single file.** There is exactly one API spec per project. Always use `--id API --out docs/04-design/api-spec.md` when calling `new_artifact.py`; never auto-name as `API-NNN.md`. The OpenAPI file is always `docs/04-design/openapi.yaml`.

## Input References

- SUM-003 v0.2 — Phase 3 Summary (Approved 2026-10-17).
- REQ-001 v0.3 — APLX AMS: User Stories, S-1 to S-33 (Approved 2026-10-17).
- BR-001 v0.3 — APLX AMS: Business Rules, B-1 to B-24 (Approved 2026-10-17).
- NFR-001 v0.3 — APLX AMS: Non-Functional Requirements, N-1 to N-9 (Approved 2026-10-17).
- GLO-001 v0.3 — APLX AMS: Domain Glossary (Approved 2026-10-17).
- PRS-001 v0.3 — APLX AMS: Product Requirement Specification, F-1 to F-8 (Approved 2026-10-17).
- ADR-001 v0.3 — APLX AMS: Architecture Decision Records, A-3, A-6, A-7, A-11, A-13 (Approved 2026-10-17).
- THR-001 v0.2 — APLX AMS Threat Model, § Mitigations, § Authentication and authorization model (Approved 2026-10-17).
- PIB-004 v0.1 — Phase 4 Input Brief (Approved 2026-10-17): API conventions, auth model, rate limits, confirmed A-019.
- PER-001 v0.2 — APLX AMS: Personas, P-1 to P-4 (Approved 2026-10-17).
- SCR S-3 (Approved 2026-10-17): password management endpoints S-30, S-31.
- SCR S-4 (Approved 2026-10-17): security events in audit trail, S-32, S-33.

## Purpose And Scope

Covers: the complete REST API contract for APLX AMS release 1, including authentication, authorization, pagination, error model, security controls, and one endpoint per story need (S-1 to S-33). The contract spans 8 features: ticket management (F-1, F-2), SLA timer and status (F-3), service reporting and dashboards (F-4), effort tracking (F-5), client log-in and client-facing portal (F-6), user account management (F-6), audit trail (F-8), and finance export (F-5). All 46 endpoints are listed in the Endpoint Summary and defined in `docs/04-design/openapi.yaml`.

Does not cover: screen layout, CSS, component design (Phase 4 UI spec), database DDL (Phase 4 database design), infrastructure or deployment configuration (Phase 8), third-party API integrations (none in scope, PRS Non-Goals).

## Conventions

### URL pattern
All endpoints are under the `/api/` prefix, served by Nginx forwarding to the Django backend on the same origin (ADR A-3). No version segment in the path for release 1; if a breaking change is needed after release 1, `/api/v2/` is added by ADR (ADR A-3, PIB-004). Trailing slashes are included on all paths (Django convention).

### Media type
All request and response bodies are `Content-Type: application/json; charset=utf-8`. File downloads (Excel, CSV, PDF) respond with the matching MIME type (`application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`, `text/csv`, `application/pdf`) and a `Content-Disposition: attachment` header. The format is selected by the `?format=xlsx|csv|pdf` query parameter on download endpoints.

### Timestamps
All timestamps in UTC, ISO 8601 with Z suffix: `2026-10-17T09:00:00Z`. The frontend displays times in IST (Asia/Kolkata, UTC+05:30, no daylight saving) (ADR A-9, A-027 — open assumption).

### Authentication
Session-based only. Clients obtain a session by calling `POST /api/auth/login/`. The server sets an `HttpOnly; Secure; SameSite=Strict` cookie named `sessionid`. All subsequent requests carry this cookie. Sessions expire after 60 minutes of inactivity (rolling) and at most 12 hours after sign-in (ADR A-7, DEC-030). A new session identifier is issued at every sign-in. The `sessionid` cookie is the only authentication mechanism; no Bearer token or API key.

### CSRF protection
Django CSRF token required on every state-changing request (POST, PUT, PATCH, DELETE). The client fetches the `csrftoken` cookie after sign-in and sends it as the `X-CSRFToken` header on state-changing requests (THR T-9 control; ADR A-7). The OpenAPI spec marks all state-changing operations with `x-csrf-required: true`.

### Roles
Four roles per PER-001 and the `role_enum` PostgreSQL ENUM in DBD-001:

| Persona shorthand | DB enum value | Description |
| --- | --- | --- |
| P1 | `l1_support` | L1 support engineer |
| P2 | `l2l3_support` | L2/L3 support engineer |
| P3 | `delivery_manager` | Delivery manager |
| P4 | `client_user` | Client user |

Every endpoint declares its permitted roles using the `x-roles` OpenAPI extension, which uses the canonical DB enum values (`l1_support`, `l2l3_support`, `delivery_manager`, `client_user`). The endpoint summary tables below use the P1–P4 shorthand for readability. Deny by default: any role not listed is refused with HTTP 403 (THR T-13 control; ADR A-7 § Decision, follow-up).

### Client organization scoping (ADR A-6)
All endpoints that return client-owned data enforce client organization scoping at the API layer. For a client user (P4), the backend queries filter by the client organization bound to their user account using PostgreSQL row-level security. For internal users (P1, P2, P3), all client organizations' data is accessible. A client user attempting to access another organization's resource receives HTTP 403 with no detail of the resource.

### Pagination
List endpoints return paginated JSON: `{"count": N, "next": "url|null", "previous": "url|null", "results": [...]}`. Default page size: 50 items. Clients pass `?page=N` to navigate. There is no cursor-based pagination in release 1.

### Idempotency
GET, PUT, and DELETE requests are idempotent. POST requests are not idempotent; duplicating a POST creates a new resource. PATCH requests apply partial updates to the named resource. No idempotency key header is required in release 1.

### Security controls

**Rate limiting on sign-in (THR T-2, T-35 control):** Nginx limits `POST /api/auth/login/` to 10 requests per minute per client IP address with a burst of 5 (Nginx `limit_req_zone`). Requests exceeding the limit receive HTTP 429. This is enforced at the `proxy` container, not the application.

**Content Security Policy:** Nginx sets `Content-Security-Policy: default-src 'self'; script-src 'self'; frame-ancestors 'none'` on all responses (THR T-6, T-9 control). The `X-Frame-Options: DENY` header is also set.

**HSTS:** Nginx sets `Strict-Transport-Security: max-age=31536000; includeSubDomains` after the self-signed certificate is installed as trusted on user machines (ADR A-14).

**Export formula escaping (THR T-14 control):** All Excel and CSV cells whose value starts with `=`, `+`, `-`, or `@` are prefixed with a single quote when written by XlsxWriter or the Python `csv` module, preventing formula injection (ADR A-12 follow-up).

**Password values never returned:** No API response includes a password, temporary password, hash, or session identifier value (THR T-16 control; BR B-24; ADR A-8 follow-up).

**Sign-in refusal message (A-019, CONFIRMED):** `POST /api/auth/login/` responds with HTTP 401 and the generic message `"Invalid credentials."` for every refusal — wrong password, unknown account name, deactivated user account, locked user account — without saying which field was wrong (REQ S-21 AC-2; THR T-10 control).

## Error Model

All error responses use one of two formats from Django REST Framework.

**Simple error (HTTP 4xx or 5xx):**
```json
{"detail": "Human-readable message.", "code": "machine_code"}
```

**Validation error (HTTP 400):**
```json
{"field_name": ["Error message for this field."], "non_field_errors": ["..."] }
```

Status codes used:

| Code | Meaning | Example trigger |
| --- | --- | --- |
| 200 | OK | Successful GET, PATCH |
| 201 | Created | Successful POST that creates a resource |
| 204 | No Content | Successful DELETE or action with no response body |
| 400 | Bad Request | Validation failure (missing field, invalid value) |
| 401 | Unauthorized | Session missing or expired |
| 403 | Forbidden | Role not permitted; client user accessing another organization's resource |
| 404 | Not Found | Resource ID does not exist or is not visible to the caller |
| 409 | Conflict | Business rule violation (for example, a second active contract, or closing a non-Resolved ticket) |
| 429 | Too Many Requests | Nginx rate limit on the sign-in endpoint |
| 500 | Internal Server Error | Unhandled backend exception (no stack trace in response) |

The `code` field in simple errors uses kebab-case identifiers, for example: `authentication_failed`, `permission_denied`, `not_found`, `conflict`, `validation_error`.

## Versioning

No version segment in the path for release 1. The API is an internal tool serving one frontend on the same origin; breaking changes require a new ADR before they are introduced. If `/api/v2/` is added later, `/api/v1/` (the current paths without a version segment) remains until all clients are migrated and a deprecation window closes. This is an ADR-gate decision, not a unilateral change.

## Endpoint Summary

46 endpoints in total. Roles: P1 = L1 support engineer, P2 = L2/L3 support engineer, P3 = delivery manager, P4 = client user. Auth = session cookie required (Y/N).

### Authentication (F-5)

| # | Method | Path | Purpose | Roles | Auth | Story IDs |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | POST | /api/auth/login/ | Sign in; create session | (none — public) | N | REQ S-21 |
| 2 | POST | /api/auth/logout/ | Sign out; end session | P1, P2, P3, P4 | Y | REQ S-21 |
| 3 | GET | /api/auth/me/ | Current signed-in user information | P1, P2, P3, P4 | Y | REQ S-21 |

### User account management (F-6)

| # | Method | Path | Purpose | Roles | Auth | Story IDs |
| --- | --- | --- | --- | --- | --- | --- |
| 4 | POST | /api/accounts/users/ | Create user account | P3 | Y | REQ S-20, S-30 |
| 5 | GET | /api/accounts/users/ | List user accounts | P3 | Y | REQ S-20 |
| 6 | GET | /api/accounts/users/{id}/ | Get user account detail | P3 | Y | REQ S-20 |
| 7 | PATCH | /api/accounts/users/{id}/ | Update user account (name, email, role, client org) | P3 | Y | REQ S-20 |
| 8 | POST | /api/accounts/users/{id}/deactivate/ | Deactivate user account | P3 | Y | REQ S-20 |
| 9 | POST | /api/accounts/users/{id}/set-temp-password/ | Set temporary password; clears lockout | P3 | Y | REQ S-30 |
| 10 | POST | /api/accounts/me/change-password/ | Change own password (current password required) | P1, P2, P3, P4 | Y | REQ S-31 |

### Organization setup (F-1, F-5 portal, setup)

| # | Method | Path | Purpose | Roles | Auth | Story IDs |
| --- | --- | --- | --- | --- | --- | --- |
| 11 | POST | /api/organizations/ | Create client organization | P3 | Y | REQ S-18 |
| 12 | GET | /api/organizations/ | List client organizations (P4 sees own org only) | P1, P2, P3, P4 | Y | REQ S-18, S-22 |
| 13 | GET | /api/organizations/{id}/ | Get client organization detail | P1, P2, P3 | Y | REQ S-18 |
| 14 | PATCH | /api/organizations/{id}/ | Update client organization name | P3 | Y | REQ S-18 |
| 15 | POST | /api/organizations/{id}/sap-applications/ | Add SAP application to client organization | P3 | Y | REQ S-18 |
| 16 | GET | /api/organizations/{id}/sap-applications/ | List SAP applications of client organization | P1, P2, P3, P4 | Y | REQ S-18, S-1 |

### Contract management (F-4, F-5)

| # | Method | Path | Purpose | Roles | Auth | Story IDs |
| --- | --- | --- | --- | --- | --- | --- |
| 17 | POST | /api/organizations/{id}/contracts/ | Create contract (hours bank or fixed fee) | P3 | Y | REQ S-19 |
| 18 | GET | /api/organizations/{id}/contracts/ | List contracts for client organization | P3 | Y | REQ S-16, S-19 |
| 19 | POST | /api/organizations/{id}/contracts/{contract_id}/end/ | End active contract | P3 | Y | REQ S-27 |
| 20 | GET | /api/organizations/{id}/contracts/active/ | Get active contract with hours bank balance | P3 | Y | REQ S-16, S-19 |

### Company holiday list (SLA timers — F-2 support)

| # | Method | Path | Purpose | Roles | Auth | Story IDs |
| --- | --- | --- | --- | --- | --- | --- |
| 21 | GET | /api/holidays/ | List company holiday dates | P1, P2, P3 | Y | REQ S-24 |
| 22 | POST | /api/holidays/ | Add company holiday date | P3 | Y | REQ S-24 |
| 23 | DELETE | /api/holidays/{id}/ | Remove company holiday date | P3 | Y | REQ S-24 |

### Ticket management (F-1)

| # | Method | Path | Purpose | Roles | Auth | Story IDs |
| --- | --- | --- | --- | --- | --- | --- |
| 24 | POST | /api/tickets/ | Raise ticket (incident or service request) | P4 | Y | REQ S-1 |
| 25 | GET | /api/tickets/ | List tickets with SLA state and escalation flag | P1, P2, P3, P4 | Y | REQ S-2, S-10, S-11, S-12, S-22 |
| 26 | GET | /api/tickets/{id}/ | Get ticket detail with SLA state and escalation flag | P1, P2, P3, P4 | Y | REQ S-2, S-5, S-10, S-11, S-22 |
| 27 | PATCH | /api/tickets/{id}/priority/ | Change ticket priority with reason | P1 | Y | REQ S-4 |
| 28 | POST | /api/tickets/{id}/assign/ | Assign ticket to L2/L3 support engineer | P1 | Y | REQ S-5 |
| 29 | POST | /api/tickets/{id}/resolve/ | Set ticket status to Resolved | P1, P2 | Y | REQ S-6 |
| 30 | POST | /api/tickets/{id}/close/ | Close a Resolved ticket | P1 | Y | REQ S-7 |
| 31 | POST | /api/tickets/{id}/await-client/ | Set awaiting client (assigned support engineer only, object-level) | P1, P2 | Y | REQ S-8 |
| 32 | DELETE | /api/tickets/{id}/await-client/ | Clear awaiting client (assigned support engineer only, object-level) | P1, P2 | Y | REQ S-8 |
| 33 | POST | /api/tickets/{id}/comments/ | Add comment on ticket (P4 own org only, object-level) | P1, P2, P3, P4 | Y | REQ S-28, S-29 |
| 34 | GET | /api/tickets/{id}/comments/ | List comments on ticket (P4 own org only, object-level) | P1, P2, P3, P4 | Y | REQ S-2, S-28, S-29 |

### Effort tracking (F-4)

| # | Method | Path | Purpose | Roles | Auth | Story IDs |
| --- | --- | --- | --- | --- | --- | --- |
| 35 | POST | /api/tickets/{id}/effort/ | Record effort entry on ticket (assigned support engineer only, object-level) | P1, P2 | Y | REQ S-15 |
| 36 | GET | /api/tickets/{id}/effort/ | List effort entries on ticket | P1, P2, P3 | Y | REQ S-15, S-16 |
| 37 | PATCH | /api/effort/{effort_id}/ | Edit effort entry (own within month for P1/P2; any for P3 at any time) | P1, P2, P3 | Y | REQ S-25, S-26 |
| 38 | DELETE | /api/effort/{effort_id}/ | Delete own effort entry within calendar month of its date (P1, P2 only; P3 cannot delete) | P1, P2 | Y | REQ S-25 |

### Service reporting and dashboards (F-3)

| # | Method | Path | Purpose | Roles | Auth | Story IDs |
| --- | --- | --- | --- | --- | --- | --- |
| 39 | GET | /api/reports/dashboard/ | Live dashboard: open ticket counts, SLA states, escalation flags, hours bank balances, and per-SAP-application breakdown per client organization (UIS-001) | P1, P2, P3 | Y | REQ S-12 |
| 40 | POST | /api/reports/client-reports/{org_id}/{year}/{month}/generate/ | Generate monthly client report for a client organization | P3 | Y | REQ S-13 |
| 41 | POST | /api/reports/client-reports/{org_id}/{year}/{month}/publish/ | Publish generated monthly client report | P3 | Y | REQ S-13, S-14 |
| 42 | GET | /api/reports/client-reports/{org_id}/{year}/{month}/ | View monthly client report (P4 own org and published only, object-level) | P1, P2, P3, P4 | Y | REQ S-13, S-14 |
| 43 | GET | /api/reports/client-reports/{org_id}/{year}/{month}/download/ | Download monthly client report as Excel or PDF (?format=xlsx|pdf) (P4 own org and published only) | P1, P2, P3, P4 | Y | REQ S-14, A-029 |

### Finance export (F-8)

| # | Method | Path | Purpose | Roles | Auth | Story IDs |
| --- | --- | --- | --- | --- | --- | --- |
| 44 | GET | /api/reports/finance-export/{year}/{month}/ | Download finance export as Excel or CSV (?format=xlsx|csv) | P3 | Y | REQ S-17, A-029 |

**Finance export columns (FinanceExportRow schema in openapi.yaml):** one row per effort entry recorded in the given month. Columns: `period` (YYYY-MM), `client_org` (string), `contract_type` (hours_bank or fixed_fee), `ticket_ref` (string), `ticket_title` (string), `engineer` (full name), `hours` (decimal > 0), `remaining_hours_bank_balance` (decimal or null — null for fixed_fee contracts; BR B-17; A-011 confirmed).

### Audit trail (F-7)

| # | Method | Path | Purpose | Roles | Auth | Story IDs |
| --- | --- | --- | --- | --- | --- | --- |
| 45 | GET | /api/tickets/{id}/audit/ | List audit entries for a ticket (status, priority, assignment, effort changes) | P1, P2, P3 | Y | REQ S-23 |
| 46 | GET | /api/audit/security-events/ | View security events (P3 all accounts; P1/P2 own account only, object-level) | P1, P2, P3 | Y | REQ S-33 |

### Endpoint count by feature

| Feature | Endpoints | Count |
| --- | --- | --- |
| F-1 Ticket management | 24–34 | 11 |
| F-2 SLA timer and status | Embedded in 25, 26, 39 | 0 separate |
| F-3 Service reporting and dashboards | 39–43 | 5 |
| F-4 Effort tracking | 35–38 | 4 |
| F-5 Client log-in and client-facing portal | 1–3, 11–12, 16 | 6 |
| F-6 User account management | 4–10 | 7 |
| F-7 Audit trail | 45–46 | 2 |
| F-8 Finance export | 44 | 1 |
| Setup (org, contract, holiday — shared) | 13–15, 17–23 | 10 |
| **Total** | | **46** |

Note: SLA timer state and escalation flag are computed on read (ADR A-10) and embedded in ticket detail (endpoint 26) and ticket list (endpoint 25) responses. No separate SLA read endpoint is needed; F-2 story requirements are met by the ticket and dashboard endpoints.

## OpenAPI Reference

Machine-readable OpenAPI 3.1 definition: `docs/04-design/openapi.yaml`.

The YAML file defines all 46 paths, request/response schemas, the `sessionAuth` security scheme (cookie `sessionid`), and `x-roles` extensions per operation. Every schema field is cross-checked against the database design. The YAML file is the authoritative contract; this narrative spec is the human-readable companion.

## Assumptions

- A-019 (CONFIRMED): A refused sign-in does not say whether the account name or the password was wrong. The API responds HTTP 401 with `{"detail": "Invalid credentials.", "code": "authentication_failed"}` for all four refusal cases: wrong password, unknown account name, deactivated user account, locked user account (REQ S-21 AC-2; THR T-10 control; PIB-004 confirmed).
- A-027 (Open): All timestamps stored in UTC, displayed in IST. The API returns all timestamps as UTC ISO 8601 (`2026-10-17T09:00:00Z`). The frontend converts to IST for display (ADR A-9). Assumption status: open; no impact on the API contract unless IST timestamps are required in responses.
- A-029 (Open): Excel, CSV and PDF files generated with free, open-source libraries (XlsxWriter, Python `csv`, WeasyPrint; ADR A-12). Download endpoints 43 and 44 stream files; no file is stored on disk. If a library is replaced, the download response format and MIME types remain unchanged.

## Open Questions

None raised by this artifact. Inherited open assumptions A-008, A-026 to A-029, A-031 to A-036, A-038 are logged in `docs/logs/assumptions-log.md` and do not require additional open questions from the API design.

## Traceability Links

- Upstream: PIB-004 v0.1; SUM-003 v0.2; REQ-001 v0.3 (S-1 to S-33); BR-001 v0.3 (B-1 to B-24); NFR-001 v0.3 (N-1 to N-9); GLO-001 v0.3; PRS-001 v0.3 (F-1 to F-8); ADR-001 v0.3 (A-3, A-6, A-7, A-11, A-12, A-13); THR-001 v0.2; PER-001 v0.2 (P-1 to P-4); SCR S-3; SCR S-4.
- Downstream: docs/04-design/openapi.yaml; Phase 4 backend design (BED); Phase 4 database design (DBD); Phase 5 feature breakdown; Phase 6 feature builder context packs.

## Quality Checklist

- [x] Every template section is filled, or marked "Not applicable - reason"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)
- [x] Every story that needs data has an endpoint
- [x] One error model across all endpoints
- [x] OpenAPI parses and matches the summary table

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
