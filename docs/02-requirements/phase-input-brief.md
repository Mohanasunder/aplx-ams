---
id: PIB-002
title: Phase 2 input brief
phase: 2
version: 0.1
template: phase-input-brief
template_version: 2.0
status: Approved
author_agent: orchestrator
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# Phase 2 input brief

> **One file per phase.** Each phase produces exactly one `phase-input-brief.md` in its own folder. Use `--out docs/0N-<phase-slug>/phase-input-brief.md` when calling `new_artifact.py`; never let it auto-name as `PIB-NNN.md`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- SUM-001 v0.3 Phase 1 summary (`docs/01-discovery/SUMMARY.md`), Approved 2026-10-17 by Mohanasunder (Business owner / BA).
- Phase 1 artifacts indexed by SUM-001, all Approved 2026-10-17: BRF-001 v0.2, PER-001 v0.2, SCP-001 v0.2, RSK-001 v0.2, PRC-001 v0.2, PIB-001 v0.1, INT-001 v0.1, IRC-002 v0.1.
- INT-002 v0.1 Phase 2 interview (`docs/02-requirements/interview-record.md`): evidence record, approved with this brief; answers by Mohanasunder on 2026-10-17.
- `project.md`: approvers and capacity settings.
- `docs/logs/open-questions-log.md` (OQ-034 to OQ-036 answered by INT-002 Q15, Q16, Q14), `docs/logs/risk-register.md` (RSK R-4, R-6), `docs/logs/decision-log.md` (DEC-018, DEC-020, DEC-022).

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: the human-confirmed inputs for Phase 2 (Requirements) of APLX AMS: MVP priority, SLA calendar and clock rules, compliance measure, ticket intake, priority change, sign-in, setup ownership, availability and performance targets, data retention and backup, audit, notifications, reports, effort-to-contract mapping, escalation and hand-back rules, and the assumptions and open questions the producers carry.

Producers and outputs:
- `requirements-analyst`: `epics.md`, `user-stories.md`, `nfrs.md`, `business-rules.md`, `backlog.md`, `domain-glossary.md`, `product-requirement-specification.md` (required by `.ai/checker-rules/phase-2.md` non-overridable check; DEC-018), Phase 2 `SUMMARY.md`.
- `traceability`: seeds `docs/logs/traceability-matrix.md` with BRF goal, epic, and story links after the analyst finishes.

Does not cover: design choices (endpoints, tables, screens, technology) or discussion notes. Phase purpose: testable stories with Given/When/Then criteria, measurable NFRs, business rules, and the domain glossary. Not this: design choices.

## User Intent
<!-- guidance: The user's request in their words plus the phase goal -->
- In the user's words: "I want to build Application management services solution" (`docs/01-discovery/inputs/requirements.txt`); scoped in Phase 1 to an internal AMS delivery tool for SAP application support, with client log-in, for a pilot live by 2027-01-17 (SUM-001 v0.3 § Decisions).
- Phase 2 goal: turn SCP-001 v0.2 § In Scope IS-1 to IS-5 and BRF-001 v0.2 goals G-1 to G-4 into testable stories with Given/When/Then criteria, measurable NFRs, business rules, a prioritized backlog, a domain glossary, and the product requirement specification, ready for Phase 3.

## Required Inputs Status
<!-- guidance: Table: input, source (human/approved artifact/external), status, location -->
| # | Input | Source | Status | Location |
| --- | --- | --- | --- | --- |
| 1 | Approved discovery artifacts | Approved artifacts | Present | SUM-001 v0.3 and the artifacts it indexes |
| 2 | Answers to open questions | Human (Q14, Q15, Q16) | Present: OQ-034, OQ-035, OQ-036 answered | INT-002; `docs/logs/open-questions-log.md` |
| 3 | Stakeholder priorities | Human (Q1) | Present: IS-1 to IS-5 all Must | INT-002 Q1 |
| 4 | Existing system documentation | Approved artifacts | Not applicable: replaces mailbox and spreadsheet; no SOPs exist (OQ-004) | PRC-001 v0.2 |
| 5 | Compliance requirements | Human (Q7, Q10, Q11) | Present: none known (INT-001 Q11, Q15); sign-in, retention, backup and audit decided | INT-002 Q7, Q10, Q11 |
| 6 | Release or MVP expectations | Human (Q1) | Present: all of IS-1 to IS-5 for go-live 2027-01-17 | INT-002 Q1; SUM-001 v0.3 § Constraints Set |
| 7 | Reporting and integration needs | Human (Q12, Q13, Q14, Q5) | Present: SLA risk and breach alerts in-app, monthly client report, finance export; no integrations (SCP OS-3) | INT-002 Q5, Q12 to Q14, Q12a, Q14a |
| 8 | Named Phase 2 approver | `project.md` | Present: Mohanasunder (Product owner / BA) | `project.md` |

## Interview Answers
<!-- guidance: Question, answer, who answered, date; deferred items are marked as assumptions -->
All answers by Mohanasunder (Product owner / BA and all other approver roles), 2026-10-17, chat via Claude Code. Full record: INT-002 (including follow-ups Q4a, Q10a, and Q9a, Q12a, Q14a answered after the checker run). No item deferred.

| Q | Topic | Answer |
| --- | --- | --- |
| Q1 | MVP priority | IS-1 to IS-5 are all Must for the 2027-01-17 go-live |
| Q2 | Business calendar | 09:00 to 18:00 IST, Monday to Friday, India holiday list; one calendar for the pilot |
| Q3 | SLA clock | Starts when the ticket is raised; response clock stops at first L1 acknowledgement; resolution clock stops at Resolved; paused while awaiting client |
| Q4 | SLA compliance % | Response % and resolution % reported separately; BRF G-1 (80% to 95%) measures resolution % |
| Q5 | Ticket intake | Portal only: client users raise tickets in APLX AMS; the shared mailbox is retired |
| Q6 | Priority change | L1 may change priority with a reason; SLA targets recalculate from the raise time |
| Q7 | Sign-in | App accounts for staff and client users, with a password policy; no MFA (human security decision) |
| Q8 | Setup | The delivery manager (PER P-3) sets up client organizations, SAP applications, contracts and user accounts; no new persona |
| Q9 | Availability and performance | 99% availability within business hours; page p95 under 2 s for about 30 users |
| Q9a | Performance load | The p95 target is for 30 concurrent users (about 10 engineers and about 20 client users) |
| Q10 | Retention and backup | Keep data indefinitely; weekly backup; RPO 7 days; RTO 1 business day (human compliance decision) |
| Q11 | Audit | Log every change to status, priority, assignment and effort, with user and time; visible to internal users |
| Q12 | Notifications | SLA risk and breach alerts: in-app only (colour-coded SLA timers on the dashboard), no email |
| Q12a | SLA timer states | "At risk" at 90% of elapsed target time; "breached" at 100% (business rule; colour and layout are Phase 4) |
| Q13 | Reports | Monthly per-client report (compliance % per priority, breaches listed, MTTR, ticket counts) that client users view in the tool and download as Excel or PDF; internal live dashboard |
| Q14 | Effort to contract (OQ-036) | One active contract per client organization; all its hours count against it. Finance export fields: client, contract, ticket, engineer, date, hours, remaining hours-bank balance |
| Q14a | Fixed-fee contracts | Hours recorded for visibility only, not counted against a balance; finance export shows hours with the balance column blank |
| Q15 | L1 target (OQ-034) | L1's own target is 50% of the resolution target, then the ticket is flagged for escalation; triage happens in APLX AMS |
| Q16 | Hand-back (OQ-035) | L2/L3 sets Resolved; the ticket returns to L1's queue for closure (L1 closes, per OQ-028) |

## Referenced Artifact Versions
<!-- guidance: Exact IDs and versions of approved upstream artifacts -->
- SUM-001 v0.3 § Decisions, § Constraints Set, § Open Items, § What The Next Phase Needs.
- BRF-001 v0.2 § Business Goals And KPIs (G-1 to G-4).
- SCP-001 v0.2 § In Scope (IS-1 to IS-5), § Out Of Scope (OS-1 to OS-4).
- PER-001 v0.2 § Persona P-1 to P-4 (Key Journeys).
- PRC-001 v0.2 § Process M-1 to M-3 (Pain Points).
- RSK-001 v0.2 § Risk R-4, § Risk R-6.
- PIB-001 v0.1, INT-001 v0.1, IRC-002 v0.1 (Phase 1 entry interview evidence).

## Constraints
<!-- guidance: Technology, compliance, budget, timeline, capacity -->
- Timeline: go-live with the pilot client by 2027-01-17; all of IS-1 to IS-5 are Must (Q1).
- Budget: existing staff and AI agents only; existing on-prem servers; no new paid licences (SUM-001 v0.3 § Constraints Set).
- Scope: SAP applications only; desktop web browser only; no billing or invoicing; no ITSM integration (SCP-001 v0.2 OS-1 to OS-4). Intake is portal only, no mailbox ingestion (Q5).
- Data boundary: client users see only their own organization's data (IS-5). Per RSK R-6 and DEC-022, the business rules and acceptance criteria must cover at least two client organizations, even though the pilot has one (Applexus).
- SLA: standard SLA (P1 1 h / 4 h, P2 4 h / 1 day, P3 1 day / 3 days, P4 2 days / 5 days) on the Q2 calendar, with the Q3 clock rules and Q6 recalculation.
- Measurement: RSK R-4 mitigation (compliance formula) is answered by Q4: response % and resolution % separately; BRF G-1 uses resolution %. The analyst states the formula and how it compares with the month-end manual count.
- Effort: hours-bank contracts draw down a balance; fixed-fee contracts record hours for visibility only, with the export balance column blank (Q14, Q14a).
- SLA timer states: "at risk" at 90% of elapsed target time, "breached" at 100% (Q12a). SLA risk and breach alerts are in-app only, no email (Q12). The to-be channel for the finance export and for closure messages to the client is not decided: the requirements-analyst raises open questions for both.
- NFR targets: 99% availability within business hours; page p95 under 2 s for 30 concurrent users, about 10 engineers and about 20 client users (Q9, Q9a); RPO 7 days, RTO 1 business day, indefinite retention (Q10); audit of status, priority, assignment and effort changes (Q11).
- Human decisions to respect, not override: Q7 (no MFA) and Q10 (weekly backup, RPO 7 days). The requirements-analyst records them as stated, and records the candidate risks (no MFA on the external-facing client log-in once external clients join; up to 7 days of ticket and effort data lost on a restore, RPO 7 days) as RSK entries in `docs/02-requirements/risks.md` plus rows in `docs/logs/risk-register.md`, each with a named owner.
- Capacity (`project.md`): 4 acceptance criteria per feature at most; 3 parallel builder agents; 6 PR reviews per week; one approver, no backup (DEC-020).
- Requirements only: no endpoints, tables, screens or technology in Phase 2 outputs.

Producer pointers:
- Glossary path: CLAUDE.md names `docs/02-requirements/GLO-001.md`, while the domain-glossary template requires `docs/02-requirements/domain-glossary.md`. Use the template path; CLAUDE.md is human-owned, so the discrepancy is reported to the human, not edited.
- Downstream citations use `REQ S-N AC-n`.
- Glossary candidates from the answers: ticket, incident, service request, priority, response time, resolution time, acknowledgement, Resolved, Closed, awaiting client, business hours, SLA breach, escalation flag, contract, hours bank, fixed fee, client organization, SAP application.

## Readiness Verdict
<!-- guidance: Ready | Ready with assumptions | Not ready, with the reason -->
Ready. All blocker questions are answered by the human (Q1 to Q16); no item was deferred. OQ-034, OQ-035 and OQ-036 are answered. One producer default (browser support) is stated as a labeled assumption, A-008, which does not block the producers.

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-008 (Open): supported browsers are the current and previous major versions of Google Chrome and Microsoft Edge on desktop (not asked in the interview; producer default; SCP OS-4 limits release 1 to desktop web browser).
- A-001 to A-005 and A-007 Confirmed, A-006 Rejected (Phase 1; SUM-001 v0.3 § Assumptions).

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
Logged in `docs/logs/open-questions-log.md`.
- Answered 2026-10-17 in this interview: OQ-034 (Q15), OQ-035 (Q16), OQ-036 (Q14).
- Open: none. OQ-001 to OQ-036 are all answered.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: SUM-001 v0.3; BRF-001 v0.2; PER-001 v0.2; SCP-001 v0.2; RSK-001 v0.2; PRC-001 v0.2; PIB-001 v0.1; INT-001 v0.1; IRC-002 v0.1; INT-002; `project.md`.
- Downstream: IRC-003 (Phase 2 readiness); `docs/02-requirements/epics.md`, `user-stories.md`, `nfrs.md`, `business-rules.md`, `backlog.md`, `domain-glossary.md`, `product-requirement-specification.md`, Phase 2 `SUMMARY.md`; `docs/logs/traceability-matrix.md`.

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions (except INT-002, the evidence record approved with this brief)
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
| Role | Product owner / BA |
| Version | 0.1 |
| Conditions | None |
| Comments | Run-1 Minor findings F-1 to F-6 fixed; follow-ups Q9a, Q12a, Q14a answered. |
| Timestamp | 2026-10-17 07:01 UTC |
