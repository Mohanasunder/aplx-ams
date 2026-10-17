---
id: IRC-004
title: Phase 3 readiness
phase: 3
version: 0.2
template: input-readiness-checklist
template_version: 2.0
status: Approved
author_agent: orchestrator
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# Phase 3 readiness

> **One file per phase.** Each phase produces exactly one `input-readiness-checklist.md` in its own folder. Use `--out docs/0N-<phase-slug>/input-readiness-checklist.md` when calling `new_artifact.py`; never let it auto-name the file as `IRC-NNN.md`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- Citations updated under SCR S-4 (2026-10-17).
- SUM-002 v0.4 and the artifacts it indexes: RSK-002 v0.1 (Approved 2026-10-17, unchanged by SCR S-3 and SCR S-4); NFR-001 v0.3, REQ-001 v0.3, BR-001 v0.3, GLO-001 v0.3, EPC-001 v0.3, BKL-001 v0.3, PRS-001 v0.3 (revised by SCR S-3 (Approved) and SCR S-4 (`docs/logs/spec-changes.md`, Approved 2026-10-17)).
- SUM-001 v0.3 and RSK-001 v0.2 (Approved 2026-10-17).
- INT-003 v0.2 Phase 3 interview, 2026-10-17: evidence record, approved with the brief (PIB-003).
- `project.md` (approvers, capacity).

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: the status of each Phase 3 required input (`docs/03-architecture/README.md`) after the entry interview, and the readiness verdict for starting the Phase 3 producers (`solution-architect`, then `security-architect` and `infra-cost-analyst`).

Does not cover: the content of the architecture deliverables.

## Required Inputs Checklist
<!-- guidance: One row per required input: present / partial / missing, source, notes -->
| # | Required input | Status | Source | Notes |
| --- | --- | --- | --- | --- |
| 1 | Approved requirements (especially NFRs and integrations) | Present | SUM-002 v0.4; RSK-002 v0.1; NFR-001, REQ-001, BR-001, GLO-001, EPC-001, BKL-001, PRS-001 v0.3 | RSK-002 Approved 2026-10-17; SCR S-3 and SCR S-4 Approved 2026-10-17 (v0.3 revisions, SUM-002 v0.4); NFR N-1 to N-9 |
| 2 | Enterprise architecture standards and approved technology list | Present | INT-003 Q9 | None exists; the approved Phase 3 ADRs become the project's approved list |
| 3 | Team skills and preferred stack | Present | INT-003 Q4 | Python backend (Django or FastAPI), React TypeScript frontend |
| 4 | Hosting and cloud constraints | Present | INT-003 Q1, Q2, Q6; OQ-021 | Existing on-prem Linux VMs, containers allowed; 2 servers (production, test); Applexus network or VPN only, HTTPS with internal CA |
| 5 | Documentation of systems to integrate with | Not applicable | SCP-001 v0.2 OS-3; INT-002 Q5, Q12; OQ-038 | No integrations in release 1 |
| 6 | Security policies | Present | NFR-001 v0.3 N-5; INT-003 Q6, Q8, Q9; SCR S-3, S-4 | Password policy N-5; no company IT security policy (Q9); HTTPS, not internet-facing (Q6); Q8 temporary passwords now in the requirements via SCR S-3 (Approved): REQ-001 v0.3 S-30 (delivery manager sets or resets a temporary password, which clears a lockout at once; OQ-054 Answered) and S-31 (any signed-in user changes their own password after entering the current one; OQ-053 Answered), BR-001 v0.3 B-21, B-23, NFR-001 v0.3 N-5; no forced change. Producers design password handling only per REQ-001 v0.3 S-20, S-21, S-30, S-31 and BR-001 v0.3 B-21, B-23. SCR S-4 Approved 2026-10-17 |
| 7 | Budget limits | Present | INT-001 Q10, Q16; INT-003 Q5 | No new paid licences; existing staff and AI agents; Q5: "Keep the github.com repository and GitHub-hosted CI; a human deploys a built package to on-prem manually" |
| 8 | Expected scale: users, data volume, traffic | Present | INT-003 Q12; OQ-007, OQ-033; INT-002 Q9a | About 10 engineers and 20 client users, 30 concurrent, 1 pilot organization; under 200 tickets per month |
| 9 | Named Phase 3 approver | Present | `project.md` | Mohanasunder (Architect / tech lead); no backup (DEC-020) |
| 10 | Phase 2 approved | Present | SUM-002 previous version, approved 2026-10-17 (approval log); SUM-002 v0.4 Approved with SCR S-4 | - |

Verdict: Ready. Producers started under v0.1 (after SCR S-3 approval); v0.2 updates citations to the SCR S-4 versions (NFR-001, REQ-001, BR-001, GLO-001, EPC-001, BKL-001, PRS-001 v0.3; SUM-002 v0.4), now Approved. No Blocker or open High question. Four producer defaults logged as assumptions A-026 to A-029; OQ-052 (personal github.com account) Answered (DEC-027).

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-026 (Open): cost estimate in INR (new spend, expected 0; share of existing server capacity; staff and AI agent hours).
- A-027 (Open): timestamps stored in UTC, displayed in IST; SLA business time on the IST calendar.
- A-028 (Open): password hashing with Argon2id or bcrypt, chosen in the stack ADR.
- A-029 (Open): Excel, CSV and PDF generation with free, open-source libraries only, licence checked.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
Open: none. OQ-052 (Answered, DEC-027): company code may stay on the personal github.com account (`github.com/Mohanasunder/aplx-ams`) for the pilot; the repository is public. OQ-001 to OQ-051 Answered; OQ-053 and OQ-054 (raised by SCR S-3) Answered and folded into REQ-001 v0.3 S-31, S-30 and NFR-001 v0.3 N-5. All in `docs/logs/open-questions-log.md`.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: SUM-002 v0.4; NFR-001 v0.3; REQ-001 v0.3; BR-001 v0.3; SUM-001 v0.3; INT-003; `project.md`.
- Downstream: PIB-003; Phase 3 deliverables in `docs/03-architecture/`.

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions (all cited versions Approved; INT-003 is the evidence record approved with the brief)
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
