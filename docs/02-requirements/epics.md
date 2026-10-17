---
id: EPC-001
title: APLX AMS: Epics
phase: 2
version: 0.3
template: epic
template_version: 2.0
status: Approved
author_agent: requirements-analyst
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# APLX AMS: Epics

> **Collection file.** All epics for this project live in this one file. Add one `## Epic E-N` section per epic; never create a separate EPC-NNN file for an additional epic. Downstream artifacts reference a specific epic as `EPC E-N` (e.g. `EPC E-3`).

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- PIB-002 v0.1 § Interview Answers, § Constraints.
- INT-002 v0.1 § Questions And Answers (evidence record).
- SUM-001 v0.3 § Decisions.
- BRF-001 v0.2 § Business Goals And KPIs (G-1 to G-4).
- SCP-001 v0.2 § In Scope (IS-1 to IS-5).
- PER-001 v0.2 § Persona P-1 to P-4; PRC-001 v0.2 § Process M-1 to M-3 (Pain Points).
- SCR S-3 (`docs/logs/spec-changes.md`): password set, reset and change (REQ S-30, S-31 in E-5), decided by Mohanasunder (Product owner / BA), chat, 2026-10-17.
- SCR S-4 (`docs/logs/spec-changes.md`): security events in the audit trail (REQ S-32, S-33 in E-5), OQ-062 answered by Mohanasunder (Product owner / BA), chat, 2026-10-17.

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: the five epics of APLX AMS release 1, each citing the brief goals it serves and listing its stories (REQ S-N in REQ-001). All epics are Must for the 2027-01-17 go-live (INT-002 Q1).

Goal citation format: goals are cited as `BRF-001 G-n`, not `BRF G-n`. Checked on 2026-10-17: `scripts/traceability.py` keys the brief's goals by its front-matter ID (`BRF-001 G-1` to `BRF-001 G-4`), so a `BRF G-n` citation is reported as "not a goal of an Approved brief" and the goals as uncovered. The same format is used in PRS-001, REQ-001 and the traceability matrix. Aligning the standard (`BRF G-N`) and the script is a human change to `scripts/` or the ID standard.

Goal coverage: G-1 by E-1, E-2, E-3; G-2 by E-1, E-2; G-3 by E-1, E-3, E-4, E-5; G-4 by E-3, E-4, E-5. No goal is left uncovered. Each epic cites every goal that one of its stories cites in its Priority line (REQ-001 § Traceability Links, goal-link rule).

Does not cover: story detail (REQ-001), rules (BR-001), NFRs (NFR-001), or design.

---

## Epic E-1: Ticket intake and handling

### Description
Client users raise incidents and service requests in APLX AMS; L1 support engineers acknowledge, triage, change priority, escalate and close; the assigned support engineer (L1 or L2/L3) marks awaiting client; client users add comments on their organization's tickets, which clears awaiting client, and internal users add comments visible to the client user (OQ-045, OQ-051, DEC-026); L2/L3 support engineers resolve and hand back to the L1 queue. Covers SCP IS-1 (ticket management) and IS-4 (raise tickets, comments). Replaces the shared mailbox and spreadsheet (PRC M-1).

### Business Value
BRF-001 G-1
BRF-001 G-2
BRF-001 G-3

Recording every acknowledgement and Resolved time in the tool feeds response % and resolution % (G-1, SLA compliance %); escalation by assignment removes the email hand-off delay (PRC PP-1.4, G-2 MTTR); no copying of emails into the spreadsheet cuts manual admin hours (PRC PP-1.1, G-3).

### Stories
REQ S-1, REQ S-2, REQ S-3, REQ S-4, REQ S-5, REQ S-6, REQ S-7, REQ S-8, REQ S-28, REQ S-29

---

## Epic E-2: SLA timers and escalation flag

### Description
SLA timers per ticket on the business-hours calendar against the standard SLA, with pause, priority-change recalculation, at-risk and breached states shown in-app, and the L1 escalation flag at 50% of the resolution target; the delivery manager maintains the company holiday list (OQ-041). Covers SCP IS-1 (SLA timers).

### Business Value
BRF-001 G-1
BRF-001 G-2

At-risk states at 90% let engineers act before a target is missed instead of finding breaches up to 30 days later (PRC PP-2.1), raising resolution % (G-1, 80% to 95%); the escalation flag at 50% moves tickets to L2/L3 before L1's time runs out, cutting MTTR (G-2, 3 days to 1 day).

### Stories
REQ S-9, REQ S-10, REQ S-11, REQ S-24

---

## Epic E-3: SLA reporting and dashboards

### Description
The internal live dashboard across client organizations and SAP applications, and the monthly client report per client organization that client users view in APLX AMS and download as Excel or PDF. Covers SCP IS-2 and the report part of IS-4.

### Business Value
BRF-001 G-1
BRF-001 G-3
BRF-001 G-4

Response % and resolution % computed per ticket give G-1 its measure (resolution %); the generated monthly client report replaces manual compilation (PRC PP-2.2, G-3 manual admin and reporting hours); the live dashboard puts each client organization in one view (G-4, % of clients on the dashboard, 0% to 100%).

### Stories
REQ S-12, REQ S-13, REQ S-14

---

## Epic E-4: Effort tracking against contracts

### Description
Support engineers record hours on tickets assigned to them and change or delete their own effort entries until the end of the month; the delivery manager corrects any effort entry, sets up each client organization's one active contract (hours bank or fixed fee), ends it and sets up a new one, reviews effort and the hours bank balance (with a warning at 0 or below), and downloads the monthly finance export as Excel or CSV to email to finance (OQ-038, OQ-042, OQ-048). Covers SCP IS-3.

### Business Value
BRF-001 G-3
BRF-001 G-4

Effort recorded once per ticket and exported per contract removes the monthly hand compilation (PRC PP-3.1, G-3 manual admin and reporting hours, 40 to 10 per month); effort per contract in one place gives the single view of effort (PRC PP-3.2, G-4).

### Stories
REQ S-15, REQ S-16, REQ S-17, REQ S-19, REQ S-25, REQ S-26, REQ S-27

---

## Epic E-5: Access, setup and client data boundary

### Description
Delivery manager setup of client organizations, SAP applications and user accounts; sign-in with user accounts and a password policy (no MFA); the delivery manager sets a temporary password on a new user account and a new temporary password for a user who forgot their password, and any signed-in user changes their own password, with no forced change (SCR S-3); the client data boundary built and tested with two client organizations; the audit trail of ticket changes and of security events (sign-ins, lockouts, temporary passwords set, own password changes, viewed by the delivery manager for all user accounts and by each internal user for their own; SCR S-4). Covers SCP IS-4 (log-in), IS-5, and INT-002 Q7, Q8, Q11.

### Business Value
BRF-001 G-3
BRF-001 G-4

A client organization counts as on the dashboard (G-4, denominator 1 in release 1) only once it is set up, its client users can sign in, and they see only their own organization's data (DEC-022, RSK R-6). The audit trail (REQ S-23, S-32, S-33) serves G-3, as PRS F-8 serves PRS G-3: ticket changes are recorded in the one tool instead of the shared mailbox and spreadsheet.

### Stories
REQ S-18, REQ S-20, REQ S-21, REQ S-22, REQ S-23, REQ S-30, REQ S-31, REQ S-32, REQ S-33

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
None specific to the epics. Story-level assumptions A-009 to A-025 (A-009 to A-011, A-013, A-017, A-018, A-023 to A-025 Confirmed; A-012 Rejected) are listed in REQ-001, BR-001 and GLO-001 and logged in `docs/logs/assumptions-log.md`.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
None specific to the epics. OQ-037 to OQ-051 are Answered (2026-10-17); all logged in `docs/logs/open-questions-log.md`. No brief goal is left uncovered, so no product owner scope decision is needed. Scope decision DEC-026 (client comments, part of IS-4) adds REQ S-28 and REQ S-29 to E-1. SCR S-3 adds REQ S-30 and REQ S-31 to E-5; their questions OQ-053, OQ-054 are Answered (2026-10-17) and listed in REQ-001. SCR S-4 (OQ-062, OQ-064, OQ-065 Answered, 2026-10-17) adds REQ S-32 and REQ S-33 to E-5; the questions are listed in REQ-001.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason'.
     Cite individual epics downstream as EPC E-N (e.g. EPC E-2). -->
- Upstream: BRF-001 v0.2 (G-1 to G-4); SCP-001 v0.2 (IS-1 to IS-5); PIB-002 v0.1; INT-002 v0.1; PER-001 v0.2; PRC-001 v0.2.
- Downstream: REQ-001 (REQ S-1 to S-33); BKL-001; PRS-001 (features F-1 to F-8); `docs/logs/traceability-matrix.md` (seeded by the traceability agent).

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Every epic has a unique E-N ID; IDs are consecutive and never reused
- [x] Business Value cites at least one brief goal as 'BRF G-n' for each epic (written `BRF-001 G-n`, the form the traceability script accepts; see Purpose And Scope)
- [x] Stories section lists REQ S-N references for each epic
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
| Version | 0.3 |
| Conditions | None |
| Comments | Security events in the audit trail per SCR S-4 (OQ-062, OQ-064, OQ-065); R-10 accepted. |
| Timestamp | 2026-10-17 10:59 UTC |
