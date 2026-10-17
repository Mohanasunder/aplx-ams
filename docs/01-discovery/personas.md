---
id: PER-001
title: APLX AMS: Personas
phase: 1
version: 0.2
template: persona
template_version: 2.0
status: Approved
author_agent: discovery-analyst
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# APLX AMS: Personas

> **Collection file.** All personas for this project live in this one file. Add one `## Persona P-N` section per persona; never create a separate PER-NNN file for an additional persona. Downstream artifacts reference a specific persona as `PER P-N` (e.g. `PER P-2`).

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- PIB-001 v0.1 Phase 1 input brief, Approved 2026-10-17: § User Intent, § Interview Answers.
- INT-001 v0.1 Phase 1 interview, Approved 2026-10-17: Q1, Q2, Q3, Q3a, Q4, Q5, Q6, Q14, Q15, Q17.
- IRC-002 v0.1 Phase 1 readiness, Approved 2026-10-17.
- Answers to OQ-004, OQ-005, OQ-006, OQ-007, OQ-008, OQ-011, OQ-015, OQ-016, OQ-017, OQ-018, OQ-019, OQ-022, OQ-024 and OQ-025 to OQ-033, given by Mohanasunder (Business owner / BA) in chat on 2026-10-17 and recorded in `docs/logs/open-questions-log.md`; DEC-021 (`docs/logs/decision-log.md`).

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: the user groups of release 1: L1 support engineers (P-1), L2/L3 support engineers (P-2), delivery managers (P-3) and client users (P-4) (INT-001 Q3, Q3a; OQ-018).

Does not cover: stakeholders who are not users (sponsor and delivery head, both Applexus, OQ-006; see BRF-001 § Stakeholders), screens, or permissions design.

Evidence limit: one interview and one set of chat answers from one person (Mohanasunder; INT-001; OQ answers of 2026-10-17); no user was interviewed directly and no SOP documents were supplied (OQ-004). Anything not stated in these sources is marked as not stated or as an open question. Personal details (names, ages, photos) are not used.

Persona split and numbering: L1 differs from L2/L3, so they are separate personas (OQ-018 answered by Mohanasunder 2026-10-17; A-006 Rejected). Mohanasunder decided on 2026-10-17 to renumber the personas (DEC-021): P-1 L1 support engineer, P-2 L2/L3 support engineer, P-3 delivery manager, P-4 client user. Earlier numbering: v0.1: P-1 L1/L2/L3, P-2 delivery manager, P-3 client user; first v0.2 draft: P-4 L2/L3. No approved artifact cites a persona ID yet.

Release 1 access: desktop web browser only, no mobile (OQ-011). Pilot scale: about 10 engineers in total (L1 and L2/L3 together; split not stated) and about 20 client users (OQ-007). The release 1 pilot is internal: Applexus acts as its own client and Applexus staff are the client users; external clients come after release 1 (OQ-024).

---

## Persona P-1: L1 support engineer (triage)

### Profile
- Role: member of the company's own AMS team at level L1, the first point for tickets on clients' SAP applications (INT-001 Q1, Q3, Q4, Q17; OQ-018).
- Context today: takes client emails from a shared mailbox, logs each ticket in one shared spreadsheet with the priority (P1 to P4) the client states in the email, triages it, and resolves it or escalates it to L2/L3 (OQ-005, OQ-017, OQ-027). L1 always sends the closing email and updates the spreadsheet at closure (OQ-028). Records their own effort in hours per ticket in the same spreadsheet (OQ-015, OQ-032). The L1 lead owns the ticket handling process, PRC M-1 (OQ-025).
- Technical comfort: not stated in any source.
- Number of users in release 1: part of about 10 engineers (OQ-007); the L1 count is not stated.

### Goals
- Record and triage every incoming ticket within the SLA response target (OQ-004) for its client-stated priority (OQ-005, OQ-027; INT-001 Q2 problem 1).
- Spend less time on manual tracking of tickets and effort in email and spreadsheets (INT-001 Q2 problem 2).
- See tickets across clients and applications in one place (INT-001 Q2 problem 3).
Supports BRF G-1, G-2, G-3, G-4.

### Pain Points
- Tickets arrive by email to a shared mailbox and are logged by hand in one shared spreadsheet (OQ-005; INT-001 Q2, Q6).
- Missed response or resolution targets are found only at month-end, up to about 30 days late (OQ-016).
- No single view across clients and applications (INT-001 Q2).
- Escalation hand-off is by email plus a manual spreadsheet update (OQ-026).

### Key Journeys
1. Receive a client email, record the ticket with the client-stated priority and triage it (OQ-005, OQ-015, OQ-027; today: PRC M-1).
2. Resolve the ticket, or escalate it to L2/L3 (PER P-2) when it cannot be resolved within its target or needs functional or technical SAP skills (OQ-005, OQ-026).
3. Check the SLA timer of open tickets to act before a target is missed (INT-001 Q2, Q5).
4. Close the ticket: send the closing email to the client and update the ticket record (OQ-028; today: PRC M-1).
5. Record effort in hours per ticket in the shared spreadsheet (OQ-032; OQ-015; INT-001 Q5; today: PRC M-3). Mapping hours to a client contract is the delivery manager's compilation step (P-3, PRC M-3.2; method open, OQ-036).

---

## Persona P-2: L2/L3 support engineer (resolution)

### Profile
- Role: member of the company's own AMS team at level L2 or L3, who resolves tickets that L1 escalates (INT-001 Q3; OQ-005, OQ-018).
- Context today: receives tickets escalated by L1 by email plus a spreadsheet update, when L1 cannot resolve within the target or the ticket needs functional or technical SAP skills (OQ-005, OQ-026); records their own effort in hours per ticket in the shared spreadsheet (OQ-015, OQ-032). Works from email and spreadsheets (INT-001 Q6).
- Technical comfort: not stated in any source.
- Number of users in release 1: part of about 10 engineers (OQ-007); the L2/L3 count is not stated.

### Goals
- Resolve escalated tickets within their SLA resolution targets (OQ-005; INT-001 Q2 problem 1; standard SLA in OQ-004).
- Spend less time on manual tracking of effort (INT-001 Q2 problem 2).
Supports BRF G-1, G-2, G-3.

### Pain Points
- Missed resolution targets are found only at month-end, up to about 30 days late (OQ-016).
- Effort is tracked by hand in hours per ticket in the shared spreadsheet (INT-001 Q2, Q6; OQ-032).
- Escalated tickets arrive by email plus a manual spreadsheet update (OQ-026).

### Key Journeys
1. Take over a ticket escalated by L1 (PER P-1) and resolve it within its SLA target (OQ-005, OQ-026; today: PRC M-1). L1 then closes it (OQ-028).
2. Check the SLA timer of assigned tickets (INT-001 Q2, Q5).
3. Record effort in hours per ticket in the shared spreadsheet (OQ-032; OQ-015; INT-001 Q5; today: PRC M-3). Mapping hours to a client contract is the delivery manager's compilation step (P-3, PRC M-3.2; method open, OQ-036).

---

## Persona P-3: Delivery manager

### Profile
- Role: internal AMS team member named as a primary user (INT-001 Q3).
- Context today: tracks SLA in the same shared spreadsheet, reviewed at month-end only, and compiles the SLA reports (OQ-015, OQ-030); SLA breaches are found at month-end report compilation, up to about 30 days late (OQ-016). Emails each client contact the monthly SLA report as Excel/PDF (OQ-029). Compiles effort per contract and emails the Excel/CSV export to finance (OQ-031). Owns SLA tracking and reporting (PRC M-2) and effort tracking (PRC M-3) (OQ-025). Works from email and spreadsheets (INT-001 Q6).
- Technical comfort: not stated in any source.
- Number of users in release 1: not stated (OQ-007 gives engineer and client user counts only).

### Goals
- Monitor SLA status during the month instead of finding breaches at month-end (OQ-016, OQ-019; INT-001 Q2).
- Review and send per-client SLA reports with less manual compilation (OQ-019; INT-001 Q2, Q7).
- Review effort against client contracts (hours bank and fixed fee) (OQ-008, OQ-019; INT-001 Q5).
Supports BRF G-1, G-3, G-4.

### Pain Points
- SLA breaches are found up to about 30 days late, at month-end (OQ-016).
- SLA reports and the effort export are compiled by hand from one shared spreadsheet and sent by email (OQ-005, OQ-029, OQ-031; INT-001 Q2, Q6).
- No single view across clients and applications (INT-001 Q2).

### Key Journeys
Release 1 tasks confirmed by OQ-019 (A-005 Confirmed, Mohanasunder 2026-10-17).
1. Monitor SLA status of open tickets across clients (OQ-019; today: PRC M-2).
2. Review and send the per-client SLA report to the client contact each month (OQ-019, OQ-029; INT-001 Q5; today: PRC M-2, by email as Excel/PDF).
3. Review effort recorded against a client contract (OQ-019; today: PRC M-3).
4. Compile effort per contract and send the monthly Excel/CSV effort export to finance (OQ-008, OQ-031; today: PRC M-3, by email).

Note: billing and invoicing happen outside APLX AMS, in finance (INT-001 Q8; SCP-001 IS-3, OS-1).

---

## Persona P-4: Client user

### Profile
- Role: a user from a client organization whose SAP applications the AMS team supports (INT-001 Q3, Q4). Logs in to APLX AMS in release 1 (INT-001 Q3a). One client role: every client user can raise tickets and view their organization's SLA reports (OQ-022).
- Release 1 pilot: the pilot is internal; Applexus acts as its own client and Applexus staff are the client users. External client organizations' users come after release 1 (OQ-024, Mohanasunder 2026-10-17).
- Data boundary: sees and acts only on their own organization's tickets and SLA reports (INT-001 Q14, A-002).
- Personal data held about this user: name and email; no specific data-protection obligations known (INT-001 Q15).
- Technical comfort: not stated in any source.
- Number in release 1: about 20 client users (OQ-007) in one pilot client organization, Applexus (OQ-033), all Applexus staff in the internal pilot (OQ-024).

### Goals
- Raise tickets for their SAP applications (INT-001 Q3a).
- View their own organization's SLA reports (INT-001 Q3a, Q14).
Supports BRF G-1, G-4.

### Pain Points
- Today tickets are raised by email to a shared mailbox, with the client stating the priority, and closed by email from L1 (OQ-005, OQ-017, OQ-027, OQ-028); SLA reports arrive monthly by email as Excel/PDF (OQ-029).
- No pain point has been stated by a client user; no client was interviewed (OQ-006). In release 1 the client users are Applexus staff (OQ-024), so no external client user's view is captured before go-live (RSK R-8).

### Key Journeys
1. Log in and raise a ticket (incident or service request) for one of their organization's SAP applications (INT-001 Q3a, Q5).
2. View their organization's SLA report (INT-001 Q3a, Q14).
3. See only their own organization's tickets and reports, never another client's (INT-001 Q14).

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-002 (Confirmed, INT-001 Q14): client users see and act only on their own organization's data (P-4).
- A-003 (Confirmed, INT-001 Q17): users support SAP applications only (P-1, P-2, P-4).
- A-005 (Confirmed, Mohanasunder 2026-10-17, OQ-019): delivery managers are the internal users of per-client SLA reports, dashboards and effort data (P-3).
- A-006 (Rejected, Mohanasunder 2026-10-17, OQ-018): L1, L2 and L3 are not one persona; split into P-1 and P-2.
- A-007 (Confirmed, Mohanasunder 2026-10-17, OQ-015): engineers record their own effort (P-1, P-2).
- No new assumptions in this version.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
- OQ-036 (Open, Low; owner Mohanasunder, Business owner / BA): how per-ticket effort hours are mapped to a client contract (hours bank or fixed fee); compilation step owned by P-3 (PRC M-3.2). Cited in P-1 Key Journey 5 and P-2 Key Journey 3.
- Answered 2026-10-17: OQ-004, OQ-005, OQ-006, OQ-007, OQ-008, OQ-011, OQ-015, OQ-016, OQ-017, OQ-018, OQ-019, OQ-022, OQ-024 (internal pilot; P-4), OQ-025 (process owners; P-1, P-3), OQ-026 (escalation criteria and hand-off; P-1, P-2), OQ-027 (client states priority; P-1, P-4), OQ-028 (L1 closes; P-1), OQ-029 (SLA report emailed monthly; P-3, P-4), OQ-030 (SLA tracked in the shared spreadsheet; P-3), OQ-031 (delivery manager sends the effort export; P-3), OQ-032 (effort in hours per ticket; P-1, P-2), OQ-033 (one pilot client organization; P-4).

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason'.
     Cite individual personas downstream as PER P-N (e.g. PER P-2). -->
- Upstream: PIB-001 v0.1; INT-001 v0.1 (Q1 to Q8, Q3a, Q14, Q15, Q17); IRC-002 v0.1; OQ answers of 2026-10-17.
- Related Phase 1: BRF-001 (goals G-1 to G-4, stakeholders); SCP-001; PRC-001 (PRC M-1 to M-3); RSK-001 (RSK R-6, R-8).
- Downstream: Phase 2 user stories cite PER P-1, PER P-2, PER P-3, PER P-4 (not yet created).

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Every persona has a unique P-N ID; IDs are consecutive and never reused
- [x] Every claim in each persona cites a source file
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
| Version | 0.2 |
| Conditions | None |
| Comments | Reviewed after validation run 5; KPI baselines and targets confirmed; OQ-034 to OQ-036 deferred to Phase 2. |
| Timestamp | 2026-10-17 06:05 UTC |
