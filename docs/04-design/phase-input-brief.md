---
id: PIB-004
title: Phase 4 input brief
phase: 4
version: 0.1
template: phase-input-brief
template_version: 2.0
status: Approved
author_agent: orchestrator
approver: Mohanasunder
date: 2026-10-17
validation: Pass
---
# Phase 4 input brief

> **One file per phase.** Each phase produces exactly one `phase-input-brief.md` in its own folder. Use `--out docs/0N-<phase-slug>/phase-input-brief.md` when calling `new_artifact.py`; never let it auto-name as `PIB-NNN.md`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- SUM-003 v0.2 â€” Phase 3 summary â€” docs/03-architecture/SUMMARY.md (Approved 2026-10-17)
- SUM-002 v0.4 â€” Phase 2 summary â€” docs/02-requirements/SUMMARY.md (Approved 2026-10-17)
- SUM-001 v0.3 â€” Phase 1 summary â€” docs/01-discovery/SUMMARY.md (Approved 2026-10-17)
- Phase 4 entry interview answers, Mohanasunder, chat, 2026-10-17 (INT-004 v0.1)

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
This brief gives every Phase 4 producer the complete context needed to build the solution design artifacts: database design, OpenAPI specification, backend design, UI specification, permission matrix, coding standards, and test strategy. It covers the phase goal, every approved upstream decision and constraint producers must not violate, the six interview decisions made in the Phase 4 entry interview, and the open assumptions that must be carried and labeled throughout Phase 4 work. It does not repeat detail already captured in the upstream summaries; producers open a full document only for the sections listed under Â§ Referenced Artifact Versions.

## User Intent
<!-- guidance: The user's request in their words plus the phase goal -->
Mohanasunder (Architect / tech lead, Product owner, Business owner / BA) approved Phases 1 to 3 on 2026-10-17 and directed Phase 4 to begin. The phase goal is: produce all contracts and standards the build phase requires â€” the approved database schema, OpenAPI specification, backend design, UI specification, permission matrix, coding standards, and test strategy â€” so that Phase 5 (Build planning) can slice the work into buildable features with no open design questions remaining.

## Required Inputs Status
<!-- guidance: Table: input, source (human/approved artifact/external), status, location -->
| Input | Source | Status | Location |
| --- | --- | --- | --- |
| SUM-003 v0.2 â€” Phase 3 summary | Approved artifact | Available | docs/03-architecture/SUMMARY.md |
| SUM-002 v0.4 â€” Phase 2 summary | Approved artifact | Available | docs/02-requirements/SUMMARY.md |
| SUM-001 v0.3 â€” Phase 1 summary | Approved artifact | Available | docs/01-discovery/SUMMARY.md |
| ADR-001 v0.3 Â§ ADR A-6, A-7, A-11, A-13, A-17 | Approved artifact | Available | docs/03-architecture/adrs.md |
| ARC-001 v0.3 Â§ Components, Â§ NFR Mapping | Approved artifact | Available | docs/03-architecture/architecture-overview.md |
| THR-001 v0.2 Â§ Mitigations, Â§ Authentication and authorization model | Approved artifact | Available | docs/03-architecture/threat-model.md |
| TEC-001 v0.3 Â§ Recommendation | Approved artifact | Available | docs/03-architecture/technology-comparison.md |
| TOP-001 v0.2 Â§ Environments | Approved artifact | Available | docs/03-architecture/deployment-topology.md |
| NFR-001 v0.3 Â§ NFRs N-1 to N-9 | Approved artifact | Available | docs/02-requirements/nfrs.md |
| REQ-001 v0.3 Â§ Stories S-1 to S-33 | Approved artifact | Available | docs/02-requirements/user-stories.md |
| BR-001 v0.3 Â§ Rules B-1 to B-24 | Approved artifact | Available | docs/02-requirements/business-rules.md |
| GLO-001 v0.3 â€” Domain glossary | Approved artifact | Available | docs/02-requirements/domain-glossary.md |
| PRS-001 v0.3 â€” Product requirement specification | Approved artifact | Available | docs/02-requirements/product-requirement-specification.md |
| BKL-001 v0.3 â€” Backlog | Approved artifact | Available | docs/02-requirements/backlog.md |
| UI library decision (Q1) | Human â€” Mohanasunder, chat, 2026-10-17 | Available â€” confirmed | INT-004 v0.1 Â§ Q1 |
| Phase 2 assumptions A-014 to A-022 confirmation (Q2) | Human â€” Mohanasunder, chat, 2026-10-17 | Available â€” confirmed | INT-004 v0.1 Â§ Q2 |
| Sign-in rate limit (Q3) | Human â€” Mohanasunder, chat, 2026-10-17 | Available â€” confirmed | INT-004 v0.1 Â§ Q3 |
| Development tooling (Q4) | Human â€” Mohanasunder, chat, 2026-10-17 | Available â€” confirmed | INT-004 v0.1 Â§ Q4 |
| Accessibility target (Q5) | Human â€” Mohanasunder, chat, 2026-10-17 | Available â€” confirmed | INT-004 v0.1 Â§ Q5 |
| Code coverage targets (Q6) | Human â€” Mohanasunder, chat, 2026-10-17 | Available â€” confirmed | INT-004 v0.1 Â§ Q6 |
| Third-party API documentation | External | Not applicable â€” greenfield system, no external integrations (SUM-003 v0.2 Â§ Decisions) | N/A |

## Interview Answers
<!-- guidance: Question, answer, who answered, date; deferred items are marked as assumptions -->
All answers given by Mohanasunder, chat, 2026-10-17.

**Q1 â€” UI component library (BLOCKER â€” resolved)**
- Affects: ui-spec.md (UIS) Â§ Component library; coding-standards.md (STD) Â§ Frontend dependencies
- Answer: Material UI v6 (MUI), MIT licence, default theme. No custom theme in Phase 4; the default MUI theme applies throughout. Decision DEC-041.

**Q2 â€” Phase 2 open assumptions A-014 to A-022 (BLOCKER â€” resolved)**
- Affects: database-design.md (DBD), api-spec.md (API), backend-design.md (BED), ui-spec.md (UIS), permission-matrix.md (PRM)
- Answer: All seven assumptions confirmed as stated:
  - A-014: at-risk and breached states are evaluated separately for the response clock and the resolution clock of a ticket.
  - A-015: the reporting period of the monthly client report is the calendar month in IST; a ticket counts in the month its clock stops; ticket counts are tickets raised, Resolved and Closed per priority.
  - A-016: each audit entry holds the old value and the new value; no user can edit or delete an audit entry.
  - A-019: a refused sign-in does not say whether the account name or the password was wrong (generic error message).
  - A-020: an effort entry must have more than 0 hours; 0 or negative hours are not saved.
  - A-021: when the denominator of response % or resolution % is 0, the % is shown as "no tickets", not 0% or 100%.
  - A-022: ticket statuses in release 1 are Open, Awaiting client, Resolved and Closed.
  - Decision DEC-041.

**Q3 â€” Sign-in rate limit (ADVISORY â€” resolved)**
- Affects: api-spec.md (API) Â§ Security; backend-design.md (BED) Â§ Authentication; coding-standards.md (STD) Â§ Rate limiting
- Answer: 10 requests per minute per IP address, burst of 5. Enforced at the Nginx reverse proxy layer (consistent with ADR A-14 and THR-001 v0.2 Â§ Mitigations). Decision DEC-042.

**Q4 â€” Development tooling (ADVISORY â€” resolved)**
- Affects: coding-standards.md (STD) Â§ Linting, Â§ Static analysis, Â§ Test tooling; test-strategy.md (TST) Â§ Tools
- Answer: Adopt all proposed defaults:
  - Python: ruff (linting and formatting), mypy --strict (type checking), pytest + pytest-django (unit and integration tests), bandit (security static analysis), pip-audit (dependency vulnerability scan), detect-secrets (secret scanning).
  - TypeScript: eslint with the TypeScript plugin (linting), tsc --noEmit (type checking), vitest (unit tests), playwright (end-to-end tests).
  - Decision DEC-043.

**Q5 â€” Accessibility target (ADVISORY â€” resolved)**
- Affects: ui-spec.md (UIS) Â§ Accessibility; coding-standards.md (STD) Â§ Accessibility; test-strategy.md (TST) Â§ Accessibility testing
- Answer: WCAG 2.1 Level A. All UI components and interactions must meet Level A criteria. Decision DEC-044.

**Q6 â€” Code coverage targets (ADVISORY â€” resolved)**
- Affects: coding-standards.md (STD) Â§ Coverage gates; test-strategy.md (TST) Â§ Coverage targets
- Answer: 80% line coverage for backend Python code (CI-enforced); 70% line coverage for frontend TypeScript code (CI-enforced). Decision DEC-045.

## Referenced Artifact Versions
<!-- guidance: Exact IDs and versions of approved upstream artifacts -->
Every producer must read this brief and the summaries first. Open a full document only for the sections named below.

| Artifact | Version | Sections to open | Path |
| --- | --- | --- | --- |
| SUM-003 | v0.2 | All | docs/03-architecture/SUMMARY.md |
| SUM-002 | v0.4 | Â§ Decisions, Â§ Constraints Set, Â§ Open Items | docs/02-requirements/SUMMARY.md |
| SUM-001 | v0.3 | Â§ Constraints Set | docs/01-discovery/SUMMARY.md |
| ADR-001 | v0.3 | Â§ ADR A-6 (RLS), Â§ ADR A-7 (sessions), Â§ ADR A-11 (audit trail), Â§ ADR A-13 (CI rules), Â§ ADR A-17 (secrets) | docs/03-architecture/adrs.md |
| ARC-001 | v0.3 | Â§ Components, Â§ NFR Mapping | docs/03-architecture/architecture-overview.md |
| THR-001 | v0.2 | Â§ Mitigations, Â§ Authentication and authorization model | docs/03-architecture/threat-model.md |
| TEC-001 | v0.3 | Â§ Recommendation | docs/03-architecture/technology-comparison.md |
| TOP-001 | v0.2 | Â§ Environments | docs/03-architecture/deployment-topology.md |
| NFR-001 | v0.3 | All (9 NFRs N-1 to N-9) | docs/02-requirements/nfrs.md |
| REQ-001 | v0.3 | All (S-1 to S-33) | docs/02-requirements/user-stories.md |
| BR-001 | v0.3 | All (B-1 to B-24) | docs/02-requirements/business-rules.md |
| GLO-001 | v0.3 | All | docs/02-requirements/domain-glossary.md |
| PRS-001 | v0.3 | Â§ Features F-1 to F-8, Â§ Non-Goals | docs/02-requirements/product-requirement-specification.md |
| BKL-001 | v0.3 | All | docs/02-requirements/backlog.md |

## Constraints
<!-- guidance: Technology, compliance, budget, timeline, capacity -->
**Technology constraints** (ADR-001 v0.3; TEC-001 v0.3 Â§ Recommendation):
- Backend: Python 3.13, Django 5.2 LTS, Django REST Framework, Gunicorn.
- Frontend: React with TypeScript, Vite (build only; Node.js not in production).
- UI library: Material UI v6 (MUI), MIT licence, default theme (Q1, DEC-041).
- Database: PostgreSQL 18, one database, no files on disk (ADR A-4).
- Infrastructure: Docker Engine + Compose on Ubuntu LTS VMs; Nginx TLS termination (ADR A-5, A-14).
- Report generation: XlsxWriter (Excel), Python csv module (CSV), WeasyPrint (PDF) â€” all free open-source (ADR A-12; A-029 inherited open).
- Secrets: root-only Docker Compose file secrets; none in code or the repository (ADR A-17; DEC-027).
- Any library not on the TEC-001 v0.3 Â§ Recommendation list requires a new ADR before use.

**Security constraints** (THR-001 v0.2 Â§ Mitigations; ADR-001 v0.3):
- PostgreSQL row-level security enforced at the data-access layer; every client-owned row carries the client organization ID (ADR A-6).
- Server-side sessions, 60-minute idle timeout, 12-hour absolute timeout (ADR A-7).
- Argon2id password storage (ADR A-8, A-028).
- UTC storage, IST display; SLA timers computed on the IST business calendar (ADR A-9).
- Append-only audit trail (ADR A-11); runtime role cannot UPDATE or DELETE audit entries.
- Security events recorded in the audit trail: successful sign-ins, failed sign-ins, account lockouts, temporary passwords set, own password changes (BR-001 v0.3 B-24; REQ-001 v0.3 S-32).
- Refused sign-in shows generic error â€” no hint whether the account name or the password was wrong (A-019 confirmed, Q2).
- Sign-in rate limit: 10 requests per minute per IP, burst 5 (Q3, DEC-042).
- CSP, CSRF protection, export formula escaping (THR-001 v0.2 Â§ Mitigations).
- No secret, server address, host name, or production data in the public repository (ADR A-13).

**NFR constraints** (NFR-001 v0.3 N-1 to N-9):
- N-1: 99% availability of business hours per month.
- N-2: page p95 under 2 s at 30 concurrent users (10 engineer, 20 client user sessions).
- N-3: backup every 7 days, RPO 7 days, RTO 9 business hours.
- N-4: 0 automatic deletions.
- N-5: passwords at least 8 characters (upper-case, lower-case, digit); locked 30 minutes after 5 failed sign-ins; no MFA.
- N-6: 100% audit of status, priority, assignment, and effort changes and of the 5 security event types; 0 audit entries with a password value.
- N-7: 0 cross-organization records visible to a client user.
- N-8: Chrome and Edge current and previous major versions on desktop (A-008 inherited open).
- N-9: personal data limited to name and email per user account.

**Scope constraints** (PRS-001 v0.3 Â§ Non-Goals NG-3 to NG-5; SCP-001 v0.2):
- Desktop web browser only; no mobile views.
- Intake via portal only; no mailbox integration; no external ITSM integration.
- SAP applications only in release 1.
- Finance export downloaded and emailed by the delivery manager outside the tool; no finance user role.
- No external APIs; greenfield system.
- No new paid licences; new spend INR 0 (CST-001 v0.2).

**Development standards** (Q4 DEC-043; Q5 DEC-044; Q6 DEC-045):
- Accessibility: WCAG 2.1 Level A.
- Backend coverage gate: 80% line coverage (CI-enforced).
- Frontend coverage gate: 70% line coverage (CI-enforced).
- Linting, type checking, security scans, and secret detection as specified in Q4.

**Producer instructions â€” sequence and assignment:**

Wave 1 (run in parallel):
- database-designer: Produce database-design.md (DBD). Read ARC-001 v0.3 Â§ Components; REQ-001 v0.3; BR-001 v0.3; GLO-001 v0.3; ADR-001 v0.3 Â§ A-6, A-11. Design the full PostgreSQL 18 schema for modules: accounts, organizations, tickets, sla, effort, reports, audit. Enforce client organization ID on every client-owned row (ADR A-6). Design the append-only audit table with old_value and new_value columns (A-016 confirmed). Use exactly these ticket statuses as a PostgreSQL enum: Open, Awaiting client, Resolved, Closed (A-022 confirmed). Label every design decision that depends on an open inherited assumption.
- api-designer: Produce api-spec.md + openapi.yaml (OpenAPI 3.1). Read ARC-001 v0.3 Â§ Components; THR-001 v0.2 Â§ Mitigations, Â§ Authentication and authorization model; REQ-001 v0.3; NFR-001 v0.3; BR-001 v0.3; ADR-001 v0.3 Â§ A-7, A-13. Define all endpoints under /api/ for the 8 features. Include sign-in rate limit: 10 req/min per IP, burst 5 (DEC-042). Include role-based access per 4 personas (P-1 L1, P-2 L2/L3, P-3 delivery manager, P-4 client user). Refused sign-in must not reveal account name or password (A-019). Use UTC for all timestamps in request and response bodies.

Wave 2 (run in parallel, after Wave 1):
- backend-designer: Produce backend-design.md (BED). Read DBD (Wave 1), api-spec.md (Wave 1), ARC-001 v0.3 Â§ Components, Â§ NFR Mapping; ADR-001 v0.3 Â§ A-6, A-7, A-8, A-9, A-11, A-12, A-15, A-17; THR-001 v0.2 Â§ Mitigations. Design Django 5.2 module structure, service layer, data-access layer with RLS (ADR A-6), session management (ADR A-7), Argon2id password storage (ADR A-8, A-028), SLA timer evaluation on read (ADR A-10), audit function (append-only, ADR A-11), report generation with XlsxWriter, csv, WeasyPrint (ADR A-12, A-029). State Gunicorn worker count assumption (A-034). Label all inherited open assumptions.
- ux-ui-designer: Produce ui-spec.md (UIS). Read REQ-001 v0.3; PRS-001 v0.3 Â§ Features; GLO-001 v0.3; NFR-001 v0.3 N-8. Use Material UI v6 default theme (DEC-041). All screens must meet WCAG 2.1 Level A (DEC-044). Desktop only; no mobile views. Show "no tickets" (not 0%) when the SLA denominator is 0 (A-021 confirmed). Show SLA status separately for response and resolution clocks (A-014 confirmed). Use only these ticket statuses: Open, Awaiting client, Resolved, Closed (A-022 confirmed).

Wave 3 (after Wave 2):
- standards-author: Produce permission-matrix.md (PRM), coding-standards.md (STD), and test-strategy.md (TST).
  - PRM: cross-reference 4 personas against all endpoints from api-spec.md; read THR-001 v0.2 Â§ Authentication and authorization model; ADR-001 v0.3 Â§ A-11; BR-001 v0.3 B-22, B-24.
  - STD: incorporate Q4 tooling (DEC-043), WCAG 2.1 Level A (DEC-044), coverage gates 80% backend / 70% frontend (DEC-045), secrets rules (ADR A-17, A-038 labeled), branching rules (.ai/standards/branching-standard.md), TEC-001 v0.3 approved technology list.
  - TST: cover unit, integration, end-to-end (playwright), load (NFR N-2 at 30 concurrent users), accessibility (WCAG 2.1 Level A), and security testing; state coverage targets (DEC-045); reference tooling from STD; max test runtime 10 minutes (project.md).

All producers: use `python3 scripts/new_artifact.py <template> --out docs/04-design/<filename>` to create each artifact; label every design decision that depends on an open inherited assumption (A-008, A-026 to A-029, A-031 to A-036, A-038) with the assumption ID; do not invent any library, endpoint, table, screen, or rule not traceable to an approved upstream artifact or an interview answer in this brief; follow GLO-001 v0.3 terminology throughout; run `python3 scripts/validate_artifact.py` before submitting for checker review.

## Readiness Verdict
<!-- guidance: Ready | Ready with assumptions | Not ready, with the reason -->
Ready with assumptions.

All blockers from the entry interview are resolved. The seven Phase 2 open assumptions (A-014 to A-022) are confirmed. The UI library is decided. No open questions remain from any earlier phase. Twelve inherited open assumptions (A-008, A-026 to A-029, A-031 to A-036, A-038) are carried forward and must be labeled as assumptions in each Phase 4 artifact where they affect a design decision. None blocks Phase 4 from starting.

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
Confirmed in this interview (status changes to Confirmed; update docs/logs/assumptions-log.md):
- A-014 confirmed: at-risk and breached states evaluated separately per clock â€” Confirmed, Mohanasunder, chat, 2026-10-17.
- A-015 confirmed: monthly report period is calendar month IST; ticket counts per priority â€” Confirmed, Mohanasunder, chat, 2026-10-17.
- A-016 confirmed: each audit entry holds old and new value; no user can edit or delete â€” Confirmed, Mohanasunder, chat, 2026-10-17.
- A-019 confirmed: refused sign-in shows generic error (no account name or password hint) â€” Confirmed, Mohanasunder, chat, 2026-10-17.
- A-020 confirmed: effort entry must be > 0 hours; 0 or negative hours are not saved â€” Confirmed, Mohanasunder, chat, 2026-10-17.
- A-021 confirmed: 0-denominator response % or resolution % shown as "no tickets" â€” Confirmed, Mohanasunder, chat, 2026-10-17.
- A-022 confirmed: ticket statuses are Open, Awaiting client, Resolved, Closed â€” Confirmed, Mohanasunder, chat, 2026-10-17.

Inherited open assumptions carried into Phase 4 (producers must label any design choice that depends on one of these):
- A-008: supported browsers are current and previous major Chrome and Edge on desktop â€” Open.
- A-026: cost estimate in INR, new spend 0, share of server capacity, staff and AI hours â€” Open.
- A-027: timestamps stored in UTC, displayed in IST, SLA on IST business calendar â€” Open (consistent with ADR A-9; label in DBD and BED).
- A-028: passwords stored with Argon2id â€” Open (consistent with ADR A-8; label in BED and STD).
- A-029: report libraries free and open-source (XlsxWriter, csv, WeasyPrint) â€” Open (consistent with ADR A-12; label in BED).
- A-031: weekly dump copied to the test server; test server holds production data â€” Open.
- A-032: database stays under 5 GB for 5 years â€” Open.
- A-033: pg_dump file is at most 2 GB; 8 weekly dumps kept on the test server â€” Open.
- A-034: peak load is 30 concurrent users at at most 15 API requests per second; one app container with 5 Gunicorn workers â€” Open (label in BED Â§ Capacity).
- A-035: GitHub Actions use stays within the free-tier quota on the public repository â€” Open.
- A-036: operating effort is about 8 staff hours per month â€” Open.
- A-038: no secret manager; secrets as root-only Docker Compose file secrets â€” Open (consistent with ADR A-17; label in STD).

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
None. All Phase 2 and Phase 3 open questions are answered. The Phase 4 entry interview resolved all two blockers. No new open questions were raised in this interview. If any producer identifies a gap, raise a new OQ-NNN in docs/logs/open-questions-log.md before proceeding.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: SUM-003 v0.2, SUM-002 v0.4, SUM-001 v0.3; INT-004 v0.1; IRC-005 v0.1; ADR-001 v0.3; ARC-001 v0.3; THR-001 v0.2; TEC-001 v0.3; TOP-001 v0.2; NFR-001 v0.3; REQ-001 v0.3; BR-001 v0.3; GLO-001 v0.3; PRS-001 v0.3; BKL-001 v0.3.
- Downstream: Phase 4 deliverables (DBD, API, BED, UIS, PRM, STD, TST â€” under docs/04-design/).

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
| Comments | Phase 4 entry interview complete; all blockers resolved; 6 decisions recorded DEC-040 to DEC-045 |
| Timestamp | 2026-10-17 11:54 UTC |
