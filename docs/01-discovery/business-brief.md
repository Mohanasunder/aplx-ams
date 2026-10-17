---
id: BRF-001
title: APLX AMS: Business brief
phase: 1
version: 0.2
template: business-brief
template_version: 1.1
status: Approved
author_agent: discovery-analyst
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# APLX AMS: Business brief

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- PIB-001 v0.1 Phase 1 input brief (`docs/01-discovery/phase-input-brief.md`), Approved 2026-10-17.
- INT-001 v0.1 Phase 1 interview (`docs/01-discovery/interview-record.md`), Approved 2026-10-17; cited below by question number (INT-001 Q1 to Q17, Q3a).
- IRC-002 v0.1 Phase 1 readiness (`docs/01-discovery/input-readiness-checklist.md`), Approved 2026-10-17.
- `project.md` (Phase 0 Approved 2026-10-17): project name, approvers, capacity.
- Raw input `docs/01-discovery/inputs/requirements.txt`.
- Answers to the open questions given by Mohanasunder (Business owner / BA) in chat on 2026-10-17, recorded in `docs/logs/open-questions-log.md` (OQ-001, OQ-004 to OQ-008, OQ-010, OQ-011, OQ-013 to OQ-033); DEC-020, DEC-022 (`docs/logs/decision-log.md`).

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: the business problem, goals with KPIs, stakeholders, constraints, and a pointer to the release 1 scope for APLX AMS, "An Application Management Services Solution" (`project.md`).

Does not cover: requirements, acceptance criteria, design, or technology choices (Phases 2 to 4). Detailed scope is in SCP-001 (`scope-statement.md`); users in PER-001 (`personas.md`); risks in RSK-001 (`risks.md`); as-is processes in `process-maps.md`.

## Problem Statement
<!-- guidance: Max 3 sentences -->
The company's own AMS team runs support for its clients' SAP applications with a shared mailbox and one shared spreadsheet (INT-001 Q1, Q4, Q6; OQ-005). As a result, SLA breaches are found only at month-end report compilation, up to about 30 days late, tickets, effort and reports are tracked by hand, and there is no single view across clients and applications (INT-001 Q2; OQ-016). APLX AMS is the internal delivery tool to fix this, which client users also log in to in release 1 (INT-001 Q1, Q3a).

## Business Goals And KPIs
<!-- guidance: Table: ID, goal, KPI, baseline, target, source. ID is G-1, G-2, ... in the first column, never reused; later artifacts cite a goal as 'BRF G-n'. A goal dropped in a later version keeps its row with 'Removed - reason' as the goal. Every goal must be covered by at least one epic with a story in Phase 2, or put out of scope by a named human's decision (checked by scripts/traceability.py check --phase 2) -->
| ID | Goal | KPI | Baseline | Target | Source |
| --- | --- | --- | --- | --- | --- |
| G-1 | Raise SLA compliance: fewer missed response and resolution targets, found in time | SLA compliance % against the standard SLA (P1 to P4 response and resolution targets, 9x5 support hours; OQ-004); formula defined in Phase 2 (RSK R-4) | 80% (from the month-end manual count, confirmed by Mohanasunder, 2026-10-17, chat; breaches found up to about 30 days late, OQ-016, OQ-030) | 95% | INT-001 Q2, Q7; OQ-001, OQ-004, OQ-016, OQ-030 answered by Mohanasunder 2026-10-17 |
| G-2 | Reduce the time taken to resolve tickets | MTTR (mean time to resolve), in days | 3 days | 1 day | INT-001 Q7; OQ-001 answered by Mohanasunder 2026-10-17 |
| G-3 | Reduce manual tracking of tickets, effort and reports in email and spreadsheets | Manual admin and reporting hours per month | 40 hours per month | 10 hours per month | INT-001 Q2, Q6, Q7; OQ-001 answered by Mohanasunder 2026-10-17 |
| G-4 | Give one view of tickets, SLA status and effort across clients and SAP applications | % of clients on the dashboard (release 1 denominator: 1 pilot client organization, Applexus; OQ-033) | 0% (no client is on a dashboard today) | 100% | INT-001 Q2 (problem 3: fragmented tools); OQ-020, OQ-023, OQ-033 answered by Mohanasunder 2026-10-17 |

Note: G-4 restates the third problem from INT-001 Q2 as a goal; its KPI and target come from the OQ-020 answer and its baseline from the OQ-023 answer. Baselines and targets for G-1 to G-3 come from the OQ-001 answer. Target dates were not stated per KPI; they are read as release 1 targets, with release 1 live with a pilot client by 2027-01-17 (OQ-001, OQ-013). No numbers are invented here.

## Stakeholders
<!-- guidance: Table: name or role, interest, influence -->
| Name or role | Interest | Influence | Source |
| --- | --- | --- | --- |
| Mohanasunder: Business owner / BA, Product owner, Project manager, Architect / tech lead, and every other approver role | Owns the problem and the release 1 scope; approves every gate | High: sole approver, no backup; single-approver risk accepted for the pilot (DEC-020, RSK R-1) | `project.md`; INT-001; OQ-014 |
| Sponsor: Applexus (organization) | Has a stake or a say in the tool (interest not stated) | Not stated | INT-001 Q12; OQ-006 |
| Delivery head: Applexus (organization) | Has a stake or a say in the tool (interest not stated) | Not stated | INT-001 Q12; OQ-006 |
| Pilot client: Applexus (organization), internal pilot | Acts as its own client in release 1; Applexus staff are the client users who log in; go-live with the pilot client by 2027-01-17 | Not stated | INT-001 Q12, Q3a; OQ-006, OQ-013, OQ-024 |
| L1 support engineers, PER P-1 | Primary users: record tickets with the client-stated priority, triage, resolve or escalate, send the closing email; the L1 lead owns ticket handling (PRC M-1) | Not stated | INT-001 Q3; OQ-005, OQ-018, OQ-025, OQ-027, OQ-028 |
| L2/L3 support engineers, PER P-2 | Primary users: resolve escalated tickets | Not stated | INT-001 Q3; OQ-005, OQ-018, OQ-026 |
| Delivery managers, PER P-3 | Primary users: monitor SLA, review and email per-client SLA reports, review effort against contracts and email the effort export to finance; own SLA tracking and reporting (PRC M-2) and effort tracking (PRC M-3) | Not stated | INT-001 Q3; OQ-019, OQ-025, OQ-029, OQ-031 |
| Client users, PER P-4 | Raise tickets and view their own organization's SLA reports; in release 1, Applexus staff (OQ-024) | Not stated | INT-001 Q3a, Q14; OQ-022, OQ-024 |
| Finance | Receives the monthly effort data export (Excel/CSV) by email from the delivery manager | Not stated | OQ-008, OQ-031 |

Stakeholders are named as organizations only; no individuals are named (OQ-006). INT-001 Q12 also mentioned practice heads; the OQ-006 answer did not name them. The release 1 pilot is internal: Applexus acts as its own client, Applexus staff are the client users, and external client organizations come after release 1 (OQ-024, Mohanasunder 2026-10-17). No external client organization is a release 1 stakeholder.

## Scope Summary
<!-- guidance: Link to the scope statement -->
Full scope: SCP-001 (`docs/01-discovery/scope-statement.md`).
- In scope, release 1 (small pilot: one pilot client organization, Applexus (OQ-033); up to about 10 SAP applications, about 10 engineers, about 20 client users, OQ-007): incident and service-request management with SLA timers on the standard SLA (OQ-004); SLA and service reporting and dashboards per client; effort and time tracking against hours-bank and fixed-fee contracts, with a monthly Excel/CSV effort export to finance (OQ-008); client user log-in to raise tickets and view SLA reports, one client role, limited to their own organization (INT-001 Q3a, Q5, Q8, Q14; OQ-022). SAP applications only (INT-001 Q17).
- Out of scope, release 1: billing and invoicing (INT-001 Q8); non-SAP applications (INT-001 Q17); ITSM tool replacement and integration with client ITSM tools (OQ-010); mobile access, desktop web browser only (OQ-011).
- Undecided: none.

## Constraints
<!-- guidance: Budget, timeline, regulatory, technical -->
- Timeline: the 3-month window started 2026-10-17; first usable release means live with a pilot client by 2027-01-17 (INT-001 Q9; OQ-013; A-001 Confirmed).
- Budget: existing staff and AI agents only, no extra spend (INT-001 Q10); hosting on existing on-prem servers (OQ-021); no new paid licences (INT-001 Q16).
- Capacity (`project.md`): 3 parallel builder agents; 6 PRs reviewed per week; 3 open feature branches; approval SLA 1 business day; one approver for all roles, no backup, risk accepted for the pilot (DEC-020).
- Regulatory: none known (INT-001 Q11). Personal data: names and emails only; no specific data-protection obligations known (INT-001 Q15).
- Pilot: release 1 is piloted internally, with Applexus as its own client and Applexus staff as the client users; external clients come after release 1 (OQ-024).
- Data boundary: each client user sees only their own organization's tickets and SLA reports (INT-001 Q14, A-002). The internal pilot has one client organization (OQ-033), so it does not exercise this boundary; it is built and tested with at least two client organizations' data before any external client joins (DEC-022, Mohanasunder 2026-10-17; RSK R-6).
- Landscape: SAP applications only (INT-001 Q4, Q17, A-003).
- Service levels: standard SLA for SLA timers: P1 response 1 h, resolution 4 h; P2 4 h, 1 day; P3 1 day, 3 days; P4 2 days, 5 days; support hours 9x5 business days (OQ-004).
- Access: desktop web browser only (OQ-011).
- Technical: none stated beyond hosting; technology is not chosen in Phase 1 (PIB-001 § Constraints).

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-001 (Confirmed, Mohanasunder 2026-10-17, OQ-013): the 3-month window starts 2026-10-17; pilot go-live by 2027-01-17.
- A-002 (Confirmed, INT-001 Q14): client users see and act only on their own organization's data.
- A-003 (Confirmed, INT-001 Q17): release 1 covers SAP applications only.
- A-005 (Confirmed, Mohanasunder 2026-10-17, OQ-019): delivery managers are the internal users of per-client SLA reports, dashboards and effort data (PER P-3).
- No new assumptions in this version.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
- None open.
- Answered 2026-10-17 by Mohanasunder: OQ-001 (80% baseline from the month-end manual count, confirmed), OQ-004 (SLA terms confirmed as real), OQ-005, OQ-006, OQ-007, OQ-008, OQ-010, OQ-011, OQ-013 to OQ-023, OQ-024 (internal pilot: Applexus as its own client, Applexus staff as client users; external clients after release 1), OQ-025 to OQ-032 (as-is detail: process owners, escalation, client-stated priority, closure, SLA report and effort export by email; none changes a goal, KPI or scope item), OQ-033 (one pilot client organization; G-4 denominator 1).
All in `docs/logs/open-questions-log.md`.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: PIB-001 v0.1; INT-001 v0.1 (Q1 to Q17, Q3a); IRC-002 v0.1; `project.md`; OQ answers of 2026-10-17; `docs/logs/decision-log.md` (single-approver decision).
- Related Phase 1: PER-001 (PER P-1 to P-4); SCP-001 (IS-1 to IS-5, OS-1 to OS-4); RSK-001 (RSK R-1 to R-8); PRC-001 (`process-maps.md`).
- Downstream: Phase 2 epics and stories cite goals as BRF G-1 to G-4 (not yet created).

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Every goal has an ID (G-n) and a measurable KPI with baseline and target (G-1 to G-3: OQ-001; G-4: OQ-020, OQ-023; all answered 2026-10-17)
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
