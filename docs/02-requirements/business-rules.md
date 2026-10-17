---
id: BR-001
title: APLX AMS: Business Rules
phase: 2
version: 0.3
template: business-rule
template_version: 2.0
status: Approved
author_agent: requirements-analyst
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# APLX AMS: Business Rules

> **Collection file.** All business rules for this project live in this one file. Add one `## Rule B-N` section per rule; never create a separate BR-NNN file. Downstream artifacts reference a specific rule as `BR B-N` (e.g. `BR B-3`).

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- PIB-002 v0.1 § Interview Answers (Q1 to Q16, Q9a, Q12a, Q14a), § Constraints, § Assumptions.
- INT-002 v0.1 § Questions And Answers (evidence record; answers by Mohanasunder, 2026-10-17).
- SUM-001 v0.3 § Decisions, § Constraints Set.
- BRF-001 v0.2 § Business Goals And KPIs (G-1 to G-4).
- SCP-001 v0.2 § In Scope (IS-1 to IS-5), § Out Of Scope (OS-1 to OS-4).
- PER-001 v0.2 § Persona P-1 to P-4.
- PRC-001 v0.2 § Process M-1 to M-3.
- RSK-001 v0.2 § Risk R-4, § Risk R-5, § Risk R-6.
- Answered open questions OQ-004, OQ-022, OQ-026 to OQ-028, OQ-034 to OQ-051 and decisions DEC-022, DEC-025, DEC-026 (`docs/logs/`).
- SCR S-3 (`docs/logs/spec-changes.md`): password set, reset and change, decided by Mohanasunder (Product owner / BA), chat, 2026-10-17.
- SCR S-4 (`docs/logs/spec-changes.md`): security events in the audit trail, OQ-062 answered by Mohanasunder (Product owner / BA), chat, 2026-10-17.
- NFR-001 v0.3 § NFR N-5, § NFR N-6.

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: the business rules of APLX AMS release 1: SLA targets, the business-hours calendar, SLA timer start, stop and pause, priority change, SLA timer states, the L1 escalation flag, hand-back and closure, the response % and resolution % formulas, MTTR, the monthly client report, contract and effort rules, the finance export, the client data boundary, roles and setup, the audit trail, password set, reset and change (B-23, SCR S-3), and security events in the audit trail (B-24, SCR S-4). Terms follow the domain glossary GLO-001.

Does not cover: how rules are built (screens, colours, layout, endpoints, tables, technology; Phases 3 and 4), or NFR targets (NFR-001). Where a source left a value open, the rule names the open question and the labeled assumption (A-NNN) it uses.

---

## Rule B-1: Standard SLA targets per priority

### Rule
Every ticket has a response target and a resolution target set by its priority, the same for every client organization (standard SLA):

| Priority | Response target | Resolution target |
| --- | --- | --- |
| P1 | 1 business hour | 4 business hours |
| P2 | 4 business hours | 1 business day (9 business hours) |
| P3 | 1 business day (9 business hours) | 3 business days (27 business hours) |
| P4 | 2 business days (18 business hours) | 5 business days (45 business hours) |

A target given in days is converted at 1 business day = 9 business hours (OQ-040 answered by Mohanasunder, 2026-10-17: 1 day = 9 h, 3 days = 27 h, 5 days = 45 h).

### Source
OQ-004 answer (Mohanasunder, 2026-10-17; standard SLA for all clients); SCP-001 v0.2 § In Scope IS-1; PIB-002 v0.1 § Constraints. Day-to-hours conversion: OQ-040 answer (Mohanasunder, 2026-10-17; A-010 Confirmed).

### Applies To
REQ S-1, REQ S-4, REQ S-9, REQ S-10, REQ S-11, REQ S-13

---

## Rule B-2: Business-hours calendar

### Rule
SLA timers count business hours only: 09:00 to 18:00 IST, Monday to Friday, excluding the dates on the company holiday list. The company holiday list is the Applexus company holiday list; the delivery manager enters it in APLX AMS and keeps it current each year. One calendar applies to every ticket in release 1. Time outside business hours and on holiday dates is not counted. A date added to or removed from the company holiday list applies from the time of the change onward; business time already counted on running SLA timers is not recalculated (OQ-050).

### Source
INT-002 v0.1 Q2 (Mohanasunder, 2026-10-17). Which list and who keeps it: OQ-041 answered (Mohanasunder, 2026-10-17, chat): the Applexus company holiday list, entered and maintained each year by the delivery manager. Effect of a change: OQ-050 answered (Mohanasunder, 2026-10-17, chat).

### Applies To
REQ S-9, REQ S-10, REQ S-11, REQ S-13, REQ S-24

---

## Rule B-3: SLA timer start

### Rule
The response clock and the resolution clock of a ticket both start at the time the ticket is raised. A ticket raised outside business hours starts counting at the next business-hours start (09:00 IST on the next business day).

### Source
INT-002 v0.1 Q3 (clocks start when the ticket is raised); Q2 (business hours only).

### Applies To
REQ S-1, REQ S-9

---

## Rule B-4: Response clock stop

### Rule
The response clock stops at the acknowledgement of the ticket: the first action on the ticket by an L1 support engineer (PER P-1). Any first L1 action counts, whether an explicit acknowledgement or another action, for example a priority change (BR B-7), an assignment to an L2/L3 support engineer, or a comment (BR B-6; confirmed rule, Phase 2 review answers, 2026-10-17). An action is a change recorded on the ticket; opening or viewing the ticket is not an action (A-017, confirmed rule, Phase 2 review answers, 2026-10-17). Later L1 actions do not change the stop time. Actions by other users do not stop the response clock. The response target is met only if the response clock stops before the elapsed business time reaches 100% of the response target; a stop at exactly 100% of the response target or later is breached (BR B-8). When the first L1 action is a priority change, the response clock stops at that action and met or breached is judged against the new priority's response target (OQ-046).

### Source
INT-002 v0.1 Q3. Confirmed rules, Phase 2 gate answers, 2026-10-17 (Mohanasunder, Product owner / BA, chat): any first action by an L1 support engineer counts as acknowledgement and stops the response clock (VAL-009 M-3); a stop at exactly 100% of the target is breached, a target is met only if its clock stops before 100% (VAL-009 M-1). What counts as an action: A-017, Confirmed by Mohanasunder, Phase 2 review answers, 2026-10-17. An L1 support engineer's comment counts as an L1 action: confirmed by Mohanasunder, Phase 2 review answers, 2026-10-17 (VAL R4-1). First action is a priority change: OQ-046 answered (Mohanasunder, 2026-10-17, chat): judged against the new priority's response target.

### Applies To
REQ S-3, REQ S-4, REQ S-5, REQ S-9, REQ S-13, REQ S-29

---

## Rule B-5: Resolution clock stop

### Rule
The resolution clock stops when the ticket's status is set to Resolved. The resolution target is met only if the resolution clock stops before the elapsed business time reaches 100% of the resolution target; a stop at exactly 100% of the resolution target or later is breached (BR B-8).

### Source
INT-002 v0.1 Q3, Q16. Confirmed rule, Phase 2 gate answers, 2026-10-17 (Mohanasunder, Product owner / BA, chat; VAL-009 M-1): a clock that stops at exactly 100% of its target is breached.

### Applies To
REQ S-6, REQ S-7, REQ S-9, REQ S-13

---

## Rule B-6: Pause while awaiting client

### Rule
While a ticket's status is awaiting client, its running SLA timers are paused; paused time is not counted as elapsed time. The SLA timers resume when the status leaves awaiting client. Only the assigned support engineer of the ticket sets awaiting client, and may clear it. A comment added by a client user on the ticket clears awaiting client automatically. A comment added by an internal user does not clear awaiting client. Client users add comments on their own client organization's tickets, and internal users (support engineers and the delivery manager) add comments on any ticket (confirmed as written, Phase 2 review answers, 2026-10-17), visible to the client users of the ticket's client organization (DEC-026). A ticket not assigned to an L2/L3 support engineer counts as assigned to every L1 support engineer; a ticket assigned to an L2/L3 support engineer counts as assigned to that engineer only (A-024, Confirmed).

### Source
INT-002 v0.1 Q3 (paused while awaiting client). OQ-045 answered (Mohanasunder, 2026-10-17, chat): the assigned support engineer sets awaiting client; a client user's comment clears it automatically; client users can add comments in release 1 (scope decision DEC-026, part of SCP-001 IS-4). A-013 Confirmed. Internal user comments, visible to the client user, and not clearing awaiting client: OQ-051 answered (Mohanasunder, 2026-10-17, chat), under DEC-026. A-024 Confirmed by Mohanasunder, 2026-10-17.

### Applies To
REQ S-8, REQ S-9, REQ S-28, REQ S-29

---

## Rule B-7: Priority at raise and priority change

### Rule
The client user sets the priority (P1 to P4) when raising a ticket. After the raise, only an L1 support engineer may change the priority, and must enter a reason. The priority cannot be changed once the ticket is Resolved (or Closed); such a change is refused. On a change, only the SLA timers still running recalculate: each takes the target of the new priority (BR B-1), measured from the original raise time, and its state (BR B-8) is evaluated against the new target. A timer paused while awaiting client counts as running for this rule (A-018, confirmed rule, Phase 2 review answers, 2026-10-17). A stopped SLA timer, met or breached, keeps its result. When the priority change is the first L1 action, it stops the response clock (BR B-4), and that stop is judged against the new priority's response target (OQ-046). The L1 escalation point moves to 50% of the new resolution target (BR B-10).

### Source
OQ-027 answer (the client states the priority; L1 records it); INT-002 v0.1 Q6 (L1 may change priority with a reason; targets recalculate from the raise time). Confirmed rules, Phase 2 gate answers, 2026-10-17 (Mohanasunder, Product owner / BA, chat; VAL-009 M-2): only running clocks recalculate, from the raise time; stopped clocks, met or breached, keep their result; priority cannot be changed after the ticket is Resolved; the L1 50% escalation point moves with the new resolution target. Paused timers: A-018, Confirmed by Mohanasunder, Phase 2 review answers, 2026-10-17. Priority change as the first L1 action: OQ-046 answered (Mohanasunder, 2026-10-17, chat).

### Applies To
REQ S-1, REQ S-2, REQ S-4, REQ S-11

---

## Rule B-8: SLA timer states

### Rule
Each SLA timer (the response clock and the resolution clock, evaluated separately, assumption A-014) is in one of these states:
- On track: elapsed business time below 90% of the target.
- At risk: elapsed business time at or above 90% and below 100% of the target, while the timer runs.
- Breached: elapsed business time at or above 100% of the target, whether the timer is running or stopped. A timer that stops at exactly 100% of its target is breached.
- Met: the timer stopped before its elapsed business time reached 100% of the target.
A stopped timer keeps its final state (met or breached), including after a priority change (BR B-7).

### Source
INT-002 v0.1 Q12a (at risk at 90% of elapsed target time; breached at 100%); Q12 (colour-coded SLA timers; colour and layout are Phase 4). Confirmed rule, Phase 2 gate answers, 2026-10-17 (Mohanasunder, Product owner / BA, chat; VAL-009 M-1): a stop at exactly 100% is breached; met only if stopped before 100%. Per-timer evaluation: A-014.

### Applies To
REQ S-3, REQ S-4, REQ S-10, REQ S-12, REQ S-13

---

## Rule B-9: SLA alerts are in-app only

### Rule
SLA risk and breach alerts are shown inside APLX AMS only, as SLA timer states on tickets and the live dashboard. APLX AMS sends no email for SLA risk or breach.

### Source
INT-002 v0.1 Q12. Closure is not an SLA alert: the client user learns of closure from the Closed status only (BR B-11; OQ-037). The finance export leaves APLX AMS by download only (BR B-18; OQ-038).

### Applies To
REQ S-10, REQ S-12

---

## Rule B-10: L1 escalation flag

### Rule
L1's own target is 50% of the ticket's resolution target. When the resolution clock reaches 50% of the resolution target while the ticket is still with L1 (not Resolved and not assigned to an L2/L3 support engineer), the ticket is flagged for escalation. The escalation flag stays visible until the ticket is assigned to an L2/L3 support engineer, set to Resolved, or cleared by a priority change as below. Example: P1 (4 business hours) is flagged at 2 business hours. When the priority changes (BR B-7), the escalation point moves to 50% of the new resolution target and the flag is re-evaluated at the change: a ticket still with L1 whose resolution elapsed time is at or above the new point is flagged; a flagged ticket whose elapsed time is below the new point (priority lowered) has its flag cleared, and the flag reappears when the elapsed time reaches the new point.

### Source
INT-002 v0.1 Q15 (OQ-034 answered); OQ-026 answer (L1 escalates when it cannot resolve within its target or the ticket needs functional or technical SAP skills). Confirmed rule, Phase 2 gate answers, 2026-10-17 (Mohanasunder, Product owner / BA, chat; VAL-009 M-2): the L1 50% escalation point moves with the new resolution target. Confirmed rule, Phase 2 review answers, 2026-10-17 (Mohanasunder, Product owner / BA, chat; VAL-010 R3-1): when the priority is lowered and the elapsed time falls below the new 50% point, the flag clears, is re-evaluated, and reappears when the elapsed time reaches the new point.

### Applies To
REQ S-4, REQ S-5, REQ S-11, REQ S-12

---

## Rule B-11: Hand-back and closure

### Rule
An L1 support engineer or an L2/L3 support engineer sets a ticket to Resolved. A Resolved ticket appears in the L1 queue for closure. Only an L1 support engineer closes a ticket, and only a Resolved ticket can be closed. On closure the client user sees the status Closed on the ticket in APLX AMS; APLX AMS sends no email or other message about the closure.

### Source
INT-002 v0.1 Q16 (OQ-035 answered: L2/L3 sets Resolved, the ticket returns to L1's queue); OQ-028 answer (L1 always closes); PRC-001 v0.2 § Process M-1 (M-1.4 L1 resolves). Closure notice: OQ-037 answered (Mohanasunder, 2026-10-17, chat): Closed status in the tool only, no email or other message.

### Applies To
REQ S-6, REQ S-7

---

## Rule B-12: Response % and resolution %

### Rule
For a client organization and a reporting period (calendar month in IST, assumption A-015), per priority and in total:
- Response % = (tickets whose response clock stopped in the period with the response target met) / (tickets whose response clock stopped in the period) x 100.
- Resolution % = (tickets whose resolution clock stopped in the period with the resolution target met) / (tickets whose resolution clock stopped in the period) x 100.
- When the denominator is 0, the % is shown as "no tickets", not 0% or 100% (assumption A-021).
- A ticket whose clock has not stopped by the period end is counted in the period in which its clock stops.
BRF-001 G-1 (SLA compliance %, baseline 80%, target 95%) is measured by resolution %; response % is reported but is not the goal measure. "Met" follows BR B-4, B-5 and B-8: a clock that stops at exactly 100% of its target is not met.

Comparison with the baseline: the 80% baseline comes from the delivery manager's month-end manual count from the shared spreadsheet (OQ-001, OQ-016, OQ-030); how that count treated response and resolution targets is not recorded (RSK R-4). Release 1 counts with business-hours SLA timers per ticket, so its resolution % is not like-for-like with the 80% baseline. Mohanasunder decided to keep the 80% baseline as stated, with no re-measurement (DEC-025, 2026-10-17).

### Source
INT-002 v0.1 Q4, Q4a; BRF-001 v0.2 § Business Goals And KPIs G-1; RSK-001 v0.2 § Risk R-4 (formula to be defined in Phase 2); PIB-002 v0.1 § Constraints (Measurement). Formula wording confirmed as written by Mohanasunder (Product owner / BA), Phase 2 review answers, 2026-10-17 (VAL-009 M-19). Period: A-015. Zero-denominator display: A-021. Report generation and publication: BR B-14 (OQ-047).

### Applies To
REQ S-13, REQ S-14

---

## Rule B-13: MTTR

### Rule
MTTR (mean time to resolve) for a client organization and a calendar month = the mean, over the tickets set to Resolved in that month, of each ticket's business time from raise to Resolved, excluding paused (awaiting client) time (BR B-6), expressed in business days of 9 business hours. Example: tickets Resolved after 9 and 18 business hours give MTTR 1.5 business days. The 3-day baseline of BRF-001 G-2 was in business days, so it is like-for-like with this definition (OQ-049).

### Source
BRF-001 v0.2 § Business Goals And KPIs G-2 (MTTR in days, baseline 3 days, target 1 day); INT-002 v0.1 Q13 (MTTR in the monthly client report). Definition: OQ-039 answered (Mohanasunder, 2026-10-17, chat); A-009 Confirmed. Baseline unit: OQ-049 answered (Mohanasunder, 2026-10-17, chat): business days.

### Applies To
REQ S-13, REQ S-14

---

## Rule B-14: Monthly client report content

### Rule
For each client organization and each calendar month (A-015), the monthly client report holds: response % and resolution % per priority and in total (BR B-12); the list of tickets with a breached response or resolution target; MTTR (BR B-13); and ticket counts per priority: tickets raised, set to Resolved, and Closed in the month (A-015). The delivery manager generates the monthly client report, reviews it, and publishes it. Client users of that client organization see a monthly client report only once it is published; they view it in APLX AMS and download it as Excel or PDF.

### Source
INT-002 v0.1 Q13; OQ-029 answer (today emailed monthly as Excel/PDF). Ticket count breakdown and period: A-015. Generation and publication: OQ-047 answered (Mohanasunder, 2026-10-17, chat): the delivery manager generates and publishes the report after review; client users see it once published.

### Applies To
REQ S-13, REQ S-14

---

## Rule B-15: One active contract per client organization

### Rule
Each client organization has at most one active contract at a time, of type hours bank or fixed fee. All effort hours recorded on that client organization's tickets while the contract is active count against that contract. No effort entry can be recorded on a ticket of a client organization with no active contract. The delivery manager can end the active contract and then set up a new one; an ended contract keeps its effort entries and its hours bank balance, and nothing carries over to the new contract (A-023, Confirmed). Effort entries:
- Each support engineer records their own effort (OQ-015 answer; A-007 Confirmed), only on tickets assigned to them (assignment per BR B-6; A-024, Confirmed); an effort entry must have more than 0 hours (assumption A-020).
- A support engineer may change or delete their own effort entries until the end of the calendar month (IST) of the effort entry's date (A-025, Confirmed); after that, the change or deletion is refused.
- The delivery manager can correct (change) any effort entry at any time, but cannot delete it (confirmed as written, Phase 2 review answers, 2026-10-17).
- Every saved, changed or deleted effort entry is recorded in the audit trail (BR B-22).

### Source
INT-002 v0.1 Q14 (OQ-036 answered); OQ-008 answer (contract types hours bank and fixed fee); OQ-015 answer (each engineer records their own effort). Hours above 0: A-020. No active contract, ending and replacing a contract: OQ-042 answered (Mohanasunder, 2026-10-17, chat); balance of an ended contract: A-023, Confirmed by Mohanasunder, 2026-10-17. Effort entry changes: OQ-048 answered (Mohanasunder, 2026-10-17, chat): only on tickets assigned to them; own entries editable or deletable until the end of that month; delivery manager can correct any entry; all changes audited. "That month": A-025, Confirmed by Mohanasunder, 2026-10-17.

### Applies To
REQ S-15, REQ S-16, REQ S-19, REQ S-25, REQ S-26, REQ S-27

---

## Rule B-16: Hours bank balance

### Rule
For an hours bank contract, hours bank balance = contracted hours - the sum of effort hours recorded against the contract. Effort entries are still saved when the balance is 0 or below, and the balance may go negative. While the balance is 0 or below, the delivery manager sees a warning with the balance.

### Source
INT-002 v0.1 Q14 (remaining hours-bank balance in the finance export). Balance at or below 0: OQ-042 answered (Mohanasunder, 2026-10-17, chat).

### Applies To
REQ S-12, REQ S-16, REQ S-17, REQ S-19, REQ S-26, REQ S-27

---

## Rule B-17: Fixed-fee contract hours

### Rule
For a fixed fee contract, effort hours are recorded for visibility only: they are shown against the contract but do not count against any balance, and no hours bank balance is shown.

### Source
INT-002 v0.1 Q14a.

### Applies To
REQ S-16, REQ S-17, REQ S-19

---

## Rule B-18: Finance export content

### Rule
The finance export covers one calendar month and holds one row per effort entry recorded in that month, with these fields: client organization, contract, ticket, engineer, date, hours, remaining hours bank balance. The remaining hours bank balance is the balance at the end of the export month (month end), the same on every row of that contract; for a fixed fee contract the balance field is blank. The file format is Excel or CSV. The delivery manager downloads the finance export and emails it to finance outside APLX AMS; finance has no user account or role in APLX AMS.

### Source
INT-002 v0.1 Q14, Q14a; OQ-008 answer (monthly, Excel/CSV, to finance); SCP-001 v0.2 § In Scope IS-3 (finance does billing and invoicing outside APLX AMS, OS-1). Balance at month end: OQ-043 answered (Mohanasunder, 2026-10-17, chat); A-011 Confirmed. Channel: OQ-038 answered (Mohanasunder, 2026-10-17, chat).

### Applies To
REQ S-17

---

## Rule B-19: Ticket raise through the portal only

### Rule
Client users raise tickets in APLX AMS only; the shared mailbox is retired and no email is turned into a ticket. Each ticket is an incident or a service request, for one SAP application of the client user's own client organization, with a priority P1 to P4.

### Source
INT-002 v0.1 Q5; SCP-001 v0.2 § In Scope IS-1, IS-4 (SAP applications only, OS-2); PER-001 v0.2 § Persona P-4 Key Journey 1.

### Applies To
REQ S-1, REQ S-18

---

## Rule B-20: Client organization data boundary

### Rule
A client user sees and acts only on their own client organization's tickets, monthly client reports and SAP applications, never another client organization's. Internal users (PER P-1, P-2, P-3) see every client organization's data. The rule is built and tested with at least two client organizations' data, although the release 1 pilot has one client organization (Applexus).

### Source
INT-001 v0.1 Q14 (A-002 Confirmed); SCP-001 v0.2 § In Scope IS-5; DEC-022 (Mohanasunder, 2026-10-17); RSK-001 v0.2 § Risk R-6.

### Applies To
REQ S-1, REQ S-2, REQ S-12, REQ S-14, REQ S-18, REQ S-22, REQ S-28, REQ S-29

---

## Rule B-21: Roles and setup ownership

### Rule
Release 1 has four roles: L1 support engineer, L2/L3 support engineer, delivery manager, and client user. Every client user has the one client role (raise tickets, view their own client organization's tickets and statuses, add comments on their own client organization's tickets, and view their own client organization's published monthly client reports) and belongs to exactly one client organization. Finance has no role (OQ-038). Only the delivery manager sets up client organizations, SAP applications, contracts (including ending a contract) and user accounts, sets temporary passwords on user accounts (BR B-23), and maintains the company holiday list.

### Source
INT-002 v0.1 Q8; OQ-022 answer (one client role); PER-001 v0.2 (PER P-1 to P-4); SCP-001 v0.2 § In Scope IS-4. Comments: OQ-045, DEC-026. Contract end: OQ-042. Company holiday list: OQ-041. No finance role: OQ-038 (all answered by Mohanasunder, 2026-10-17, chat). Temporary passwords: SCR S-3 (Mohanasunder, 2026-10-17, chat).

### Applies To
REQ S-18, REQ S-19, REQ S-20, REQ S-21, REQ S-24, REQ S-27, REQ S-28, REQ S-29, REQ S-30

---

## Rule B-22: Audit trail

### Rule
Every change to a ticket's status, priority, assignment, or effort entries (an effort entry saved, changed or deleted) is recorded in the audit trail with the user who made it, the date and time, the old value and the new value (old and new value: assumption A-016). Internal users can view the audit trail; client users cannot. No user can edit or delete an audit entry (A-016). Security events are also recorded in the audit trail; their content and who views them follow BR B-24.

### Source
INT-002 v0.1 Q11. Old and new value and read-only entries: A-016. Effort entry changes and deletions audited: OQ-048 answered (Mohanasunder, 2026-10-17, chat).

### Applies To
REQ S-2, REQ S-4, REQ S-5, REQ S-7, REQ S-8, REQ S-15, REQ S-23, REQ S-25, REQ S-26, REQ S-32, REQ S-33

---

## Rule B-23: Password set, reset and change

### Rule
The delivery manager sets a temporary password on each user account when creating it. A user who forgets their password asks the delivery manager outside APLX AMS, and the delivery manager sets a new temporary password on that user account, which replaces the previous password. Any signed-in user (internal user or client user) can change their own password, after entering their current password (OQ-053), and no other user's password. When the delivery manager sets a new temporary password on a user account locked after 5 failed sign-ins, the lock clears at once and the user can sign in immediately (OQ-054; NFR N-5). Every temporary password and every changed password meets the password policy (NFR N-5). No user is asked or forced to change their password, at first sign-in or after the delivery manager sets a new temporary password (lower security chosen knowingly). Release 1 has no password reset by email and no self-service password reset.

### Source
Binding source: SCR S-3 human decision (a) to (d), Mohanasunder (Product owner / BA), chat, 2026-10-17 (option C on VAL-013 F-1). Context: the behaviour was raised in the Phase 3 interview (INT-003 Q8). Password policy: NFR-001 v0.3 N-5 (OQ-044). OQ-053 and OQ-054 answered (Mohanasunder, 2026-10-17, chat).

### Applies To
REQ S-30, REQ S-31, REQ S-32

---

## Rule B-24: Security events in the audit trail

### Rule
Five security events are recorded in the audit trail, like other audit entries: a successful sign-in, a failed sign-in (every refused sign-in: wrong password, account name that matches no user account, deactivated user account or locked user account; OQ-065), a user account lockout (after 5 failed sign-ins, NFR N-5), a temporary password set by the delivery manager (BR B-23), and a user changing their own password (BR B-23). Each audit entry holds the event, the user who did it, the user account it concerns (for a failed sign-in with an account name that matches no user account: the account name as typed, OQ-065), and the date and time. No audit entry holds a password value (a password entered, a temporary password, a previous password or a new password); it records only that the event happened, who, when and which user account. The delivery manager can view all security events, per user account; each internal user can view their own security events; client users cannot view security events (OQ-064; for security events this replaces the BR B-22 rule that every internal user views the audit trail). No user can edit or delete a security event (as BR B-22). No other event is a security event in release 1 (user account deactivation is not one), and there is no alerting on security events and no new reporting.

### Source
Binding source: OQ-062 answered by Mohanasunder (Product owner / BA), chat, 2026-10-17 (SCR S-4), including that no password value is recorded. Viewing: OQ-064; refused sign-ins and unknown account names: OQ-065 (both answered by Mohanasunder, 2026-10-17, chat). Context: raised by the Phase 3 threat model (THR-001 Draft, T-3, T-5).

### Applies To
REQ S-32, REQ S-33

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
Logged in `docs/logs/assumptions-log.md`; Open unless marked Confirmed:
- A-009 (BR B-13), A-010 (BR B-1), A-011 (BR B-18), A-013 (BR B-6): Confirmed by Mohanasunder, 2026-10-17 (OQ-039, OQ-040, OQ-043, OQ-045); stated as rules, no longer assumptions.
- A-023 (BR B-15), A-024 (BR B-6, B-15), A-025 (BR B-15): Confirmed by Mohanasunder, 2026-10-17; stated as rules.
- A-014 (BR B-8): SLA timer states are evaluated separately for the response clock and the resolution clock.
- A-015 (BR B-12, B-14): the reporting period is the calendar month in IST; tickets count in the month their clock stops; ticket counts are raised, Resolved and Closed per priority.
- A-016 (BR B-22): audit entries hold the old and new value and cannot be edited or deleted.
- A-017 (BR B-4), Confirmed by Mohanasunder, Phase 2 review answers, 2026-10-17: an L1 action that counts as acknowledgement is a change recorded on the ticket; opening or viewing a ticket is not. Stated as a rule.
- A-018 (BR B-7), Confirmed by Mohanasunder, Phase 2 review answers, 2026-10-17: an SLA timer paused while awaiting client counts as running and recalculates on a priority change. Stated as a rule.
- A-020 (BR B-15): an effort entry must have more than 0 hours.
- A-021 (BR B-12): a % with a denominator of 0 is shown as "no tickets".

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
Logged in `docs/logs/open-questions-log.md`, owner Mohanasunder:
- Answered 2026-10-17 (Mohanasunder, chat) and applied: OQ-037 (BR B-9, B-11), OQ-038 (B-18, B-21), OQ-039 (B-13), OQ-040 (B-1), OQ-041 (B-2, B-21), OQ-042 (B-15, B-16), OQ-043 (B-18), OQ-045 (B-6, B-21), OQ-046 (B-4, B-7), OQ-047 (B-14), OQ-048 (B-15, B-22).
- Answered 2026-10-17 (Mohanasunder, chat) and applied: OQ-049 (BR B-13), OQ-050 (B-2), OQ-051 (B-6). 
- Raised by SCR S-3 and Answered 2026-10-17 (Mohanasunder, chat) and applied: OQ-053 (BR B-23, current password on change), OQ-054 (BR B-23, temporary password clears the lock). No open question remains for these rules.
- SCR S-4: OQ-062 Answered 2026-10-17 (Mohanasunder, chat) and applied (BR B-24). Raised by SCR S-4 and Answered 2026-10-17 (Mohanasunder, chat) and applied: OQ-064 (BR B-24, who views security events), OQ-065 (BR B-24, every refused sign-in is a failed sign-in; unknown account name as typed). No open question remains for these rules.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason'.
     Cite individual rules downstream as BR B-N (e.g. BR B-2). -->
- Upstream: PIB-002 v0.1; INT-002 v0.1; SCR S-3; SCR S-4; NFR-001 v0.3 (N-5, N-6); SUM-001 v0.3; BRF-001 v0.2 (G-1, G-2); SCP-001 v0.2 (IS-1 to IS-5, OS-1, OS-2); PER-001 v0.2; PRC-001 v0.2 (M-1 to M-3); RSK-001 v0.2 (R-4, R-5, R-6).
- Related Phase 2: REQ-001 (stories cite BR B-N), NFR-001, GLO-001, PRS-001, EPC-001.
- Downstream: Phase 4 backend design and UI spec; Phase 5 feature acceptance (not yet created).

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Every rule has a unique B-N ID; IDs are consecutive and never reused
- [x] Every rule has a source (stakeholder, document, or regulation)
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
