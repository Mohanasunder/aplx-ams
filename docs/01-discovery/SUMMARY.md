---
id: SUM-001
title: Phase 1 summary
phase: 1
version: 0.3
template: phase-summary
template_version: 1.0
status: Approved
author_agent: discovery-analyst
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# Phase 1 summary

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- PIB-001 v0.1, INT-001 v0.1, IRC-002 v0.1 (all Approved 2026-10-17).
- `project.md` (Phase 0 Approved 2026-10-17).
- Answers to the open questions by Mohanasunder in chat on 2026-10-17 (`docs/logs/open-questions-log.md`); DEC-020, DEC-021, DEC-022.
- All Phase 1 deliverables listed under § Documents are Approved at v0.2 (2026-10-17); this summary revised per SCR S-1.

## Purpose And Scope
<!-- guidance: One or two sentences: which phase this summarizes. File docs/0N-*/SUMMARY.md -->
Summarises Phase 1 (Business discovery) of APLX AMS so Phase 2 (Requirements) can start from this page and open full documents only for the sections listed.

## Decisions
<!-- guidance: Bullets: the decision, the reason in one clause, and its source 'ID vX.Y § section'. Only decisions later phases must respect -->
- APLX AMS is an internal AMS delivery tool for the company's own team; client users also log in in release 1 (INT-001 v0.1 Q1, Q3a).
- Release 1 is a small pilot: one pilot client organization (Applexus), up to about 10 SAP applications, about 10 engineers, about 20 client users (OQ-007, OQ-033; SCP-001 v0.2 § In Scope).
- The pilot is internal: Applexus acts as its own client and Applexus staff are the client users; external clients come after release 1 (OQ-024; BRF-001 v0.2 § Stakeholders).
- Client data separation (IS-5) is built and tested with at least two client organizations' data before any external client joins (DEC-022, Mohanasunder 2026-10-17; RSK R-6).
- In scope: IS-1 incident and service-request management with SLA timers on the standard SLA (P1 1 h / 4 h, P2 4 h / 1 day, P3 1 day / 3 days, P4 2 days / 5 days, 9x5); IS-2 per-client SLA and service reporting and dashboards; IS-3 effort tracking against hours-bank and fixed-fee contracts with a monthly Excel/CSV export to finance; IS-4 client log-in, one client role (raise tickets, view SLA reports); IS-5 own-organization data boundary (SCP-001 v0.2 § In Scope).
- Out of scope: OS-1 billing and invoicing; OS-2 non-SAP applications; OS-3 ITSM replacement or integration; OS-4 mobile, desktop web browser only (SCP-001 v0.2 § Out Of Scope). No undecided scope items.
- Goals and KPIs (baseline to target): BRF G-1 SLA compliance % 80% to 95%; G-2 MTTR 3 days to 1 day; G-3 manual admin and reporting hours 40 to 10 per month; G-4 % of clients on the dashboard 0% to 100%, denominator 1 in release 1 (BRF-001 v0.2 § Business Goals And KPIs). The 80% baseline comes from the month-end manual count (confirmed by Mohanasunder, 2026-10-17; OQ-001).
- Personas: PER P-1 L1 support engineer (triage), PER P-2 L2/L3 support engineer (resolution), PER P-3 delivery manager, PER P-4 client user (PER-001 v0.2; OQ-018; renumbering DEC-021).
- Process owners: L1 lead owns PRC M-1 ticket handling; the delivery manager owns M-2 SLA tracking and reporting and M-3 effort tracking (OQ-025; PRC-001 v0.2).
- No backup approver for the pilot; single-approver risk accepted (DEC-020).

## Constraints Set
<!-- guidance: Bullets: limits later phases must work within (technology, NFR targets, scope exclusions, compliance), each with its source ID -->
- Live with a pilot client by 2027-01-17; window started 2026-10-17 (INT-001 v0.1 Q9; OQ-013).
- Existing staff and AI agents only; existing on-prem servers; no new paid licences (INT-001 v0.1 Q10, Q16; OQ-021).
- Client users see only their own organization's tickets and SLA reports (INT-001 v0.1 Q14).
- Personal data: names and emails only; no regulatory or data-protection obligations known (INT-001 v0.1 Q11, Q15).
- SAP applications only (INT-001 v0.1 Q17); desktop web browser only (OQ-011).
- Capacity: 3 builder agents, 6 PR reviews per week, 1-business-day approval SLA, one approver (`project.md`; DEC-020).

## Open Items
<!-- guidance: Open questions (OQ-), assumptions (A-), and risks (RSK-) still open, with owner; or 'None' -->
All owned by Mohanasunder.
- Open OQs: OQ-001 to OQ-033 all answered by 2026-10-17. Low, for Phase 2: OQ-034 (L1 resolution target and triage tool, PRC M-1.3), OQ-035 (L2/L3 to L1 resolved hand-back, PRC M-1.6), OQ-036 (per-ticket hours to contract mapping, PRC M-3.2).
- Open assumptions: none. A-001, A-002, A-003, A-004, A-005, A-007 Confirmed; A-006 Rejected (2026-10-17).
- Risks: High: RSK R-2, R-6 (Open), R-1 (Accepted, DEC-020); Medium: R-4, R-5 (Mitigating), R-8 (Open); Low: R-3 (Open); R-7 Closed (Mohanasunder, Phase 1 gate risk review, 2026-10-17) (RSK-001 v0.2; docs/logs/risk-register.md).

## Documents
<!-- guidance: One line per Approved artifact of the phase: 'ID vX.Y - title - path'. Checked by scripts/context_pack.py summaries -->
Approved:
- PIB-001 v0.1 - Phase 1 input brief - docs/01-discovery/phase-input-brief.md
- INT-001 v0.1 - Phase 1 interview - docs/01-discovery/interview-record.md
- IRC-002 v0.1 - Phase 1 readiness - docs/01-discovery/input-readiness-checklist.md
- BRF-001 v0.2 - APLX AMS: Business brief - docs/01-discovery/business-brief.md
- PER-001 v0.2 - APLX AMS: Personas - docs/01-discovery/personas.md
- SCP-001 v0.2 - APLX AMS: Release 1 scope statement - docs/01-discovery/scope-statement.md
- RSK-001 v0.2 - APLX AMS: Phase 1 risks - docs/01-discovery/risks.md
- PRC-001 v0.2 - As-is process maps - docs/01-discovery/process-maps.md

## What The Next Phase Needs
<!-- guidance: The few documents or sections the next phase should open in full, as 'ID vX.Y § section'; everything else is covered above -->
- BRF-001 v0.2 § Business Goals And KPIs; SCP-001 v0.2 § In Scope, § Out Of Scope; PER-001 v0.2 § Persona P-1 to P-4 (Key Journeys); PRC-001 v0.2 § Process M-1 to M-3 (Pain Points); RSK-001 v0.2 § Risk R-4, § Risk R-6.

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-001, A-002, A-003, A-004, A-005, A-007 (Confirmed); A-006 (Rejected).

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
Listed under § Open Items; all in docs/logs/open-questions-log.md. None new from this summary.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: PIB-001 v0.1; INT-001 v0.1; IRC-002 v0.1; project.md; `docs/logs/decision-log.md` (single-approver decision).
- Indexes: BRF-001; PER-001; SCP-001; RSK-001; PRC-001.
- Downstream: Phase 2 input brief (not yet created).

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)
- [x] Documents lists every Approved artifact of the phase as 'ID vX.Y'
- [x] About half a page: a reader can start the next phase from this summary alone

## Approval Record
| Field | Value |
| --- | --- |
| Decision | Approve |
| Approver | Mohanasunder |
| Role | Business owner / BA |
| Version | 0.3 |
| Conditions | None |
| Comments | Revised per SCR S-1; wording only. |
| Timestamp | 2026-10-17 06:22 UTC |
