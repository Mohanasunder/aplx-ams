---
id: GLO-001
title: APLX AMS: Domain Glossary
phase: 2
version: 0.3
template: domain-glossary
template_version: 2.0
status: Approved
author_agent: requirements-analyst
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# APLX AMS: Domain Glossary

> **Single file.** There is exactly one domain glossary per project. Always use `--id GLO --out docs/02-requirements/domain-glossary.md` when calling `new_artifact.py`; never auto-name as `GLO-NNN.md`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved): brief, personas, scope, as-is process map -->
- BRF-001 v0.2 § Business Goals And KPIs, § Stakeholders.
- PER-001 v0.2 § Persona P-1 to P-4.
- SCP-001 v0.2 § In Scope, § Out Of Scope.
- PRC-001 v0.2 § Process M-1 to M-3.
- PIB-002 v0.1 § Interview Answers, § Constraints (glossary candidates listed under Producer pointers).
- INT-002 v0.1 § Questions And Answers.
- Answers to OQ-037 to OQ-051 and the Phase 2 review answers, 2026-10-17 (Mohanasunder, 2026-10-17, chat); DEC-026.
- SCR S-3 (`docs/logs/spec-changes.md`): password set, reset and change, decided by Mohanasunder (Product owner / BA), chat, 2026-10-17.
- SCR S-4 (`docs/logs/spec-changes.md`): security events in the audit trail, OQ-062 answered by Mohanasunder (Product owner / BA), chat, 2026-10-17.
- NFR-001 v0.3 § NFR N-5, § NFR N-6.

## Purpose And Scope
<!-- guidance: Business terms of this product, so each has one meaning for people and agents. Methodology terms stay in .ai/standards/glossary.md -->
Covers: the business terms of APLX AMS used in BRF-001, PIB-002, the stories and criteria (REQ-001), the rules (BR-001), the NFRs (NFR-001) and PRS-001, each defined once with its source and the synonyms to avoid. Stories, criteria and rules use exactly these terms.

Does not cover: methodology terms (epic, story, feature, NFR, gate), which stay in `.ai/standards/glossary.md`. Note: CLAUDE.md names this file `docs/02-requirements/GLO-001.md`; the template requires `docs/02-requirements/domain-glossary.md`, which is used here (PIB-002 § Constraints, producer pointers). The front matter ID is GLO-001 because `scripts/new_artifact.py` requires the `PREFIX-NNN` form.

## Terms
<!-- guidance: Table with header | Term | Definition | Avoid | Example | Source |. One row per business term. Definition: one or two sentences. Avoid: synonyms that must not be used for this term, comma separated, or '-'. Source: the BRF-, PER-, REQ-, or BR- ID where the term comes from. Checked by scripts/glossary_check.py -->
| Term | Definition | Avoid | Example | Source |
| --- | --- | --- | --- | --- |
| APLX AMS | The internal AMS delivery tool for the company's support of client organizations' SAP applications, which client users also sign in to in release 1. | - | Client users raise tickets in APLX AMS. | BRF-001 Problem Statement |
| Client organization | An organization whose SAP applications the AMS team supports; it owns tickets, a contract, SAP applications and client users. Release 1 pilot: one client organization, Applexus. | customer, tenant | Applexus is the pilot client organization. | SCP-001 IS-5; BRF-001 Stakeholders |
| Client user | A person from a client organization who signs in to raise tickets, view their client organization's tickets and statuses, add comments on their client organization's tickets, and view their client organization's published monthly client reports (one client role); PER P-4. | end user | An Applexus staff member raises a P2 incident. | PER-001 P-4; BR-001 B-21; DEC-026 |
| L1 support engineer | AMS team member at level L1 who acknowledges, triages, changes priority, escalates, resolves and closes tickets; PER P-1. | - | The L1 support engineer closes the Resolved ticket. | PER-001 P-1 |
| L2/L3 support engineer | AMS team member at level L2 or L3 who resolves tickets escalated by L1; PER P-2. | - | The L2/L3 support engineer sets the ticket to Resolved. | PER-001 P-2 |
| Support engineer | An L1 support engineer or an L2/L3 support engineer. | - | Each support engineer records their own effort. | PER-001 P-1, P-2 |
| Delivery manager | Internal user who sets up client organizations, SAP applications, contracts (and ends them) and user accounts, sets temporary passwords on user accounts, maintains the company holiday list, monitors SLA, generates and publishes monthly client reports, reviews and corrects effort entries, and downloads the finance export to email to finance; PER P-3. | - | The delivery manager publishes the September 2026 report. | PER-001 P-3; INT-002 Q8; OQ-038, OQ-041, OQ-042, OQ-047, OQ-048; BR-001 B-23 |
| Internal user | An L1 support engineer, L2/L3 support engineer or delivery manager; not a client user. | - | Internal users see every client organization's tickets. | INT-002 Q11; BR-001 B-20 |
| User account | The APLX AMS sign-in account of one person (staff or client user), with a password and a role; a client user's account belongs to one client organization. Created, changed and deactivated only by the delivery manager, who also sets its temporary password; the user can change their own password (BR-001 B-23). INT-002 Q7 calls it an "app account"; Phase 2 uses "user account". | - | The delivery manager deactivates a user account. | BR-001 B-21, B-23; INT-002 Q7, Q8 |
| Temporary password | A password the delivery manager sets on a user account when creating it, or when the user has told the delivery manager outside APLX AMS that they forgot their password. It meets the password policy, replaces the previous password, clears a lock after 5 failed sign-ins at once (OQ-054), and stays the user's password until the user changes it or the delivery manager sets a new one; the user is not asked to change it (SCR S-3 decision (d)). | - | The delivery manager sets temporary password "Abcdefg1" on a new user account. | BR-001 B-23; REQ-001 S-30; SCR S-3; OQ-054 |
| Password policy | The rule every password in APLX AMS meets: at least 8 characters, with at least 1 upper-case letter, 1 lower-case letter and 1 digit (OQ-044). | - | "Abcdefg1" meets the password policy; "abcdefg1" does not. | NFR-001 N-5; OQ-044; BR-001 B-23 |
| Role | The set of tasks a user account may do. Release 1 has four roles: L1 support engineer, L2/L3 support engineer, delivery manager and client user (one client role). | - | A user account with role client user. | BR-001 B-21; INT-002 Q8; OQ-022 |
| SAP application | An SAP application of a client organization that the AMS team supports; every ticket is for one SAP application. | - | A P1 incident on the client organization's SAP application. | SCP-001 IS-1; BRF-001 Constraints |
| Ticket | A record of one incident or one service request raised by a client user for one SAP application. | issue | Ticket raised 10:00 IST, priority P2. | SCP-001 IS-1; REQ-001 S-1 |
| Incident | A ticket type: something on an SAP application is not working as it should. | - | A client user raises an incident. | SCP-001 IS-1 |
| Service request | A ticket type: a request for a service on an SAP application, not a fault. | - | A client user raises a service request. | SCP-001 IS-1 |
| Priority | The urgency of a ticket, P1 (highest) to P4, set by the client user at raise and changeable only by an L1 support engineer with a reason, and not after the ticket is Resolved; it sets the SLA targets. On a change only running SLA timers recalculate, from the raise time (a timer paused while awaiting client counts as running: A-018, confirmed 2026-10-17); stopped timers keep their met or breached result; the escalation point moves to 50% of the new resolution target. Confirmed rule, Phase 2 gate answers, 2026-10-17. | severity | P3 changed to P1 with a reason. | BR-001 B-7, B-10; INT-002 Q6; Phase 2 gate answers, 2026-10-17 |
| Standard SLA | The one set of response and resolution targets per priority used for every client organization. | - | P1: 1 business hour response, 4 business hours resolution. | BR-001 B-1; SCP-001 IS-1 |
| Response target | The business time, set by the ticket's priority, before which the response clock must stop (acknowledgement) for the target to be met; a stop at exactly 100% of it is breached. | first response | P2 response target: 4 business hours. | BR-001 B-1, B-4, B-8 |
| Resolution target | The business time, set by the ticket's priority, before which the ticket must be set to Resolved for the target to be met; a stop at exactly 100% of it is breached. | - | P3 resolution target: 27 business hours. | BR-001 B-1, B-5, B-8 |
| Business hours | 09:00 to 18:00 IST, Monday to Friday, excluding the dates on the company holiday list; the only time SLA timers count. | working hours, office hours | 17:30 to 18:00 IST Friday is 0.5 business hours. | BR-001 B-2; INT-002 Q2 |
| Business day | One day of business hours, counted as 9 business hours when converting targets in days (OQ-040 answered). | - | P3 response target 1 business day = 9 business hours. | BR-001 B-1 |
| Company holiday list | The Applexus company holiday list: the holiday dates excluded from business hours, entered in APLX AMS and kept current each year by the delivery manager; a change applies from the time of the change onward, with no recalculation of business time already counted (OQ-050). INT-002 Q2 calls it the "India holiday list"; OQ-041 named it. | - | A date on the company holiday list adds 0 business hours. | BR-001 B-2; INT-002 Q2; OQ-041 |
| SLA timer | The count of elapsed business time of a ticket against one target. Each ticket has two SLA timers: the response clock and the resolution clock. | - | A P2 ticket's two SLA timers start at 10:00 IST. | BR-001 B-3, B-8; SCP-001 IS-1; INT-002 Q3, Q12 |
| Response clock | The SLA timer of a ticket against its response target; it starts at raise and stops at acknowledgement. | response timer | The response clock stops at 12:00 IST. | BR-001 B-3, B-4; INT-002 Q3 |
| Resolution clock | The SLA timer of a ticket against its resolution target; it starts at raise and stops when the ticket is set to Resolved. | resolution timer | The resolution clock stops at 15:00 IST. | BR-001 B-3, B-5; INT-002 Q3 |
| Acknowledgement | The first action on a ticket by an L1 support engineer, whether an explicit acknowledgement or another action such as a priority change or an assignment; it stops the response clock. An action is a change recorded on the ticket, not a view (A-017, confirmed rule, Phase 2 review answers, 2026-10-17). Confirmed rule, Phase 2 gate answers, 2026-10-17. A comment by an L1 support engineer is an action (Phase 2 review answers, 2026-10-17). When the acknowledgement is a priority change, it is judged against the new priority's response target (OQ-046). | - | A priority change at 10:30 IST is the acknowledgement. | BR-001 B-4; INT-002 Q3; Phase 2 gate answers, 2026-10-17; OQ-046 |
| Awaiting client | A ticket status set while the AMS team waits on the client user; SLA timers are paused while it is set. Only the assigned support engineer sets it; the assigned support engineer may clear it, and a client user's comment on the ticket clears it automatically (OQ-045; A-013 Confirmed). | on hold | Awaiting client for 4 business hours adds 0 elapsed time. | BR-001 B-6; INT-002 Q3; OQ-045 |
| Comment | Text added on a ticket in APLX AMS, saved with the user and the time: by a client user on their own client organization's ticket (visible to internal users), or by an internal user on any ticket (confirmed, Phase 2 review answers, 2026-10-17; visible to the client users of that ticket's client organization). Only a client user's comment clears awaiting client. | - | A client user adds a comment and the SLA timers resume. | BR-001 B-6; REQ-001 S-28, S-29; DEC-026; OQ-045, OQ-051 |
| On track | SLA timer state: elapsed business time below 90% of the target. | - | 30 minutes into a P1 response target. | BR-001 B-8 |
| At risk | SLA timer state: elapsed business time at or above 90% and below 100% of the target while the timer runs. | - | P1 response clock at 54 business minutes. | BR-001 B-8; INT-002 Q12a |
| Breached | SLA timer state: elapsed business time at or above 100% of the target, running or stopped; a timer that stops at exactly 100% of its target is breached. An SLA breach. Confirmed rule, Phase 2 gate answers, 2026-10-17. | SLA violation, overdue | P1 response clock stopped at exactly 1 business hour. | BR-001 B-4, B-5, B-8; INT-002 Q12a; Phase 2 gate answers, 2026-10-17 |
| Met | SLA timer state: the timer stopped before its elapsed business time reached 100% of the target; a met or breached result is kept after a priority change. Confirmed rule, Phase 2 gate answers, 2026-10-17. | - | Response clock stopped at 2 of 4 business hours. | BR-001 B-4, B-5, B-7, B-8; Phase 2 gate answers, 2026-10-17 |
| L1 target | 50% of a ticket's resolution target (the escalation point); L1's own time before the ticket is flagged for escalation. It moves with the resolution target when the priority changes. | - | P1 L1 target: 2 business hours. | BR-001 B-10; INT-002 Q15; Phase 2 gate answers, 2026-10-17 |
| Escalation flag | A mark on a ticket still with L1 once its L1 target has elapsed; removed when the ticket is assigned to an L2/L3 support engineer or set to Resolved. On a priority change it is re-evaluated against the new L1 target: if the priority is lowered and the elapsed time falls below the new point, the flag clears and reappears when the elapsed time reaches the new point. Confirmed rule, Phase 2 review answers, 2026-10-17. | - | Flag shown at 4.5 business hours on a P2 ticket. | BR-001 B-10; INT-002 Q15; Phase 2 review answers, 2026-10-17 |
| Escalate | To assign a ticket from L1 to an L2/L3 support engineer. | - | L1 escalates the ticket to an L2/L3 support engineer. | PRC-001 M-1; BR-001 B-10 |
| Triage | An L1 support engineer's check of a ticket to decide whether to resolve it at L1 or escalate it; escalate when L1 cannot resolve it within its L1 target or it needs functional or technical SAP skills. Done in APLX AMS. | - | L1 triages a new P2 ticket and escalates it. | PRC-001 M-1.3; OQ-026; INT-002 Q15 |
| Assignment | Who a ticket is currently given to: L1 (the L1 queue) or a named L2/L3 support engineer after escalation; every change of assignment is recorded in the audit trail. | - | Assignment changed from L1 to an L2/L3 support engineer. | BR-001 B-10, B-22; INT-002 Q11 |
| Assigned support engineer | The support engineer a ticket is currently assigned to: the named L2/L3 support engineer, or, when no L2/L3 support engineer is assigned, every L1 support engineer (A-024, Confirmed). Only the assigned support engineer records effort on the ticket and sets awaiting client. | assignee | The assigned support engineer sets awaiting client. | BR-001 B-6, B-15, B-22; INT-002 Q11; OQ-045, OQ-048; A-024 |
| L1 queue | The list of tickets for L1 support engineers: tickets still with L1 (not assigned to an L2/L3 support engineer and not Resolved) and Resolved tickets awaiting closure. | - | A Resolved ticket returns to the L1 queue. | BR-001 B-10, B-11; INT-002 Q16 |
| Ticket reference | The identifier of one ticket by which users find and open it, and which the finance export shows in its ticket field. | - | A client user opens a ticket by its ticket reference. | REQ-001 S-22; BR-001 B-18; INT-002 Q14 |
| Ticket status | The stage of a ticket: Open, Awaiting client, Resolved or Closed. Awaiting client, Resolved and Closed come from the sources; "Open" for any other stage is assumption A-022. | - | Status Resolved. | BR-001 B-6, B-11; INT-002 Q3, Q16; A-022 |
| Open ticket | A ticket whose status is Open or Awaiting client, that is, not Resolved and not Closed. | - | The live dashboard counts 5 open tickets. | REQ-001 S-12; A-022 |
| New ticket | A ticket with no L1 action yet; its response clock is running. | - | A new ticket raised at 10:00 IST. | BR-001 B-4; REQ-001 S-3 |
| Resolved | Ticket status set by a support engineer when the fault or request is dealt with; it stops the resolution clock and returns the ticket to the L1 queue. Not the same as Closed. | solved | The L2/L3 support engineer sets Resolved at 15:00 IST. | BR-001 B-5, B-11; INT-002 Q16 |
| Closed | Final ticket status, set only by an L1 support engineer on a Resolved ticket; the client user sees it in APLX AMS and receives no email or other message about it. | - | L1 closes the Resolved ticket. | BR-001 B-11; PRC-001 M-1; OQ-037 |
| Response % | Share of tickets whose response clock stopped in the period with the response target met. | - | 19 of 20 met = 95%. | BR-001 B-12; INT-002 Q4 |
| Resolution % | Share of tickets whose resolution clock stopped in the period with the resolution target met; the measure of BRF-001 G-1. | - | 18 of 20 met = 90%. | BR-001 B-12; INT-002 Q4a |
| SLA compliance % | The BRF-001 G-1 KPI (baseline 80%, target 95%), measured as resolution %. | - | September resolution % 90% is the SLA compliance %. | BRF-001 G-1; INT-002 Q4a |
| MTTR | Mean time to resolve: for a client organization and a calendar month, the mean over tickets set to Resolved in that month of each ticket's business time from raise to Resolved, excluding paused (awaiting client) time, in business days of 9 business hours. | - | Tickets Resolved after 9 and 18 business hours: MTTR 1.5 business days. | BRF-001 G-2; BR-001 B-13; OQ-039 |
| Monthly client report | The per-client-organization report for one calendar month: response % and resolution % per priority, breached tickets, MTTR and ticket counts. The delivery manager generates it, reviews it and publishes it; client users see it only once published, view it in APLX AMS and download it as Excel or PDF. | - | September 2026 report for Applexus, published by the delivery manager. | BR-001 B-14; INT-002 Q13; OQ-047 |
| Live dashboard | The internal view of open tickets, SLA timer states, escalation flags and hours bank balance across client organizations and SAP applications. | - | 2 at-risk tickets for Applexus. | REQ-001 S-12; INT-002 Q13 |
| Contract | The agreement between the company and a client organization against which effort counts; type hours bank or fixed fee. The delivery manager can end a contract; an ended contract is no longer active and keeps its effort entries and hours bank balance (A-023, Confirmed). | - | Applexus has an hours bank contract. | BR-001 B-15; INT-002 Q14; OQ-042 |
| Active contract | The one contract of a client organization that effort hours count against at a given time; no effort entry can be recorded for a client organization with no active contract. | - | A second active contract is refused. | BR-001 B-15; INT-002 Q14; OQ-042 |
| Hours bank | Contract type with a number of contracted hours that recorded effort draws down. | hour bank, prepaid | Hours bank of 100 contracted hours. | BR-001 B-16; BRF-001 Scope Summary |
| Contracted hours | The hours an hours bank contract holds before any effort is recorded. | - | 100 contracted hours. | BR-001 B-16 |
| Hours bank balance | Contracted hours minus effort hours recorded against an hours bank contract; it may go negative, and while it is 0 or below the delivery manager sees a warning. | - | 100 - 30 = 70 hours; 1 - 3 = -2 hours with a warning. | BR-001 B-16; INT-002 Q14; OQ-042 |
| Fixed fee | Contract type where effort hours are recorded for visibility only and do not count against a balance. | fixed price, retainer | 12 hours shown, no balance. | BR-001 B-17; INT-002 Q14a |
| Effort entry | Hours a support engineer records on one ticket assigned to them for one date. The support engineer may change or delete their own effort entry until the end of the calendar month of its date (A-025, Confirmed); the delivery manager can correct (change, not delete) any effort entry; every save, change and deletion is in the audit trail. | timesheet | 1.5 hours on 2026-11-02. | BR-001 B-15; INT-002 Q14; OQ-048 |
| Finance export | The monthly Excel or CSV file for finance with one row per effort entry: client organization, contract, ticket, engineer, date, hours, remaining hours bank balance (the balance at the end of the export month). The delivery manager downloads it and emails it to finance outside APLX AMS. | - | October 2026 finance export. | BR-001 B-18; INT-002 Q14; OQ-038, OQ-043 |
| Audit trail | The record of every change to a ticket's status, priority, assignment and effort entries, with user, date and time, visible to internal users only; it also records every security event, which the delivery manager views for all user accounts, each internal user for their own user account, and client users not at all (SCR S-4; OQ-064). | - | Priority P3 to P1 by an L1 support engineer at 11:00 IST. | BR-001 B-22, B-24; INT-002 Q11; OQ-062, OQ-064 |
| Account name | The name a person types at sign-in to identify their user account; when it matches no user account, a failed sign-in records it as typed (OQ-065). | - | A sign-in with account name "user.unknown" is refused and recorded as typed. | BR-001 B-24; REQ-001 S-21, S-32; OQ-065 |
| Audit entry | One record in the audit trail: a ticket change (user, date and time, old value and new value) or a security event (event, user, user account or the account name as typed, date and time). No user can edit or delete an audit entry, and no audit entry holds a password value. | - | A failed sign-in entry for a user account at 10:01:10 IST. | BR-001 B-22, B-24; NFR-001 N-6 |
| Security event | One of 5 events recorded in the audit trail, each on a user account or, for a failed sign-in with an account name that matches no user account, on the account name as typed: a successful sign-in, a failed sign-in (any refused sign-in: wrong password, account name that matches no user account, deactivated or locked user account; OQ-065), a user account lockout, a temporary password set by the delivery manager, or a user changing their own password. No other event is a security event in release 1; there is no alerting on security events. | - | The delivery manager sets a temporary password on a user account: one security event. | BR-001 B-24; REQ-001 S-32, S-33; OQ-062, OQ-065; SCR S-4 |
| Client data boundary | The rule that a client user sees and acts only on their own client organization's data. | - | A client user of A cannot open B's ticket. | BR-001 B-20; SCP-001 IS-5 |
| Portal | APLX AMS as used by client users to raise tickets; the only ticket intake in release 1. | - | Tickets are raised in the portal only. | INT-002 Q5; BR-001 B-19 |

## Ambiguities Resolved
<!-- guidance: Terms that were used with more than one meaning, and how each was settled (who decided; OQ- or DEC- ID), or 'None' -->
- SLA compliance %: BRF-001 G-1 did not say whether it covers response targets, resolution targets or both. Settled by Mohanasunder, 2026-10-17 (INT-002 Q4, Q4a): response % and resolution % are reported separately; G-1 is resolution %.
- Resolved vs Closed: as-is closure was one step by L1 (OQ-028). Settled by Mohanasunder, 2026-10-17 (INT-002 Q16, OQ-035): Resolved is set by a support engineer and stops the resolution clock; Closed is set only by L1 afterwards.
- L1 "target": OQ-026 used "its target" for L1 without a value. Settled by Mohanasunder, 2026-10-17 (INT-002 Q15, OQ-034): the L1 target is 50% of the resolution target; it is distinct from the response and resolution targets of the standard SLA.
- Client contact: PRC-001 M-2.4 names the "client contact" who receives the emailed report today; in release 1 the client user views the monthly client report in APLX AMS (INT-002 Q13). "Client contact" stays in Phase 1 text only; Phase 2 uses "client user".
- Business day in SLA targets: "1 day" means 9 business hours (3 days = 27, 5 days = 45). Settled by Mohanasunder, 2026-10-17 (OQ-040 answered).
- Acknowledgement: the rules and stories said "explicit acknowledgement" while this glossary said "any first L1 action" (VAL-009 M-3). Settled by Mohanasunder, Product owner / BA, Phase 2 gate answers, 2026-10-17: any first action by an L1 support engineer on the ticket counts as acknowledgement and stops the response clock.
- Met vs breached at exactly 100% (VAL-009 M-1). Settled by Mohanasunder, Phase 2 gate answers, 2026-10-17: a clock that stops at exactly 100% of its target is breached; a target is met only if its clock stops before 100%.
- Priority change on stopped clocks (VAL-009 M-2). Settled by Mohanasunder, Phase 2 gate answers, 2026-10-17: only running clocks recalculate (from the raise time); stopped clocks, met or breached, keep their result; no priority change after Resolved; the 50% escalation point moves with the new resolution target.
- SLA clock: earlier wording in Approved INT-002 (Q2, Q3) and PIB-002 (Q3); same meaning as "SLA timer" (preferred, SCP-001 IS-1, INT-002 Q12). Not listed under Avoid because Approved artifacts, including the human's own interview wording, use it; Phase 2 drafts use "SLA timer" only. The two SLA timers are named "response clock" and "resolution clock" (INT-002 Q3).
- App account: earlier wording in Approved INT-002 (Q7) and PIB-002 (Q7); same meaning as "user account" (preferred). Not listed under Avoid for the same reason; Phase 2 drafts use "user account" only.
- MTTR: settled by Mohanasunder, 2026-10-17 (OQ-039 answered; A-009 Confirmed): business time from raise to Resolved, paused time excluded, in business days of 9 business hours; monthly mean over tickets Resolved in the month. The 3-day BRF-001 G-2 baseline was in business days, like-for-like (OQ-049 answered, 2026-10-17).
- One-time temporary password: wording raised in the Phase 3 interview (INT-003 Q8, context only). Binding source: SCR S-3 human decision (d), Mohanasunder (Product owner / BA), chat, 2026-10-17: no forced password change at first sign-in or after a reset, so a temporary password stays the user's password until the user changes it or the delivery manager sets a new one; Phase 2 uses "temporary password". Not listed under Avoid because it is the human's own interview wording.
- India holiday list: earlier wording in Approved INT-002 (Q2) and PIB-002 (Q2). Settled by Mohanasunder, 2026-10-17 (OQ-041 answered): it is the Applexus company holiday list; Phase 2 drafts use "company holiday list". Not listed under Avoid because Approved artifacts use the earlier wording.

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-009 Confirmed 2026-10-17 (OQ-039): MTTR definition (term MTTR).
- A-010 Confirmed 2026-10-17 (OQ-040): 1 business day = 9 business hours (terms Business day, Standard SLA).
- A-013 Confirmed 2026-10-17 (OQ-045): the assigned support engineer sets awaiting client (term Awaiting client).
- A-023, A-024, A-025 Confirmed by Mohanasunder, 2026-10-17 (terms Contract, Assigned support engineer, Effort entry); stated as rules.
- A-017 Confirmed by Mohanasunder, Phase 2 review answers, 2026-10-17: an action is a change recorded on the ticket, not a view (term Acknowledgement); stated as a rule.
- A-018 Confirmed by Mohanasunder, Phase 2 review answers, 2026-10-17: an SLA timer paused while awaiting client recalculates on a priority change (term Priority); stated as a rule.
- A-022 (Open): ticket statuses are Open, Awaiting client, Resolved and Closed; "Open" names any stage that is not one of the other three (terms Ticket status, Open ticket).

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
- Answered 2026-10-17 (Mohanasunder, chat): OQ-037 (Closed), OQ-038 (Finance export), OQ-039 (MTTR), OQ-040 (Business day), OQ-041 (Company holiday list), OQ-042 (Contract, Active contract, Hours bank balance), OQ-043 (Finance export), OQ-045 (Awaiting client, Comment), OQ-046 (Acknowledgement), OQ-047 (Monthly client report), OQ-048 (Effort entry).
- Also answered 2026-10-17: OQ-049 (MTTR), OQ-050 (Company holiday list), OQ-051 (Comment). 
- Raised by SCR S-3 and Answered 2026-10-17 (Mohanasunder, chat): OQ-053 (changing a password needs the current password), OQ-054 (Temporary password clears the lock). No open question remains for these terms.
- SCR S-4: OQ-062 Answered 2026-10-17 (Mohanasunder, chat) (terms Audit trail, Audit entry, Security event). Raised by SCR S-4 and Answered 2026-10-17 (Mohanasunder, chat): OQ-064 (who views security events; term Audit trail), OQ-065 (every refused sign-in is a failed sign-in, unknown account name as typed; terms Security event, Audit entry). No open question remains for these terms.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: BRF-001 v0.2; PER-001 v0.2; SCP-001 v0.2; PRC-001 v0.2; PIB-002 v0.1; INT-002 v0.1; SCR S-3; SCR S-4; NFR-001 v0.3 (N-5, N-6).
- Related Phase 2: REQ-001, BR-001, NFR-001, EPC-001, BKL-001, PRS-001 (all use these terms).
- Downstream: agent charter (`.ai/standards/agent-charter.md`, built from the Approved glossary); Phase 4 API and schema naming; checked by `scripts/glossary_check.py`.

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)
- [x] Every business term used in the stories, criteria, and brief is defined once, with a source
- [x] Synonyms that caused or could cause confusion are listed under Avoid

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
