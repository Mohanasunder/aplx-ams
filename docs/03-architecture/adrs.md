---
id: ADR-001
title: APLX AMS: Architecture Decision Records
phase: 3
version: 0.3
template: adr
template_version: 2.0
status: Approved
author_agent: solution-architect
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# APLX AMS: Architecture Decision Records

> **Collection file.** All architectural decision records for the project live in this single file. Always use `--out docs/03-architecture/adrs.md` when calling `new_artifact.py`. Each decision is a `## ADR A-N: [Title]` section (A-1, A-2, …). A specific ADR is cited downstream as `ADR A-N`. Never renumber after approval — append new decisions at the end; mark a superseded one `Superseded by ADR A-M - SCR S-N`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- PIB-003 v0.2 § Interview Answers (Q1 to Q12), § Constraints (including producer pointers), § Assumptions (A-026 to A-029), § Open Questions; IRC-004 v0.2.
- INT-003 v0.2 § Questions And Answers (evidence record).
- SUM-002 v0.4 § Decisions, § Constraints Set, § What The Next Phase Needs.
- NFR-001 v0.3 § NFR N-1 to N-9.
- REQ-001 v0.3 § Story S-20, S-21, S-22, S-30, S-31 (also S-12 to S-17 for reports and exports).
- BR-001 v0.3 § Rule B-1 to B-11 (SLA timers), § Rule B-2 (business-hours calendar), § Rule B-14, B-18, § Rule B-20 (data boundary), § Rule B-21, § Rule B-22 (audit), § Rule B-23 (passwords).
- PRS-001 v0.3 § Product Scope; GLO-001 v0.3 § Terms.
- RSK-001 v0.2 § Risk R-3, R-6; RSK-002 v0.1 § Risk R-1, R-2; SUM-001 v0.3 § Constraints Set.
- SCR S-4 (Approved 2026-10-17): NFR-001 v0.3 § NFR N-6 (security events), REQ-001 v0.3 § Story S-32, S-33, BR-001 v0.3 § Rule B-24, GLO-001 v0.3 § Terms, EPC-001 v0.3, BKL-001 v0.3, PRS-001 v0.3, SUM-002 v0.4 § Decisions, § Constraints Set.
- Human answers, Mohanasunder, chat, 2026-10-17: OQ-052 and OQ-058 (DEC-027: public repository on the personal github.com account for the pilot), OQ-055 (servers at the A-030 minimum, Ubuntu LTS, Docker Engine, SSH production to test), OQ-056 (downtime email to the Release manager / DevOps), OQ-057 (DEC-029: self-signed certificate), OQ-059 (Applexus IT owns firewall and DNS; host name moved within 2 business hours), OQ-060 (Docker Engine in WSL 2 on workstations), OQ-061 (sessions: 60 minutes idle, 12 hours maximum), OQ-063 (OS access: Mohanasunder and Applexus IT administrators), OQ-066 (Applexus IT installs the certificate as trusted on every user's machine); DEC-028 (RSK-003 R-1 accepted for the pilot), DEC-030 (session limits), DEC-031 (TLS certificate and key recovery copy on the test server).
- This phase, Draft (context, not approved input): TEC-001 v0.3 (weighted comparison behind ADR A-2 to A-16); THR-001 v0.2 (threats and § Secrets handling behind ADR A-17); TOP-001 v0.2 (sizing, RTO budget); CST-001 v0.2.

## Purpose And Scope
<!-- guidance: What this collection covers and what it does not -->
Covers: every significant architecture decision of APLX AMS release 1: structure, stack, runtime and hosting, client data separation, sign-in, sessions and password storage, time handling, SLA timer evaluation, audit trail and security events, report and export libraries, source hosting and delivery, network exposure and TLS, backup, monitoring, and secrets on the servers (ADR A-1 to A-17). Each ADR is Proposed until the Architect / tech lead approves this file; the approved ADRs are the project's approved technology list (INT-003 Q9).

Does not cover: the OpenAPI contract, database schema DDL, screen specifications and coding standards (Phase 4); the threat model (`threat-model.md`, `security-architect`); server-level topology, firewall rules and cost (`deployment-topology.md`, `cost-estimate.md`, `infra-cost-analyst`). Human decisions recorded as stated and not overridden: no MFA (NFR N-5), RPO 7 days (NFR N-3), no forced password change (BR B-23), public repository (DEC-027), single production server accepted for the pilot (DEC-028), self-signed certificate (DEC-029), refused sign-ins with unknown account names recorded as typed (BR B-24).

---

## ADR A-1: Modular monolith with one backend and one single-page application

### Status And Date
Proposed, 2026-10-17

### Context
- 2 servers only, 1 production and 1 test (INT-003 Q2); release 1 load is 30 concurrent users and under 200 tickets per month (NFR N-2; INT-003 Q12).
- 1 human reviewer and approver (`project.md`; DEC-020), 6 PR reviews per week, 3 builder agents, go-live 2027-01-17 (SUM-001 v0.3 § Constraints Set).
- 8 features PRS F-1 to F-8 share one data model: tickets, SLA timers, effort entries and reports all read the same client organizations, contracts and user accounts.

### Options Considered
1. Microservices (separate services for tickets, SLA, effort, reports, accounts): independent deployment and scaling; but 5 or more deployables, network calls between services, distributed transactions for audit entries, and more containers than 2 servers and 1 reviewer can carry.
2. Single monolith with no internal module boundaries: fastest start; but builder agents working in parallel collide in shared files, and the client data boundary and audit rules are scattered.
3. Modular monolith: one backend deployable split into modules with one owner each (accounts, organizations, tickets, SLA, effort, reports, audit), plus one frontend single-page application: one transaction per change, one deployable; module boundaries keep features in separate folders.

### Decision
Option 3. One backend deployable and one frontend bundle; modules: `accounts` (user accounts, roles, sign-in, passwords), `organizations` (client organizations, SAP applications, contracts), `tickets` (tickets, comments, assignment, ticket status), `sla` (business-hours calendar, company holiday list, SLA timers, escalation flag), `effort` (effort entries, hours bank balance), `reports` (live dashboard, monthly client report, finance export), `audit` (audit trail). Reason: the load and team size need no independent scaling, and one transaction per change makes the audit trail (NFR N-6) and data boundary (NFR N-7) enforceable in one place.

### Consequences
- Positive: 1 backend container and 1 static bundle to build, test and deploy; a change and its audit entry commit in one database transaction.
- Negative: a fault in one module can stop the whole backend; mitigated by container restart (ADR A-5) and monitoring (ADR A-16).
- Follow-up: Phase 4 backend design fixes module interfaces; Phase 5 slices features along these modules so each builder session touches 1 or 2 modules.

### Traceability Links
- Upstream: NFR N-2, N-6, N-7; PRS F-1 to F-8; INT-003 Q2, Q12; TEC-001.
- Downstream: ARC-001 § Containers, § Components; Phase 4 backend design; Phase 5 feature breakdown.

---

## ADR A-2: Backend framework Django 5.2 LTS with Django REST framework

### Status And Date
Proposed, 2026-10-17

### Context
- The human limits the backend to Python with Django or FastAPI and asks for the choice in an ADR (INT-003 Q4).
- Sign-in, password policy, lockout and temporary passwords must be built with no MFA (NFR N-5; REQ S-21, S-30, S-31; BR B-23); security rests on the password path (RSK-002 R-1).
- No new paid licences (SUM-001 v0.3 § Constraints Set).

### Options Considered
1. Django 5.2 LTS + Django REST framework + Gunicorn (TEC-001 T-1: 460 of 500): built-in authentication, server-side sessions, CSRF protection, password validators, Argon2 hasher, migrations and ORM; security fixes until April 2028. Trade-off: more framework conventions; synchronous request handling (sufficient for 30 concurrent users).
2. FastAPI + SQLAlchemy 2 + Alembic + Uvicorn (TEC-001 T-1: 380 of 500): asynchronous, typed request models, automatic OpenAPI output. Trade-off: authentication, sessions, CSRF and password hashing are separate libraries or custom code, each a security review item for the one reviewer.

### Decision
Option 1: Python 3.13, Django 5.2 LTS, Django REST framework, Gunicorn as the application server. Reason: equal reviewability (both named in Q4) and stronger built-in security and delivery speed (TEC-001 T-1 C2, C7).

### Consequences
- Positive: sign-in, sessions, CSRF and password storage use framework code instead of custom code.
- Negative: Django 5.2 security support ends April 2028; an upgrade to the next LTS (6.2, due April 2027) is needed before then.
- Follow-up: Phase 4 defines a custom user account model holding only name and email as personal data (NFR N-9), and the password policy validator (8 characters, upper-case, lower-case, digit; NFR N-5). Phase 4 coding standards set lint, type check and test tools.

### Traceability Links
- Upstream: NFR N-2, N-5, N-9; REQ S-20, S-21, S-30, S-31; BR B-21, B-23; INT-003 Q4; TEC-001 T-1.
- Downstream: Phase 4 coding standards, backend design, OpenAPI contract; agent charter stack section.

---

## ADR A-3: React TypeScript single-page application with a same-origin REST API

### Status And Date
Proposed, 2026-10-17

### Context
- The human sets React with TypeScript for the frontend (INT-003 Q4); desktop Chrome and Edge only, current and previous major versions (NFR N-8; PRS NG-4).
- Sign-in uses session cookies (ADR A-7), which are simplest when browser and API share one origin.
- Contract first: the API is specified in OpenAPI and approved in Phase 4 before code (CLAUDE.md rule 2).

### Options Considered
1. React + TypeScript single-page application built with Vite, served as static files by the reverse proxy, calling a REST JSON API under `/api/` on the same host name (TEC-001 T-2: 420): no Node.js at runtime; no cross-origin requests. Trade-off: no server-side rendering (not needed for an internal tool).
2. Next.js with a Node.js server (TEC-001 T-2: 330): server-side rendering and routing. Trade-off: a third runtime container and a second server-side codebase to review and secure.
3. GraphQL API instead of REST for option 1: one flexible endpoint. Trade-off: per-field authorization for the client data boundary is harder to review than per-endpoint permissions; OpenAPI tooling and contract checks apply to REST.

### Decision
Option 1 with a REST JSON API. One host name: the reverse proxy serves the built frontend files at `/` and forwards `/api/` to the backend. Reason: fewest runtime parts, same-origin cookies and CSRF, and an OpenAPI contract the reviewer approves in Phase 4.

### Consequences
- Positive: Node.js 24 LTS is needed only in CI to build the bundle; the production server runs no Node.js.
- Negative: every page loads data through API calls; NFR N-2 (p95 under 2 s per page) is measured in the browser, so Phase 4 keeps each page to a small number of API calls.
- Follow-up: Phase 4 UI specification and OpenAPI contract; the build targets the 4 browser versions of NFR N-8.

### Traceability Links
- Upstream: NFR N-2, N-8; PRS NG-4; INT-003 Q4; TEC-001 T-2.
- Downstream: Phase 4 OpenAPI contract and UI specification; ADR A-7, A-14.

---

## ADR A-4: PostgreSQL 18 as the single database

### Status And Date
Proposed, 2026-10-17

### Context
- The human sets PostgreSQL, free and open source, on the existing servers (INT-003 Q3), with row-level security for client data separation (INT-003 Q11).
- All data is kept with no end date (NFR N-4); under 200 tickets per month (INT-003 Q12); database under 5 GB for 5 years (A-032).

### Options Considered
1. PostgreSQL 18 (TEC-001 T-3: 435): row-level security, roles and grants, `pg_dump` for backup; supported until 2030-11-14. Trade-off: newest major version, so fewer patch releases behind it than 17.
2. PostgreSQL 17: supported until 2029-11-08; same features for this use. Trade-off: support ends a year earlier.
3. MariaDB 11 LTS (TEC-001 T-3: 335): no row-level security, so separation would rest on the application alone, against INT-003 Q11.

### Decision
Option 1: PostgreSQL 18, run from the official container image (ADR A-5), one database for all client organizations, accessed through psycopg 3. All application state lives in this database; release 1 stores no files on disk (no story stores attachments), so the database dump is the complete backup (ADR A-15).

### Consequences
- Positive: one data store to back up, restore and secure; row-level security available (ADR A-6); grants make the audit trail read-only to the application (ADR A-11).
- Negative: one database on one production server is a single point of failure (RSK-003 R-1).
- Follow-up: Phase 4 database design and schema; 2 database roles (owner for migrations, runtime role without table ownership; ADR A-6).

### Traceability Links
- Upstream: NFR N-3, N-4, N-6, N-7; INT-003 Q3, Q11, Q12; TEC-001 T-3.
- Downstream: Phase 4 database design; ADR A-6, A-11, A-15.

---

## ADR A-5: Docker Engine and Docker Compose on the 2 existing Linux VMs

### Status And Date
Proposed, 2026-10-17

### Context
- Existing on-prem Linux VMs, Docker containers allowed (INT-003 Q1); exactly 2 servers: production and test, the test server also hosting the restore drill and the uptime checker (Q2, Q10).
- A human deploys a built package manually; no automated cloud-to-on-prem deploy (Q5).
- No new paid licences (SUM-001 v0.3 § Constraints Set); both servers: 2 vCPU, 4 GB RAM, 40 GB free disk, current Ubuntu LTS with Docker Engine (OQ-055 answer; A-030 Confirmed); developer workstations run Docker Engine inside WSL 2, no Docker Desktop (OQ-060 answer).

### Options Considered
1. Docker Engine + Docker Compose, images built in CI and shipped as image archives (TEC-001 T-8: 405): the images CI tested are the images deployed; same layout on test and production. Trade-off: Docker administration skills needed on the servers.
2. Operating system packages, Python virtual environment and systemd services (TEC-001 T-8: 320): no container layer. Trade-off: the server's installed packages differ from CI; the deploy package is source plus install steps, so test and production can drift.
3. Kubernetes (single-node distribution): orchestration features. Trade-off: far more to operate than 3 containers on one server need; no benefit at 30 concurrent users.

### Decision
Option 1. Production runs 3 containers in one Compose project: `proxy` (Nginx, ADR A-14), `app` (Django and Gunicorn), `db` (PostgreSQL 18), on a private Docker network; only `proxy` publishes ports. The test server runs the same Compose project for testing, plus the restore drill database (ADR A-15) and the uptime checker (ADR A-16). Every container has a restart policy (`unless-stopped`) and a health check.

### Consequences
- Positive: the deployed artifact is the tested artifact; a failed container restarts without a human (NFR N-1).
- Negative: the test server carries test, restore drill and monitoring together; heavy load on it does not affect production but a test server outage stops monitoring (RSK-003 R-1).
- Follow-up: `deployment-topology.md` sizes both servers (production RAM about 75%, test server disk about 77% at the 5-year ceiling); Phase 8 writes the Compose files and runbooks. Docker Desktop is not used anywhere: servers and workstations run Docker Engine (Apache-2.0), on workstations inside WSL 2.

### Traceability Links
- Upstream: NFR N-1, N-2; INT-003 Q1, Q2, Q5, Q10; RSK-001 R-3; TEC-001 T-8.
- Downstream: deployment topology, Phase 8 runbooks; ADR A-13, A-14, A-15, A-16.

---

## ADR A-6: Client data separation with a client organization ID, one data-access layer and PostgreSQL row-level security

### Status And Date
Proposed, 2026-10-17

### Context
- A client user never sees or acts on another client organization's tickets, monthly client reports, SAP applications, names or emails: 0 records across tests with at least 2 client organizations (NFR N-7; BR B-20; REQ S-22).
- Internal users see every client organization's data (BR B-20; REQ S-22 AC-4).
- The human sets the method: one PostgreSQL database; every client-owned row carries the client organization ID, enforced in one data-access layer plus PostgreSQL row-level security; tested with 2 client organizations (INT-003 Q11; DEC-022). Risk rating High (RSK R-6).

### Options Considered
1. One database per client organization: strongest isolation. Trade-off: a database per client organization to migrate, back up and monitor; internal users' cross-organization views (live dashboard) need queries across databases.
2. One schema per client organization in one database: isolation by search path. Trade-off: migrations repeat per schema; cross-organization views still need unions.
3. One database, client organization ID on every client-owned row, filter in the application only: simplest. Trade-off: one missed filter exposes another organization's data with nothing to stop it.
4. One database, client organization ID on every client-owned row, one data-access layer applying the filter, plus PostgreSQL row-level security as a second barrier (human choice, INT-003 Q11): a missed filter is still blocked by the database. Trade-off: row-level security policies and per-request database settings to write and test.

### Decision
Option 4:
- Every client-owned table (tickets, comments, SAP applications, contracts, effort entries, monthly client reports, client users' user accounts) has a non-null client organization ID.
- One data-access layer in the backend is the only path to client-owned data; it scopes every query by the signed-in user: a client user to their own client organization, internal users to all.
- At the start of each request transaction the backend sets two transaction-local PostgreSQL settings: the user kind (internal user or client user) and, for a client user, the client organization ID. Row-level security policies on every client-owned table allow a row only when the user kind is internal user or the row's client organization ID equals the setting; with no setting, no row is allowed.
- The runtime database role does not own the tables, is not a superuser and has no `BYPASSRLS`; tables use `FORCE ROW LEVEL SECURITY`. Migrations run with a separate owner role.
- Automated tests with client organizations A and B cover list, open by ticket reference, report view and download, and raise against the other organization's SAP application (NFR N-7 verification), and run against PostgreSQL in CI.

### Consequences
- Positive: two independent barriers; a defect in one is caught by the other and by the A/B tests.
- Negative: every request runs in a transaction (Django `ATOMIC_REQUESTS`); database settings must be transaction-local so a reused connection never carries another user's context.
- Follow-up: `security-architect` records the threats and controls in `threat-model.md`; Phase 4 database design lists the client-owned tables and policies; the boundary tests are re-run before the first external client organization goes live (RSK R-6).

### Traceability Links
- Upstream: NFR N-7; BR B-20; REQ S-1, S-2, S-12, S-14, S-22, S-28, S-29; INT-003 Q11; RSK-001 R-6; TEC-001 T-1, T-3.
- Downstream: threat model; Phase 4 database design and backend design; Phase 6 feature tests; Phase 7 system tests.

---

## ADR A-7: Sign-in with server-side sessions, session time limits and account lockout in the accounts module

### Status And Date
Proposed, 2026-10-17 (revised 2026-10-17: session time limits per DEC-030; security events per BR B-24)

### Context
- Every user signs in with a user account and password; no MFA (NFR N-5; PRS NG-7; RSK-002 R-1).
- Lockout: locked for 30 minutes after 5 failed sign-ins, cleared at once when the delivery manager sets a temporary password (NFR N-5; BR B-23; REQ S-21 AC-4, S-30 AC-3).
- A deactivated user can no longer sign in (REQ S-20 AC-3); a refused sign-in does not say whether the account name or the password was wrong (REQ S-21 AC-2).
- Password changes need the current password (REQ S-31 AC-4); no email, no self-service password reset, no forced change (BR B-23).
- Sessions end after 60 minutes without activity and at most 12 hours after sign-in, for all users (DEC-030, Mohanasunder, 2026-10-17, answering OQ-061; recorded as a decision, not an NFR change; THR T-7).
- Sign-ins, failed sign-ins, lockouts, temporary passwords set and own password changes are security events in the audit trail (BR B-24; REQ S-32).

### Options Considered
1. Django server-side sessions in PostgreSQL with an HttpOnly, Secure, SameSite=Strict cookie and Django CSRF protection: deactivation or a password change can end sessions at once; idle and maximum limits are checked on the server. Trade-off: each request reads the session row (negligible at 30 users).
2. JSON Web Tokens (JWT) held by the browser: no session store. Trade-off: a token stays valid after deactivation until it expires; an idle limit needs refresh-token code; storage in browser script is exposed to cross-site scripting.
3. A third-party identity provider (for example Keycloak, Apache-2.0): central identity and MFA later. Trade-off: one more container and product to run; release 1 has no MFA and no single sign-on requirement.

### Decision
Option 1. The `accounts` module owns sign-in, the failed sign-in count and lock-until time per user account, setting temporary passwords (delivery manager only) and changing one's own password (current password required). Session limits: the session expires 60 minutes after the last request (rolling expiry) and is refused 12 hours after sign-in whatever the activity (sign-in time stored in the session and checked on every request); the frontend returns to the sign-in page when the API refuses an ended session. A new session identifier is issued at sign-in. Setting a temporary password clears the lock and ends the user's other sessions; deactivating a user account ends its sessions. Each sign-in outcome and each password event is written as a security event through the audit function (ADR A-11). No library beyond Django is added for lockout or session limits.

### Consequences
- Positive: one origin, one cookie, framework CSRF protection; sessions can be revoked at once; an unattended desktop is exposed for at most 60 minutes (THR T-7).
- Negative: users idle for 60 minutes sign in again; a refused sign-in writes an audit entry, so scripted sign-ins grow the audit trail (THR T-35; rate limit at `proxy`, ADR A-14).
- Follow-up: Phase 4 OpenAPI contract for sign-in, sign-out, set temporary password and change password; Phase 6 tests for every NFR N-5 verification step, both session limits and the 5 security events.

### Traceability Links
- Upstream: NFR N-5, N-6; REQ S-20, S-21, S-30, S-31, S-32; BR B-21, B-23, B-24; PRS NG-7; RSK-002 R-1; TEC-001 T-1; THR-001 (THR T-6, T-7, T-8).
- Downstream: threat model; Phase 4 OpenAPI contract and backend design; ADR A-8, A-11.
---

## ADR A-8: Password storage with Argon2id

### Status And Date
Proposed, 2026-10-17

### Context
- NFR N-5 sets the password policy but not storage; assumption A-028 asks for an OWASP-recommended adaptive hash (Argon2id or bcrypt) chosen in the stack ADR.
- With no MFA (RSK-002 R-1), stored password hashes are the last barrier if a database dump or backup leaks; the test server holds production dumps (ADR A-15).

### Options Considered
1. Argon2id through Django's Argon2 hasher and `argon2-cffi`, MIT (TEC-001 T-6: 425): memory-hard; listed first by OWASP. Trade-off: one extra library; uses memory per hash (sign-ins are few).
2. bcrypt through Django's bcrypt hasher, Apache-2.0 (TEC-001 T-6: 405): widely used. Trade-off: input beyond 72 bytes ignored; not memory-hard.
3. PBKDF2-SHA256, Django default (TEC-001 T-6: 410): no extra library. Trade-off: not memory-hard; weaker against GPU guessing.

### Decision
Option 1: Argon2id first in Django's hasher list, with Django's default Argon2 parameters as the minimum; PBKDF2 kept second only to read any hash created before the switch.

### Consequences
- Positive: strongest of the 3 options against offline guessing of a leaked dump.
- Negative: hashing takes memory and time per sign-in; NFR N-2 load tests in Phase 7 include sign-in.
- Follow-up: Phase 4 coding standards state that passwords, temporary passwords and hashes are never logged or returned by the API.

### Traceability Links
- Upstream: NFR N-5; REQ S-21, S-30, S-31; BR B-23; RSK-002 R-1; TEC-001 T-6.
- Downstream: threat model; Phase 4 coding standards and backend design.

---

## ADR A-9: Times stored in UTC, shown in IST, SLA on the IST business calendar

### Status And Date
Proposed, 2026-10-17

### Context
- Business hours are 09:00 to 18:00 IST, Monday to Friday, minus the company holiday list (BR B-2); reports and the finance export are per calendar month (BR B-14, B-18); effort entries are editable until the end of the calendar month in IST (BR B-15).
- The audit trail records date and time to the second (NFR N-6).
- Assumption A-027: store UTC, display IST, compute SLA business time on the IST calendar.

### Options Considered
1. Store every timestamp as UTC (`timestamptz`); convert to IST (Asia/Kolkata, UTC+05:30, no daylight saving) for display, for the business-hours calendar and for month boundaries: one unambiguous stored form. Trade-off: every conversion point must use the same time zone setting.
2. Store IST local timestamps without a time zone: no conversion for display. Trade-off: ambiguous if a server or user is not in IST; arithmetic and comparisons across systems are error-prone.
3. Store UTC and compute business time in UTC with a converted calendar (03:30 to 12:30 UTC): no conversion in the SLA code. Trade-off: holiday dates and month ends are IST dates, so the conversion moves into the calendar data and is harder to review.

### Decision
Option 1. Django `USE_TZ = True`; the database and servers keep UTC; the SLA module and month boundaries convert to Asia/Kolkata; the frontend shows times in IST. Company holiday list entries are IST calendar dates. Both servers keep time with NTP.

### Consequences
- Positive: one stored form; IST has no daylight saving, so every IST hour maps to one UTC hour.
- Negative: tests must cover the IST day boundary (18:30 UTC is 00:00 IST the next day).
- Follow-up: Phase 4 backend design; Phase 8 NTP on both servers.

### Traceability Links
- Upstream: BR B-2, B-14, B-15, B-18, B-22; NFR N-1, N-6; PIB-003.
- Downstream: ADR A-10; Phase 4 backend design and coding standards.

---

## ADR A-10: SLA timers evaluated on read from stored ticket events, with stopped results stored

### Status And Date
Proposed, 2026-10-17

### Context
- Each ticket has a response clock and a resolution clock on business hours; pause while awaiting client; recalculation of running timers on priority change from the raise time; on track, at risk at 90%, breached at 100%, met; the escalation flag at 50% of the resolution target; in-app only (BR B-1 to B-11; PRS F-3; PRS NG-6).
- A company holiday list change applies from the time of the change onward; business time already counted is not recalculated (BR B-2; OQ-050).
- Stopped timers keep met or breached after a priority change (BR B-7).
- Under 200 tickets per month (INT-003 Q12).

### Options Considered
1. Scheduled job every minute that recomputes and stores the elapsed time and state of every running SLA timer: states are ready to read. Trade-off: a worker container and scheduler to run and monitor; states lag by up to 1 minute; a stopped job silently freezes every timer.
2. Evaluate on read: one SLA calculation component computes elapsed business time, state and escalation flag from the ticket's stored events (raise, pauses, acknowledgement, Resolved, priority changes) and the company holiday list history whenever a ticket, list, live dashboard or report is shown; when a timer stops, its result (elapsed business time, met or breached) is stored in the same transaction. Trade-off: computation on every page view (small at this volume); holiday list changes must be kept with the time they were made.

### Decision
Option 2. The SLA calculation component is a pure function with no database writes, used by every module that shows SLA state. Company holiday list entries keep the time they were added and removed (never hard-deleted), and a business-hours moment counts as a holiday only if the entry for that date was in effect at that moment; this implements BR B-2 (no recalculation of business time already counted) on read.

### Consequences
- Positive: no background worker container; states are exact at the moment of viewing; the function is unit-testable with fixed times.
- Negative: list and dashboard pages compute SLA state per ticket; Phase 7 load tests confirm NFR N-2 with the live dashboard in the journey.
- Follow-up: Phase 4 backend design defines the event data the function reads; Phase 6 tests cover every BR B-1 to B-11 example.

### Traceability Links
- Upstream: BR B-1 to B-11; PRS F-3, NG-6; REQ S-9, S-10, S-11, S-12, S-24; NFR N-2; INT-003 Q12.
- Downstream: Phase 4 backend design; ADR A-9; Phase 7 NFR test report.

---

## ADR A-11: Append-only audit trail, including security events, written by one audit function

### Status And Date
Proposed, 2026-10-17 (revised 2026-10-17: security events per SCR S-4, BR B-24)

### Context
- 100% of status, priority, assignment and effort changes (saved, changed, deleted) have an audit entry with user, date and time to the second, old value and new value; 0 audit entries editable or deletable by any user; visible to internal users only (NFR N-6; BR B-22; PRS F-8).
- SCR S-4: 5 security events are audit entries: successful sign-in, failed sign-in (wrong password, account name matching no user account recorded as typed, deactivated or locked user account), user account lockout, temporary password set, own password change; each with event, user, user account concerned and time; 0 audit entries hold a password value; the delivery manager views all security events, each internal user their own, client users none; no alerting (BR B-24; REQ S-32, S-33; NFR N-6 v0.3).

### Options Considered
1. Audit entries written by the backend service that makes the change, in the same database transaction, through one audit function in the `audit` module; security events written by the same function; the runtime database role has INSERT and SELECT only on the audit table: the change and its entry commit or fail together, and the database refuses edits and deletions. Trade-off: every change path and sign-in outcome must call the audit function; checked by tests and review.
2. PostgreSQL triggers on the audited tables write audit entries: catches every change, including ones that bypass the backend. Trade-off: audit logic in PL/pgSQL, a second language for the one reviewer; the user identity must be passed in through a database setting; refused sign-ins change no table row, so security events would still need application code.
3. Application log file of changes and security events: no schema work. Trade-off: log files can be edited or rotated away; no old and new value structure for internal users to view; fails NFR N-6.

### Decision
Option 1. Audit entries, ticket changes and security events alike, are stored in PostgreSQL in one append-only table; the runtime database role has no UPDATE or DELETE grant on it. The audit function has no parameter that takes a password, so no password value can reach an entry through it. A refused sign-in and a lockout are committed in their own transaction even though the sign-in is refused. Viewing: every internal user sees every ticket's audit entries (status, priority, assignment and effort changes; BR B-22) plus their own security events; the delivery manager sees all security events, per user account; client users see no audit entries, their own security events included (BR B-22, B-24; REQ S-33). A failed sign-in with an account name that matches no user account belongs to no user account, so only the delivery manager sees it.

### Consequences
- Positive: a change without its audit entry cannot commit; edits and deletions of audit entries are refused by the database itself; misuse of a known temporary password leaves a sign-in record (THR T-3).
- Negative: a builder can forget the audit call on a new change path; the Phase 7 system test compares every change of the 4 types and the 5 security events with the audit entries (NFR N-6 verification). A password typed into the account-name field is stored as typed (BR B-24, human decision; THR T-34; RSK-003 R-10). Refused sign-ins add entries that are never deleted (NFR N-4; THR T-35).
- Follow-up: Phase 4 backend design names every change path for the 4 change types and the 5 security events, and the viewing rules per role.

### Traceability Links
- Upstream: NFR N-4, N-6; BR B-15, B-22, B-24; PRS F-8; REQ S-23, S-32, S-33; THR-001 (THR T-3, T-15, T-34, T-35).
- Downstream: Phase 4 database design and backend design; Phase 7 system tests.
---

## ADR A-12: Excel, CSV and PDF files with XlsxWriter, Python csv and WeasyPrint

### Status And Date
Proposed, 2026-10-17

### Context
- Client users and the delivery manager download the monthly client report as Excel or PDF (BR B-14; REQ S-14); the delivery manager downloads the finance export as Excel or CSV (BR B-18; REQ S-17).
- Free, open-source libraries only, each licence checked (A-029; SUM-001 v0.3 § Constraints Set).

### Options Considered
1. XlsxWriter (BSD-2-Clause) for Excel, Python standard library `csv` for CSV, WeasyPrint (BSD-3-Clause) for PDF from an HTML template (TEC-001 T-4: 395, T-5: 420). Trade-off: WeasyPrint needs Pango system libraries in the backend image.
2. openpyxl (MIT) for Excel, Python `csv`, ReportLab open-source toolkit (BSD) for PDF (TEC-001 T-4: 385, T-5: 350). Trade-off: PDF layout written in Python drawing code, harder to review than a template.
3. fpdf2 (LGPL-3.0) for PDF (TEC-001 T-5: 330). Trade-off: copyleft licence and layout in code.

### Decision
Option 1. Files are generated on request in the backend and streamed to the browser; they are not stored on disk. The data-access layer and row-level security (ADR A-6) apply to the data read for every file.

### Consequences
- Positive: no paid licence; the PDF layout is an HTML template the reviewer reads like a page.
- Negative: the backend image is larger (Pango); PDF rendering uses more memory than Excel (checked against A-030 in Phase 7).
- Follow-up: Phase 4 backend design fixes file layouts; CI licence scan re-checks these libraries and their dependencies.

### Traceability Links
- Upstream: BR B-14, B-18; REQ S-14, S-17; NFR N-7; TEC-001 T-4, T-5.
- Downstream: Phase 4 backend design; ADR A-6.

---

## ADR A-13: Public github.com repository and GitHub-hosted CI, with a human deploying a built bundle

### Status And Date
Proposed, 2026-10-17 (revised 2026-10-17: public repository per DEC-027)

### Context
- Human answer (INT-003 Q5): "Keep the github.com repository and GitHub-hosted CI; a human deploys a built package to on-prem manually"; no automated cloud-to-on-prem deploy.
- The repository `github.com/Mohanasunder/aplx-ams` stays on the personal account for the pilot and becomes public, so standard GitHub-hosted runner minutes are free (DEC-027, Mohanasunder, 2026-10-17; OQ-052, OQ-058 answers). Everything in it, including the architecture, threat model, logs and CI logs, is publicly visible (THR T-31, T-32); anyone can fork it and open a pull request (THR T-33).
- Production servers are not internet-facing (INT-003 Q6).

### Options Considered
1. GitHub Actions on GitHub-hosted runners builds and tests; it produces a versioned bundle (image archives saved with `docker save`, Compose file, configuration templates without secrets, SHA-256 checksums); a human downloads it, copies it to the test server and then the production server, verifies checksums and deploys with Docker Compose. Trade-off: manual steps; deploy time depends on the human.
2. CI pushes images to GitHub Container Registry and the servers pull them: no file copying. Trade-off: the servers need outbound internet access and a registry credential stored on them.
3. A self-hosted GitHub Actions runner on the on-prem network deploys automatically. Trade-off: contradicts INT-003 Q5; on a public repository, a runner on the internal network could run code from outside pull requests.

### Decision
Option 1, on the public repository:
- CI runs lint, type checks, tests (including the client data boundary tests against PostgreSQL 18 in a CI service container), security, licence and secret scans, then builds the bundle.
- The bundle is built only on pushes to the protected `main` branch (required PR review and CI pass), never from a pull request; the human compares bundle checksums with the CI run summary before deploying.
- Pull requests from forks: no `pull_request_target` or `workflow_run` job checks out or runs pull request code; the default `GITHUB_TOKEN` permission is read-only, raised per job only where needed; workflows for pull requests from outside collaborators run only after approval; pull request titles and branch names reach scripts only through environment variables; third-party actions are pinned by full commit SHA; changes under `.github/workflows/` are reviewed by the Architect / tech lead (THR T-33).
- Secret scanning with push protection on (free for public repositories) and a full-history secret scan before the repository is made public; any secret ever committed is rotated, not only removed from history (THR T-32).
- No secret, server address, host name, server user name or production data in the repository, CI variables or CI logs (THR T-31); two-factor sign-in on the GitHub account (THR T-23).
- Deploys go to the test server first, then production, in a window outside business hours (09:00 to 18:00 IST, Monday to Friday) so planned downtime does not count against NFR N-1. Before each production deploy the human takes an extra `pg_dump` (in addition to the weekly backup, ADR A-15), encrypted at rest like the weekly dumps (DEC-034, DEC-036). Database migrations run as a one-off container with the owner role. The previous bundle stays on the server for rollback.

### Consequences
- Positive: no inbound or outbound connection between GitHub and the servers; the deployed images are the ones CI tested; CI minutes cost INR 0 on the public repository (CST-001).
- Negative: the design, residual risks and logs are public (accepted by DEC-027; RSK-003 R-6); a human step per deploy and one deployer (RSK-003 R-2); making the repository private again brings back the plan's minute and storage limits (CST-001).
- Follow-up: Phase 8 deployment runbook and rollback plan; Phase 4 `standards-author` fills the CI commands and the workflow rules above.

### Traceability Links
- Upstream: INT-003 Q5, Q6, Q9; NFR N-1, N-3, N-7; TEC-001 T-8; THR-001 (THR T-23, T-31, T-32, T-33).
- Downstream: deployment topology, cost estimate, Phase 8 deployment runbook and rollback plan; ADR A-5, A-17.
---

## ADR A-14: Internal network only, HTTPS terminated at Nginx with a self-signed certificate trusted on every user's machine

### Status And Date
Proposed, 2026-10-17 (revised 2026-10-17: self-signed certificate per DEC-029; trust installed by Applexus IT per the OQ-066 answer; recovery copy per DEC-031)

### Context
- Release 1 is reachable from the Applexus network or VPN only, not internet-facing (INT-003 Q6). Applexus IT owns the firewall rules and the DNS record of the APLX AMS host name (OQ-059 answer).
- The human chose a self-signed TLS certificate for the pilot instead of an internal-CA certificate (DEC-029); Applexus IT installs it as trusted on every user's machine before go-live, all pilot users being Applexus staff (OQ-066 answer).
- Passwords are sent at every sign-in (NFR N-5); Chrome and Edge current and previous majors (NFR N-8). Users who click through certificate warnings can be intercepted (THR T-30); an expired certificate stops all sign-ins (THR T-26).

### Options Considered
1. Nginx container terminates TLS (TLS 1.2 and 1.3), redirects HTTP to HTTPS, sets HSTS and security headers, serves the frontend and forwards `/api/` to the backend; only ports 443 and 80 (redirect) are published (TEC-001 T-7: 395). Trade-off: one more container.
2. Caddy as the reverse proxy (TEC-001 T-7: 370): simpler configuration. Trade-off: its automatic public certificates do not apply on an internal network; less widely documented.
3. TLS in the application server (Gunicorn) with no reverse proxy. Trade-off: static files served by Python; certificate handling inside the application container.
4. Plain HTTP inside the company network: no certificate work. Trade-off: passwords and session cookies sent unencrypted; rejected by INT-003 Q6.

Certificate source (sub-decision): (a) self-signed, installed as trusted on every user's machine by Applexus IT (DEC-029; OQ-066 answer): no dependence on an internal CA; renewal and redistribution are manual; (b) internal-CA certificate (the original INT-003 Q6 answer): already trusted by company machines, issued and renewed by Applexus IT; not chosen for the pilot (DEC-029).

### Decision
Option 1 with certificate (a). The certificate and key are generated on the production server by the Release manager / DevOps and name the host name Applexus IT assigns. Their only other copy is a protected recovery copy on the test server, encrypted at rest (DEC-036) and also root-owned, mode 0400, own directory apart from the dumps, never mounted into any container, checksum recorded), restored on recovery so users' installed trust survives and recovery stays within the RTO (DEC-031; THR T-26, T-36; TOP-001 RTO step 5; ADR A-17); the test deployment uses its own, different certificate. Applexus IT installs the certificate as trusted on every user's machine before go-live, so Chrome and Edge show no warning and HSTS then blocks click-through; users are told that any certificate warning means stop and report. The validity period and renewal date are recorded in the Phase 8 runbook, with a renewal reminder; Uptime Kuma trusts this certificate and warns before expiry (ADR A-16). Access from outside the Applexus network or VPN is blocked by the Applexus IT firewall, recorded in the deployment topology. `proxy` limits the request rate on the sign-in endpoint (THR T-2, T-35; value in Phase 4 coding standards).

### Consequences
- Positive: one encrypted entry point; no warning to click through once trust is installed; the database is unreachable from the network.
- Negative: renewal is manual and needs Applexus IT to install the new certificate on every machine again; a machine without the installed trust shows a warning (RSK-003 R-5); the key copy on the test server is readable by its OS-level administrators and, if taken, lets a person on the network impersonate APLX AMS with no warning (THR T-36; RSK-003 R-4); on suspected exposure the certificate is replaced and trust re-installed.
- Follow-up: re-decide certificate source, exposure and MFA (RSK-002 R-1) before external client organizations' users sign in from outside the network; Phase 7 checks that each of the 4 browser versions opens the sign-in page with no warning.

### Traceability Links
- Upstream: INT-003 Q6; NFR N-1, N-5, N-8; RSK-002 R-1; TEC-001 T-7; THR-001 (THR T-18, T-26, T-30, T-36); TOP-001.
- Downstream: threat model, deployment topology; Phase 8 runbooks; ADR A-16, A-17.
---

## ADR A-15: Weekly native PostgreSQL dump copied to the test server by a write-only backup account, restore drill on the test server

### Status And Date
Proposed, 2026-10-17 (revised 2026-10-17: write-only backup account, drill database dropped after the drill, RTO budget from TOP-001; dump encryption at rest per DEC-034, key custody per DEC-036 and DEC-037; options 2 and 3 rejected by the human)

### Context
- Backup at least once every 7 days; RPO 7 days; RTO 9 business hours; restore drill before go-live on a separate environment (NFR N-3; RSK-002 R-2).
- Human answer: weekly scheduled native PostgreSQL dump to a different on-prem server or disk (INT-003 Q7); the test server hosts the restore drill (Q2); SSH from production to test is allowed (OQ-055 answer).
- All application state is in PostgreSQL (ADR A-4); database under 5 GB for 5 years (A-032).
- OS-level access to both servers: Mohanasunder and Applexus IT administrators (OQ-063 answer); ransomware or an error on production must not be able to delete the copies (THR T-22); a restored database left running exposes production data (THR T-21).

### Options Considered
1. Weekly `pg_dump` in custom format, scheduled on the production server, copied over SSH to the test server with a SHA-256 checksum; restore drill with `pg_restore` into a separate database on the test server (human choice, RPO 7 days). Trade-off: up to 7 days of data lost on a restore (RSK-002 R-2).
2. Daily `pg_dump`, same method: RPO 1 day at no licence cost. Trade-off: changes the human's RPO decision; more test server disk (CST-001: up to about 96 GB more at the 5-year ceiling).
3. Physical base backup with continuous WAL archiving to the test server: RPO of minutes, point-in-time restore. Trade-off: more setup, monitoring and disk; restore is more complex to rehearse.

### Decision
Option 1, as decided by the human (INT-003 Q7; NFR N-3):
- The copy uses a dedicated backup account on the test server with a dedicated SSH key that can only write new files into the backup directory: no delete or overwrite from production (THR T-22). Dump files are root-only (mode 0600) and outside any served path (THR T-20).
- Encryption at rest (DEC-034, Mohanasunder, 2026-10-17): each weekly and pre-deploy dump is encrypted on the production server before it is copied, with a free open-source tool, age (BSD-3-Clause) or GnuPG (GPL-3.0, used unmodified as a tool), to a public key; the private decryption key is held offline by the Release manager / DevOps (Mohanasunder), brought to the test server only for a restore or restore drill, and removed afterwards (DEC-036); it is needed for the restore drill and for recovery (THR T-20, T-21); a sealed second copy of the key (tamper-evident envelope) is held by Applexus IT in a locked safe, used only if the Release manager / DevOps is unavailable, and checked by the restore drill once a year (DEC-037). The same encryption applies to the TLS certificate and key recovery copy (ADR A-14, A-17). The tool is chosen in Phase 8 (TEC-001 § Licence check summary).
- Retention of dump files: the last 8 weekly dumps on the test server and the last 2 pre-deploy dumps on production (A-033); rotation deletes only older backup copies, never application data (NFR N-4). A failed dump or copy sends an email alert (ADR A-16).
- Restore drill: the drill database container is started only for the drill, publishes no port, is run by the Release manager / DevOps, and is dropped once the timing and data checks are recorded (THR T-21).
- Recovery after loss of the production server: stand-in on the test server per the TOP-001 RTO budget, worst case 5.75 business hours when the key holder is present, including up to 2 hours for Applexus IT to move the host name (OQ-059 answer); if the Release manager / DevOps is unavailable, Applexus IT hands over the sealed key copy within 2 business hours and the worst case is 7.5 business hours (DEC-038; TOP-001); both within the 9-business-hour RTO. The single production server risk is accepted for the pilot (DEC-028; RSK-003 R-1).
- Options 2 and 3 were rejected by the human at the Phase 3 gate: the RPO stays 7 days with a weekly dump (DEC-034; NFR N-3); they remain the revisit path if RSK-002 R-2 is re-rated.

### Consequences
- Positive: native dump tool plus a free encryption tool; a compromised production server cannot delete the copies; a dump file read on the test server without the key reveals no data; the restore drill proves NFR N-3 before go-live.
- Negative: up to 7 days of data loss (RSK-002 R-2); the restore drill and a recovery need the offline decryption key, so losing it makes every dump and the TLS key copy unusable, and a recovery depends on the Release manager / DevOps bringing it or on Applexus IT handing over the sealed copy within 2 business hours (DEC-037, DEC-038; RSK-003 R-11); restored databases and the TLS key copy on the test server stay readable by OS-level administrators (RSK-003 R-4); test server disk is about 77% used at the 5-year ceiling (RSK-003 R-7).
- Follow-up: Phase 8 runbook schedules the dump, rotation and alert, and records the drill; Phase 7 or 8 runs and times the restore drill.

### Traceability Links
- Upstream: NFR N-3, N-4; INT-003 Q2, Q7; RSK-002 R-2; THR-001 (THR T-20, T-21, T-22); TOP-001.
- Downstream: deployment topology, cost estimate, threat model; Phase 8 operational runbook; ADR A-4, A-5, A-16.
---

## ADR A-16: Uptime Kuma on the test server checking the production sign-in page every minute, alerting by email

### Status And Date
Proposed, 2026-10-17 (revised 2026-10-17: email alert per the OQ-056 answer)

### Context
- 99% of business hours per calendar month; verification by an automated check of the sign-in page once per minute during business hours (NFR N-1).
- Human answer: a free, open-source, self-hosted uptime checker on the test server checks once a minute and alerts on downtime (INT-003 Q10); alerts go to the Release manager / DevOps (Mohanasunder) by email through the existing company mail (OQ-056 answer).

### Options Considered
1. Uptime Kuma 2, MIT (TEC-001 T-9: 385): HTTPS checks at 60-second intervals, check history, certificate expiry warning, Email (SMTP) and 90+ notification services, web UI. Trade-off: a web UI to secure on the test server.
2. Gatus, Apache-2.0 (TEC-001 T-9: 375): checks defined in a YAML file kept in the repository. Trade-off: on the public repository (DEC-027) the check targets would be public; fewer built-in notification routes.
3. Scheduled `curl` script on the test server (TEC-001 T-9: 320): no extra software. Trade-off: custom code for history, alerting and availability reports.

### Decision
Option 1: Uptime Kuma in a container on the test server, HTTPS check of the production sign-in page every 60 seconds, trusting the self-signed certificate (not ignoring certificate errors) with certificate expiry warnings on; alerts by email (SMTP) through the existing company mail to the Release manager / DevOps. The Uptime Kuma web UI is bound to 127.0.0.1 on the test server and reached only through an SSH tunnel from an administrator workstation (TOP-001 path P-3), with an admin password meeting NFR N-5 (THR T-27). The weekly dump job sends its failure email through the same mail route (ADR A-15). Monthly availability over business hours (NFR N-1 formula) is computed from the stored check history, method set in the Phase 8 monitoring specification.

### Consequences
- Positive: meets INT-003 Q10 with no licence cost; also watches certificate expiry (ADR A-14).
- Negative: if the test server is down, production is not monitored; while the test server is the recovery stand-in, Uptime Kuma checks a service on its own host (RSK-003 R-1, accepted by DEC-028); one alert recipient with no backup (DEC-020).
- Follow-up: Phase 8 monitoring specification and operational runbook (mail server settings); Phase 9 monthly availability review.

### Traceability Links
- Upstream: NFR N-1; INT-003 Q2, Q10; TEC-001 T-9; THR-001 (THR T-26, T-27).
- Downstream: Phase 8 monitoring specification and operational runbook; Phase 9 SLO review; ADR A-5, A-14, A-15.
---

## ADR A-17: Server secrets as root-only files passed to containers as Docker Compose file secrets

### Status And Date
Proposed, 2026-10-17 (proposed by the `security-architect` in THR-001 § Secrets handling)

### Context
- Secrets: private decryption key for the encrypted dumps and TLS recovery copy (held offline by the Release manager / DevOps, DEC-036, with a sealed second copy in an Applexus IT safe, DEC-037; ADR A-15), PostgreSQL owner and runtime role passwords, Django secret key, TLS private key (ADR A-14), SSH key for the backup copy (ADR A-15), Uptime Kuma admin credential, and the company mail credential if the mail route needs one (ADR A-16) (THR-001 AS-9).
- The repository is public (DEC-027): no secret may be in GitHub, CI variables, images or the bundle (ADR A-13; THR T-17, T-32).
- No secret manager is known to be available, and no new paid licences (A-038; SUM-001 v0.3 § Constraints Set). OS-level access: Mohanasunder and Applexus IT administrators (OQ-063 answer).

### Options Considered
1. Root-owned files (mode 0400) in one directory on each server, outside the bundle, passed to containers as Docker Compose file secrets mounted under `/run/secrets/`, each container receiving only its own: no extra software; values never in environment variables. Trade-off: rotation and the recovery copy are manual runbook steps; any root user on the server can read them.
2. Environment variables from a `.env` file next to the Compose file: simplest. Trade-off: values visible through `docker inspect` and in process environments, and passed to every process in the container.
3. A self-hosted secret manager (OpenBao, MPL-2.0, as a container): central storage, audit of reads, rotation tooling. Trade-off: one more service to install, unseal, back up and monitor on 2 small servers; root on the server still reaches the unsealed values.
4. GitHub Actions secrets injected at build: values held by GitHub. Trade-off: secrets would enter images or the bundle; not allowed (ADR A-13).

### Decision
Option 1. Values are generated on each server by the Release manager / DevOps from the operating system random source at install; test and production values differ; the bundle carries configuration templates that name each secret file, never its value. Mapping: `proxy` gets the TLS certificate and key (its only other copy is the recovery copy on the test server, DEC-031, encrypted at rest, DEC-036); `app` the runtime role password and Django secret key; the migration container the owner role password; `db` the role passwords at first start. Rotation on suspected exposure and when an administrator leaves. On recovery, roles get new passwords before `pg_restore` (role passwords are not in a `pg_dump` file), the production TLS certificate and key are restored from the encrypted recovery copy on the test server with the offline private key, which is then removed from the test server (DEC-031, DEC-036; THR T-36), and the other secrets are generated anew. The offline private decryption key is the one secret not held as a server file.

### Consequences
- Positive: no new software or licence; no secret in GitHub or the bundle; least exposure inside the containers.
- Negative: Applexus IT administrators with root can read every secret (THR-001 § Residual risk item 7); the TLS certificate and key recovery copy on the test server (DEC-031) is encrypted at rest and readable only while the offline key is present for a restore (DEC-036; THR T-36; RSK-003 R-4).
- Follow-up: Phase 4 and Phase 8 verify the owner and mode a secret file has inside each container: plain Docker Compose bind-mounts file secrets with the host file's owner and mode (the `uid`, `gid` and `mode` settings may not apply outside Swarm), so a root-only 0400 file may be unreadable by a non-root container process; the Phase 8 design sets host ownership so that only the process needing each secret can read it. Phase 4 coding standards (configuration loading from files); Phase 8 infrastructure as code and runbooks (secret file list, generation, rotation, recovery copy); `.gitignore` covers the secret file names.

### Traceability Links
- Upstream: THR-001 (THR T-17, T-32, T-36, § Secrets handling); NFR N-3, N-5; TOP-001.
- Downstream: Phase 4 coding standards; Phase 8 infrastructure as code, deployment runbook, operational runbook; ADR A-5, A-13, A-14, A-15.

---

## ADR A-18: Rename AssignTicketRequest request-body field to engineer_id for glossary compliance

### Status And Date
Proposed, 2026-10-18 (SCR S-6; proposed by Orchestrator to resolve non-overridable glossary gate)

### Context
- GLO-001 v0.3 defines 'Assigned support engineer' with a synonym in the Avoid list that the identifier-aware glossary checker (`scripts/glossary_check.py check`) detects inside compound identifiers; the gate is non-overridable.
- The OpenAPI spec (docs/04-design/openapi.yaml) defines `AssignTicketRequest` with a request-body property (type: integer, the user account ID of the L2/L3 engineer to assign) whose name contained the avoided GLO-001 synonym. The checker splits snake_case tokens and flagged the name.
- The existing `EffortRecord` schema uses `engineer_id` (integer) for the same concept — the L2/L3 support engineer's user account ID. Renaming the `AssignTicketRequest` field to `engineer_id` gives both schemas consistent naming.
- No code has been written for the assign-ticket endpoint (`POST /api/tickets/{id}/assign/`) at the time of this ADR.

### Options Considered
1. Rename the field → `engineer_id`: consistent with EffortRecord.engineer_id naming; removes the avoided token; no behavioral change; no code exists yet to update. Chosen.
2. Rename the field → `support_engineer_id`: removes the avoided token, descriptive, but inconsistent with EffortRecord.engineer_id naming convention.
3. Rename the field → `assigned_to_id`: consistent with Ticket response schema (`assigned_to_id`). Removes the avoided token but introduces asymmetry with EffortRecord.engineer_id for request bodies.
4. Do not rename, add glossary exemption for technical identifiers: requires changing the domain glossary (GLO-001) and the glossary_check.py script; script changes are human-authored only per SDLC rules; rejected.

### Decision
Option 1. Rename the `AssignTicketRequest` request-body field to `engineer_id` in `docs/04-design/openapi.yaml`. Update the POST /api/tickets/{id}/assign/ 400 error description accordingly. Bump API-001 to v0.2. Consistent with EffortRecord.engineer_id naming; no behavioral change.

### Consequences
- Positive: glossary gate passes; request body naming consistent with EffortRecord schema.
- Negative: future implementations and tests for `POST /api/tickets/{id}/assign/` must use `engineer_id` in the request body; feature plans must update Input References citation from API-001 v0.1 to v0.2 before branching.
- Follow-up: when the assign-ticket feature is planned and built, use `engineer_id` as the request body field name; the feature plan's Input References must cite API-001 v0.2.

### Traceability Links
- Upstream: GLO-001 v0.3 § Terms; API-001 v0.1; openapi.yaml `AssignTicketRequest`; SCR S-6.
- Downstream: API-001 v0.2; openapi.yaml (revised); assign-ticket feature plan.

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md (collection-level) -->
- A-027 (Open): timestamps stored in UTC, shown in IST, SLA on the IST business calendar (ADR A-9).
- A-028 (Open): Argon2id or bcrypt; ADR A-8 chooses Argon2id.
- A-029 (Open): open-source report and export libraries only (ADR A-12).
- A-030 (Confirmed by the OQ-055 answer, Mohanasunder, 2026-10-17): each server has 2 vCPU, 4 GB RAM and 40 GB free disk, Ubuntu LTS with Docker Engine, SSH from production to test (ADR A-5, A-15).
- A-031 (Open): the test server is the "different on-prem server" for the weekly dump and therefore holds production data (ADR A-15).
- A-032 (Open): the database stays under 5 GB for 5 years; no file attachments in release 1 (ADR A-4, A-15).
- A-033 (Open, infra-cost-analyst): 8 weekly dumps kept on the test server, 2 pre-deploy dumps on production (ADR A-15).
- A-038 (Open, security-architect): no secret manager is available; secrets as root-only files (ADR A-17).

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md (collection-level) -->
- Answered by Mohanasunder, 2026-10-17, chat: OQ-052 and OQ-058 (public repository on the personal account, DEC-027; ADR A-13), OQ-055 (servers; ADR A-5), OQ-056 (email alert; ADR A-16), OQ-057 (self-signed certificate, DEC-029; ADR A-14), OQ-059 (Applexus IT firewall and DNS; ADR A-14, A-15), OQ-060 (Docker Engine in WSL 2; ADR A-5), OQ-061 (session limits, DEC-030; ADR A-7), OQ-063 (OS access; ADR A-15, A-17), OQ-066 (Applexus IT installs certificate trust; ADR A-14).
- OQ-062, OQ-064, OQ-065 answered through SCR S-4 (security events; ADR A-11).
- No open question remains for these ADRs.

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions (exception: same-phase Drafts TEC-001, THR-001, TOP-001, CST-001 are cited as context, not as approved input; DEC-027 to DEC-038 are human decisions in the decision log)
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Every ADR has at least two options and a rationale for the chosen one
- [x] Every ADR has its own Traceability Links citing upstream NFR/REQ/SPK S-N IDs
- [x] ADR sub-IDs (A-1, A-2, …) are consecutive from 1 with no gaps
- [x] No separate ADR-NNN.md files exist; all decisions are sections in this file
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)

## Approval Record
| Field | Value |
| --- | --- |
| Decision | Approve |
| Approver | Mohanasunder |
| Role | Architect / tech lead |
| Version | 0.3 |
| Conditions | None |
| Comments | Reviewed after validation run 6; gate decisions DEC-027 to DEC-038 applied; THR-001 envelope-opening log proposal adopted as DEC-039. |
| Timestamp | 2026-10-17 11:25 UTC |
