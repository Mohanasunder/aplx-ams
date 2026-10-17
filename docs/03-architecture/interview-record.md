---
id: INT-003
title: Phase 3 interview
phase: 3
version: 0.2
template: interview-record
template_version: 2.0
status: Approved
author_agent: orchestrator
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# Phase 3 interview

> **One file per phase.** Each phase produces exactly one `interview-record.md` in its own folder. Use `--out docs/0N-<phase-slug>/interview-record.md` when calling `new_artifact.py`; never let it auto-name as `INT-NNN.md`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- Citations updated under SCR S-4 (2026-10-17).
- SUM-002 v0.4 and the artifacts it indexes: RSK-002 v0.1 (Approved 2026-10-17, unchanged by SCR S-3 and SCR S-4); NFR-001 v0.3, REQ-001 v0.3, BR-001 v0.3, GLO-001 v0.3, EPC-001 v0.3, BKL-001 v0.3, PRS-001 v0.3 (revised by SCR S-3 (Approved) and SCR S-4 (`docs/logs/spec-changes.md`, Approved 2026-10-17)).
- SUM-001 v0.3 and RSK-001 v0.2 (Approved 2026-10-17).
- `docs/logs/open-questions-log.md` (OQ-007, OQ-021, OQ-033, OQ-038 answered earlier; cited, not re-asked).
- `project.md` (approvers, capacity); repository facts (`.github/workflows/ci.yml`, empty `src/` and `infra/`, `.ai/standards/coding-standards.md`).

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: the Phase 3 entry interview for APLX AMS. Questions were prepared by `phase-intake` from the gaps between the Phase 3 required inputs (`docs/03-architecture/README.md`), the templates, and SUM-002 (its previous version at the time of the interview; now v0.4 per SCR S-3 and SCR S-4), and asked by the Orchestrator in chat via Claude Code on 2026-10-17. This record is the evidence source the `solution-architect`, `security-architect` and `infra-cost-analyst` cite for platform, stack, delivery, network, backup, password handling, standards, monitoring, data separation and volume.

Not re-asked (settled before this interview): on-prem hosting (OQ-021); no new paid licences, existing staff and AI agents (INT-001 Q10, Q16); scale of about 10 engineers and about 20 client users, 30 concurrent, 1 pilot organization (OQ-007, OQ-033, INT-002 Q9a); NFR targets N-1 to N-9; no integrations (SCP-001 OS-3; INT-002 Q5, Q12; OQ-038); IST business calendar (BR-001 B-2); go-live 2027-01-17.

Does not cover: architecture decisions, ADRs, threat model, topology or cost (Phase 3 producer outputs).

## Questions And Answers
<!-- guidance: Table: ID, question, why it matters (template section affected), answer, answered by, date -->
All answered by Mohanasunder (Architect / tech lead and all other approver roles), 2026-10-17.

| ID | Question | Why it matters | Answer |
| --- | --- | --- | --- |
| Q1 | What server platform do the existing on-prem servers offer? | Deployment topology; technology comparison | Linux VMs; Docker containers allowed |
| Q2 | How many servers are available, and for what? | Topology; NFR N-1, N-3 (restore drill) | 2 servers: 1 production, 1 test; the test server also hosts the restore drill (N-3) |
| Q3 | Which database can run on the existing servers with no new paid licence? | Technology comparison; ADR | PostgreSQL (free, open source) on the existing servers |
| Q4 | Which stack can the sole reviewer review confidently? | Technology comparison; ADR; Phase 6 review capacity | Python backend (Django or FastAPI) with a React TypeScript frontend |
| Q5 | Where do source control and CI run, and how does a build reach the on-prem servers? | Topology; ADR; cost | "Keep the github.com repository and GitHub-hosted CI; a human deploys a built package to on-prem manually" (no automated cloud-to-on-prem deploy) |
| Q6 | Who can reach the application in release 1, and how is traffic encrypted? | Threat model; topology | Applexus network or VPN only, not internet-facing; HTTPS with a certificate from the company internal CA |
| Q7 | How is the weekly backup taken and where is it kept? | NFR N-3; topology | Weekly scheduled native PostgreSQL dump to a different on-prem server or disk; RPO 7 days unchanged |
| Q8 | How does a new user get a first password, and how is a forgotten password reset? | Threat model; NFR N-5; REQ S-20, S-21 (answer added to the requirements by SCR S-3 as REQ S-30, S-31 and BR B-23) | The delivery manager sets a one-time temporary password for a new user and for a forgotten password; no forced change at first sign-in (lower-security option chosen knowingly) |
| Q9 | Does Applexus have an approved technology list or IT security policy? | Required input (standards, security policies) | No written approved technology list or IT security policy; the approved Phase 3 ADRs become the project's approved list |
| Q10 | How is availability monitored and who is alerted? | NFR N-1; topology | A free, open-source, self-hosted uptime checker on the test server checks once a minute and alerts on downtime |
| Q11 | How is client data kept separate? | NFR N-7; BR B-20; threat model | One PostgreSQL database; every client-owned row carries the client organization ID, enforced in one data-access layer plus PostgreSQL row-level security; tested with 2 client organizations (DEC-022, N-7) |
| Q12 | What ticket volume is expected? | Expected scale; topology; cost | Under 200 tickets per month |

## Deferred Items
<!-- guidance: Questions answered with 'defer' or 'don't know yet'; each links to an assumption (A-xxx) or open question (OQ-xxx) -->
None: no question was answered with "Defer".

Not asked; producer defaults stated as labeled assumptions for the approver to confirm at review:
| Item | From | Linked to |
| --- | --- | --- |
| Cost estimate in INR: new spend (expected 0), share of existing server capacity, staff and AI agent hours | Budget constraint (INT-001 Q10, Q16) | A-026 |
| Timestamps stored in UTC, displayed in IST; SLA business time on the IST calendar | BR-001 B-2 | A-027 |
| Password hashing with an OWASP-recommended adaptive algorithm (Argon2id or bcrypt), chosen in the stack ADR | NFR N-5 | A-028 |
| Excel, CSV and PDF generation with free, open-source libraries only, licence checked in the technology comparison | No new paid licences; REQ S-14, S-17 | A-029 |

Raised for the business owner, not asked in this interview: whether company code may stay on a personal github.com account (follow-up to Q5), logged as OQ-052. SCR S-3 (raised after this interview) added OQ-053 and OQ-054; both are Answered and folded into REQ-001 v0.3 S-31, S-30 and NFR-001 v0.3 N-5.

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-026 (Open): cost estimate in INR, recording new spend (expected 0), share of existing server capacity, and staff and AI agent hours.
- A-027 (Open): timestamps stored in UTC and displayed in IST; SLA business time computed on the IST calendar.
- A-028 (Open): password hashing with Argon2id or bcrypt (OWASP-recommended adaptive algorithm), chosen in the stack ADR.
- A-029 (Open): Excel, CSV and PDF generation with free, open-source libraries only, licence checked in the technology comparison.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
- OQ-052 (Mohanasunder, Business owner / BA; Open at interview time, since Answered by DEC-027: public repository, personal github.com account allowed for the pilot): is company source code allowed on a personal github.com account with GitHub-hosted CI? Logged in `docs/logs/open-questions-log.md`.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: SUM-002 v0.4; NFR-001 v0.3; BR-001 v0.3; REQ-001 v0.3; PRS-001 v0.3; GLO-001 v0.3; EPC-001 v0.3; BKL-001 v0.3; RSK-002 v0.1; SUM-001 v0.3; RSK-001 v0.2; `project.md`.
- Downstream: PIB-003, IRC-004; Phase 3 deliverables in `docs/03-architecture/`.

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions (SCR S-4 revisions NFR-001, REQ-001, BR-001, GLO-001, EPC-001, BKL-001, PRS-001 v0.3 and SUM-002 v0.4 Approved 2026-10-17)
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
