---
id: INT-002
title: Phase 2 interview
phase: 2
version: 0.1
template: interview-record
template_version: 2.0
status: Approved
author_agent: orchestrator
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# Phase 2 interview

> **One file per phase.** Each phase produces exactly one `interview-record.md` in its own folder. Use `--out docs/0N-<phase-slug>/interview-record.md` when calling `new_artifact.py`; never let it auto-name as `INT-NNN.md`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- SUM-001 v0.3 (Approved 2026-10-17) and the artifacts it indexes: BRF-001 v0.2, PER-001 v0.2, SCP-001 v0.2, RSK-001 v0.2, PRC-001 v0.2 (Approved 2026-10-17); PIB-001 v0.1, INT-001 v0.1, IRC-002 v0.1 (Approved 2026-10-17).
- `docs/logs/open-questions-log.md` OQ-034 to OQ-036 (Open before this interview).
- `project.md` (approvers, capacity).

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: the Phase 2 entry interview for APLX AMS. Questions were prepared by `phase-intake` from the gaps between the Phase 2 required inputs (`docs/02-requirements/README.md`), the templates, and SUM-001 v0.3, and asked by the Orchestrator in chat via Claude Code on 2026-10-17. Q4 and Q10 each had one follow-up in the interview; Q9a, Q12a and Q14a were answered in chat on 2026-10-17 after the checker run (findings F-6, F-3, F-2). This record is the evidence source the requirements-analyst cites for SLA rules, NFR targets, reports and roles not settled in Phase 1.

Does not cover: epics, stories, acceptance criteria, NFRs, business rules, or design choices.

## Questions And Answers
<!-- guidance: Table: ID, question, why it matters (template section affected), answer, answered by, date -->
All answered by Mohanasunder (Product owner / BA and all other approver roles), 2026-10-17.

| ID | Question | Why it matters | Answer |
| --- | --- | --- | --- |
| Q1 | Which of IS-1 to IS-5 are Must for the 2027-01-17 go-live? | Backlog priority; PRS feature MoSCoW | All of IS-1 to IS-5 are Must |
| Q2 | Which business calendar drives the SLA clock? | Business rules (SLA timers); NFRs | 09:00 to 18:00 IST, Monday to Friday, India holiday list; one calendar for the pilot |
| Q3 | When does each SLA clock start, stop and pause? | Business rules; IS-1 acceptance criteria | Starts when the ticket is raised; response clock stops at first L1 acknowledgement; resolution clock stops at Resolved; paused while awaiting client |
| Q4 | How is SLA compliance % calculated? | BRF G-1 measure; IS-2 reports; RSK R-4 mitigation | Response % and resolution % reported separately |
| Q4a | Follow-up: which of the two does goal G-1 (80% to 95%) measure? | BRF G-1 traceability; PRS goal metric | Resolution %; response % is reported but is not the goal |
| Q5 | How do client users raise tickets? | IS-1 and IS-4 stories; integration needs | Portal only: client users raise tickets in APLX AMS; the shared mailbox is retired |
| Q6 | Can priority change after raise, and what happens to the SLA targets? | Business rules; IS-1 acceptance criteria | L1 may change priority with a reason; targets recalculate from the raise time |
| Q7 | How do staff and client users sign in? | Security NFRs; IS-4 stories | App accounts for everyone (staff and client users), with a password policy; no MFA (security decision by the human) |
| Q8 | Who sets up client organizations, SAP applications, contracts and user accounts? | Stories and personas for setup | The delivery manager (PER P-3); no new persona |
| Q9 | What availability and performance targets apply? | NFRs | 99% availability within business hours; page p95 under 2 s for about 30 users |
| Q9a | Follow-up: is the p95 target for 30 concurrent users? | NFRs (performance load) | Yes: 30 concurrent users (about 10 engineers and about 20 client users) |
| Q10 | How long is data kept, and how is it backed up? | NFRs (retention, backup) | Keep data indefinitely; weekly backup (compliance decision by the human) |
| Q10a | Follow-up: what RPO and RTO apply? | NFRs (recovery) | RPO 7 days; RTO 1 business day |
| Q11 | What must the audit trail record, and who sees it? | Business rules; NFRs | Every change to status, priority, assignment and effort, with user and time; visible to internal users |
| Q12 | How are users told about SLA risk and breaches? | IS-1 and IS-2 stories | In-app only: colour-coded SLA timers on the dashboard; no email |
| Q12a | Follow-up: when does a ticket show as "at risk" and as "breached"? | Business rules (SLA timers) | "At risk" at 90% of elapsed target time; "breached" at 100%. Colour and layout are Phase 4 design |
| Q13 | What reports do clients and internal users need? | IS-2 stories; BRF G-3, G-4 | Monthly per-client report (compliance % per priority, breaches listed, MTTR, ticket counts) that client users view in the tool and download as Excel or PDF; internal live dashboard |
| Q14 | How are per-ticket hours mapped to a contract, and what does the finance export hold? (OQ-036) | IS-3 stories; business rules | Each client organization has one active contract; all its hours count against it. Export fields: client, contract, ticket, engineer, date, hours, remaining hours-bank balance |
| Q14a | Follow-up: how are hours handled on fixed-fee contracts? | IS-3 business rules; finance export | Hours are recorded for visibility only and do not count against a balance; the finance export shows the hours with the balance column blank |
| Q15 | What is L1's own target before escalation, and where does L1 triage? (OQ-034) | IS-1 business rules; PER P-1 journey | 50% of the resolution target, after which the ticket is flagged for escalation; triage happens in APLX AMS (to-be) |
| Q16 | How does L2/L3 hand a resolved ticket back to L1? (OQ-035) | IS-1 stories; PER P-2 journey | L2/L3 sets status Resolved; the ticket returns to L1's queue for closure (keeps the OQ-028 rule that L1 closes) |

## Deferred Items
<!-- guidance: Questions answered with 'defer' or 'don't know yet'; each links to an assumption (A-xxx) or open question (OQ-xxx) -->
None: no question was answered with "Defer".

Not asked; producer default stated as a labeled assumption:
| Item | From | Linked to |
| --- | --- | --- |
| Supported browsers: current and previous major versions of Chrome and Edge on desktop | SCP OS-4 (desktop web browser only) | A-008 |

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-008 (Open): supported browsers are the current and previous major versions of Google Chrome and Microsoft Edge on desktop.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
OQ-034 (Q15), OQ-035 (Q16) and OQ-036 (Q14) answered 2026-10-17 in `docs/logs/open-questions-log.md`. No new open questions.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: SUM-001 v0.3; BRF-001 v0.2; PER-001 v0.2; SCP-001 v0.2; RSK-001 v0.2; PRC-001 v0.2; `project.md`.
- Downstream: PIB-002, IRC-003; Phase 2 deliverables in `docs/02-requirements/`.

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
| Role | Product owner / BA |
| Version | 0.1 |
| Conditions | None |
| Comments | Run-1 Minor findings F-1 to F-6 fixed; follow-ups Q9a, Q12a, Q14a answered. |
| Timestamp | 2026-10-17 07:01 UTC |
