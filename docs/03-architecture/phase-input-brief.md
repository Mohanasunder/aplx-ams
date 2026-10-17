---
id: PIB-003
title: Phase 3 input brief
phase: 3
version: 0.2
template: phase-input-brief
template_version: 2.0
status: Approved
author_agent: orchestrator
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# Phase 3 input brief

> **One file per phase.** Each phase produces exactly one `phase-input-brief.md` in its own folder. Use `--out docs/0N-<phase-slug>/phase-input-brief.md` when calling `new_artifact.py`; never let it auto-name as `PIB-NNN.md`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- Citations updated under SCR S-4 (2026-10-17).
- SUM-002 v0.4 Phase 2 summary (`docs/02-requirements/SUMMARY.md`), revised by SCR S-3 (Approved) and SCR S-4 (`docs/logs/spec-changes.md`, Approved 2026-10-17).
- Phase 2 artifacts indexed by SUM-002: RSK-002 v0.1 (Approved 2026-10-17, unchanged by SCR S-3 and SCR S-4); NFR-001 v0.3 (N-1 to N-9), REQ-001 v0.3, BR-001 v0.3, GLO-001 v0.3, EPC-001 v0.3, BKL-001 v0.3, PRS-001 v0.3 (revised by SCR S-3 (Approved) and SCR S-4 (Approved 2026-10-17)).
- SUM-001 v0.3 Phase 1 summary and RSK-001 v0.2 (Approved 2026-10-17).
- INT-003 v0.2 Phase 3 interview (`docs/03-architecture/interview-record.md`): evidence record, approved with this brief; answers by Mohanasunder on 2026-10-17.
- `project.md`: approvers and capacity settings.
- `docs/logs/open-questions-log.md` (OQ-007, OQ-021, OQ-033, OQ-038 answered earlier), `docs/logs/risk-register.md` (RSK R-3, R-6; RSK-002 R-1, R-2), `docs/logs/decision-log.md` (DEC-020, DEC-022).
- Repository facts (read 2026-10-17): origin `github.com/Mohanasunder/aplx-ams`; `.github/workflows/ci.yml` runs on GitHub-hosted `ubuntu-latest`; `src/` and `infra/` are empty; `.ai/standards/coding-standards.md` leaves language, framework and database to be set.

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: the human-confirmed inputs for Phase 3 (Solution architecture) of APLX AMS: server platform and count, database, stack, source control and CI, network exposure and certificates, backup method, password handling for new and forgotten passwords, technology and security standards, monitoring, client data separation, data volume, and the assumptions, open question and candidate risks the producers carry.

Producers and outputs (order per `docs/03-architecture/README.md`):
- `solution-architect` first: `architecture-overview.md` (ARC), `technology-comparison.md` (TEC), `adrs.md` (ADR sections `## ADR A-N:`), `spikes.md` only if a spike is needed, Phase 3 `risks.md` entries it raises, Phase 3 `SUMMARY.md`.
- Then in parallel: `security-architect`: `threat-model.md` (THR); `infra-cost-analyst`: `deployment-topology.md` (TOP), `cost-estimate.md` (CST).

Does not cover: production code or detailed contracts (OpenAPI, schema DDL are Phase 4). Phase purpose: decide structure, technology, security approach, topology and cost; record ADRs. Not this: production code or detailed contracts; experiments only as spikes on `spike/` branches.

Exit criteria: every NFR (N-1 to N-9) mapped to an architectural answer; every significant decision has an ADR; `python scripts/spike.py check` passes.

## User Intent
<!-- guidance: The user's request in their words plus the phase goal -->
- In the user's words: "I want to build Application management services solution" (`docs/01-discovery/inputs/requirements.txt`); scoped to an internal AMS delivery tool for SAP application support with client log-in, pilot live by 2027-01-17 (SUM-001 v0.3 § Decisions).
- Phase 3 goal: choose the structure, stack, security approach, deployment topology and cost of APLX AMS release 1 so that PRS-001 F-1 to F-8 and NFR-001 N-1 to N-9 can be met on existing on-prem servers with no new paid licences, and record each significant choice as an ADR for the Architect / tech lead to approve.

## Required Inputs Status
<!-- guidance: Table: input, source (human/approved artifact/external), status, location -->
| # | Input | Source | Status | Location |
| --- | --- | --- | --- | --- |
| 1 | Approved requirements (NFRs, integrations) | Approved artifacts | Present | SUM-002 v0.4; NFR-001, BR-001, REQ-001, PRS-001 v0.3 |
| 2 | Enterprise architecture standards and approved technology list | Human (Q9) | Present: none exists; the approved Phase 3 ADRs become the project's approved list | INT-003 Q9 |
| 3 | Team skills and preferred stack | Human (Q4) | Present: Python backend (Django or FastAPI), React TypeScript frontend | INT-003 Q4 |
| 4 | Hosting and cloud constraints | Human (Q1, Q2, Q6); OQ-021 | Present: existing on-prem Linux VMs, containers allowed; 2 servers (production, test); Applexus network or VPN only | INT-003 Q1, Q2, Q6 |
| 5 | Documentation of systems to integrate with | Approved artifacts | Not applicable: no integrations in release 1 | SCP-001 v0.2 OS-3; INT-002 Q5, Q12; OQ-038 |
| 6 | Security policies | Human (Q6, Q8, Q9); NFR-001 N-5 | Present: password policy N-5; no company IT security policy (Q9); HTTPS with internal CA (Q6); temporary passwords (Q8), now in REQ-001 v0.3 S-30, S-31, BR-001 v0.3 B-23 and NFR-001 v0.3 N-5 (SCR S-3 and SCR S-4, Approved) | INT-003 Q6, Q8, Q9; NFR-001 v0.3 N-5; SCR S-3, S-4 |
| 7 | Budget limits | Human; SUM-001 | Present: no new paid licences, existing staff and AI agents (INT-001 Q10, Q16); Q5: "Keep the github.com repository and GitHub-hosted CI; a human deploys a built package to on-prem manually" | SUM-001 v0.3 § Constraints Set; INT-003 Q5 |
| 8 | Expected scale (users, data volume, traffic) | Human (Q12); OQ-007, OQ-033; INT-002 Q9a | Present: about 10 engineers and 20 client users, 30 concurrent, 1 pilot organization, under 200 tickets per month | INT-003 Q12; NFR-001 v0.3 N-2 |
| 9 | Named Phase 3 approver | `project.md` | Present: Mohanasunder (Architect / tech lead); no backup (DEC-020) | `project.md` |

## Interview Answers
<!-- guidance: Question, answer, who answered, date; deferred items are marked as assumptions -->
All answers by Mohanasunder (Architect / tech lead and all other approver roles), 2026-10-17, chat via Claude Code; questions prepared by `phase-intake`. Full record: INT-003. No item deferred.

| Q | Topic | Answer |
| --- | --- | --- |
| Q1 | Server platform | Linux VMs; Docker containers allowed |
| Q2 | Servers | 2 servers: 1 production, 1 test; the test server also hosts the restore drill (NFR N-3) |
| Q3 | Database | PostgreSQL (free, open source) on the existing servers |
| Q4 | Stack | Python backend (Django or FastAPI) with a React TypeScript frontend: the stack the sole reviewer can review confidently |
| Q5 | Source control and CI | "Keep the github.com repository and GitHub-hosted CI; a human deploys a built package to on-prem manually" (no automated cloud-to-on-prem deploy) |
| Q6 | Network | Applexus network or VPN only, not internet-facing, in release 1; HTTPS with a certificate from the company internal CA |
| Q7 | Backup | Weekly scheduled native PostgreSQL dump to a different on-prem server or disk; RPO 7 days unchanged |
| Q8 | New and forgotten passwords | The delivery manager sets a one-time temporary password for a new user and for a forgotten password; no forced change at first sign-in (lower-security option chosen knowingly by the human) |
| Q9 | Standards | Applexus has no written approved technology list or IT security policy; the approved Phase 3 ADRs become the project's approved list |
| Q10 | Monitoring | A free, open-source, self-hosted uptime checker on the test server checks once a minute and alerts on downtime |
| Q11 | Data separation | One PostgreSQL database; every client-owned row carries the client organization ID, enforced in one data-access layer plus PostgreSQL row-level security; tested with 2 client organizations (DEC-022, NFR N-7) |
| Q12 | Volume | Under 200 tickets per month |

## Referenced Artifact Versions
<!-- guidance: Exact IDs and versions of approved upstream artifacts -->
- SUM-002 v0.4 § Decisions, § Constraints Set, § Open Items, § What The Next Phase Needs.
- NFR-001 v0.3 § NFR N-1 to N-9 (N-5 revised by SCR S-3: setting a temporary password clears a lockout).
- BR-001 v0.3 § Rule B-1 to B-11 (SLA timers), § Rule B-2 (business-hours calendar), § Rule B-20 (data boundary), § Rule B-21 (user accounts), § Rule B-22 (audit), § Rule B-23 (password set, reset and change), § Rule B-24 (security events in the audit trail).
- REQ-001 v0.3 § Story S-20, S-21 (user accounts, sign-in), § Story S-22 (data boundary), § Story S-30 (temporary password), § Story S-31 (change own password), § Story S-32, S-33 (security events).
- PRS-001 v0.3 § Product Scope; GLO-001 v0.3 § Terms; EPC-001 v0.3 § Epic E-5; BKL-001 v0.3.
- SCR S-3 and SCR S-4 (`docs/logs/spec-changes.md`, Approved 2026-10-17): the versions above are the current Approved versions; NFR-001 v0.3 § NFR N-6 (audit trail, security events).
- RSK-001 v0.2 § Risk R-3, § Risk R-6; RSK-002 v0.1 § Risk R-1, § Risk R-2.
- SUM-001 v0.3 § Constraints Set.

## Constraints
<!-- guidance: Technology, compliance, budget, timeline, capacity -->
Settled before this interview (not new answers):
- Hosting: existing on-prem servers (OQ-021). Budget: no new paid licences; existing staff and AI agents (INT-001 Q10, Q16).
- Scale: about 10 engineers and about 20 client users, 30 concurrent users, 1 pilot client organization (OQ-007, OQ-033, INT-002 Q9a).
- NFR targets: NFR-001 v0.3 N-1 to N-9 (99% availability in business hours; p95 under 2 s at 30 concurrent users; weekly backup, RPO 7 days, RTO 9 business hours; indefinite retention; password policy and lockout, no MFA; 100% audit; 0 cross-organization records; Chrome and Edge; names and emails only).
- Integrations: none (SCP-001 OS-3; INT-002 Q5, Q12; OQ-038).
- Calendar: 09:00 to 18:00 IST, Monday to Friday, minus the company holiday list (BR-001 B-2).
- Timeline: go-live 2027-01-17.
- Repository: origin `github.com/Mohanasunder/aplx-ams`; CI in `.github/workflows/ci.yml` on GitHub-hosted `ubuntu-latest`; `src/` and `infra/` empty; coding standards leave language, framework and database to be set (Phase 4 `standards-author` fills them from the approved ADRs).

From this interview (INT-003):
- Platform and topology: Linux VMs with containers allowed (Q1); exactly 2 servers, production and test, the test server also hosting the restore drill and the uptime checker (Q2, Q10); PostgreSQL on those servers (Q3).
- Stack: Python backend (Django or FastAPI; the `solution-architect` compares both in `technology-comparison.md` and records the choice as an ADR) and React TypeScript frontend (Q4).
- Delivery (Q5): "Keep the github.com repository and GitHub-hosted CI; a human deploys a built package to on-prem manually"; no automated cloud-to-on-prem deploy.
- Password handling (Q8; SCR S-3): producers design password handling only per REQ-001 v0.3 S-20, S-21, S-30, S-31 and BR-001 v0.3 B-21, B-23, with the NFR-001 v0.3 N-5 policy; nothing beyond (no email, no self-service reset, no MFA, no password expiry, no forced change).
- Security events (SCR S-4): producers record and show security events per REQ-001 v0.3 S-32, S-33, BR-001 v0.3 B-24 and NFR-001 v0.3 N-6; nothing beyond.
- Network: not internet-facing in release 1; HTTPS with an internal CA certificate (Q6).
- Backup: weekly native PostgreSQL dump to a different on-prem server or disk (Q7).
- Data separation: one database; client organization ID on every client-owned row; one data-access layer plus PostgreSQL row-level security; tested with 2 client organizations (Q11; DEC-022).
- Volume: under 200 tickets per month (Q12).
- Standards: the approved Phase 3 ADRs become the project's approved technology list (Q9).

Producer pointers:
- Human decisions to respect, not override: Q8 (no forced password change), NFR N-5 (no MFA), N-3 (RPO 7 days).
- `security-architect`: record as a threat and a risk that the delivery manager knows a user's temporary password: a user can change their own password (REQ S-31) but is never forced to (BR B-23), so the delivery manager may keep knowing it; together with no MFA (RSK-002 R-1).
- Password gap resolved upstream by SCR S-3 (REQ S-30: delivery manager sets or resets a temporary password, which clears a lockout at once; REQ S-31: any signed-in user changes their own password after entering the current one; BR B-23; NFR N-5; GLO-001 v0.3 terms). OQ-053 (a user must enter their current password to change it) and OQ-054 (setting a temporary password clears a lockout at once) are Answered and folded into REQ-001 v0.3 S-31, S-30 and NFR-001 v0.3 N-5. If a producer finds any further password behaviour is needed, it raises an open question or SCR; it does not design around the requirements.
- Candidate risks to record as RSK entries in `docs/03-architecture/risks.md` plus rows in `docs/logs/risk-register.md`, each with a named owner: (1) delivery manager knows user passwords (Q8; with RSK-002 R-1); (2) GitHub-hosted CI with manual deploy (Q5) and company code on a personal github.com account, allowed for the pilot with a public repository (OQ-052, DEC-027); (3) a single production server against the 99% availability target (NFR N-1).
- Every NFR N-1 to N-9 needs an architectural answer in `architecture-overview.md`.
- Capacity (`project.md`): 3 parallel builder agents; 6 PR reviews per week; 1 approver, no backup (DEC-020); spikes at most 5 days.

## Readiness Verdict
<!-- guidance: Ready | Ready with assumptions | Not ready, with the reason -->
Ready. Producers started under v0.1 (after SCR S-3 approval); v0.2 updates citations to the SCR S-4 versions (NFR-001, REQ-001, BR-001, GLO-001, EPC-001, BKL-001, PRS-001 v0.3; SUM-002 v0.4), now Approved. All 12 questions were answered by the human; no item was deferred. Four producer defaults are stated as labeled assumptions (A-026 to A-029) for the approver to confirm at review; they do not block the producers. OQ-052 (personal github.com account) is Answered (DEC-027).

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
Logged in `docs/logs/assumptions-log.md`; the approver confirms or rejects each at review.
- A-026 (Open): the cost estimate is in INR and records new spend (expected 0), the share of existing server capacity used, and staff and AI agent hours.
- A-027 (Open): timestamps are stored in UTC and displayed in IST; SLA business time is computed on the IST business calendar (BR-001 B-2).
- A-028 (Open): passwords are stored with an OWASP-recommended adaptive hashing algorithm (Argon2id or bcrypt), chosen in the stack ADR.
- A-029 (Open): Excel, CSV and PDF files are generated with free, open-source libraries only, with each licence checked in `technology-comparison.md`.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
Logged in `docs/logs/open-questions-log.md`.
- OQ-052 (Answered, DEC-027): company code may stay on the personal github.com account (`github.com/Mohanasunder/aplx-ams`) for the pilot; the repository is public.
- Raised by SCR S-3: OQ-053 (a user must enter their current password to change it) and OQ-054 (setting a temporary password clears a lockout at once) are Answered and folded into REQ-001 v0.3 S-31, S-30 and NFR-001 v0.3 N-5 (Mohanasunder, Product owner / BA).
- OQ-001 to OQ-051: all Answered.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: SUM-002 v0.4; NFR-001 v0.3; BR-001 v0.3; REQ-001 v0.3; PRS-001 v0.3; GLO-001 v0.3; EPC-001 v0.3; BKL-001 v0.3; RSK-002 v0.1; SUM-001 v0.3; RSK-001 v0.2; INT-003; `project.md`.
- Downstream: IRC-004 (Phase 3 readiness); `docs/03-architecture/architecture-overview.md`, `technology-comparison.md`, `adrs.md`, `threat-model.md`, `deployment-topology.md`, `cost-estimate.md`, `risks.md`, Phase 3 `SUMMARY.md`; `docs/logs/traceability-matrix.md`.

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions (all cited versions Approved; INT-003 is the evidence record approved with this brief)
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
| Comments | Citation update under SCR S-4; run 5 passed. |
| Timestamp | 2026-10-17 11:03 UTC |
