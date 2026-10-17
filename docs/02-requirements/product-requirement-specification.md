---
id: PRS-001
title: APLX AMS: Product Requirement Specification
phase: 2
version: 0.1
template: product-requirement-specification
template_version: 1.0
status: Approved
author_agent: requirements-analyst
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# APLX AMS: Product Requirement Specification

> **Single file.** One Product Requirement Specification per project. Create with:
> `python3 scripts/new_artifact.py --template product-requirement-specification --id PRS --title "<title>" --author <agent> --out docs/02-requirements/product-requirement-specification.md`
> Never create a separate `PRS-NNN.md` file. Downstream artifacts cite product goals as `PRS G-N`, non-goals as `PRS NG-N`, and features as `PRS F-N`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- BRF-001 v0.2 § Business Goals And KPIs (G-1 to G-4), § Constraints.
- SCP-001 v0.2 § In Scope (IS-1 to IS-5), § Out Of Scope (OS-1 to OS-4).
- SUM-001 v0.3 § Decisions, § Constraints Set.
- PIB-002 v0.1 § Interview Answers (Q1 to Q16, Q9a, Q12a, Q14a), § Constraints.
- INT-002 v0.1 § Questions And Answers (evidence record).
- PER-001 v0.2 § Persona P-1 to P-4; PRC-001 v0.2 § Process M-1 to M-3.
- Decisions DEC-018 (PRS required in Phase 2), DEC-022 (two-organization data boundary) and DEC-026 (client comments) in `docs/logs/decision-log.md`; answers to OQ-037 to OQ-051 and the Phase 2 review answers, 2026-10-17 (Mohanasunder, 2026-10-17, chat).

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: the product-level goals with success metrics, non-goals, scope and MoSCoW features of APLX AMS release 1, bridging BRF-001 goals and the stories in REQ-001. All features are Must for the 2027-01-17 go-live (INT-002 Q1). Brief goals are cited as `BRF-001 G-n`, the form `scripts/traceability.py` accepts (checked 2026-10-17; `BRF G-n` is not matched to the brief's goals); see EPC-001 § Purpose And Scope.

Does not cover: story detail (REQ-001), business rules (BR-001), NFRs (NFR-001), or design and technology (Phases 3 and 4).

---

## Product Goals

<!-- guidance: Table of product-level goals. ID is PRS G-N (G-1, G-2, …), never reused. Each goal must have a measurable success metric. Cite the upstream brief goal that this serves as BRF G-N; a PRS goal may serve more than one brief goal. A goal dropped in a later version keeps its row with 'Removed - SCR S-N' in the Goal column. -->

| ID | Goal | Success Metric | Brief Goal |
| --- | --- | --- | --- |
| PRS G-1 | Every ticket's response and resolution clocks run on business hours in APLX AMS and show at risk at 90% of the target, so engineers act before a resolution target is missed | Resolution % (BR B-12) at or above 95% per calendar month for the pilot client organization (baseline 80%) | BRF-001 G-1 |
| PRS G-2 | Tickets still with L1 at 50% of their resolution target are flagged for escalation and handed to L2/L3 by assignment, with no email step | MTTR (BR B-13: mean business time from raise to Resolved, paused time excluded, over tickets Resolved in the calendar month, in business days of 9 business hours; OQ-039) at or below 1 business day per calendar month (baseline 3 days; the baseline was in business days, like-for-like: OQ-049) | BRF-001 G-2 |
| PRS G-3 | Tickets, effort entries, the monthly client report and the finance export are produced from one tool instead of the shared mailbox and spreadsheet | Manual admin and reporting hours at or below 10 hours per month (baseline 40 hours per month) | BRF-001 G-3 |
| PRS G-4 | Each set-up client organization appears on the live dashboard, and its client users view their own monthly client report in APLX AMS | 100% of set-up client organizations on the live dashboard (release 1: 1 of 1, Applexus; baseline 0%) | BRF-001 G-4 |

---

## Non-Goals

<!-- guidance: Table of explicit non-goals — capabilities the product intentionally will not address in this release. ID is PRS NG-N (NG-1, NG-2, …), never reused. Reason must name the decision or constraint that makes it a non-goal (a business constraint, out-of-scope decision, or named human decision DEC-NNN). -->

| ID | Non-Goal | Reason |
| --- | --- | --- |
| PRS NG-1 | Billing and invoicing | SCP-001 OS-1: finance bills outside APLX AMS from the finance export (INT-001 Q8; OQ-008) |
| PRS NG-2 | Support of non-SAP applications | SCP-001 OS-2 (INT-001 Q17; A-003 Confirmed) |
| PRS NG-3 | Replacing an ITSM tool or integrating with client ITSM tools | SCP-001 OS-3 (OQ-010, Mohanasunder 2026-10-17) |
| PRS NG-4 | Mobile apps and mobile access | SCP-001 OS-4: desktop web browser only (OQ-011, Mohanasunder 2026-10-17) |
| PRS NG-5 | Turning emails into tickets (mailbox intake) | Intake is portal only; the shared mailbox is retired (INT-002 Q5, Mohanasunder 2026-10-17) |
| PRS NG-6 | Email alerts for SLA risk or breach | SLA alerts are in-app only (INT-002 Q12, Mohanasunder 2026-10-17) |
| PRS NG-7 | Multi-factor authentication | Human security decision: user accounts with a password policy, no MFA (INT-002 Q7, Mohanasunder 2026-10-17); risk RSK-002 R-1 |

---

## Product Scope

### In Scope
<!-- guidance: Bulleted capabilities included in this product release -->
- Ticket intake in the portal by client users, client user comments on their organization's tickets (DEC-026), and ticket handling by L1 and L2/L3 support engineers (SCP IS-1, IS-4): PRS F-1, F-2.
- SLA timers on the business-hours calendar (company holiday list maintained by the delivery manager) with at-risk and breached states and the L1 escalation flag (IS-1): PRS F-3.
- Live dashboard and monthly client report, viewed and downloaded as Excel or PDF (IS-2, IS-4): PRS F-4.
- Effort entries against one active contract per client organization (hours bank or fixed fee) and the monthly finance export as Excel or CSV (IS-3): PRS F-5.
- Delivery manager setup of client organizations, SAP applications, contracts and user accounts; sign-in with user accounts (IS-4; INT-002 Q7, Q8): PRS F-6.
- Client data boundary built and tested with two client organizations (IS-5; DEC-022): PRS F-7.
- Audit trail of status, priority, assignment and effort changes (INT-002 Q11): PRS F-8.

### Out Of Scope
<!-- guidance: Bulleted exclusions for this product release -->
- Billing and invoicing (PRS NG-1).
- Non-SAP applications (PRS NG-2).
- ITSM replacement or integration (PRS NG-3).
- Mobile access (PRS NG-4).
- Mailbox intake (PRS NG-5).
- Email SLA alerts (PRS NG-6).
- MFA (PRS NG-7).

---

## Feature F-1: Ticket intake in the portal

### Description
Client users raise incidents and service requests for their own client organization's SAP applications with a priority, follow their organization's tickets and statuses, and add comments on them (DEC-026).

### Priority
Must: portal-only intake replaces the shared mailbox and is needed for every other feature (INT-002 Q1, Q5); client comments are part of IS-4 (DEC-026, OQ-045).

### Goals Served
PRS G-1, PRS G-3

### Linked Stories
REQ S-1, REQ S-2, REQ S-28

---

## Feature F-2: Ticket handling by L1 and L2/L3

### Description
L1 support engineers acknowledge, change priority with a reason, escalate by assignment and close (the client user sees Closed in APLX AMS, no message is sent, OQ-037); the assigned support engineer (L1 or L2/L3) marks awaiting client, which a client user's comment clears (OQ-045); support engineers and the delivery manager add comments on any ticket, visible to the client user, which do not clear awaiting client (DEC-026, OQ-051); L2/L3 support engineers set Resolved and the ticket returns to the L1 queue.

### Priority
Must: the as-is ticket flow (PRC M-1) moves into the tool (INT-002 Q1, Q3, Q6, Q16).

### Goals Served
PRS G-1, PRS G-2, PRS G-3

### Linked Stories
REQ S-3, REQ S-4, REQ S-5, REQ S-6, REQ S-7, REQ S-8, REQ S-29

---

## Feature F-3: SLA timers and escalation flag

### Description
Response and resolution clocks per ticket on business hours against the standard SLA, with pause, recalculation on priority change, on track, at-risk, breached and met states shown in-app, and the escalation flag at the L1 target; the delivery manager maintains the company holiday list (OQ-041).

### Priority
Must: breaches found up to 30 days late are the top pain point (PRC PP-2.1; INT-002 Q1, Q2, Q12a, Q15).

### Goals Served
PRS G-1, PRS G-2

### Linked Stories
REQ S-9, REQ S-10, REQ S-11, REQ S-24

---

## Feature F-4: Live dashboard and monthly client report

### Description
The internal live dashboard across client organizations and SAP applications, and the monthly client report (response %, resolution %, breached tickets, MTTR, ticket counts) that the delivery manager generates, reviews and publishes, and client users view and download as Excel or PDF once published (OQ-047).

### Priority
Must: per-client SLA reporting is IS-2 and gives G-1 its measure (INT-002 Q1, Q4, Q13).

### Goals Served
PRS G-1, PRS G-3, PRS G-4

### Linked Stories
REQ S-12, REQ S-13, REQ S-14

---

## Feature F-5: Effort tracking and finance export

### Description
Support engineers record effort entries on tickets assigned to them and change or delete their own until the end of the month; the delivery manager corrects any effort entry, reviews effort and the hours bank balance per active contract (warning at 0 or below), ends a contract and sets up a new one, and downloads the monthly finance export as Excel or CSV to email to finance (OQ-038, OQ-042, OQ-043, OQ-048).

### Priority
Must: effort against contracts is IS-3 (INT-002 Q1, Q14, Q14a).

### Goals Served
PRS G-3, PRS G-4

### Linked Stories
REQ S-15, REQ S-16, REQ S-17, REQ S-19, REQ S-25, REQ S-26, REQ S-27

---

## Feature F-6: Setup and sign-in

### Description
The delivery manager sets up client organizations, SAP applications and user accounts with one role each; every user signs in with a user account and a password policy (at least 8 characters with an upper-case letter, a lower-case letter and a digit; locked 30 minutes after 5 failed sign-ins; OQ-044), without MFA.

### Priority
Must: no ticket can be raised or reported before setup and sign-in exist (INT-002 Q1, Q7, Q8).

### Goals Served
PRS G-4

### Linked Stories
REQ S-18, REQ S-20, REQ S-21

---

## Feature F-7: Client data boundary

### Description
Client users see and act only on their own client organization's tickets, reports and SAP applications, proven with two client organizations' data.

### Priority
Must: IS-5 and DEC-022; a defect would expose one client's data to another (RSK R-6).

### Goals Served
PRS G-4

### Linked Stories
REQ S-22

---

## Feature F-8: Audit trail

### Description
Every change to a ticket's status, priority, assignment or effort entries is recorded with user and time and is visible to internal users only.

### Priority
Must: the human named the audit content for release 1 (INT-002 Q1, Q11).

### Goals Served
PRS G-3

### Linked Stories
REQ S-23

---

<!-- Repeat the block above (from "## Feature F-N:" to the closing ---) for each additional feature.
     Increment the number: F-2, F-3, … Never reuse a number. -->

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-009 (Confirmed, OQ-039, Mohanasunder, 2026-10-17): MTTR definition used by PRS G-2.
- A-015 (Open): calendar month reporting period used by PRS G-1 and G-2.
- Other open assumptions (A-008, A-014, A-016, A-019 to A-022) are listed in REQ-001, BR-001, NFR-001 and GLO-001; A-010, A-011, A-013, A-017, A-018, A-023 to A-025 are Confirmed; A-012 is Rejected (replaced by the OQ-044 answer).

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
- OQ-037 to OQ-048 Answered (Mohanasunder, 2026-10-17, chat) and applied to PRS G-2 and F-1 to F-6.
- OQ-049 to OQ-051 Answered (Mohanasunder, 2026-10-17, chat): MTTR baseline in business days (PRS G-2); holiday list changes apply from the change onward (PRS F-3); internal users add comments visible to the client user, not clearing awaiting client (PRS F-2, REQ S-29).
- Decided: client users add comments in release 1, part of IS-4 (DEC-026, Mohanasunder, 2026-10-17).
- Decided: the 80% baseline of PRS G-1 stands as stated, although not like-for-like with resolution % (DEC-025, Mohanasunder, 2026-10-17; BR B-12; RSK R-4).

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason'.
     Cite product goals as PRS G-N, non-goals as PRS NG-N, features as PRS F-N. -->
- Upstream: BRF-001 v0.2 (G-1 to G-4); SCP-001 v0.2 (IS-1 to IS-5, OS-1 to OS-4); SUM-001 v0.3; PIB-002 v0.1; INT-002 v0.1.
- Related Phase 2: EPC-001 (E-1 to E-5); REQ-001 (S-1 to S-29); BKL-001; BR-001; NFR-001; RSK-002.
- Feature to epic: F-1, F-2 to EPC E-1; F-3 to E-2; F-4 to E-3; F-5 to E-4; F-6, F-7, F-8 to E-5.
- Downstream: Phase 3 architecture; Phase 5 feature breakdown (not yet created).

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no goals, features, or constraints without a source
- [x] Every product goal has a unique G-N ID; IDs are consecutive and never reused
- [x] Every product goal has a measurable success metric with a number and unit
- [x] Every product goal cites at least one upstream brief goal as BRF G-N
- [x] Every non-goal has a unique NG-N ID; IDs are consecutive and never reused
- [x] Every non-goal has a named reason or references DEC-NNN
- [x] In Scope and Out of Scope are both filled; no capability is ambiguously placed
- [x] Every feature has a unique F-N ID; IDs are consecutive and never reused
- [x] Every feature has a MoSCoW priority with a reason
- [x] Every feature cites at least one product goal (PRS G-N) it serves
- [x] Every Must or Should feature cites at least one linked story (REQ S-N)
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
| Comments | Reviewed after validation run 4; all open questions answered; R4 findings fixed. |
| Timestamp | 2026-10-17 08:46 UTC |
