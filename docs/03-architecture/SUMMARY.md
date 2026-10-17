---
id: SUM-003
title: Phase 3 summary
phase: 3
version: 0.2
template: phase-summary
template_version: 1.0
status: Approved
author_agent: solution-architect
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# Phase 3 summary

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- PIB-003 v0.2, INT-003 v0.2, IRC-004 v0.2 (Approved 2026-10-17).
- SUM-002 v0.4 and the Phase 2 artifacts it indexes (SCR S-4 Approved): NFR-001, REQ-001, BR-001, GLO-001, EPC-001, BKL-001, PRS-001 v0.3; RSK-002 v0.1.
- SUM-001 v0.3; RSK-001 v0.2; `project.md`.
- Human answers, Mohanasunder, chat, 2026-10-17: OQ-052, OQ-055 to OQ-066; DEC-027 to DEC-038.

## Purpose And Scope
<!-- guidance: One or two sentences: which phase this summarizes. File docs/0N-*/SUMMARY.md -->
Summarises Phase 3 (Solution architecture) of APLX AMS so Phase 4 (Design) can start from this page and open full documents only for the sections listed.

## Decisions
<!-- guidance: Bullets: the decision, the reason in one clause, and its source 'ID vX.Y § section'. Only decisions later phases must respect -->
ADR-001 v0.3 (`adrs.md`) holds ADR A-1 to A-17; on approval they form the project's approved technology list (INT-003 v0.2 Q9). Human decisions DEC-027 to DEC-038 are in `docs/logs/decision-log.md`.
- Modular monolith: 1 backend (modules accounts, organizations, tickets, sla, effort, reports, audit) and 1 single-page application; one transaction per change (ADR A-1).
- Python 3.13, Django 5.2 LTS, Django REST framework, Gunicorn; scored 460 against FastAPI 380 on built-in security and delivery speed (ADR A-2; TEC-001 v0.3 § Options T-1).
- React + TypeScript single-page application built with Vite; same-origin REST JSON API under `/api/`; Node.js only in CI (ADR A-3).
- PostgreSQL 18, one database, all state in it, no files on disk (ADR A-4).
- Docker Engine + Compose on the 2 Ubuntu LTS VMs: `proxy` (Nginx), `app`, `db`; only `proxy` publishes ports; workstations use Docker Engine in WSL 2 (ADR A-5).
- Client data separation: client organization ID on every client-owned row, one data-access layer, PostgreSQL row-level security (forced, runtime role without `BYPASSRLS`, transaction-local context), A/B tests in CI (ADR A-6).
- Server-side sessions ending after 60 minutes idle and 12 hours after sign-in (DEC-030); lockout and temporary passwords in `accounts` (ADR A-7). Argon2id password storage (ADR A-8).
- UTC storage, IST display, SLA on the IST business calendar (ADR A-9); SLA timers evaluated on read, stopped results stored, holiday list keeps change times (ADR A-10).
- Append-only audit trail through one audit function, including the 5 security events; runtime role cannot UPDATE or DELETE it; every internal user sees every ticket's audit entries plus their own security events, the delivery manager sees all security events, client users see no audit entries (ADR A-11; BR-001 v0.3 § Rule B-22, B-24).
- XlsxWriter, Python `csv`, WeasyPrint; files generated on request (ADR A-12).
- Public github.com repository on the personal account (DEC-027); GitHub Actions with fork pull request restrictions and secret scanning; a human deploys a checksum-verified bundle, test server first, outside business hours (ADR A-13).
- Internal network only; Nginx TLS with a self-signed certificate (DEC-029) that Applexus IT installs as trusted on every user's machine before go-live; a protected root-only recovery copy of the certificate and key on the test server is restored on recovery (DEC-031; ADR A-14).
- Weekly `pg_dump`, encrypted at rest with age or GnuPG like the pre-deploy dumps and the TLS key recovery copy; private key held offline by the Release manager / DevOps, brought to the test server only for a restore or drill, with a sealed second copy in an Applexus IT safe, checked yearly and handed over within 2 business hours if the holder is unavailable (DEC-034, DEC-036, DEC-037, DEC-038); copied to the test server by a write-only backup account; RPO stays 7 days (daily dump and WAL archiving rejected); 8 weekly dumps kept; restore drill database dropped after the drill; recovery worst case 5.75 business hours, or 7.5 business hours when the sealed key copy is needed, both within the 9-hour RTO (ADR A-15; TOP-001 v0.2 § Scaling And Availability).
- Uptime Kuma on the test server, 60-second check, email alerts to the Release manager / DevOps (ADR A-16).
- Secrets as root-only server files passed as Docker Compose file secrets; none in GitHub; file owner and mode inside containers verified in Phase 4/8 (ADR A-17; THR-001 v0.2 § Secrets handling).
- Single production server accepted for the pilot (DEC-028; RSK-003 R-1).
- Accepted at the Phase 3 gate: delivery manager knows temporary passwords (DEC-033; RSK-003 R-3); passwords typed as account names kept in the audit trail (DEC-032; RSK-003 R-10); server OS access by Mohanasunder and Applexus IT administrators and supply-chain residual risk (DEC-035; THR-001 v0.2 § Residual risk items 7, 8).

## Constraints Set
<!-- guidance: Bullets: limits later phases must work within (technology, NFR targets, scope exclusions, compliance), each with its source ID -->
- Stack and components limited to the TEC-001 v0.3 § Recommendation list; anything else needs a new ADR (INT-003 v0.2 Q9).
- No new paid licences; new spend INR 0 (CST-001 v0.2; SUM-001 v0.3 § Constraints Set).
- 2 servers, each 2 vCPU, 4 GB RAM, 40 GB free disk, Ubuntu LTS (OQ-055 answer; TOP-001 v0.2 § Network And Hosting); no internet exposure (INT-003 v0.2 Q6).
- Nothing in the public repository may hold a secret, server address, host name or production data (ADR A-13; THR-001 v0.2 T-31, T-32).
- NFR targets: NFR-001 v0.3 N-1 to N-9 (N-6 includes the 5 security events); all 9 mapped in ARC-001 v0.3 § NFR Mapping.
- Security controls Phase 4 carries into contracts and standards: THR-001 v0.2 § Mitigations (role per endpoint, CSP, CSRF, rate limits, export formula escaping, logging rules).

## Open Items
<!-- guidance: Open questions (OQ-), assumptions (A-), and risks (RSK-) still open, with owner; or 'None' -->
All owned by Mohanasunder.
- Open OQs: none; OQ-052 to OQ-066 Answered (2026-10-17, chat; OQ-062, OQ-064, OQ-065 through SCR S-4).
- SCR S-4 Approved: NFR-001, REQ-001, BR-001, GLO-001, EPC-001, BKL-001, PRS-001 v0.3, SUM-002 v0.4; PIB-003, INT-003, IRC-004 v0.2.
- Decisions recorded: DEC-027 (public repository), DEC-028 (single production server accepted), DEC-029 (self-signed certificate), DEC-030 (session limits), DEC-031 (TLS key recovery copy), DEC-032 (RSK-003 R-10 accepted), DEC-033 (RSK-003 R-3 accepted), DEC-034 (dump encryption at rest, RPO 7 days), DEC-035 (THR residual items 7, 8 accepted), DEC-036 (dumps and TLS key copy encrypted, offline key), DEC-037 (sealed second key copy in an Applexus IT safe), DEC-038 (sealed copy handed over within 2 business hours; worst-case RTO 7.5 business hours).
- Open assumptions: A-026 to A-029, A-031 to A-036, A-038 (A-030 Confirmed; A-037 Rejected).
- Phase 3 risks (`docs/logs/risk-register.md`): RSK-003 R-1 Accepted (DEC-028), R-3 Accepted (DEC-033), R-10 Accepted (DEC-032); R-4 Mitigating (encryption at rest, DEC-034, DEC-036); R-11 Mitigating (sealed second key copy held by Applexus IT, DEC-037; residual Low); R-2, R-5 to R-9 Open.
- Inherited risks, reviewed at the Phase 3 gate (Mohanasunder, 2026-10-17): Open RSK R-2, R-6, R-8, RSK-002 R-1, R-2; Mitigating RSK R-4, R-5; RSK R-3 Closed (server capacity recorded by OQ-055); RSK R-1 Accepted (DEC-020); RSK R-7 Closed.

## Documents
<!-- guidance: One line per Approved artifact of the phase: 'ID vX.Y - title - path'. Checked by scripts/context_pack.py summaries -->
Approved:
- PIB-003 v0.2 - Phase 3 input brief - docs/03-architecture/phase-input-brief.md
- INT-003 v0.2 - Phase 3 interview - docs/03-architecture/interview-record.md
- IRC-004 v0.2 - Phase 3 readiness - docs/03-architecture/input-readiness-checklist.md

Phase 3 deliverables, approved with this summary by the Architect / tech lead:
- ARC-001 v0.3 - APLX AMS: Architecture Overview - docs/03-architecture/architecture-overview.md
- TEC-001 v0.3 - APLX AMS: Technology Comparison - docs/03-architecture/technology-comparison.md
- ADR-001 v0.3 - APLX AMS: Architecture Decision Records - docs/03-architecture/adrs.md
- THR-001 v0.2 - APLX AMS threat model - docs/03-architecture/threat-model.md
- TOP-001 v0.2 - APLX AMS: Deployment Topology - docs/03-architecture/deployment-topology.md
- CST-001 v0.2 - APLX AMS: Cost Estimate - docs/03-architecture/cost-estimate.md
- RSK-003 v0.3 - APLX AMS: Phase 3 risks - docs/03-architecture/risks.md

## What The Next Phase Needs
<!-- guidance: The few documents or sections the next phase should open in full, as 'ID vX.Y § section'; everything else is covered above -->
- ADR-001 v0.3 § ADR A-6, A-7, A-11, A-13, A-17 (data separation, sessions, audit and security events, CI rules, secrets).
- ARC-001 v0.3 § Components, § NFR Mapping.
- THR-001 v0.2 § Mitigations, § Authentication and authorization model.
- TEC-001 v0.3 § Recommendation (approved technology list).
- TOP-001 v0.2 § Environments (local, CI, test, production).

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- Open: A-026 to A-029, A-031 to A-036, A-038; Confirmed: A-030; Rejected: A-037; listed under § Open Items; logged in `docs/logs/assumptions-log.md`.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
- OQ-052 to OQ-066 Answered; none Open; logged in `docs/logs/open-questions-log.md`.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: PIB-003; INT-003; IRC-004; SUM-002; SUM-001; NFR-001; REQ-001; BR-001; GLO-001; EPC-001; BKL-001; PRS-001; RSK-001; RSK-002.
- Indexes: ARC-001; TEC-001; ADR-001; THR-001; TOP-001; CST-001; RSK-003.
- Downstream: Phase 4 input brief (not yet created).

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions (Phase 3 deliverables under § Documents are approved with this summary)
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)
- [x] Documents lists every Approved artifact of the phase as 'ID vX.Y'
- [x] About half a page: a reader can start the next phase from this summary alone

## Approval Record
| Field | Value |
| --- | --- |
| Decision | Approve |
| Approver | Mohanasunder |
| Role | Architect / tech lead |
| Version | 0.2 |
| Conditions | None |
| Comments | Reviewed after validation run 6; gate decisions DEC-027 to DEC-038 applied; THR-001 envelope-opening log proposal adopted as DEC-039. |
| Timestamp | 2026-10-17 11:25 UTC |
