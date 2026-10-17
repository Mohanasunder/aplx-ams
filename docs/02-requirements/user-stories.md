---
id: REQ-001
title: APLX AMS: User Stories
phase: 2
version: 0.3
template: user-story
template_version: 2.0
status: Approved
author_agent: requirements-analyst
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# APLX AMS: User Stories

> **Collection file.** All user stories for this project live in this one file. Add one `## Story S-N` section per story; never create a separate REQ-NNN file for an additional story. Downstream artifacts reference a specific story as `REQ S-N` (e.g. `REQ S-3`) and a specific acceptance criterion as `REQ S-N AC-n` (e.g. `REQ S-3 AC-2`).

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- PIB-002 v0.1 § Interview Answers (Q1 to Q16, Q9a, Q12a, Q14a), § Constraints.
- INT-002 v0.1 § Questions And Answers (evidence record).
- SUM-001 v0.3 § Decisions, § Constraints Set.
- BRF-001 v0.2 § Business Goals And KPIs (G-1 to G-4).
- SCP-001 v0.2 § In Scope (IS-1 to IS-5), § Out Of Scope (OS-1 to OS-4).
- PER-001 v0.2 § Persona P-1 to P-4 (Key Journeys).
- PRC-001 v0.2 § Process M-1 to M-3 (Pain Points).
- RSK-001 v0.2 § Risk R-6; DEC-022; DEC-026 (client comments, Mohanasunder, 2026-10-17).
- Answers to OQ-037 to OQ-051 and the Phase 2 review answers, 2026-10-17 (Mohanasunder, 2026-10-17, chat; `docs/logs/open-questions-log.md`).
- Phase 2 drafts referenced, not used as input: BR-001 (business rules), NFR-001 (NFRs), GLO-001 (domain glossary).
- SCR S-3 (`docs/logs/spec-changes.md`): password set, reset and change, decided by Mohanasunder (Product owner / BA), chat, 2026-10-17 (option C on VAL-013 F-1); adds REQ S-30, S-31.
- SCR S-4 (`docs/logs/spec-changes.md`): security events in the audit trail, OQ-062 answered by Mohanasunder (Product owner / BA), chat, 2026-10-17; adds REQ S-32, S-33.
- NFR-001 v0.3 § NFR N-5 (password policy), § NFR N-6 (audit trail completeness).

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: the release 1 user stories of APLX AMS, S-1 to S-33 (S-30 and S-31 added by SCR S-3; S-32 and S-33 by SCR S-4), with Given/When/Then acceptance criteria (AC-n) including edge, error and permission cases. Personas: PER P-1 L1 support engineer, PER P-2 L2/L3 support engineer, PER P-3 delivery manager, PER P-4 client user. All stories are Must for the 2027-01-17 go-live (INT-002 Q1). Each story has at most 4 criteria (`project.md` max_acceptance_criteria_per_feature, used as sizing guidance). Terms follow GLO-001.

Does not cover: screens, colours, layout, endpoints, tables or technology (Phases 3 and 4), NFR targets (NFR-001), or the rule detail held in BR-001. Examples use business hours per BR B-2 on business days with no holiday.

---

## Story S-1: Client user raises a ticket in the portal

### Story Statement
As a client user (PER P-4), I want to raise an incident or a service request for one of my client organization's SAP applications in APLX AMS, so that the AMS team receives it with its priority and the SLA timers start without a mailbox step.

### Acceptance Criteria
1. Given a signed-in client user of client organization A, when they raise a ticket with a type (incident or service request), one of organization A's SAP applications, a priority P1 to P4 and a description, then the ticket is created with the raise time, the response and resolution targets of that priority (BR B-1), and appears in the L1 queue.
2. Given a client user raising a ticket, when the type, SAP application, priority or description is missing, then no ticket is created and the client user is told which field is missing.
3. Given a client user of client organization A, when they try to raise a ticket for an SAP application of client organization B, then the ticket is refused and no ticket is created.
4. Given a client user raises a ticket at 18:30 IST on a business day, when the SLA timers start, then elapsed business time stays 0 until 09:00 IST on the next business day (BR B-3).

### Business Rules
BR B-1, BR B-3, BR B-7, BR B-19, BR B-20

### NFR References
NFR N-2, NFR N-7

### Priority
Must: portal-only intake replaces the shared mailbox and the copying of emails into the spreadsheet, and records the raise time that starts the SLA timers (INT-002 Q5, Q1; SCP IS-1, IS-4; PRC PP-1.1; BRF-001 G-1, G-3).

---

## Story S-2: Client user follows their client organization's tickets

### Story Statement
As a client user (PER P-4), I want to see the tickets of my client organization and the status of each, so that I know where my requests stand without emailing the AMS team.

### Acceptance Criteria
1. Given client organization A has 3 tickets and client organization B has 2 tickets, when a client user of organization A views tickets, then they see the 3 tickets of organization A, each with its status and priority, and none of organization B's tickets.
2. Given a ticket of organization A is set to Resolved or Closed, when a client user of organization A views that ticket, then it shows the status Resolved or Closed.
3. Given a client user of organization A, when they view one of their organization's tickets, then the audit trail is not shown (BR B-22).
4. Given a client user of organization A viewing one of their organization's tickets after it is raised, when they try to change its priority, then the change is refused and the priority stays as it was (BR B-7).

### Business Rules
BR B-7, BR B-20, BR B-22

### NFR References
NFR N-2, NFR N-7

### Priority
Must: client users view their own organization's tickets and statuses in APLX AMS instead of asking the AMS team by email (SCP IS-4, IS-5; INT-002 Q1; BRF-001 G-3). Client users add comments on their organization's tickets in REQ S-28 (OQ-045, DEC-026).

---

## Story S-3: L1 support engineer acknowledges a new ticket

### Story Statement
As an L1 support engineer (PER P-1), I want to acknowledge and triage new tickets in APLX AMS, so that the response clock stops at my first action and the response target is measured from what L1 actually did.

### Acceptance Criteria
1. Given a P2 ticket raised at 10:00 IST, when an L1 support engineer acknowledges it at 12:00 IST the same business day, then the response clock stops at 2 business hours and the response target is met (BR B-4).
2. Given a ticket whose first L1 action was at 12:00 IST, when another L1 support engineer acknowledges it or acts on it at 13:00 IST, then the response clock stop time stays 12:00 IST (BR B-4).
3. Given a P1 ticket raised at 10:00 IST, when the first L1 action on it is at 11:00 IST, then the response clock stops at exactly 1 business hour (100% of the response target) and the response target is breached, not met (BR B-4, BR B-8).
4. Given a client user, an L2/L3 support engineer or a delivery manager, when they view a new ticket, then they cannot acknowledge it and the response clock keeps running (BR B-4).

### Business Rules
BR B-4, BR B-8

### NFR References
NFR N-2

### Priority
Must: the response clock stop drives response % (INT-002 Q3, Q4; BRF-001 G-1). Any first L1 action counts as acknowledgement (Phase 2 gate answers, 2026-10-17); what counts as an action: A-017.

---

## Story S-4: L1 support engineer changes a ticket's priority

### Story Statement
As an L1 support engineer (PER P-1), I want to change a ticket's priority with a reason, so that the SLA targets match the real urgency.

### Acceptance Criteria
1. Given a P3 ticket raised at 10:00 IST Monday with no L1 action yet, when an L1 support engineer changes the priority to P1 at 12:00 IST with a reason, then the change is the first L1 action, so the response clock stops at 2 business hours and is judged against the new P1 response target of 1 business hour: breached, not met (BR B-4, OQ-046); and the running resolution clock recalculates to 4 business hours from 10:00 IST (resolution due 14:00 IST Monday) (BR B-7).
2. Given a P1 ticket raised at 09:00 IST Monday whose response clock stopped at 10:30 IST (1.5 business hours, response target breached), when an L1 support engineer changes the priority to P3 at 11:00 IST with a reason, then the response clock stays breached and only the running resolution clock recalculates to 27 business hours from 09:00 IST (BR B-7, BR B-8).
3. Given an L1 support engineer changing a priority, when no reason is entered, then the priority does not change.
4. Given a ticket set to Resolved, when an L1 support engineer tries to change its priority, then the change is refused and the priority and both stopped clocks keep their values (BR B-7).

### Business Rules
BR B-1, BR B-4, BR B-7, BR B-8, BR B-10, BR B-22

### NFR References
NFR N-6

### Priority
Must: priority drives every SLA target (INT-002 Q6; PRC PP-1.3; BRF-001 G-1). Recalculation rules confirmed in the Phase 2 gate answers, 2026-10-17. The client user's refusal is REQ S-2 AC-4; the audit entry for a priority change is REQ S-23 AC-1; the moved escalation point is REQ S-11 AC-2. When the first L1 action is the priority change itself, the response clock stop is judged against the new priority's response target (OQ-046 answered, Mohanasunder, 2026-10-17); AC-1 tests that case.

---

## Story S-5: L1 support engineer escalates a ticket to L2/L3

### Story Statement
As an L1 support engineer (PER P-1), I want to escalate a ticket I cannot resolve within my L1 target, or that needs functional or technical SAP skills, to an L2/L3 support engineer in APLX AMS, so that the hand-off needs no email or spreadsheet update.

### Acceptance Criteria
1. Given a P2 ticket raised at 10:00 IST in the L1 queue with no L1 action yet, when an L1 support engineer assigns it to an L2/L3 support engineer at 11:00 IST, then the ticket appears in that L2/L3 support engineer's assigned tickets, leaves the L1 queue, and the response clock stops at 1 business hour because the assignment is the first L1 action (BR B-4).
2. Given a ticket with the escalation flag, when an L1 support engineer assigns it to an L2/L3 support engineer, then the escalation flag is removed (BR B-10).
3. Given a ticket is assigned to an L2/L3 support engineer, when the assignment is saved, then the audit trail holds the old and new assigned support engineer, the user and the time (BR B-22).
4. Given a client user, when they view their organization's ticket, then they cannot change its assignment.

### Business Rules
BR B-4, BR B-10, BR B-22

### NFR References
NFR N-6

### Priority
Must: removes the manual escalation hand-off that delays resolution (PRC PP-1.4; BRF-001 G-2).

---

## Story S-6: Support engineer sets a ticket to Resolved

### Story Statement
As an L2/L3 support engineer (PER P-2) or an L1 support engineer (PER P-1), I want to set a ticket to Resolved, so that the resolution clock stops and the ticket goes to the L1 queue for closure.

### Acceptance Criteria
1. Given a P2 ticket raised at 10:00 IST Monday, assigned to an L2/L3 support engineer, when they set it to Resolved at 15:00 IST Monday, then the resolution clock stops at 5 business hours and the resolution target (9 business hours) is met (BR B-5).
2. Given an L2/L3 support engineer sets a ticket to Resolved, when an L1 support engineer views the L1 queue, then the ticket appears there for closure (BR B-11).
3. Given an L1 support engineer resolves a ticket themselves, when they set it to Resolved, then the resolution clock stops and the ticket is in the L1 queue for closure.
4. Given an L2/L3 support engineer, when they try to close a Resolved ticket, then the close is refused and the status stays Resolved.

### Business Rules
BR B-5, BR B-11

### NFR References
NFR N-6

### Priority
Must: the Resolved hand-back answers OQ-035 and stops the resolution clock behind resolution % and MTTR (BRF-001 G-1, G-2).

---

## Story S-7: L1 support engineer closes a Resolved ticket

### Story Statement
As an L1 support engineer (PER P-1), I want to close a Resolved ticket, so that the ticket's lifecycle ends and the client user sees it Closed.

### Acceptance Criteria
1. Given a Resolved ticket in the L1 queue, when an L1 support engineer closes it, then its status is Closed, it leaves the L1 queue, and the client user of its client organization sees it as Closed.
2. Given a ticket that is not Resolved, when an L1 support engineer tries to close it, then the close is refused and the status does not change.
3. Given a Resolved ticket, when it is closed, then the resolution clock stop time does not change (the clock stopped at Resolved, BR B-5).
4. Given a Resolved ticket of client organization A, when an L1 support engineer closes it, then APLX AMS sends no email or other message about the closure to the client user; the Closed status on the ticket is the only notice (BR B-11, OQ-037).

### Business Rules
BR B-5, BR B-11, BR B-22

### NFR References
NFR N-6

### Priority
Must: L1 closes every ticket in APLX AMS instead of updating the shared spreadsheet at closure (OQ-028, INT-002 Q16; BRF-001 G-3). The client user learns of closure from the Closed status only (OQ-037 answered, Mohanasunder, 2026-10-17).

---

## Story S-8: Support engineer marks a ticket as awaiting client

### Story Statement
As the assigned support engineer of a ticket (PER P-1 or PER P-2), I want to mark it as awaiting client, and have that status cleared when the client user adds a comment or when I clear it, so that time spent waiting on the client is not counted against the SLA targets.

### Acceptance Criteria
1. Given a P3 ticket with its resolution clock running at 2 business hours, when the assigned support engineer sets awaiting client and clears it 4 business hours later, then the resolution elapsed time is still 2 business hours at the moment it is cleared.
2. Given a ticket in awaiting client, when business hours pass, then neither SLA timer changes state.
3. Given a ticket in awaiting client, when the status is cleared, then the paused SLA timers resume from the elapsed time at the pause.
4. Given a client user or a support engineer who is not the assigned support engineer, when they view a ticket that is not awaiting client, then they cannot set awaiting client (BR B-6, OQ-045).

### Business Rules
BR B-6, BR B-22

### NFR References
NFR N-6

### Priority
Must: the pause rule is part of the SLA timers (INT-002 Q3; BRF-001 G-1). OQ-045 answered (Mohanasunder, 2026-10-17; A-013 Confirmed): the assigned support engineer sets awaiting client; a client user's comment clears it automatically (REQ S-28 AC-2). Assigned support engineer for a ticket not assigned to an L2/L3 support engineer: BR B-6 (A-024, Confirmed).

---

## Story S-9: SLA timers count business hours against the standard SLA

### Story Statement
As an L1 support engineer (PER P-1), I want each ticket's SLA timers to count only business hours against the standard SLA targets, so that the elapsed time I see matches the client contract.

### Acceptance Criteria
1. Given a P1 ticket raised at 17:30 IST on Friday, when the next business day starts, then the response target falls due at 09:30 IST on Monday (0.5 business hours on Friday and 0.5 on Monday).
2. Given a P3 ticket raised at 10:00 IST on the business day before a date on the company holiday list, when elapsed business time is counted, then the holiday contributes 0 business hours.
3. Given tickets of P1, P2, P3 and P4, when they are raised, then their response and resolution targets are 1 and 4, 4 and 9, 9 and 27, and 18 and 45 business hours (BR B-1).
4. Given a ticket raised at 08:00 IST on a business day, when the clocks start, then elapsed business time is 0 until 09:00 IST the same day.

### Business Rules
BR B-1, BR B-2, BR B-3, BR B-4, BR B-5, BR B-6

### NFR References
NFR N-2

### Priority
Must: SLA timers are the core of IS-1 (INT-002 Q2, Q3; BRF-001 G-1).

---

## Story S-10: Support engineer sees SLA timer states in APLX AMS

### Story Statement
As an L1 support engineer (PER P-1) or an L2/L3 support engineer (PER P-2), I want each ticket's SLA timers to show on track, at risk, breached or met, so that I act before a target is missed instead of finding it at month end.

### Acceptance Criteria
1. Given a P1 ticket not yet acknowledged, when its response elapsed time reaches 54 business minutes (90% of 1 business hour), then its response clock shows at risk.
2. Given a P1 ticket not yet Resolved, when its resolution elapsed time reaches 4 business hours, then its resolution clock shows breached.
3. Given a ticket whose response clock stopped at 50% of the response target, when its resolution clock is at risk, then the response clock shows met and the resolution clock shows at risk (A-014).
4. Given any ticket reaches at risk or breached, when the state changes, then no email is sent for it (BR B-9).

### Business Rules
BR B-1, BR B-2, BR B-8, BR B-9

### NFR References
NFR N-2

### Priority
Must: breaches found in time is the top pain point (PRC PP-2.1; INT-002 Q12, Q12a; BRF-001 G-1).

---

## Story S-11: Ticket is flagged for escalation at L1's target

### Story Statement
As an L1 support engineer (PER P-1), I want a ticket still with L1 to be flagged for escalation when half of its resolution target has elapsed, so that I escalate it before the resolution target is missed.

### Acceptance Criteria
1. Given a P1 ticket still with L1, when its resolution elapsed time reaches 2 business hours (50% of 4), then the ticket shows the escalation flag.
2. Given a P2 ticket still with L1 at 3 business hours of resolution elapsed time (escalation point 4.5 business hours, 50% of 9), when an L1 support engineer changes the priority to P1 with a reason, then the escalation point moves to 2 business hours (50% of the new 4-hour resolution target) and the ticket shows the escalation flag at the change (BR B-7, BR B-10).
3. Given a P1 ticket assigned to an L2/L3 support engineer at 1 business hour, when its resolution elapsed time reaches 2 business hours, then no escalation flag is shown.
4. Given a P1 ticket still with L1 showing the escalation flag at 2.5 business hours of resolution elapsed time, when an L1 support engineer changes the priority to P2 with a reason, then the escalation point moves to 4.5 business hours (50% of 9), the flag clears at the change, and the flag shows again when the resolution elapsed time reaches 4.5 business hours (BR B-7, BR B-10).

### Business Rules
BR B-1, BR B-2, BR B-7, BR B-10

### NFR References
NFR N-2

### Priority
Must: escalation without waiting for L1 to miss its target cuts MTTR (INT-002 Q15; PRC PP-1.4; BRF-001 G-2). The moving escalation point is confirmed in the Phase 2 gate answers, 2026-10-17; the flag clearing when the priority is lowered (AC-4) is confirmed in the Phase 2 review answers, 2026-10-17. AC-4 replaces the earlier "set to Resolved at 1.5 business hours, no flag" case to stay within 4 criteria; that case follows from BR B-10 (a Resolved ticket is no longer with L1) and has the same no-flag result as AC-3.

---

## Story S-12: Delivery manager monitors the live dashboard

### Story Statement
As a delivery manager (PER P-3), I want a live dashboard of open tickets, SLA timer states, escalation flags and effort across client organizations and SAP applications, so that I monitor SLA during the month in one view.

### Acceptance Criteria
1. Given open tickets in client organizations A and B, when the delivery manager views the live dashboard, then it shows, per client organization and per SAP application, the count of open tickets, at-risk tickets, breached tickets and tickets with the escalation flag.
2. Given a ticket's SLA timer changes from on track to at risk, when the delivery manager next views the live dashboard, then the at-risk count includes that ticket.
3. Given client organization A has an hours bank contract, when the delivery manager views the live dashboard, then it shows organization A's hours bank balance (BR B-16).
4. Given a client user, when they try to view the live dashboard, then access is refused.

### Business Rules
BR B-8, BR B-9, BR B-10, BR B-16, BR B-20

### NFR References
NFR N-2, NFR N-7

### Priority
Must: one view across clients and SAP applications is BRF-001 G-4 (INT-002 Q13; SCP IS-2).

---

## Story S-13: Delivery manager generates the monthly client report per client organization

### Story Statement
As a delivery manager (PER P-3), I want to generate the monthly client report for each client organization in APLX AMS, review it and publish it, so that I stop compiling SLA reports by hand from the spreadsheet.

### Acceptance Criteria
1. Given in September 2026 client organization A had 20 P2 tickets whose resolution clock stopped, 18 with the resolution target met, when the delivery manager generates the September 2026 report for organization A, then P2 resolution % is 90% (BR B-12).
2. Given in September 2026 client organization A had no P1 tickets whose clocks stopped, when the delivery manager generates the report, then P1 response % and resolution % show "no tickets" (A-021).
3. Given the generated September 2026 report for organization A, in which exactly 2 tickets were set to Resolved, after 9 and 18 business hours (paused time excluded), when the delivery manager reviews it, then it lists every ticket with a breached response or resolution target in that month, shows MTTR 1.5 business days (BR B-13), and the counts of tickets raised, Resolved and Closed per priority (BR B-14).
4. Given a ticket raised in September 2026 and set to Resolved in October 2026, when the delivery manager generates the reports, then the ticket counts in October's resolution % and MTTR, not September's (A-015).

### Business Rules
BR B-1, BR B-2, BR B-4, BR B-5, BR B-8, BR B-12, BR B-13, BR B-14

### NFR References
NFR N-2

### Priority
Must: manual SLA report compilation is PRC PP-2.2 (BRF-001 G-1, G-3; INT-002 Q4, Q13). The delivery manager generates, reviews and publishes the report (OQ-047 answered, Mohanasunder, 2026-10-17); publication and client visibility are REQ S-14 AC-4. MTTR definition: OQ-039 answered (A-009 Confirmed).

---

## Story S-14: Client user views and downloads the monthly client report

### Story Statement
As a client user (PER P-4), I want to view my client organization's monthly client report in APLX AMS and download it as Excel or PDF, so that I see our SLA performance without waiting for an email.

### Acceptance Criteria
1. Given the monthly client report for September 2026 is published for client organization A, when a client user of organization A opens it, then they see its response %, resolution %, breached tickets, MTTR and ticket counts.
2. Given that report, when the client user downloads it as Excel and as PDF, then each file holds the same figures as the report viewed in APLX AMS.
3. Given a client user of client organization A, when they try to open client organization B's monthly client report, then access is refused.
4. Given the September 2026 report for organization A is generated but not yet published, when a client user of organization A looks for it, then it is not shown; when the delivery manager then publishes it, the client user can open it (BR B-14, OQ-047).

### Business Rules
BR B-12, BR B-13, BR B-14, BR B-20

### NFR References
NFR N-2, NFR N-7

### Priority
Must: client users view SLA reports (SCP IS-2, IS-4; INT-002 Q13; BRF-001 G-4). Client users see a month's report once the delivery manager publishes it (OQ-047 answered, Mohanasunder, 2026-10-17).

---

## Story S-15: Support engineer records effort on a ticket

### Story Statement
As an L1 support engineer (PER P-1) or an L2/L3 support engineer (PER P-2), I want to record the hours I spend on a ticket assigned to me, with the date, so that effort is captured against the client organization's contract without a spreadsheet.

### Acceptance Criteria
1. Given a ticket of client organization A with an active contract, assigned to a support engineer, when that support engineer records 1.5 hours on 2026-11-02, then an effort entry with that support engineer as the engineer, the date, 1.5 hours and the ticket is saved and counts against organization A's active contract (BR B-15; each engineer records their own effort, OQ-015).
2. Given a support engineer recording effort, when the hours are 0 or negative, then the effort entry is not saved (A-020).
3. Given an effort entry is saved, when the audit trail of the ticket is viewed, then it holds the new effort entry, the user and the time (BR B-22).
4. Given a ticket assigned to an L2/L3 support engineer X, when a different support engineer or a client user tries to record effort on it, then no effort entry is saved (BR B-15, OQ-048).

### Business Rules
BR B-15, BR B-22

### NFR References
NFR N-6

### Priority
Must: effort recorded by hand is PRC PP-3.1 (SCP IS-3; INT-002 Q14; BRF-001 G-3). Effort only on tickets assigned to the support engineer (OQ-048 answered, Mohanasunder, 2026-10-17; tickets with L1 per BR B-6, A-024 Confirmed). Changing and deleting entries: REQ S-25, S-26. No active contract: REQ S-27 AC-2. Hours bank balance at or below 0: REQ S-16 AC-4.

---

## Story S-16: Delivery manager reviews effort against a contract

### Story Statement
As a delivery manager (PER P-3), I want to review the effort recorded against each client organization's active contract, with the hours bank balance for hours bank contracts, so that I see contract use during the month.

### Acceptance Criteria
1. Given client organization A has an hours bank contract of 100 contracted hours and 30 hours recorded, when the delivery manager reviews it, then it shows 30 hours recorded and an hours bank balance of 70 hours (BR B-16).
2. Given client organization B has a fixed fee contract and 12 hours recorded, when the delivery manager reviews it, then it shows 12 hours recorded and no hours bank balance (BR B-17).
3. Given a client user, when they try to review effort against a contract, then access is refused.
4. Given client organization A's hours bank balance is 1 hour, when a support engineer records 3 hours on a ticket of organization A assigned to them, then the effort entry is saved, the hours bank balance is -2 hours, and the delivery manager reviewing the contract sees a warning with the balance (BR B-16, OQ-042).

### Business Rules
BR B-15, BR B-16, BR B-17

### NFR References
NFR N-2

### Priority
Must: no single view of effort per contract is PRC PP-3.2 (PER P-3 Key Journey 3; BRF-001 G-3, G-4).

---

## Story S-17: Delivery manager produces the monthly finance export

### Story Statement
As a delivery manager (PER P-3), I want APLX AMS to produce the monthly finance export as Excel or CSV for me to download and email to finance, so that finance gets effort per contract without manual compilation.

### Acceptance Criteria
1. Given effort entries recorded in October 2026, when the delivery manager produces the October 2026 finance export, then it holds one row per effort entry recorded in October 2026 with client organization, contract, ticket, engineer, date, hours and remaining hours bank balance (BR B-18).
2. Given an effort entry on a fixed fee contract, when it appears in the finance export, then its hours are shown and its remaining hours bank balance field is blank (BR B-17).
3. Given client organization A's hours bank balance at the end of October 2026 is 70 hours, when the October 2026 finance export is produced, then every row of organization A shows 70 in the remaining hours bank balance field (BR B-18, OQ-043).
4. Given the finance export is produced, when the delivery manager downloads it as Excel or as CSV, then the downloaded file is in the chosen format with the same rows, and APLX AMS sends nothing to finance (BR B-18, OQ-038).

### Business Rules
BR B-16, BR B-17, BR B-18

### NFR References
NFR N-2

### Priority
Must: the monthly export to finance is in IS-3 (OQ-008; INT-002 Q14, Q14a; BRF-001 G-3). The delivery manager downloads the finance export and emails it to finance outside APLX AMS; finance has no role (OQ-038 answered, Mohanasunder, 2026-10-17). Balance at month end: OQ-043 answered (A-011 Confirmed).

---

## Story S-18: Delivery manager sets up client organizations and SAP applications

### Story Statement
As a delivery manager (PER P-3), I want to set up client organizations and the SAP applications we support for each, so that tickets, reports and contracts belong to the right client organization.

### Acceptance Criteria
1. Given the delivery manager, when they create client organization Applexus and add an SAP application to it, then client users of Applexus can choose that SAP application when raising a ticket.
2. Given two client organizations A and B, when the delivery manager adds an SAP application to organization A, then client users of organization B cannot choose it.
3. Given an L1 support engineer, an L2/L3 support engineer or a client user, when they try to create or change a client organization or SAP application, then the change is refused.

### Business Rules
BR B-19, BR B-20, BR B-21

### NFR References
NFR N-7

### Priority
Must: setup is needed before any ticket can be raised (INT-002 Q8; BRF-001 G-4).

---

## Story S-19: Delivery manager sets up a client organization's contract

### Story Statement
As a delivery manager (PER P-3), I want to set up a client organization's contract as hours bank (with contracted hours) or fixed fee, so that recorded effort counts against the right contract.

### Acceptance Criteria
1. Given client organization A with no active contract, when the delivery manager creates an active hours bank contract of 100 contracted hours, then organization A's hours bank balance shows 100 hours.
2. Given client organization A already has an active contract, when the delivery manager tries to make a second contract active for organization A, then it is refused and organization A keeps one active contract (BR B-15).
3. Given the delivery manager creates a fixed fee contract, when it is saved, then no contracted hours or hours bank balance is held for it.
4. Given a user who is not a delivery manager, when they try to create or change a contract, then the change is refused.

### Business Rules
BR B-15, BR B-16, BR B-17, BR B-21

### NFR References
NFR N-6

### Priority
Must: contracts are needed for effort tracking (INT-002 Q8, Q14; SCP IS-3; BRF-001 G-3). Ending a contract and setting up a new one: REQ S-27 (OQ-042 answered, Mohanasunder, 2026-10-17).

---

## Story S-20: Delivery manager manages user accounts

### Story Statement
As a delivery manager (PER P-3), I want to create, change and deactivate user accounts with one role each, linking each client user to one client organization, so that every user signs in with the right access.

### Acceptance Criteria
1. Given the delivery manager, when they create a user account with role L1 support engineer, L2/L3 support engineer, delivery manager or client user, then the account is saved with that role.
2. Given the delivery manager creates a client user account, when no client organization is chosen, then the account is not saved.
3. Given an active user account, when the delivery manager deactivates it, then that user can no longer sign in.
4. Given a user who is not a delivery manager, when they try to create, change or deactivate a user account, then the change is refused.

### Business Rules
BR B-21

### NFR References
NFR N-5, NFR N-7, NFR N-9

### Priority
Must: user accounts for staff and client users (INT-002 Q7, Q8; SCP IS-4; BRF-001 G-4).

---

## Story S-21: User signs in with a user account

### Story Statement
As any user (PER P-1, PER P-2, PER P-3 or PER P-4), I want to sign in with my APLX AMS user account and password, so that I reach only the tasks of my role.

### Acceptance Criteria
1. Given an active user account with a correct password, when the user signs in, then they reach APLX AMS with the tasks of their role, and no second factor is asked for (NFR N-5).
2. Given a wrong password, when the user signs in, then sign-in is refused without saying whether the account name or the password was wrong (A-019).
3. Given a user setting a password, when it has fewer than 8 characters or lacks an upper-case letter, a lower-case letter or a digit (for example "abcdefg1" with no upper-case letter), then the password is refused; "Abcdefg1" is accepted (NFR N-5, OQ-044).
4. Given 5 failed sign-ins on one user account, when a sixth sign-in is tried within 30 minutes of the fifth failure, then it is refused even with the correct password; after the 30 minutes the correct password is accepted (NFR N-5, OQ-044).

### Business Rules
BR B-21

### NFR References
NFR N-5

### Priority
Must: client user log-in is IS-4 (INT-002 Q7; SCP IS-4; BRF-001 G-4). Password policy and lockout: OQ-044 answered (Mohanasunder, 2026-10-17; replaces A-012, now Rejected). Exception to AC-4: a new temporary password set by the delivery manager clears the lock at once (BR B-23; REQ S-30 AC-3; OQ-054, SCR S-3).

---

## Story S-22: Client data boundary holds across two client organizations

### Story Statement
As a client user (PER P-4), I want to see and act only on my own client organization's data, so that no other client organization sees our tickets, reports, names or emails.

### Acceptance Criteria
1. Given client organizations A and B each have tickets, when a client user of organization A lists tickets, then only organization A's tickets are listed.
2. Given a ticket of organization B, when a client user of organization A opens it by its ticket reference, then access is refused and no detail of the ticket is shown.
3. Given organization B's monthly client report and SAP applications, when a client user of organization A tries to view or use them, then access is refused.
4. Given an L1 support engineer, an L2/L3 support engineer or a delivery manager, when they list tickets, then tickets of organizations A and B are both listed.

### Business Rules
BR B-20

### NFR References
NFR N-7

### Priority
Must: IS-5 built and tested with at least two client organizations (DEC-022; RSK R-6; BRF-001 G-4).

---

## Story S-23: Internal user views a ticket's audit trail

### Story Statement
As a delivery manager (PER P-3), I want to view the audit trail of a ticket, so that I can see who changed status, priority, assignment or effort, and when.

### Acceptance Criteria
1. Given a ticket whose priority, status, assignment and effort were each changed once, when the delivery manager views its audit trail, then it shows 4 entries, each with the user, date and time, old value and new value.
2. Given an L1 support engineer or an L2/L3 support engineer, when they view the audit trail of a ticket, then they see the same entries.
3. Given a client user, when they try to view the audit trail of their organization's ticket, then access is refused.
4. Given any user, when they try to edit or delete an audit entry, then the change is refused (A-016).

### Business Rules
BR B-22

### NFR References
NFR N-6, NFR N-4

### Priority
Must: audit of every status, priority, assignment and effort change (INT-002 Q11). Goal: BRF-001 G-3, matching PRS F-8 (audit trail), which serves PRS G-3 (one tool instead of the shared mailbox and spreadsheet) and so BRF-001 G-3.

---

## Story S-24: Delivery manager maintains the company holiday list

### Story Statement
As a delivery manager (PER P-3), I want to enter and keep current each year the Applexus company holiday list in APLX AMS, so that SLA timers do not count holiday dates.

### Acceptance Criteria
1. Given the delivery manager adds 2027-01-26 (a Tuesday) to the company holiday list before that date, when a P3 ticket raised at 10:00 IST on Monday 2027-01-25 has its elapsed business time counted, then 2027-01-26 contributes 0 business hours (BR B-2).
2. Given 2027-03-15 (a Monday) was on the company holiday list, when the delivery manager removes it before that date, then 2027-03-15 counts as a business day of 9 business hours (BR B-2).
3. Given an L1 support engineer, an L2/L3 support engineer or a client user, when they try to add or remove a date on the company holiday list, then the change is refused (BR B-21).
4. Given a P3 ticket raised at 09:00 IST on Monday 2027-02-01 whose resolution clock has counted 3 business hours by 12:00 IST, when the delivery manager adds 2027-02-01 to the company holiday list at 12:00 IST, then the 3 business hours stay counted and no further business time is counted on 2027-02-01 after 12:00 IST (BR B-2, OQ-050).

### Business Rules
BR B-2, BR B-21

### NFR References
NFR N-1

### Priority
Must: business hours exclude holiday dates (INT-002 Q2); the list is the Applexus company holiday list, maintained each year by the delivery manager (OQ-041 answered, Mohanasunder, 2026-10-17; BRF-001 G-1). A change applies from the time of the change onward, with no recalculation of time already counted (OQ-050 answered, Mohanasunder, 2026-10-17).

---

## Story S-25: Support engineer changes or deletes their own effort entry

### Story Statement
As an L1 support engineer (PER P-1) or an L2/L3 support engineer (PER P-2), I want to change or delete my own effort entries until the end of their month, so that mistakes are fixed before the month closes.

### Acceptance Criteria
1. Given support engineer X recorded an effort entry of 1.5 hours dated 2026-11-02, when X changes it to 2 hours on 2026-11-20, then the change is saved and the audit trail holds old value 1.5, new value 2, user X and the time (BR B-15, BR B-22).
2. Given support engineer X recorded an effort entry of 1.5 hours dated 2026-11-02, when X deletes it on 2026-11-25, then it no longer counts against the contract and the audit trail holds the deletion with old value 1.5, user X and the time (BR B-15, BR B-22).
3. Given an effort entry of X dated 2026-11-02, when X tries to change or delete it on 2026-12-01, then the change is refused and the entry keeps its values (BR B-15, A-025).
4. Given an effort entry recorded by support engineer X, when support engineer Y tries to change or delete it, then the change is refused (BR B-15).

### Business Rules
BR B-15, BR B-22

### NFR References
NFR N-6

### Priority
Must: effort entries need correction without a spreadsheet (OQ-048 answered, Mohanasunder, 2026-10-17; INT-002 Q11, Q14; BRF-001 G-3). "That month" is the calendar month of the effort entry's date (A-025, Confirmed by Mohanasunder, 2026-10-17).

---

## Story S-26: Delivery manager corrects an effort entry

### Story Statement
As a delivery manager (PER P-3), I want to correct any effort entry, including after its month has ended, so that contract use and the finance export are right.

### Acceptance Criteria
1. Given support engineer X recorded an effort entry of 2 hours dated 2026-10-15 on an hours bank contract with balance 70 hours, when the delivery manager changes it to 1.5 hours on 2026-11-10, then the change is saved, the hours bank balance is 70.5 hours, and the audit trail holds old value 2, new value 1.5, the delivery manager and the time (BR B-15, BR B-16, BR B-22).
2. Given the delivery manager correcting an effort entry, when the hours are 0 or negative, then the change is not saved (A-020).
3. Given a client user, when they try to change any effort entry, then the change is refused (BR B-15).
4. Given an effort entry recorded by support engineer X, when the delivery manager tries to delete it, then the deletion is refused and the entry keeps its values (BR B-15; Phase 2 review answers, 2026-10-17).

### Business Rules
BR B-15, BR B-16, BR B-22

### NFR References
NFR N-6

### Priority
Must: the delivery manager owns effort tracking (PRC M-3) and can correct any effort entry (OQ-048 answered, Mohanasunder, 2026-10-17; BRF-001 G-3). The delivery manager changes but cannot delete another user's effort entry (confirmed as written, Phase 2 review answers, 2026-10-17).

---

## Story S-27: Delivery manager ends a contract and sets up a new one

### Story Statement
As a delivery manager (PER P-3), I want to end a client organization's active contract and set up a new one, so that effort counts against the contract in force.

### Acceptance Criteria
1. Given client organization A has an active hours bank contract with hours bank balance 10 hours, when the delivery manager ends it, then organization A has no active contract and the ended contract keeps its effort entries and its balance of 10 hours (BR B-15, A-023).
2. Given client organization A has no active contract, when a support engineer tries to record effort on a ticket of organization A assigned to them, then no effort entry is saved (BR B-15, OQ-042).
3. Given organization A's contract has ended, when the delivery manager sets up a new active hours bank contract of 50 contracted hours, then organization A's hours bank balance shows 50 hours and effort entries saved after that count against the new contract (BR B-15, BR B-16, A-023).
4. Given a user who is not a delivery manager, when they try to end a contract, then the change is refused (BR B-21).

### Business Rules
BR B-15, BR B-16, BR B-21

### NFR References
NFR N-6

### Priority
Must: one active contract at a time needs a way to replace it (OQ-042 answered, Mohanasunder, 2026-10-17; INT-002 Q14; BRF-001 G-3). Balance of the ended contract is not carried over (A-023, Confirmed by Mohanasunder, 2026-10-17).

---

## Story S-28: Client user adds a comment on their client organization's ticket

### Story Statement
As a client user (PER P-4), I want to add a comment on my client organization's ticket in APLX AMS, so that I answer the AMS team without email and the SLA timers resume.

### Acceptance Criteria
1. Given a client user of client organization A, when they add a comment on a ticket of organization A, then the comment is saved on the ticket with the client user and the time, and internal users viewing the ticket see it.
2. Given a ticket of organization A in awaiting client with resolution elapsed time 2 business hours, when a client user of organization A adds a comment, then awaiting client is cleared automatically and the paused SLA timers resume from 2 business hours (BR B-6).
3. Given a ticket of organization A that is not in awaiting client, when a client user of organization A adds a comment, then the ticket status does not change.
4. Given a client user of organization A, when they try to add a comment on a ticket of organization B, then it is refused and no comment is saved (BR B-20).

### Business Rules
BR B-6, BR B-20, BR B-21

### NFR References
NFR N-2, NFR N-7

### Priority
Must: release 1 scope decision DEC-026 (Mohanasunder, 2026-10-17), part of SCP IS-4; client comments replace email replies and clear awaiting client (OQ-045 answered; BRF-001 G-1, G-3). Internal user comments: REQ S-29 (OQ-051 answered).

---

## Story S-29: Internal user adds a comment on a ticket

### Story Statement
As a support engineer (PER P-1 or PER P-2) or a delivery manager (PER P-3), I want to add a comment on a ticket that the client user can see, so that I ask for or give information without email.

### Acceptance Criteria
1. Given a ticket of client organization A, when a support engineer or the delivery manager adds a comment on it, then the comment is saved on the ticket with the user and the time, and client users of organization A viewing the ticket see it (BR B-6).
2. Given a ticket of organization A in awaiting client with resolution elapsed time 2 business hours, when an internal user adds a comment, then the ticket stays in awaiting client and its SLA timers stay paused at 2 business hours (BR B-6).
3. Given an internal user's comment on a ticket of organization A, when a client user of organization B lists or opens tickets, then the comment is not shown to them (BR B-20).
4. Given a new P2 ticket raised at 10:00 IST with no L1 action yet, when an L1 support engineer adds a comment on it at 11:00 IST, then the comment is the acknowledgement: the response clock stops at 1 business hour and the response target is met (BR B-4).

### Business Rules
BR B-4, BR B-6, BR B-20, BR B-21

### NFR References
NFR N-2, NFR N-7

### Priority
Must: internal users add comments visible to the client user; an internal comment does not clear awaiting client (OQ-051 answered, Mohanasunder, 2026-10-17); internal users comment on any ticket, and an L1 support engineer's comment counts as an L1 action (confirmed, Phase 2 review answers, 2026-10-17; under scope decision DEC-026, part of SCP IS-4; BRF-001 G-3).

---

## Story S-30: Delivery manager sets a temporary password

### Story Statement
As a delivery manager (PER P-3), I want to set a temporary password when I create a user account, and set a new temporary password when a user tells me outside APLX AMS that they forgot their password, so that every user can sign in.

### Acceptance Criteria
1. Given the delivery manager creates a user account with temporary password "Abcdefg1", when the account is saved, then the user signs in with that user account and "Abcdefg1" and is not asked to change the password (BR B-23).
2. Given the delivery manager sets a temporary password, when it has fewer than 8 characters or lacks an upper-case letter, a lower-case letter or a digit (for example "abcdefg1"), then the temporary password is refused (NFR N-5, OQ-044).
3. Given user X told the delivery manager outside APLX AMS that they forgot their password, and X's user account is locked after 5 failed sign-ins, when the delivery manager sets new temporary password "Bcdefgh2" on X's user account, then the lock clears at once, X signs in immediately with "Bcdefgh2", X's previous password is refused, and X is not asked to change the password (BR B-23, OQ-054).
4. Given a user who is not a delivery manager, when they try to set a temporary password on another user's user account, then the change is refused (BR B-21, BR B-23).

### Business Rules
BR B-21, BR B-23

### NFR References
NFR N-5

### Priority
Must: users need a first password and a way back in after forgetting it (SCR S-3 decision (a), (b) and (d), Mohanasunder, Product owner / BA, 2026-10-17; INT-002 Q7, Q8; SCP IS-4; BRF-001 G-4). No email and no self-service password reset in release 1. A temporary password set on a locked user account clears the lock at once (OQ-054 answered, Mohanasunder, 2026-10-17).

---

## Story S-31: User changes their own password

### Story Statement
As any signed-in user (PER P-1, PER P-2, PER P-3 or PER P-4), I want to change my own password, so that I replace a temporary password or an earlier password with one of my own.

### Acceptance Criteria
1. Given signed-in user X (an internal user or a client user), when X enters their current password and changes their own password to "Cdefghi3", then X's next sign-in succeeds with "Cdefghi3" and X's previous password is refused (BR B-23).
2. Given signed-in user X, when the new password has fewer than 8 characters or lacks an upper-case letter, a lower-case letter or a digit (for example "cdefghi3"), then the change is refused and X's previous password stays valid (NFR N-5, OQ-044).
3. Given signed-in user X who is not a delivery manager, when X tries to change the password of another user's user account, then the change is refused (BR B-23).
4. Given signed-in user X, when X enters a wrong current password while changing their own password, then the change is refused and X's previous password stays valid (BR B-23, OQ-053).

### Business Rules
BR B-23

### NFR References
NFR N-5

### Priority
Must: any signed-in user, internal or client, can change their own password (SCR S-3 decision (c), Mohanasunder, Product owner / BA, 2026-10-17; INT-002 Q7; SCP IS-4; BRF-001 G-4). The user enters their current password to change it (OQ-053 answered, Mohanasunder, 2026-10-17).

---

## Story S-32: Security events are recorded in the audit trail

### Story Statement
As a delivery manager (PER P-3), I want sign-ins, lockouts and password changes on every user account recorded in the audit trail like other audit entries, so that the use of a temporary password or a taken-over user account leaves a record of who did what, on which user account, and when.

### Acceptance Criteria
1. Given active, unlocked user account X, when X signs in with the correct password at 10:00:05 IST and a sign-in on X with a wrong password is refused at 10:01:10 IST, then the audit trail holds a successful sign-in entry and a failed sign-in entry, each with user account X and its date and time to the second (BR B-24).
2. Given user account X with 4 failed sign-ins, when a fifth sign-in with a wrong password is refused and X is locked (NFR N-5), and then a sign-in on X with the correct password is refused while X is locked, then the audit trail holds a failed sign-in entry, a user account lockout entry and a second failed sign-in entry for X, each with its date and time (BR B-24, OQ-065).
3. Given deactivated user account Y and the account name "user.unknown", which matches no user account, when a sign-in on Y and a sign-in with "user.unknown" are each refused, then the audit trail holds a failed sign-in entry for user account Y and a failed sign-in entry holding the account name "user.unknown" as typed, each with its date and time (BR B-24, OQ-065).
4. Given delivery manager D sets temporary password "Bcdefgh2" on user account X, and signed-in user Z changes their own password to "Cdefghi3", when each change is saved, then the audit trail holds a temporary password set entry with user D, user account X and the time, and an own password change entry with user Z, user account Z and the time; and a search of every audit entry for every password value entered during the test of AC-1 to AC-4 (the correct and wrong passwords entered at sign-in, "Bcdefgh2", "Cdefghi3" and the current password entered by Z) finds 0 matches (BR B-23, BR B-24).

### Business Rules
BR B-22, BR B-23, BR B-24

### NFR References
NFR N-6, NFR N-5, NFR N-4

### Priority
Must: security events are recorded in the audit trail like other audit entries, with no alerting and no new reporting (OQ-062 answered, Mohanasunder, Product owner / BA, 2026-10-17, chat; SCR S-4; trigger THR T-3, T-5). Every refused sign-in is a failed sign-in, and an unknown account name is recorded as typed (OQ-065 answered, Mohanasunder, 2026-10-17, chat). Goal: BRF-001 G-3, as REQ S-23 (the audit trail is kept in the one tool, PRS F-8). Viewing: REQ S-33.

---

## Story S-33: Users view security events

### Story Statement
As an internal user (PER P-1, PER P-2 or PER P-3), I want to view security events, all user accounts' as the delivery manager and my own otherwise, so that misuse of a user account can be seen.

### Acceptance Criteria
1. Given security events recorded for user accounts X and Y and a failed sign-in with the account name "user.unknown", when the delivery manager views security events, then they see the security events of any user account they choose, X or Y, and the failed sign-in for "user.unknown", each with the event, the user, the user account or account name typed, and the date and time (BR B-24, OQ-064).
2. Given an L1 support engineer, an L2/L3 support engineer or a delivery manager with user account W, when they view their own security events, then they see every security event of user account W (BR B-24, OQ-064).
3. Given an L1 support engineer or an L2/L3 support engineer with user account W, when they try to view the security events of another user account, then access is refused (BR B-24, OQ-064).
4. Given a client user, when they try to view any security event, their own included, then access is refused; and given any user, when they try to edit or delete a security event entry, then the change is refused (BR B-22, BR B-24, OQ-064).

### Business Rules
BR B-22, BR B-24

### NFR References
NFR N-6, NFR N-7

### Priority
Must: who views security events was decided with OQ-064 (answered, Mohanasunder, Product owner / BA, 2026-10-17, chat; SCR S-4): the delivery manager views all security events, per user account; each internal user views their own; client users view none. No alerting and no new reporting (OQ-062). Goal: BRF-001 G-3, as REQ S-23 (the audit trail is kept in the one tool, PRS F-8).

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
Logged in `docs/logs/assumptions-log.md`:
- Confirmed by Mohanasunder, 2026-10-17: A-009 MTTR definition (REQ S-13; OQ-039); A-011 finance export balance at month end (REQ S-17; OQ-043); A-013 assigned support engineer sets awaiting client (REQ S-8; OQ-045); A-017 an L1 action is a change recorded on the ticket, not a view (REQ S-3, S-4, S-5); A-018 paused SLA timers recalculate on a priority change (BR B-7).
- Rejected: A-012 password policy (REQ S-21), replaced by the OQ-044 answer.
- Open: A-014 SLA timer states per clock (REQ S-10); A-015 calendar month period and ticket counts (REQ S-13); A-016 audit entries read-only with old and new value (REQ S-23); A-019 sign-in refusal does not say which of account name or password was wrong (REQ S-21 AC-2); A-020 effort entry hours above 0 (REQ S-15 AC-2, S-26 AC-2); A-021 "no tickets" when a % denominator is 0 (REQ S-13 AC-2); A-022 ticket status names (GLO-001).
- Confirmed by Mohanasunder, 2026-10-17, stated as rules: A-023 ended contract keeps its balance, nothing carried over (REQ S-27); A-024 a ticket not assigned to an L2/L3 support engineer counts as assigned to every L1 support engineer (REQ S-8, S-15); A-025 "end of that month" is the end of the calendar month of the effort entry's date (REQ S-25 AC-3).
- A-008 supported browsers (NFR N-8), carried from PIB-002.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
Logged in `docs/logs/open-questions-log.md`, owner Mohanasunder. Answered 2026-10-17 (Mohanasunder, chat) and applied: OQ-037 (REQ S-7 AC-4), OQ-038 (S-17 AC-4), OQ-039 (S-13 AC-3), OQ-041 (S-24), OQ-042 (S-16 AC-4, S-27), OQ-043 (S-17 AC-3), OQ-044 (S-21 AC-3, AC-4), OQ-045 (S-8, S-28; DEC-026), OQ-046 (S-4 AC-1), OQ-047 (S-13, S-14 AC-4), OQ-048 (S-15 AC-4, S-25, S-26). Also answered 2026-10-17: OQ-049 MTTR baseline in business days (REQ S-13); OQ-050 holiday list change applies from the change onward (REQ S-24 AC-4); OQ-051 internal user comments (REQ S-29).
- Raised by SCR S-3 and Answered 2026-10-17 (Mohanasunder, chat): OQ-053 the user enters their current password to change it (REQ S-31 AC-1, AC-4); OQ-054 a new temporary password clears the lock at once (REQ S-30 AC-3). No open question remains for these stories.
- SCR S-4: OQ-062 Answered 2026-10-17 (Mohanasunder, chat): the 5 security events are recorded in the audit trail (REQ S-32). Raised by SCR S-4 and Answered 2026-10-17 (Mohanasunder, chat): OQ-064 the delivery manager views all security events, each internal user their own, client users none (REQ S-33); OQ-065 every refused sign-in is a failed sign-in, an unknown account name recorded as typed (REQ S-32 AC-2, AC-3). No open question remains for these stories.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason'.
     Cite individual stories as REQ S-N; cite individual criteria as REQ S-N AC-n. -->
- Upstream: PIB-002 v0.1; INT-002 v0.1; SCR S-3; SCR S-4; NFR-001 v0.3 (N-5, N-6); SUM-001 v0.3; BRF-001 v0.2 (G-1 to G-4); SCP-001 v0.2 (IS-1 to IS-5); PER-001 v0.2 (P-1 to P-4); PRC-001 v0.2 (M-1 to M-3); RSK-001 v0.2 (R-6).
- Related Phase 2: EPC-001 (epics list REQ S-N), BR-001, NFR-001, BKL-001, PRS-001, GLO-001.
- Goal links (one rule): each story's Priority line cites the brief goals the story itself serves, as `BRF-001 G-n`; the Goal / KPI column of `docs/logs/traceability-matrix.md` holds the story's epic and exactly those goals. Each goal cited is also cited by the story's epic in EPC-001.
- Story to scope: IS-1 REQ S-1 to S-11, S-24; IS-2 REQ S-12 to S-14; IS-3 REQ S-15 to S-17, S-19, S-25 to S-27; IS-4 REQ S-1, S-2, S-14, S-20, S-21, S-28, S-29, S-30, S-31 (scope decision in § Input References; S-30, S-31 by SCR S-3); IS-5 REQ S-22 (and data boundary criteria in S-1, S-2, S-12, S-14, S-18, S-28, S-29); setup (INT-002 Q8) REQ S-18 to S-20, S-24, S-30; audit (Q11) REQ S-23; security events in the audit trail (SCR S-4) REQ S-32, S-33.
- Downstream: Phase 5 feature acceptance cites REQ S-N AC-n; Phase 7 test cases (not yet created).

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Every story has a unique S-N ID; IDs are consecutive and never reused
- [x] Every story has at least one Given/When/Then acceptance criterion
- [x] Criteria are numbered AC-1, AC-2, … within each story; never renumbered after approval
- [x] Business rules reference BR B-N; NFRs reference NFR N-N
- [x] Persona citations use PER P-N format
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
