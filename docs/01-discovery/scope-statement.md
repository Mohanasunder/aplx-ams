---
id: SCP-001
title: APLX AMS: Release 1 scope statement
phase: 1
version: 0.2
template: scope-statement
template_version: 1.0
status: Approved
author_agent: discovery-analyst
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# APLX AMS: Release 1 scope statement

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- PIB-001 v0.1 Phase 1 input brief, Approved 2026-10-17: § User Intent, § Interview Answers, § Constraints.
- INT-001 v0.1 Phase 1 interview, Approved 2026-10-17: Q1, Q3, Q3a, Q4, Q5, Q8, Q9, Q10, Q11, Q14, Q15, Q16, Q17.
- IRC-002 v0.1 Phase 1 readiness, Approved 2026-10-17.
- `project.md` (Phase 0 Approved 2026-10-17): capacity and approvers.
- Answers to OQ-004, OQ-006, OQ-007, OQ-008, OQ-010, OQ-011, OQ-013, OQ-014, OQ-021, OQ-022, OQ-024, OQ-029, OQ-031 and OQ-033, given by Mohanasunder (Business owner / BA) in chat on 2026-10-17 and recorded in `docs/logs/open-questions-log.md`; DEC-020, DEC-022.

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: what release 1 of APLX AMS, the internal AMS delivery tool (INT-001 Q1), includes and excludes; the hard limits it must respect; and what it depends on.

Does not cover: how capabilities are built (screens, endpoints, tables, technology), story-level detail, or priorities within release 1 (Phase 2 onward). No market or competitor research was requested for Phase 1 (INT-001 Q13); that is a process choice, not a product exclusion, so it is not listed under § Out Of Scope.

## In Scope
<!-- guidance: Bulleted capabilities -->
Release 1, SAP applications only (INT-001 Q4, Q17, A-003), for a small pilot: one pilot client organization, Applexus (OQ-033; OQ-007 had said 1 to 2), up to about 10 SAP applications, about 10 engineers, about 20 client users (OQ-007):
- IS-1 Incident and service-request management with SLA timers (INT-001 Q5). SLA targets follow the standard SLA: P1 response 1 h, resolution 4 h; P2 4 h, 1 day; P3 1 day, 3 days; P4 2 days, 5 days; support hours 9x5 business days (OQ-004).
- IS-2 SLA and service reporting and dashboards per client (INT-001 Q5).
- IS-3 Effort and time tracking against contracts (hours bank and fixed fee), for billing, including a monthly effort data export to finance as Excel/CSV (INT-001 Q5, Q8; OQ-008). The boundary with billing: APLX AMS produces the export; finance does billing and invoicing outside the tool (OS-1).
- IS-4 Client user log-in: client users raise tickets and view their organization's SLA reports; one client role holds both tasks (INT-001 Q3a; OQ-022).
- IS-5 Client data boundary: each client user sees and acts only on their own organization's tickets and SLA reports (INT-001 Q14, A-002).

Note (users, not a capability): IS-1 to IS-5 serve L1 support engineers, L2/L3 support engineers and delivery managers inside the company, and client users (INT-001 Q3, Q3a; OQ-018); see PER-001 (PER P-1 L1, PER P-2 L2/L3, PER P-3 delivery manager, PER P-4 client user).

Note (pilot, not a capability): the release 1 pilot is internal. Applexus acts as its own client and Applexus staff are the client users of IS-4; external client organizations come after release 1 (OQ-024, Mohanasunder 2026-10-17). The pilot has one client organization (OQ-033), so it does not exercise the IS-5 boundary. IS-5 stays in scope in full: Mohanasunder decided that client data separation is built and tested with at least two client organizations' data before any external client joins (DEC-022, 2026-10-17; RSK R-6).

## Out Of Scope
<!-- guidance: Bulleted exclusions -->
- OS-1 Billing and invoicing; release 1 provides the monthly effort data export to finance only (INT-001 Q8; OQ-008).
- OS-2 Support of non-SAP applications (INT-001 Q17).
- OS-3 Replacing an ITSM tool (none exists today) and integration with client ITSM tools (OQ-010, Mohanasunder 2026-10-17; was UD-1 in v0.1).
- OS-4 Mobile apps and mobile access; release 1 is desktop web browser only (OQ-011, Mohanasunder 2026-10-17; was UD-2 in v0.1).

No undecided scope items remain.

## Constraints
<!-- guidance: Hard limits -->
- Timeline: the 3-month window started 2026-10-17; first usable release means live with a pilot client by 2027-01-17 (INT-001 Q9; OQ-013; A-001 Confirmed).
- Budget: existing staff and AI agents only; hosting on existing on-prem servers; no new paid licences (INT-001 Q10, Q16; OQ-021).
- Capacity (`project.md`): 3 parallel builder agents; 6 PRs reviewed per week; 3 open feature branches; approval SLA 1 business day; one approver for all roles, no backup, risk accepted for the pilot (DEC-020).
- Data: personal data limited to names and emails; no specific data-protection obligations known; no regulatory rules known (INT-001 Q11, Q15).
- Client data visibility: own organization only (INT-001 Q14).
- Landscape: SAP applications only (INT-001 Q17).
- Access: desktop web browser only (OQ-011).

## Dependencies
<!-- guidance: External systems, teams, decisions -->
- Pilot client ready to go live by 2027-01-17 (OQ-013). The pilot client is Applexus acting as its own client, with Applexus staff as client users (OQ-006, OQ-024); no external client organization is needed for release 1.
- Existing on-prem servers and already-licensed software available to host release 1 (INT-001 Q16; OQ-021); capacity recorded in Phase 3 (RSK R-3).
- Finance as the recipient of the monthly effort export, sent today by the delivery manager by email (OQ-008, OQ-031).
- Approver availability: one named approver for all roles, no backup (`project.md`; DEC-020; RSK R-1).
- As-is detail for Phase 2 (process owners, escalation criteria, client-stated priority, closure by L1, monthly SLA report email to clients, effort in hours per ticket): OQ-025 to OQ-032, all answered 2026-10-17; detail in PRC-001.

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-001 (Confirmed, Mohanasunder 2026-10-17, OQ-013): the 3-month window starts 2026-10-17; pilot go-live 2027-01-17.
- A-002 (Confirmed, INT-001 Q14): client users see and act only on their own organization's data.
- A-003 (Confirmed, INT-001 Q17): release 1 covers SAP applications only.
- No new assumptions in this version.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
- None open.
- Answered 2026-10-17: OQ-004 (SLA terms confirmed as real), OQ-006, OQ-007, OQ-008, OQ-010, OQ-011, OQ-013, OQ-014, OQ-021, OQ-022, OQ-024 (internal pilot; affects IS-4 and IS-5 testing, RSK R-6), OQ-029 (SLA reports emailed to clients monthly as Excel/PDF; IS-2, IS-4), OQ-031 (delivery manager emails the effort export to finance; IS-3), OQ-033 (one pilot client organization; IS-5, RSK R-6).

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: PIB-001 v0.1; INT-001 v0.1 (Q3a, Q4, Q5, Q8, Q14, Q16, Q17); IRC-002 v0.1; `project.md`; OQ answers of 2026-10-17; `docs/logs/decision-log.md` (single-approver decision).
- Related Phase 1: BRF-001 (§ Scope Summary, goals G-1 to G-4); PER-001 (PER P-1 to P-4); RSK-001 (RSK R-1, R-2, R-3, R-6, R-7 Closed); PRC-001.
- Downstream: Phase 2 epics, stories and backlog cite IS-1 to IS-5 and OS-1 to OS-4 (not yet created).

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
| Version | 0.2 |
| Conditions | None |
| Comments | Reviewed after validation run 5; KPI baselines and targets confirmed; OQ-034 to OQ-036 deferred to Phase 2. |
| Timestamp | 2026-10-17 06:05 UTC |
