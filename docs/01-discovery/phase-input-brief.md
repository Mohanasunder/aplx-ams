---
id: PIB-001
title: Phase 1 input brief
phase: 1
version: 0.1
template: phase-input-brief
template_version: 2.0
status: Approved
author_agent: orchestrator
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# Phase 1 input brief

> **One file per phase.** Each phase produces exactly one `phase-input-brief.md` in its own folder. Use `--out docs/0N-<phase-slug>/phase-input-brief.md` when calling `new_artifact.py`; never let it auto-name as `PIB-NNN.md`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- IRC-001 v0.1 "Phase 1 readiness" (`docs/00-setup/input-readiness-checklist.md`), Approved 2026-10-17 by Mohanasunder (Tech lead).
- `project.md`: project details, approvers, capacity settings; Phase 0 Approved 2026-10-17 by Mohanasunder.
- INT-001 v0.1 Phase 1 interview (`docs/01-discovery/interview-record.md`), answers by Mohanasunder on 2026-10-17.
- Raw input `docs/01-discovery/inputs/requirements.txt`: "I want to build Application management services solution".
- No Phase 0 `SUMMARY.md` exists; `project.md` serves for Phase 0.

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: the human-confirmed inputs for Phase 1 (Business discovery) of APLX AMS: problem, users, release 1 capabilities, out-of-scope item, KPIs, constraints, stakeholder groups, and the open questions and assumptions the producers carry.

Producers and outputs:
- `discovery-analyst`: `business-brief.md`, `personas.md`, `scope-statement.md`, `risks.md`, Phase 1 `SUMMARY.md`.
- `process-mapper`: `process-maps.md`.
- `research-analyst`: not invoked (interview Q13: "No"); no `research-summary.md`.

Does not cover: requirements, acceptance criteria, design, or technology choices. Phase purpose: agree the problem, users, goals with KPIs, scope and out-of-scope, and risks. Not this: open-ended research or proposing solutions.

## User Intent
<!-- guidance: The user's request in their words plus the phase goal -->
- In the user's words: "I want to build Application management services solution" (`requirements.txt`); `project.md`: "An Application Management Services Solution".
- Clarified 2026-10-17: an internal delivery tool used by the company's own AMS team to run support for its clients (Q1). Client users also log in in release 1 to raise tickets and view their SLA reports, limited to their own organization's data (Q3, Q14). The supported landscape is SAP applications only (Q4, Q17).
- Problems to solve (Q2): (1) SLA breaches and poor visibility: missed response or resolution targets are found too late; (2) manual effort: tickets, effort and reports tracked in email and spreadsheets; (3) fragmented tools: no single view across clients and applications.
- Phase goal: commit the problem, users, goals with KPIs, release 1 scope and out-of-scope, and risks, ready for Phase 2.

## Required Inputs Status
<!-- guidance: Table: input, source (human/approved artifact/external), status, location -->
| # | Input | Source | Status | Location |
| --- | --- | --- | --- | --- |
| 1 | Problem or opportunity statement | Human (Q1 to Q4) | Present | INT-001 Q1 to Q4 |
| 2 | Stakeholder interviews, transcripts, workshop notes | Human | Partial: this interview only; stakeholder groups known, names missing | INT-001; OQ-006 |
| 3 | Existing documents: SOPs, proposals, RFPs, client SLA terms | Human | Missing | `docs/01-discovery/inputs/`; OQ-004 |
| 4 | Current systems and tools | Human (Q6) | Present: email and spreadsheets | INT-001 Q6; OQ-010 |
| 5 | Business goals, KPIs, budget, timeline | Human (Q7, Q9, Q10, Q16) | Partial: KPIs named without baseline or target | INT-001; OQ-001, OQ-013, A-001 |
| 6 | Regulatory and policy constraints | Human (Q11, Q15) | Present: none known; personal data limited to client contact names and emails | INT-001 Q11, Q15 |
| 7 | Market or competitor information | Human (Q13) | Not applicable: research not requested | INT-001 Q13 |
| 8 | Named Phase 1 approver | `project.md` | Present: Mohanasunder (Business owner / BA) | `project.md` |

## Interview Answers
<!-- guidance: Question, answer, who answered, date; deferred items are marked as assumptions -->
All answers by Mohanasunder (Business owner / BA and all other approver roles), 2026-10-17, chat via Claude Code. Full record: INT-001.

| Q | Topic | Answer |
| --- | --- | --- |
| Q1 | Product type | Internal delivery tool, used by our own AMS team to run support for our clients |
| Q2 | Main problems | SLA breaches and poor visibility; manual effort (email and spreadsheets); fragmented tools |
| Q3 | Primary users | Support engineers (L1/L2/L3), delivery managers, client users; clients log in in release 1 |
| Q4 | Landscape | SAP applications |
| Q5 | Release 1 capabilities | Incident and service-request management with SLA timers; SLA and service reporting and dashboards per client; effort and time tracking against contracts, for billing |
| Q6 | Tools today | Email and spreadsheets |
| Q7 | KPIs | SLA compliance %; MTTR reduced; manual admin and reporting hours per month reduced (no baselines or targets: OQ-001) |
| Q8 | Out of scope, release 1 | Billing and invoicing (effort data export only) |
| Q9 | Timeline | First usable release within 3 months (A-001) |
| Q10 | Budget | Existing staff and AI agents only, no extra spend |
| Q11 | Compliance | None known |
| Q12 | Stakeholders | Leadership / sponsor; delivery and practice heads; pilot client(s) (names: OQ-006) |
| Q13 | Research-analyst | No |
| Q14 | Client data visibility | Each client user sees only their own organization's tickets and SLA reports |
| Q15 | Personal data | Only client contact names and emails; no specific data-protection obligations known |
| Q16 | Meaning of "no extra spend" | Hosting must use existing infrastructure; no new paid licences |
| Q17 | SAP only | Release 1 is SAP applications only |

## Referenced Artifact Versions
<!-- guidance: Exact IDs and versions of approved upstream artifacts -->
- IRC-001 v0.1 (Approved) § Required Inputs Checklist.
- `project.md` § Approvers, § Capacity and settings, § Phase status (not versioned; Phase 0 Approved 2026-10-17).

## Constraints
<!-- guidance: Technology, compliance, budget, timeline, capacity -->
- Timeline: first usable release within 3 months (Q9); start assumed 2026-10-17 (A-001).
- Budget: existing staff and AI agents only; hosting on existing infrastructure; no new paid licences (Q10, Q16).
- Capacity (`project.md`): 3 parallel builder agents; 6 PRs reviewed per week; 3 open feature branches; 1-business-day approval SLA.
- Approval: one named human (Mohanasunder) holds every approver role, no backup (OQ-014).
- Compliance: none known (Q11). Personal data limited to client contact names and emails (Q15). Client users see only their own organization's data (Q14).
- Landscape: SAP applications only (Q4, Q17).
- Technology: none stated; not decided in Phase 1.
- Out of scope, release 1: billing and invoicing; effort data export only (Q8).

## Readiness Verdict
<!-- guidance: Ready | Ready with assumptions | Not ready, with the reason -->
Ready with assumptions. No Blocker gaps: problem, users, release 1 capabilities, out-of-scope item, KPI names, timeline, budget, compliance position, client data boundary, and stakeholder groups are confirmed by the human.

Conditions:
1. High open questions OQ-001, OQ-004, OQ-005 must be answered or accepted by the Business owner / BA before the Phase 1 gate.
2. Until OQ-004 and OQ-005 are answered, `process-maps.md` rests on interview answers only and must say so.

Candidate risks for `risks.md` (the analyst rates them): single approver with no backup (`project.md`); 3-month timeline for three capabilities plus client log-in with existing staff and AI agents only (Q5, Q9, Q10); hosting limited to existing infrastructure (Q16); KPIs not measurable without baselines (OQ-001); missing SOPs and SLA terms leave SLA rules and the as-is process incomplete (OQ-004, OQ-005).

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-001 (Open): the 3-month window starts 2026-10-17, giving a target of about 2027-01-17 (OQ-013).
- A-002 (Confirmed 2026-10-17, Q14): client users see and act only on their own organization's tickets and SLA reports.
- A-003 (Confirmed 2026-10-17, Q17): release 1 covers SAP applications only.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
Logged in `docs/logs/open-questions-log.md`.
- Open, High: OQ-001 (KPI baselines and targets), OQ-004 (SOPs, client SLA terms, sample spreadsheets), OQ-005 (as-is ticket flow and monthly reporting).
- Open, Medium: OQ-006 (stakeholder names), OQ-007 (release 1 scale), OQ-008 (effort export and contract types), OQ-010 (ITSM replacement or integration), OQ-013 (start date and meaning of "first usable release"), OQ-014 (backup approver).
- Open, Low: OQ-011 (mobile access).
- Answered 2026-10-17: OQ-002 (Q15), OQ-003 (Q14), OQ-009 (Q16), OQ-012 (Q17).

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: IRC-001 v0.1; `project.md`; INT-001.
- Downstream: IRC-002 (Phase 1 readiness); `docs/01-discovery/business-brief.md`, `personas.md`, `scope-statement.md`, `process-maps.md`, `risks.md`, Phase 1 `SUMMARY.md`; RSK rows in `docs/logs/risk-register.md`.

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
| Role | Business owner / BA |
| Version | 0.1 |
| Conditions | None |
| Comments | Minor findings F-01 to F-04 (phase-1-run-1) accepted. |
| Timestamp | 2026-10-17 04:55 UTC |
