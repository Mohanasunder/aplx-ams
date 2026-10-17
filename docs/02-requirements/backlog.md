---
id: BKL-001
title: APLX AMS: Backlog
phase: 2
version: 0.1
template: backlog-entry
template_version: 2.0
status: Approved
author_agent: requirements-analyst
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# APLX AMS: Backlog

> **Collection file.** The full prioritised backlog lives in this one file. Add one `## Entry BL-N` section per backlog item; never create a separate BKL-NNN file. Downstream artifacts reference a specific entry as `BKL BL-N` (e.g. `BKL BL-4`).

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- PIB-002 v0.1 § Interview Answers Q1 (IS-1 to IS-5 all Must for the 2027-01-17 go-live), § Constraints.
- INT-002 v0.1 Q1.
- SCP-001 v0.2 § In Scope, § Out Of Scope; SUM-001 v0.3 § Constraints Set.
- RSK-001 v0.2 § Risk R-2 (MoSCoW so that a scope cut is an early named human decision).

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: the release 1 backlog of APLX AMS: one entry per story, BL-1 to BL-29 (BL-N links to REQ S-N with the same number), each with MoSCoW priority and release. Every entry is Must for release 1 (pilot go-live 2027-01-17) because the human set IS-1 to IS-5 all Must (INT-002 Q1); no Should, Could or Won't items exist, and no item is mapped to a later release. Items out of scope for release 1 are the PRS-001 non-goals NG-1 to NG-7, not backlog entries.

Does not cover: build order, waves or feature slicing (Phase 5). No priority conflict was found; if capacity forces a cut (RSK R-2), the product owner decides which Must becomes Should, recorded as a decision.

---

## Entry BL-1: Client user raises a ticket in the portal

### Item
REQ S-1 (EPC E-1, PRS F-1)

### Priority
Must: portal-only intake (INT-002 Q1, Q5).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-2: Client user follows their client organization's tickets

### Item
REQ S-2 (EPC E-1, PRS F-1)

### Priority
Must: client users view their own organization's tickets and statuses (INT-002 Q1; SCP IS-4).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-3: L1 support engineer acknowledges a new ticket

### Item
REQ S-3 (EPC E-1, PRS F-2)

### Priority
Must: stops the response clock (INT-002 Q1, Q3).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-4: L1 support engineer changes a ticket's priority

### Item
REQ S-4 (EPC E-1, PRS F-2)

### Priority
Must: priority change with recalculation (INT-002 Q1, Q6).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-5: L1 support engineer escalates a ticket to L2/L3

### Item
REQ S-5 (EPC E-1, PRS F-2)

### Priority
Must: removes the email hand-off (INT-002 Q1; PRC PP-1.4).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-6: Support engineer sets a ticket to Resolved

### Item
REQ S-6 (EPC E-1, PRS F-2)

### Priority
Must: stops the resolution clock and hands back to L1 (INT-002 Q1, Q16).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-7: L1 support engineer closes a Resolved ticket

### Item
REQ S-7 (EPC E-1, PRS F-2)

### Priority
Must: L1 closes every ticket (INT-002 Q1, Q16; OQ-028).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-8: Support engineer marks a ticket as awaiting client

### Item
REQ S-8 (EPC E-1, PRS F-2)

### Priority
Must: pause rule of the SLA timers (INT-002 Q1, Q3).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-9: SLA timers count business hours against the standard SLA

### Item
REQ S-9 (EPC E-2, PRS F-3)

### Priority
Must: core of IS-1 (INT-002 Q1, Q2, Q3).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-10: Support engineer sees SLA timer states

### Item
REQ S-10 (EPC E-2, PRS F-3)

### Priority
Must: at-risk and breached states in-app (INT-002 Q1, Q12, Q12a).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-11: Ticket is flagged for escalation at L1's target

### Item
REQ S-11 (EPC E-2, PRS F-3)

### Priority
Must: escalation flag at 50% (INT-002 Q1, Q15).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-12: Delivery manager monitors the live dashboard

### Item
REQ S-12 (EPC E-3, PRS F-4)

### Priority
Must: one view across clients, BRF-001 G-4 (INT-002 Q1, Q13).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-13: Delivery manager generates the monthly client report per client organization

### Item
REQ S-13 (EPC E-3, PRS F-4)

### Priority
Must: measure of BRF-001 G-1; the delivery manager generates, reviews and publishes it (INT-002 Q1, Q4, Q13; OQ-047).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-14: Client user views and downloads the monthly client report

### Item
REQ S-14 (EPC E-3, PRS F-4)

### Priority
Must: client users view SLA reports (INT-002 Q1, Q13; SCP IS-4).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-15: Support engineer records effort on a ticket

### Item
REQ S-15 (EPC E-4, PRS F-5)

### Priority
Must: effort per ticket (INT-002 Q1, Q14).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-16: Delivery manager reviews effort against a contract

### Item
REQ S-16 (EPC E-4, PRS F-5)

### Priority
Must: hours bank balance and fixed fee visibility (INT-002 Q1, Q14, Q14a).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-17: Delivery manager produces the monthly finance export

### Item
REQ S-17 (EPC E-4, PRS F-5)

### Priority
Must: export to finance (INT-002 Q1, Q14; OQ-008).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-18: Delivery manager sets up client organizations and SAP applications

### Item
REQ S-18 (EPC E-5, PRS F-6)

### Priority
Must: prerequisite for raising tickets (INT-002 Q1, Q8).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-19: Delivery manager sets up a client organization's contract

### Item
REQ S-19 (EPC E-4, PRS F-5)

### Priority
Must: prerequisite for effort against contracts (INT-002 Q1, Q8, Q14).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-20: Delivery manager manages user accounts

### Item
REQ S-20 (EPC E-5, PRS F-6)

### Priority
Must: user accounts for every user (INT-002 Q1, Q7, Q8).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-21: User signs in with a user account

### Item
REQ S-21 (EPC E-5, PRS F-6)

### Priority
Must: client user log-in, IS-4 (INT-002 Q1, Q7).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-22: Client data boundary holds across two client organizations

### Item
REQ S-22 (EPC E-5, PRS F-7)

### Priority
Must: IS-5 and DEC-022 (INT-002 Q1; RSK R-6).

### Release
Release 1 (MVP, go-live 2027-01-17); boundary tests re-run before the first external client organization goes live after release 1 (RSK R-6).

---

## Entry BL-23: Internal user views a ticket's audit trail

### Item
REQ S-23 (EPC E-5, PRS F-8)

### Priority
Must: audit content named by the human (INT-002 Q1, Q11).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-24: Delivery manager maintains the company holiday list

### Item
REQ S-24 (EPC E-2, PRS F-3)

### Priority
Must: business hours exclude holiday dates; the delivery manager maintains the list each year (INT-002 Q1, Q2; OQ-041).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-25: Support engineer changes or deletes their own effort entry

### Item
REQ S-25 (EPC E-4, PRS F-5)

### Priority
Must: effort entry correction within the month (INT-002 Q1, Q14; OQ-048).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-26: Delivery manager corrects an effort entry

### Item
REQ S-26 (EPC E-4, PRS F-5)

### Priority
Must: delivery manager correction of any effort entry (INT-002 Q1, Q14; OQ-048).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-27: Delivery manager ends a contract and sets up a new one

### Item
REQ S-27 (EPC E-4, PRS F-5)

### Priority
Must: one active contract at a time needs replacement (INT-002 Q1, Q14; OQ-042).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-28: Client user adds a comment on their client organization's ticket

### Item
REQ S-28 (EPC E-1, PRS F-1)

### Priority
Must: release 1 scope decision DEC-026 (Mohanasunder, 2026-10-17), part of IS-4, all Must (INT-002 Q1; OQ-045).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Entry BL-29: Internal user adds a comment on a ticket

### Item
REQ S-29 (EPC E-1, PRS F-2)

### Priority
Must: internal user comments visible to the client user, under DEC-026, part of IS-4 (INT-002 Q1; OQ-051).

### Release
Release 1 (MVP, go-live 2027-01-17)

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
None for the backlog. Story-level assumptions A-009 to A-025 (A-009 to A-011, A-013, A-017, A-018, A-023 to A-025 Confirmed; A-012 Rejected) are in REQ-001, BR-001 and GLO-001.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
None for the backlog. OQ-037 to OQ-048 answered 2026-10-17 added BL-24 to BL-28 and criteria within existing entries; OQ-049 to OQ-051, answered the same day, added REQ S-24 AC-4 and BL-29. Each story has at most 4 criteria. No open question remains.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason'.
     Cite individual backlog entries as BKL BL-N (e.g. BKL BL-3). -->
- Upstream: PIB-002 v0.1 (Q1); INT-002 v0.1; SCP-001 v0.2; RSK-001 v0.2 (R-2); decision-log and open-questions-log answers listed under § Open Questions.
- Related Phase 2: REQ-001 (BL-N to REQ S-N); EPC-001; PRS-001 (F-1 to F-8).
- Downstream: Phase 5 feature breakdown and wave plan (not yet created).

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Every entry has a unique BL-N ID; IDs are consecutive and never reused
- [x] Every entry links to a story (REQ S-N) or epic (EPC E-N)
- [x] Every entry has a priority and a release target
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
