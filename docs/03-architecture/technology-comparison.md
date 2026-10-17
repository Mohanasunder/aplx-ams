---
id: TEC-001
title: APLX AMS: Technology Comparison
phase: 3
version: 0.3
template: technology-comparison
template_version: 2.0
status: Approved
author_agent: solution-architect
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# APLX AMS: Technology Comparison

> **Single file.** There is exactly one technology comparison per project. Always use `--id TEC --out docs/03-architecture/technology-comparison.md` when calling `new_artifact.py`; never auto-name as `TEC-NNN.md`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- PIB-003 v0.2 § Interview Answers (Q1 to Q12), § Constraints, § Assumptions (A-026 to A-029); IRC-004 v0.2.
- INT-003 v0.2 § Questions And Answers (evidence record).
- SUM-002 v0.4 § Decisions, § Constraints Set.
- NFR-001 v0.3 § NFR N-1 to N-9.
- REQ-001 v0.3 § Story S-14 (monthly client report download as Excel or PDF), § Story S-17 (finance export as Excel or CSV), § Story S-20, S-21, S-22, S-30, S-31.
- BR-001 v0.3 § Rule B-14, B-18, B-20, B-23.
- SUM-001 v0.3 § Constraints Set (existing on-prem servers, no new paid licences, go-live 2027-01-17).
- RSK-001 v0.2 § Risk R-3, R-6.
- `project.md` capacity: 3 builder agents, 6 PR reviews per week, 1 approver.
- Human answers, Mohanasunder, chat, 2026-10-17: OQ-055 (Ubuntu LTS, Docker Engine, 2 vCPU, 4 GB RAM, 40 GB disk per server), OQ-056 (alerts by email), OQ-060 (Docker Engine in WSL 2 on workstations); DEC-027 (public repository), DEC-029 (self-signed certificate).

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: a weighted comparison of real, free and open-source options for each technology choice of APLX AMS release 1 that the human answers left open or that the architecture must fix: backend framework (Django or FastAPI, INT-003 Q4), frontend build approach for React TypeScript (Q4), database engine (PostgreSQL confirmed by Q3, compared for completeness against the RLS need), Excel, CSV and PDF generation (A-029), password hashing (A-028), reverse proxy for HTTPS (Q6), runtime packaging (Q1), and uptime checker (Q10). Each licence is checked. The result feeds ADR A-2 to A-16 in `adrs.md`.

Does not cover: library versions below the major version, coding standards, lint and test tools (Phase 4 `standards-author`), and cost figures (`cost-estimate.md`, `infra-cost-analyst`). Applexus has no approved technology list (INT-003 Q9); the approved ADRs and the list under § Recommendation become the project's approved list.

## Criteria
<!-- guidance: Weighted, tied to NFRs and constraints -->
Gate (pass or fail, applied before scoring): free and open-source licence, no new paid licence (SUM-001 v0.3 § Constraints Set; A-029). An option that needs a paid licence is excluded.

| ID | Criterion | Weight | Tied to |
| --- | --- | --- | --- |
| C1 | Reviewability by the sole human reviewer: the reviewer named Python (Django or FastAPI) and React TypeScript as the stack they review confidently; fewer conventions to check per PR | 25 | INT-003 Q4; `project.md` (6 PR reviews per week, 1 approver) |
| C2 | Built-in security for sign-in, sessions, CSRF and password storage and policy | 20 | NFR N-5; REQ S-21, S-30, S-31; BR B-23 |
| C3 | Support for client data separation with PostgreSQL row-level security and a per-request client organization context | 15 | NFR N-7; BR B-20; INT-003 Q11; RSK R-6 |
| C4 | Licence clarity: permissive (MIT, BSD, Apache-2.0, PostgreSQL License) scores 5; copyleft used unmodified as a library (LGPL) scores 4 | 10 | SUM-001 § Constraints Set; A-029 |
| C5 | Fit to existing on-prem Linux VMs with Docker and a manually deployed built package; fewest runtime containers | 10 | INT-003 Q1, Q2, Q5; RSK R-3 |
| C6 | Excel, CSV and PDF generation | 10 | REQ S-14, S-17; BR B-14, B-18; A-029 |
| C7 | Delivery speed to the 2027-01-17 go-live with 3 builder agents: migrations, data access and validation built in | 10 | SUM-001 § Constraints Set; RSK R-2 |

Scoring: 1 (poor) to 5 (strong). Weighted score = sum of weight x score; maximum 500. A criterion that does not separate the options in a comparison scores 3 for every option and is marked "n/a".

## Options
<!-- guidance: Table scoring each option against the criteria -->
### T-1 Backend framework (INT-003 Q4: Django or FastAPI)

| Option | Licence | C1 (25) | C2 (20) | C3 (15) | C4 (10) | C5 (10) | C6 (10) | C7 (10) | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Django 5.2 LTS + Django REST framework 3.x, Gunicorn | BSD-3-Clause; BSD-3-Clause; MIT | 4 | 5 | 4 | 5 | 5 | 5 | 5 | 460 |
| FastAPI + SQLAlchemy 2 + Alembic + Pydantic, Uvicorn | MIT; MIT; MIT; MIT; BSD-3-Clause | 4 | 2 | 4 | 5 | 5 | 5 | 3 | 380 |

- C1: both are named by the reviewer (Q4), so both score 4. Django has one project layout and one ORM convention; FastAPI projects assemble their own layout.
- C2: Django ships authentication, server-side sessions, CSRF protection, clickjacking headers, password validators and an Argon2 hasher (Argon2id variant, needs `argon2-cffi`). FastAPI ships none of these; each is a separate library choice or custom code that the reviewer must check.
- C3: both set a PostgreSQL session setting per request transaction (Django: `ATOMIC_REQUESTS` plus middleware; SQLAlchemy: session event), so both score 4.
- C6: both use the same Python libraries (T-4, T-5).
- C7: Django includes migrations, ORM, validation and admin tooling; FastAPI needs Alembic and separate auth and session code.
- Support: Django 5.2 is the only LTS series, security fixes until April 2028 (djangoproject.com download page, read 2026-10-17); Django 6.2 LTS is due April 2027. Django REST framework 3.18 supports Django 5.2, 6.0 and 6.1 and Python 3.10 or later (PyPI, read 2026-10-17).

### T-2 Frontend build approach (INT-003 Q4: React TypeScript)

| Option | Licence | C1 (25) | C2 (20) | C3 (15) | C4 (10) | C5 (10) | C6 (10) | C7 (10) | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| React + TypeScript single-page application built with Vite; static files served by the reverse proxy | MIT; Apache-2.0; MIT | 5 | 4 | 3 (n/a) | 5 | 5 | 3 (n/a) | 4 | 420 |
| Next.js (React + TypeScript) with a Node.js server at runtime | MIT | 3 | 3 | 3 (n/a) | 5 | 3 | 3 (n/a) | 4 | 330 |

- C1: a Vite single-page application is plain React; Next.js adds server components, server routing and a second server-side codebase to review.
- C2: the single-page application is served from the same origin as the API, so Django session cookies and CSRF protection apply with no cross-origin setup; Next.js adds a second server that handles requests and cookies.
- C5: the single-page application needs Node.js only at build time in CI; Next.js needs a Node.js container at runtime on the production server.
- Server-rendered Django templates without React are not compared: INT-003 Q4 sets React TypeScript.

### T-3 Database engine (INT-003 Q3: PostgreSQL)

| Option | Licence | C1 (25) | C2 (20) | C3 (15) | C4 (10) | C5 (10) | C6 (10) | C7 (10) | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PostgreSQL 18 | PostgreSQL License | 4 | 4 | 5 | 5 | 5 | 3 (n/a) | 5 | 435 |
| MariaDB 11 LTS | GPL-2.0 (server) | 4 | 3 | 1 | 4 | 5 | 3 (n/a) | 4 | 335 |

- C3: PostgreSQL has row-level security policies (`CREATE POLICY`, `FORCE ROW LEVEL SECURITY`); MariaDB has no row-level security, so separation would rest on the data-access layer alone, against INT-003 Q11.
- C2: PostgreSQL roles and grants let the runtime role be denied UPDATE and DELETE on the audit table (NFR N-6).
- Support: PostgreSQL 18 first released 2025-09-25, supported until 2030-11-14; PostgreSQL 17 until 2029-11-08 (postgresql.org versioning page, read 2026-10-17). Django 5.2 supports PostgreSQL 14 and later.
- Database driver: psycopg 3 (LGPL-3.0, used unmodified as a library; free).

### T-4 Excel and CSV generation (A-029; REQ S-14, S-17)

| Option | Licence | C1 (25) | C2 (20) | C3 (15) | C4 (10) | C5 (10) | C6 (10) | C7 (10) | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XlsxWriter (Excel) + Python standard library `csv` (CSV) | BSD-2-Clause; PSF-2.0 | 4 | 3 (n/a) | 3 (n/a) | 5 | 5 | 5 | 4 | 395 |
| openpyxl (Excel) + Python standard library `csv` (CSV) | MIT; PSF-2.0 | 4 | 3 (n/a) | 3 (n/a) | 5 | 5 | 4 | 4 | 385 |

- C6: APLX AMS only writes Excel files (monthly client report, finance export); XlsxWriter is a write-only XLSX library with a constant-memory mode; openpyxl also reads and edits files, which release 1 does not need.
- CSV uses the Python standard library; no third-party library is needed.

### T-5 PDF generation (A-029; REQ S-14)

| Option | Licence | C1 (25) | C2 (20) | C3 (15) | C4 (10) | C5 (10) | C6 (10) | C7 (10) | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WeasyPrint (HTML and CSS template to PDF) | BSD-3-Clause | 5 | 3 (n/a) | 3 (n/a) | 5 | 4 | 5 | 5 | 420 |
| ReportLab open-source toolkit (PDF drawn in Python code) | BSD | 3 | 3 (n/a) | 3 (n/a) | 5 | 5 | 4 | 3 | 350 |
| fpdf2 (PDF drawn in Python code) | LGPL-3.0 | 3 | 3 (n/a) | 3 (n/a) | 4 | 5 | 3 | 3 | 330 |

- C1, C7: WeasyPrint renders the monthly client report from an HTML template, which the reviewer reads like any page; the other two build the layout in code.
- C5: WeasyPrint needs the Pango text-layout system libraries in the backend image (open-source operating system packages, installed at image build in CI).

### T-6 Password hashing (A-028; NFR N-5)

| Option | Licence | C1 (25) | C2 (20) | C3 (15) | C4 (10) | C5 (10) | C6 (10) | C7 (10) | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Argon2id through Django's Argon2 hasher and `argon2-cffi` | MIT | 4 | 5 | 3 (n/a) | 5 | 5 | 3 (n/a) | 5 | 425 |
| bcrypt through Django's bcrypt hasher and `bcrypt` | Apache-2.0 | 4 | 4 | 3 (n/a) | 5 | 5 | 3 (n/a) | 5 | 405 |
| PBKDF2-SHA256 (Django default, no extra library) | BSD-3-Clause (Django) | 5 | 3 | 3 (n/a) | 5 | 5 | 3 (n/a) | 5 | 410 |

- C2: OWASP Password Storage guidance lists Argon2id first, bcrypt for legacy systems and PBKDF2 where FIPS compliance is needed; bcrypt ignores input beyond 72 bytes. Argon2id is memory-hard against GPU guessing, which matters with no MFA (RSK-002 R-1).

### T-7 Reverse proxy and HTTPS termination (INT-003 Q6)

| Option | Licence | C1 (25) | C2 (20) | C3 (15) | C4 (10) | C5 (10) | C6 (10) | C7 (10) | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nginx (official container image) | BSD-2-Clause | 4 | 4 | 3 (n/a) | 5 | 5 | 3 (n/a) | 4 | 395 |
| Caddy (official container image) | Apache-2.0 | 3 | 4 | 3 (n/a) | 5 | 5 | 3 (n/a) | 4 | 370 |

- Caddy's automatic public certificates do not apply on the internal network; the pilot uses a self-signed certificate (DEC-029), so both load certificate files. Nginx configuration is the more widely documented of the two.

### T-8 Runtime packaging on the Linux VMs (INT-003 Q1, Q5)

| Option | Licence | C1 (25) | C2 (20) | C3 (15) | C4 (10) | C5 (10) | C6 (10) | C7 (10) | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Docker Engine + Docker Compose; images built in CI and shipped as image archives | Apache-2.0; Apache-2.0 | 4 | 4 | 3 (n/a) | 5 | 5 | 3 (n/a) | 5 | 405 |
| Operating system packages + Python virtual environment + systemd services | Various open source | 3 | 3 | 3 (n/a) | 5 | 3 | 3 (n/a) | 3 | 320 |

- C5: the same images run in CI, on the test server and on the production server, so the built package the human deploys (Q5) is the image set CI tested. Docker Desktop is not used anywhere: servers run Docker Engine on Ubuntu LTS and developer workstations run Docker Engine inside WSL 2 (OQ-055, OQ-060 answers); Docker Engine is free (Apache-2.0).

### T-9 Uptime checker (INT-003 Q10: free, open-source, self-hosted)

| Option | Licence | C1 (25) | C2 (20) | C3 (15) | C4 (10) | C5 (10) | C6 (10) | C7 (10) | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Uptime Kuma 2 (container `louislam/uptime-kuma`) | MIT | 4 | 3 (n/a) | 3 (n/a) | 5 | 5 | 3 (n/a) | 5 | 385 |
| Gatus (container, YAML configuration) | Apache-2.0 | 4 | 3 (n/a) | 3 (n/a) | 5 | 5 | 3 (n/a) | 4 | 375 |
| Scheduled shell script with `curl` on the test server | Not applicable - custom code | 3 | 3 (n/a) | 3 (n/a) | 5 | 4 | 3 (n/a) | 2 | 320 |

- Uptime Kuma: HTTP checks at intervals down to 20 seconds, Email (SMTP) and 90+ other notification services, a web UI with check history (GitHub repository, read 2026-10-17). Alerts go by email (SMTP) through the existing company mail to the Release manager / DevOps (OQ-056 answer).

### Licence check summary

| Component | Licence | Source checked |
| --- | --- | --- |
| Python 3.13 | PSF-2.0 | python.org licence |
| Django 5.2 LTS | BSD-3-Clause | djangoproject.com (support dates read 2026-10-17) |
| Django REST framework 3.x | BSD-3-Clause | PyPI, read 2026-10-17 |
| Gunicorn | MIT | project licence file |
| psycopg 3 | LGPL-3.0 (unmodified library use) | project licence file |
| argon2-cffi | MIT | project licence file |
| XlsxWriter | BSD-2-Clause | GitHub repository, read 2026-10-17 |
| WeasyPrint | BSD-3-Clause | PyPI and Debian package metadata, read 2026-10-17 |
| React, Vite | MIT | project licence files |
| TypeScript | Apache-2.0 | project licence file |
| Node.js 24 LTS (CI build only) | MIT | project licence file |
| PostgreSQL 18 | PostgreSQL License | postgresql.org (support dates read 2026-10-17) |
| Nginx | BSD-2-Clause | nginx.org licence |
| Docker Engine, Docker Compose | Apache-2.0 | project licence files |
| Uptime Kuma 2 | MIT | GitHub repository, read 2026-10-17 |
| age or GnuPG (backup encryption, DEC-034; one chosen in Phase 8) | age: BSD-3-Clause; GnuPG: GPL-3.0 (used unmodified as a command-line tool) | project licence files |

Every component passes the gate. The CI licence scan (Phase 4 standards, Phase 6 security scans) re-checks every package and its dependencies at each build.

## Recommendation
<!-- guidance: Choice, reasoning, and what would change it -->
Recommended stack (highest weighted score in each comparison; final stack choice is the Architect / tech lead's decision at review):

| Area | Choice | ADR |
| --- | --- | --- |
| Backend | Python 3.13, Django 5.2 LTS, Django REST framework, Gunicorn | ADR A-2 |
| Frontend | React + TypeScript single-page application built with Vite (Node.js 24 LTS in CI only) | ADR A-3 |
| Database | PostgreSQL 18, psycopg 3 | ADR A-4 |
| Runtime | Docker Engine + Docker Compose on the 2 existing Linux VMs | ADR A-5 |
| Password hashing | Argon2id (`argon2-cffi`) | ADR A-8 |
| Excel, CSV, PDF | XlsxWriter, Python `csv`, WeasyPrint | ADR A-12 |
| Source and CI | Public github.com repository, GitHub Actions on GitHub-hosted runners (minutes free on a public repository, DEC-027), GitHub secret scanning | ADR A-13 |
| Reverse proxy and HTTPS | Nginx with a self-signed certificate trusted on every user's machine | ADR A-14 |
| Uptime checker | Uptime Kuma 2 on the test server, email alerts | ADR A-16 |
| Server secrets | Docker Compose file secrets from root-only files (no new technology) | ADR A-17 |
| Backup encryption at rest | age or GnuPG, free and open source (DEC-034) | ADR A-15 |

Reasoning: Django wins on built-in security (C2) and delivery speed (C7) at equal reviewability, which matters with one reviewer, no MFA (RSK-002 R-1) and a 3-month timeline (RSK R-2). A Vite single-page application needs no Node.js at runtime and keeps the API same-origin. PostgreSQL is the only compared engine with row-level security (INT-003 Q11).

Per INT-003 Q9, once the ADRs are approved, the table above is the project's approved technology list; anything outside it needs a new ADR.

What would change it:
- The reviewer reports stronger FastAPI than Django experience: C1 would move to FastAPI 5, Django 3 (FastAPI 405, Django 435); still Django, by 30 points; re-decide if the reviewer prefers FastAPI.
- External client users after release 1 reach APLX AMS from the internet: revisit ADR A-14 (exposure) and MFA (RSK-002 R-1).
- The Phase 7 load test shows the A-030 server size (confirmed by OQ-055) is short: WeasyPrint memory use and the Gunicorn worker count are re-checked first (TOP-001).

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-028 (Open): passwords stored with Argon2id or bcrypt; this comparison recommends Argon2id (T-6, ADR A-8).
- A-029 (Open): Excel, CSV and PDF generated with free, open-source libraries only, each licence checked here (T-4, T-5, licence check summary).
- A-030 (Confirmed by the OQ-055 answer): each server has 2 vCPU, 4 GB RAM and 40 GB free disk; T-2 and T-8 favour fewer runtime containers for this reason.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
- Answered by Mohanasunder, 2026-10-17, chat: OQ-055 (servers), OQ-056 (email alerts, T-9), OQ-060 (Docker Engine in WSL 2, T-8), OQ-052 and OQ-058 (public repository, DEC-027), OQ-057 (self-signed certificate, DEC-029, T-7).
- No open question remains for this comparison.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: PIB-003; INT-003; SUM-002; NFR-001 (N-1, N-2, N-5, N-6, N-7); REQ-001 (S-14, S-17, S-21, S-30, S-31); BR-001 (B-14, B-18, B-20, B-23); SUM-001; RSK-001 (R-2, R-3, R-6); RSK-002 (R-1).
- Downstream: ADR-001 (ADR A-2 to A-17); ARC-001; TOP-001; CST-001; Phase 4 coding standards and backend design.

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
| Version | 0.3 |
| Conditions | None |
| Comments | Reviewed after validation run 6; gate decisions DEC-027 to DEC-038 applied; THR-001 envelope-opening log proposal adopted as DEC-039. |
| Timestamp | 2026-10-17 11:25 UTC |
