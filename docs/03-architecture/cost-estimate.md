---
id: CST-001
title: APLX AMS: Cost Estimate
phase: 3
version: 0.2
template: cost-estimate
template_version: 2.0
status: Approved
author_agent: infra-cost-analyst
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# APLX AMS: Cost Estimate

> **Single file.** There is exactly one cost estimate per project. Always use `--id CST --out docs/03-architecture/cost-estimate.md` when calling `new_artifact.py`; never auto-name as `CST-NNN.md`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- PIB-003 v0.2 (Approved) and INT-003 v0.2 (Approved); PIB-003 § Required Inputs Status row 7 (no new paid licences; existing staff and AI agents), § Interview Answers Q1, Q2, Q3, Q5, Q6, Q7, Q10, Q12, § Assumptions A-026 (INR; new spend, share of existing capacity, staff and AI agent hours).
- SUM-001 v0.3 (Approved) § Constraints Set (existing on-prem servers, no new paid licences).
- NFR-001 v0.3 (Approved) § NFR N-1 to N-4; SUM-002 v0.4 (Approved).
- Human answers, Mohanasunder, chat 2026-10-17: OQ-055 (servers at the A-030 minimum, current Ubuntu LTS, Docker Engine), OQ-056 (alert email via existing company mail), OQ-057 and DEC-029 (self-signed certificate), OQ-058 and DEC-027 (public repository, free GitHub Actions minutes), OQ-059 (Applexus IT owns firewall and DNS), OQ-060 (Docker Engine in WSL 2), OQ-066 (Applexus IT installs the self-signed certificate as trusted on every user's machine before go-live), DEC-028 (RSK-003 R-1 accepted for the pilot); DEC-031 (root-only recovery copy of the production certificate and key on the test server); DEC-034 (weekly dumps encrypted at rest with age or gpg; RPO stays 7 days); DEC-036 (weekly dumps, pre-deploy dumps and the certificate and key recovery copy encrypted; private key held offline by the Release manager / DevOps).
- `project.md` capacity settings (`review_capacity_prs_per_week: 6`, `max_test_runtime_minutes: 10`).
- Same phase, Draft (component list and sizing being costed): TEC-001 v0.3 § Licence check summary; ADR-001 v0.3 ADR A-5, A-13, A-14, A-15, A-16; ARC-001 v0.3; RSK-003 v0.3; THR-001 v0.2; TOP-001 v0.2 § Network And Hosting (capacity sizing).

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: the cost of running APLX AMS release 1 in INR per A-026, in 3 parts: (1) new licence and hosting spend, (2) share of existing server capacity used, (3) staff and AI agent effort in hours. Every line states its assumption.

Does not cover: build effort per feature (known only after the Phase 5 plan slices the features); money for existing capacity or staff time, because no internal chargeback rate or hourly rate is recorded in any approved input, so these are stated as capacity shares and hours, not INR.

## Assumptions Used
<!-- guidance: Volumes, users, pricing basis -->
| Basis | Value | Source |
| --- | --- | --- |
| Currency | INR | A-026 |
| Users | About 10 internal users, about 20 client users, 30 concurrent, 1 pilot client organization | NFR N-2; SUM-001 v0.3 |
| Tickets | Under 200 per month; under 12,000 in 5 years | INT-003 Q12 |
| Database | Under 5 GB for 5 years | A-032 |
| Peak load | At most 15 API requests/s | A-034 |
| Backup | Weekly dump at most 2 GB; 8 weekly and 2 pre-deploy dumps kept | INT-003 Q7; A-033 |
| CI | At most 1,500 Linux runner minutes and 4 GB artifact storage per month; public repository, so standard GitHub-hosted runner minutes are free | A-035; DEC-027 |
| Servers | 2 existing Ubuntu LTS VMs, each 2 vCPU, 4 GB RAM, 40 GB free disk, Docker Engine installed | INT-003 Q2; A-030 confirmed by the OQ-055 answer |
| Licence pricing basis | Only free and open-source components; no vendor price used anywhere in this estimate | SUM-001 v0.3; TEC-001 § Licence check summary |
| Capacity pricing basis | No internal chargeback rate given: existing capacity shown as a share, not INR | A-026 |
| Effort pricing basis | No hourly rate given: effort shown in hours only | A-026; A-036 |

## Cost Breakdown
<!-- guidance: Table: item, unit, quantity, monthly cost -->
| Line | Item | Unit | Quantity | New spend per month (INR) | One-time new spend (INR) | Basis and assumption |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | Production server (existing Ubuntu LTS VM) | VM | 1 | 0 | 0 | Existing (INT-003 Q2). Share used at 5-year ceiling: about 0.75 of 2 vCPU at peak, 3.0 of 4 GB RAM (75%), 17.4 of 40 GB free disk (44%) (TOP-001; A-030, A-032, A-033, A-034) |
| C-2 | Test server (existing Ubuntu LTS VM) | VM | 1 | 0 | 0 | Existing (INT-003 Q2). Share used at 5-year ceiling: 2.5 of 4 GB RAM during a restore drill (63%), 30.9 of 40 GB free disk (77%), incl. backup store 16 GB and drill database 6 GB (TOP-001; A-030, A-033) |
| C-3 | Ubuntu LTS on both VMs | Installation | 2 | 0 | 0 | Already installed on the existing VMs (OQ-055 answer); Ubuntu LTS is free to use; no optional paid support subscription is part of this estimate |
| C-4 | Docker Engine, Docker Compose | Installation | 2 servers | 0 | 0 | Apache-2.0 (TEC-001); Docker Engine already on the servers (OQ-055 answer); Docker Desktop not used (ADR A-5) |
| C-5 | PostgreSQL 18 | Container | 2 (production db, test db) + 1 on demand (drill) | 0 | 0 | PostgreSQL License (TEC-001; INT-003 Q3) |
| C-6 | Nginx | Container | 2 | 0 | 0 | BSD-2-Clause (TEC-001; ADR A-14) |
| C-7 | Backend runtime: Python 3.13, Django 5.2 LTS, Django REST framework, Gunicorn, psycopg 3, argon2-cffi, XlsxWriter, WeasyPrint | Libraries | 1 image | 0 | 0 | PSF-2.0; BSD-3-Clause; BSD-3-Clause; MIT; LGPL-3.0 (unmodified library use); MIT; BSD-2-Clause; BSD-3-Clause (TEC-001; A-029) |
| C-8 | Frontend build: React, Vite, TypeScript, Node.js 24 LTS (CI build only) | Libraries | 1 build | 0 | 0 | MIT; MIT; Apache-2.0; MIT (TEC-001) |
| C-9 | GitHub repository and GitHub Actions (GitHub-hosted runners, artifact storage) | Runner minutes; GB storage | At most 1,500 min; at most 4 GB | 0 | 0 | INT-003 Q5; ADR A-13; usage A-035; repository made public so standard GitHub-hosted runner minutes carry no charge (DEC-027); no GitHub price used |
| C-10 | Uptime Kuma 2 | Container | 1 (test server) | 0 | 0 | MIT (TEC-001; INT-003 Q10; ADR A-16) |
| C-11 | Self-signed TLS certificate for the pilot | Certificate | 1 production (+1 test) | 0 | 0 | Generated with free tooling (DEC-029); Applexus IT installs it as trusted on every user's machine before go-live (OQ-066 answer; IT hours not counted here); root-only recovery copy of certificate and key on the test server uses existing disk (DEC-031) |
| C-12 | Downtime alert email | Channel | 1 | 0 | 0 | Existing company mail to the Release manager / DevOps (OQ-056 answer) |
| C-13 | Backup storage | GB on the test server | 16 GB dumps + 6 GB drill database | 0 | 0 | Inside C-2 share; no separate backup product (INT-003 Q7; A-031, A-033); encryption does not change dump size materially |
| C-19 | Backup encryption tool: age or GnuPG (choice in Phase 8) | Command-line tool | 1 on the production server, 1 on the test server | 0 | 0 | age BSD-3-Clause; GnuPG GPL-3.0 (used as a tool, unmodified); both free (DEC-034, DEC-036); key pair generation and offline key storage fit inside the C-16 hours (timed restore drill 4 h); key handling per restore fits the C-15 deploy hours; staff hours unchanged |
| C-14 | Network: Applexus network, VPN, firewall rules, DNS record | Rules | P-1 to P-7 in TOP-001 | 0 | 0 | Existing Applexus network (INT-003 Q6); Applexus IT owns firewall and DNS and moves the host name within 2 business hours on request (OQ-059 answer); IT hours not counted here |
| C-15 | Staff operating effort (Release manager / DevOps) | Hours | About 8 h per month | Hours only, no rate | - | A-036: 2 deploys x 1.5 h, 4 dump checks x 0.25 h, availability review 1 h, patching 2 h, certificate and alert checks 1 h; plus the yearly restore drill with the sealed key copy, about 4 h per year (about 0.3 h per month; DEC-037; same 4 h as the C-16 drill, producer estimate) |
| C-16 | Staff one-time setup before go-live | Hours | About 16 h | - | Hours only, no rate | A-036: Docker install and hardening 6 h, certificate 1 h, Uptime Kuma 2 h, first deploy 3 h, timed restore drill 4 h |
| C-17 | Local developer container runtime | Workstation | Per developer | 0 | 0 | Docker Engine in WSL 2, Apache-2.0; no Docker Desktop licence (OQ-060 answer) |
| C-18 | Build effort (staff and AI agents, Phases 4 to 8) | Hours | Not estimated in Phase 3 | 0 new (existing AI agents) | - | Existing staff and AI agents (PIB-003 row 7); hours known after the Phase 5 plan; capacity 3 parallel builder agents, 6 PR reviews per week (`project.md`) |

Totals:
- New licence and hosting spend: INR 0 per month and INR 0 one-time; no line depends on an open question.
- Existing capacity: 2 existing VMs; production uses up to 75% RAM and 44% disk of the confirmed size, test up to 77% disk.
- Staff hours: about 16 h one-time, then about 8 h per month (A-036); build hours from the Phase 5 plan.

## Risks To Estimate
<!-- guidance: What could move the number -->
| What could move the number | Effect | Lines | Reference |
| --- | --- | --- | --- |
| The repository is made private again or moves to a company-owned account | Included minutes and storage limits then apply; paid minutes or storage would be new spend above INR 0 and need a human budget decision | C-9 | DEC-027; A-035 |
| Artifact storage on the public repository grows past free limits | Shorter bundle retention in CI (Phase 8) | C-9 | A-035 |
| The test server disk is short for 8 dumps (77% used at the 5-year ceiling) | Fewer dumps kept, or Applexus IT adds disk on the existing platform; internal cost not known | C-2, C-13 | A-033 |
| Human lowers the RPO (daily dump or WAL archiving, ADR A-15 options 2 and 3) | No licence cost; 56 daily dumps kept for 8 weeks (112 GB) need up to about 96 GB more than the 8 weekly dumps on the test server at the 5-year ceiling | C-2, C-13 | RSK-002 R-2 |
| Human later reverses DEC-028 and asks for VM-level protection against a production server loss | Depends on the Applexus virtualization platform; may carry cost | C-1 | RSK-003 R-1; DEC-028 |
| Applexus IT replaces the self-signed certificate with an internal-CA certificate (DEC-029 alternative) | Internal CA: INR 0; staff hours only | C-11 | DEC-029 |
| More deploys per month or incident work | Operating hours above 8 h per month | C-15 | A-036 |
| External client organizations sign in from the internet (after release 1) | Public certificate, internet exposure, MFA: new design and possibly new spend | C-11, C-14 | ADR A-14; RSK-002 R-1 |
| Django 5.2 LTS security support ends April 2028 | Upgrade effort hours in Phase 9 | C-18 | ADR A-2 |

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-026 (Open, phase-intake): INR; new spend, share of existing capacity, staff and AI agent hours.
- A-030 (Confirmed, Mohanasunder, 2026-10-17, OQ-055): server minimum.
- A-031, A-032 (Open, solution-architect): dump location, database ceiling.
- A-033 (Open): weekly dump at most 2 GB; 8 weekly and 2 pre-deploy dumps kept.
- A-034 (Open): peak load at most 15 API requests/s; one production instance suffices.
- A-035 (Open): CI at most 1,500 runner minutes and 4 GB artifact storage per month; with the public repository (DEC-027) the minutes carry no cost.
- A-036 (Open): operating effort about 8 staff hours per month and about 16 one-time staff hours.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
Answered by Mohanasunder, 2026-10-17: OQ-055 (C-1 to C-4), OQ-056 (C-12), OQ-057 (C-11, DEC-029), OQ-058 (C-9, DEC-027), OQ-059 (C-14), OQ-060 (C-17), OQ-066 (C-11). OQ-052 (company code on a personal github.com account) is settled for the pilot by DEC-027.

No open questions remain for this artifact.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: PIB-003 (row 7; Q1, Q2, Q3, Q5, Q6, Q7, Q10, Q12); INT-003; SUM-001; SUM-002; NFR-001 (N-1, N-2, N-3, N-4); RSK-002 (R-1, R-2).
- Same phase: TOP-001 (`deployment-topology.md`); THR-001 (`threat-model.md`); TEC-001; ADR-001 (ADR A-2, A-5, A-13, A-14, A-15, A-16); RSK-003 (R-1); ARC-001.
- Downstream: Phase 5 build plan (build effort hours); Phase 8 infrastructure as code and operational runbook; Phase 9 cost and capacity review.

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions (justified exception: same-phase Draft TEC-001, ADR-001, ARC-001, RSK-003, THR-001, TOP-001 cited only as the component list and sizing being costed, labelled Draft)
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
| Version | 0.2 |
| Conditions | None |
| Comments | Reviewed after validation run 6; gate decisions DEC-027 to DEC-038 applied; THR-001 envelope-opening log proposal adopted as DEC-039. |
| Timestamp | 2026-10-17 11:25 UTC |
