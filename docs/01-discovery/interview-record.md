---
id: INT-001
title: Phase 1 interview
phase: 1
version: 0.1
template: interview-record
template_version: 2.0
status: Approved
author_agent: orchestrator
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# Phase 1 interview

> **One file per phase.** Each phase produces exactly one `interview-record.md` in its own folder. Use `--out docs/0N-<phase-slug>/interview-record.md` when calling `new_artifact.py`; never let it auto-name as `INT-NNN.md`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- IRC-001 v0.1 (Approved 2026-10-17).
- `project.md` (Phase 0 Approved 2026-10-17).
- `docs/01-discovery/inputs/requirements.txt`.

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: the Phase 1 entry interview for APLX AMS. Questions were prepared by `phase-intake` and asked by the Orchestrator in chat via Claude Code on 2026-10-17, in two rounds (round 1: Q1 to Q13 and a clarification of Q3; round 2: Q14 to Q17 on items needing a human decision). This record is the evidence source producers cite, since no other stakeholder documents exist.

Does not cover: discovery deliverables, requirements, or design.

## Questions And Answers
<!-- guidance: Table: ID, question, why it matters (template section affected), answer, answered by, date -->
All answered by Mohanasunder (Business owner / BA), 2026-10-17.

| ID | Question | Why it matters | Answer |
| --- | --- | --- | --- |
| Q1 | What kind of product is APLX AMS? (internal delivery tool / client-facing portal / commercial product) | Business brief § problem; personas; scope | Internal delivery tool: used by our own AMS team to run support for our clients |
| Q2 | What is the main problem it must fix today? | Business brief § problem; process maps § pain points | All three: SLA breaches / visibility (missed response or resolution targets, found too late); manual effort (tickets, effort and reports in email or spreadsheets); fragmented tools (no single view across clients and applications) |
| Q3 | Who are the primary users? | Personas; scope; stakeholders | Support engineers (L1/L2/L3), delivery managers, client users (and "Defer" also selected) |
| Q3a | Clarification: do client users log in to this internal tool in release 1? | Personas; scope; risks | "Yes, clients log in": clients raise tickets and view their SLA reports in release 1 |
| Q4 | Which application landscape does the service support? | Scope § in scope, dependencies | SAP applications |
| Q5 | Which capabilities must the first release include? | Scope § in scope; process map selection | Incident and service-request management with SLA timers; SLA and service reporting / dashboards per client; effort / time tracking against contracts, for billing |
| Q6 | What tools do you use today for this work? | Process maps (as-is); scope § dependencies | Email and spreadsheets |
| Q7 | How should success be measured? | Business brief § goals and KPIs | SLA compliance %; MTTR reduced; manual admin / reporting hours per month reduced |
| Q8 | What is explicitly out of scope for the first release? | Scope § out of scope | Billing / invoicing (effort data export only). "Replacing existing ITSM" and "Mobile apps" were offered and not selected |
| Q9 | Target timeline for a first usable release? | Business brief § constraints; risks | Within 3 months |
| Q10 | Budget or team constraint? | Business brief § constraints; risks | Existing staff + AI agents only, no extra spend |
| Q11 | Which regulatory or data-protection rules apply? | Business brief § constraints; risks | None known |
| Q12 | Who else has a stake or a say? | Business brief § stakeholders | Leadership / sponsor; delivery / practice heads; pilot client(s) |
| Q13 | Do you want market or competitor research (research-analyst)? | Whether `research-summary.md` is produced | No |
| Q14 | Is each client user limited to their own organization's tickets and SLA reports? | Personas; scope; security posture | Yes, own organization only |
| Q15 | Do tickets or client user accounts hold personal data that triggers data-protection obligations? | Business brief § constraints; risks | Only names and emails; no specific obligations |
| Q16 | Does "no extra spend" exclude hosting and paid licences? | Business brief § constraints; risks | Use existing infrastructure; no new licences |
| Q17 | Is release 1 SAP applications only? | Scope § in scope | SAP only |

## Deferred Items
<!-- guidance: Questions answered with 'defer' or 'don't know yet'; each links to an assumption (A-xxx) or open question (OQ-xxx) -->
| Item | From | Linked to |
| --- | --- | --- |
| KPI baselines and targets not given | Q7 | OQ-001 |
| Existing SOPs, client SLA terms, sample spreadsheets and reports not supplied | IRC-001 row 3 | OQ-004 |
| As-is ticket flow and monthly reporting steps not described | Q2, Q6 | OQ-005 |
| Stakeholder names not given | Q12 | OQ-006 |
| Release 1 scale (clients, applications, users) not given | Q3, Q5 | OQ-007 |
| Effort export recipient, format, and contract types | Q5, Q8 | OQ-008 |
| ITSM replacement or integration not selected either way | Q8 | OQ-010 |
| Mobile access not selected either way | Q8 | OQ-011 |
| Start date and meaning of "first usable release" | Q9 | OQ-013, A-001 |
| No backup approver | `project.md` | OQ-014 |

Resolved in round 2: OQ-002 (Q15), OQ-003 and A-002 (Q14), OQ-009 (Q16), OQ-012 and A-003 (Q17).

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-001 (Open): 3-month window starts 2026-10-17.
- A-002 (Confirmed, Q14): client users see only their own organization's data.
- A-003 (Confirmed, Q17): release 1 is SAP applications only.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
OQ-001 to OQ-014 in `docs/logs/open-questions-log.md`; OQ-002, OQ-003, OQ-009, OQ-012 answered 2026-10-17.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: IRC-001 v0.1; `project.md`.
- Downstream: PIB-001, IRC-002; Phase 1 deliverables in `docs/01-discovery/`.

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
