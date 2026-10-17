---
id: RSK-001
title: APLX AMS: Phase 1 risks
phase: 1
version: 0.2
template: risk-register-entry
template_version: 2.0
status: Approved
author_agent: discovery-analyst
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# APLX AMS: Phase 1 risks

> **Collection file.** All risks raised in this phase live in this one file. Add one `## Risk R-N` section per risk; never create a separate RSK-NNN file for an additional risk in the same phase. The risk-register index (`docs/logs/risk-register.md`) references each risk as `RSK R-N` (e.g. `RSK R-2`). The live status of each risk lives there, not here.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- PIB-001 v0.1 Phase 1 input brief, Approved 2026-10-17: § Readiness Verdict (candidate risks), § Constraints.
- INT-001 v0.1 Phase 1 interview, Approved 2026-10-17: Q1, Q2, Q3a, Q5 to Q10, Q12, Q14 to Q16.
- IRC-002 v0.1 Phase 1 readiness, Approved 2026-10-17: rows 2, 3, 5.
- `project.md` (Phase 0 Approved 2026-10-17): Approvers, Capacity and settings.
- Answers to OQ-001, OQ-004 to OQ-008, OQ-010, OQ-011, OQ-013 to OQ-024 and OQ-025 to OQ-033, given by Mohanasunder (Business owner / BA) in chat on 2026-10-17 and recorded in `docs/logs/open-questions-log.md`; DEC-020, DEC-022 (`docs/logs/decision-log.md`).

## Purpose And Scope
<!-- guidance: What risks this artifact covers and what it does not. One collection per phase. -->
Covers: business, delivery and scope risks visible at Phase 1 for APLX AMS release 1. R-1 to R-5 are the candidate risks listed in PIB-001 § Readiness Verdict; R-6 to R-8 are raised by the discovery analyst from INT-001 and IRC-002 evidence. Version 0.2 updates every risk with the answers of 2026-10-17, including the internal pilot (OQ-024) and the closure of R-7 at the Phase 1 gate risk review.

Does not cover: technical or security design risks (Phase 3 threat model and architecture), or delivery risks per feature (Phase 5).

Rating method: Likelihood and Impact are each Low, Medium or High. Overall rating: High if either is High and the other is at least Medium; Medium if both are Medium, or one is High and the other Low; otherwise Low. Owners are roles from `project.md`; every role is held by Mohanasunder.

---

## Risk R-1: Single approver with no backup

### Risk Description
- Cause: one person, Mohanasunder, holds every approver role, and no backup approver is named for the release 1 pilot (`project.md` § Approvers; OQ-014 answered 2026-10-17).
- Event: the approver is unavailable or overloaded at a gate, a test-set approval, or a PR review.
- Consequence: work stops; the 1-business-day approval SLA and the review capacity of 6 PRs per week (`project.md`) cannot be met, threatening the 2027-01-17 pilot go-live (OQ-013).

### Likelihood And Impact
- Likelihood: Medium. One person carries 7 approver roles across every phase; any absence blocks all approvals.
- Impact: High. Every phase gate and every Phase 6 test set and PR needs a named human approval (CLAUDE.md rules 3 and 7).
- Overall rating: High.

### Mitigation
- Accepted: Mohanasunder decided on 2026-10-17 to name no backup approver for the pilot and accepted the single-approver risk (DEC-020, answer to OQ-014). Register status: Accepted.
- Remaining measures: plan approval slots against the 1-business-day SLA and keep open feature branches at or below 3 (`project.md`); naming a backup approver stays the alternative recorded in DEC-020.
- Owner of actions: Project manager (Mohanasunder).

### Owner
Project manager (Mohanasunder)

---

## Risk R-2: Three-month timeline for release 1 scope with existing staff and AI agents only

### Risk Description
- Cause: release 1 includes three capabilities plus client user log-in (INT-001 Q3a, Q5; SCP-001 IS-1 to IS-5) and must be live with a pilot client by 2027-01-17, in a window that started 2026-10-17 (INT-001 Q9; OQ-013 answered 2026-10-17; A-001 Confirmed), with existing staff and AI agents only and no extra spend (INT-001 Q10). Pilot scale: one pilot client organization, Applexus (OQ-033), up to about 10 SAP applications, about 10 engineers, about 20 client users (OQ-007).
- Event: the release 1 scope does not fit the time and capacity available.
- Consequence: the 2027-01-17 pilot go-live is missed, or scope is cut late.

### Likelihood And Impact
- Likelihood: High (unchanged). "First usable release" means live with a pilot client (OQ-013). The pilot is internal: Applexus acts as its own client with Applexus staff as client users (OQ-024, 2026-10-17), which removes any dependency on an external client's readiness or onboarding, but the full release 1 scope (IS-1 to IS-5) is still required and capacity is still limited to 3 parallel builder agents and 6 PR reviews per week (`project.md`) with one approver (RSK R-1). The capacity cause is unchanged, so the rating is not lowered.
- Impact: High. The timeline is the stated delivery constraint (INT-001 Q9).
- Overall rating: High.

### Mitigation
- Start date and meaning of "first usable release" confirmed (OQ-013, 2026-10-17); internal pilot confirmed (OQ-024, 2026-10-17), so go-live readiness depends on Applexus only.
- In Phase 2, prioritise release 1 stories with MoSCoW so a scope cut, if needed, is a named human decision made early, not late.
- Re-check the plan against `project.md` capacity in Phase 5.
- Owner of actions: Product owner (Mohanasunder).

### Owner
Product owner (Mohanasunder)

---

## Risk R-3: Hosting limited to existing on-prem servers and no new paid licences

### Risk Description
- Cause: release 1 is hosted on existing on-prem servers (OQ-021 answered 2026-10-17) and no new paid licences are allowed (INT-001 Q16). The capacity of those servers and the already-licensed software on them are not recorded.
- Event: the existing on-prem servers lack the capacity or capabilities release 1 needs.
- Consequence: Phase 3 options narrow, or a spend decision is needed that conflicts with the no-extra-spend constraint (INT-001 Q10).

### Likelihood And Impact
- Likelihood: Low (was Medium). The hosting target is now named (OQ-021) and the pilot load is small: about 10 engineers and about 20 client users (OQ-007).
- Impact: Medium. It constrains Phase 3 choices but does not change release 1 scope.
- Overall rating: Low.

### Mitigation
- Carry "existing on-prem servers, no new paid licences" (OQ-021, INT-001 Q16) into the Phase 3 input brief as a hard constraint; the Phase 3 intake records server capacity and already-licensed software; any need beyond it is escalated to the Business owner / BA as a budget decision.
- Owner of actions: Architect / tech lead (Mohanasunder).

### Owner
Architect / tech lead (Mohanasunder)

---

## Risk R-4: KPIs cannot be measured reliably against their baselines and targets

### Risk Description
- Cause: baselines and targets are set for G-1 to G-3 (SLA compliance % 80% to 95%; MTTR 3 days to 1 day; manual admin and reporting hours 40 to 10 per month; OQ-001) and G-4 (% of clients on the dashboard, 0% to 100%; OQ-020, OQ-023). The standard SLA is now known (P1 to P4 response and resolution targets, 9x5 support hours; OQ-004). Today SLA breaches are found only at month-end report compilation, up to about 30 days late (OQ-016), by the delivery manager from one shared spreadsheet reviewed at month-end only (OQ-005, OQ-015, OQ-030). Mohanasunder confirmed (2026-10-17, chat; OQ-001) that the 80% baseline comes from the month-end manual count, while release 1 measures with SLA timers (SCP-001 IS-1).
- Event: release 1 counts breaches that the manual month-end count missed, or counts them differently (for example, response and resolution targets separately or together).
- Consequence: success of release 1 against BRF G-1 cannot be shown on a like-for-like basis.

### Likelihood And Impact
- Likelihood: Medium. The measurement method behind the baseline is now known but is manual and late (OQ-016); the SLA compliance % formula is not yet defined.
- Impact: Medium. Delivery can proceed, but the business case cannot be proven.
- Overall rating: Medium.

### Mitigation
- OQ-001, OQ-004, OQ-016, OQ-020, OQ-023, OQ-030 and OQ-033 (G-4 denominator 1) answered 2026-10-17.
- In Phase 2, define the SLA compliance % formula from the standard SLA (OQ-004) and state how it compares with the month-end manual count behind the 80% baseline (OQ-016).
- Owner of actions: Product owner (Mohanasunder).

### Owner
Product owner (Mohanasunder)

---

## Risk R-5: SLA rules and the as-is process rest on chat answers, with no SOPs or sample spreadsheets

### Risk Description
- Cause: the client SLA terms and the as-is flow are now given as answers (standard SLA, OQ-004; ticket flow, OQ-005; who does each step, OQ-015; breach detection, OQ-016; process owners, escalation, priority, closure, report and export sending, SLA tracking and effort recording, OQ-025 to OQ-032), but no SOP documents or sample spreadsheets were supplied (OQ-004; IRC-002 row 3).
- Event: Phase 2 SLA timer rules or reporting stories rest on an answer that differs from how the team actually works.
- Consequence: SLA timers (SCP-001 IS-1) and per-client reports (IS-2) are specified wrong and must be reworked through spec change records later.

### Likelihood And Impact
- Likelihood: Low (was Medium). Priority levels, response and resolution targets, support hours, the ticket flow and the actor for each step are now stated by the Business owner / BA (OQ-004, OQ-005, OQ-015).
- Impact: High. SLA timers and SLA reporting are core release 1 capabilities (INT-001 Q5) and the top problem (INT-001 Q2).
- Overall rating: Medium.

### Mitigation
- OQ-004, OQ-005, OQ-015, OQ-016, OQ-017 and OQ-025 to OQ-032 answered 2026-10-17; `process-maps.md` marks steps that rest on interview or chat answers only (PIB-001 § Readiness Verdict condition 2).
- Phase 2 business rules for SLA timers cite the OQ-004 answer as their source, so the Business owner / BA confirms them at the Phase 2 gate.
- Owner of actions: Business owner / BA (Mohanasunder).

### Owner
Business owner / BA (Mohanasunder)

---

## Risk R-6: One client's data seen by another client's users

### Risk Description
- Cause: client users log in to the same tool that holds every client's tickets and SLA reports (INT-001 Q3a); tickets and accounts hold names and emails (INT-001 Q15). All client users share one client role that raises tickets and views their organization's SLA reports (OQ-022). The release 1 pilot is internal: Applexus acts as its own client, Applexus staff are the about 20 client users, and external clients come after release 1 (OQ-007, OQ-024). The pilot has one client organization, Applexus (OQ-033), so the client data boundary is not exercised at all during the pilot.
- Event: the own-organization-only rule (INT-001 Q14) is not specified, built or tested completely, and the gap is not found in the pilot because no second real external organization uses the tool.
- Consequence: the defect surfaces only after release 1, when the first external client organization goes live: that client sees another client's (or Applexus's) tickets, SLA reports, names or emails; loss of client trust. During the pilot itself exposure is limited to Applexus's own data.

### Likelihood And Impact
- Likelihood: Medium (unchanged). The rule is confirmed (A-002) but not yet specified; release 1 is the first time clients log in (INT-001 Q3a). The internal pilot lowers the chance of real cross-client exposure during the pilot but raises the chance that a boundary defect goes undetected until external clients join.
- Impact: High (unchanged). Exposure of one client's data to another affects every client using the tool once external clients join.
- Overall rating: High.

### Mitigation
- Carry INT-001 Q14 into Phase 2 as a business rule with testable acceptance criteria covering at least two client organizations, and into the Phase 3 security approach.
- Decided by Mohanasunder, 2026-10-17 (DEC-022): client data separation (SCP-001 IS-5) is built and tested with at least two client organizations' data before any external client joins, even though the pilot is internal (OQ-024, OQ-033). Testing happens in Phase 6 feature tests and Phase 7 system testing, independent of the pilot.
- Before the first external client organization goes live after release 1, re-run the data boundary tests and review the result as a named human go-live decision.
- Owner of actions: Architect / tech lead (Mohanasunder).

### Owner
Architect / tech lead (Mohanasunder)

---

## Risk R-7: Release 1 scope boundaries not fully decided

### Risk Description
- Cause: the effort export, ITSM and mobile boundaries were open (OQ-008, OQ-010, OQ-011). All three were decided on 2026-10-17: effort data is exported monthly to finance as Excel/CSV, against hours-bank and fixed-fee contracts (OQ-008); no ITSM tool replacement or integration with client ITSM tools in release 1 (OQ-010; SCP-001 OS-3); desktop web browser only (OQ-011; SCP-001 OS-4).
- Event: one of these items is pulled back into release 1 after Phase 2 starts.
- Consequence: scope grows after requirements are approved, adding rework and pressure on the timeline (RSK R-2).

### Likelihood And Impact
- Likelihood: Low (was Medium). No undecided scope item remains in SCP-001.
- Impact: Medium. Each item adds work but none changes the core capabilities.
- Overall rating: Low.

### Mitigation
- OQ-008, OQ-010 and OQ-011 answered 2026-10-17 and recorded in SCP-001 (IS-3, OS-1, OS-3, OS-4).
- Status: Closed. Mohanasunder (Business owner / BA) confirmed closing R-7 (scope boundaries decided) at the Phase 1 gate risk review, 2026-10-17.
- Any later change to these boundaries is a named human scope decision (`scripts/log_decision.py`) or a spec change record.
- Owner of actions: Product owner (Mohanasunder).

### Owner
Product owner (Mohanasunder)

---

## Risk R-8: Discovery rests on one person's input

### Risk Description
- Cause: all Phase 1 evidence comes from one interview and one set of chat answers from Mohanasunder (INT-001; IRC-002 row 2; OQ answers of 2026-10-17). No support engineer, delivery manager or client user was consulted; stakeholders are named as an organization (Applexus) only, with no individuals (OQ-006). The release 1 pilot is internal, with Applexus staff as the client users (OQ-024), so no external client gives input before go-live.
- Event: user groups' real goals, tasks or pain points differ from what is recorded in PER-001; for client users (PER P-4), the needs of external client organizations differ from those of Applexus staff acting as clients.
- Consequence: Phase 2 stories miss needs of L1 support engineers, L2/L3 support engineers, delivery managers or client users, found only at UAT; external client needs are found only after release 1, when the first external client goes live.

### Likelihood And Impact
- Likelihood: Medium (unchanged). The persona assumptions are resolved by the Business owner / BA (A-005 and A-007 Confirmed; A-006 Rejected, so L1 and L2/L3 are split), but still by one person; OQ-024 confirms no external client user input before go-live.
- Impact: Medium (unchanged). Internal users' gaps cost rework in stories and acceptance criteria if found before Phase 4; external client gaps fall after release 1, outside the pilot go-live.
- Overall rating: Medium.

### Mitigation
- Persona questions answered 2026-10-17 (OQ-018, OQ-019, OQ-022, OQ-024); PER-001 holds PER P-1 to P-4.
- Involve Applexus staff acting as client users (PER P-4) and at least one engineer and one delivery manager in Phase 7 UAT.
- Before the first external client organization is onboarded after release 1, gather that client's input through Phase 9 feedback and route gaps into Phase 2 as backlog items.
- Owner of actions: Business owner / BA (Mohanasunder).

### Owner
Business owner / BA (Mohanasunder)

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-001 (Confirmed, Mohanasunder 2026-10-17, OQ-013): the 3-month window starts 2026-10-17; pilot go-live 2027-01-17 (R-2).
- A-002 (Confirmed, INT-001 Q14): client users see only their own organization's data (R-6).
- A-005 and A-007 (Confirmed, Mohanasunder 2026-10-17, OQ-019 and OQ-015) and A-006 (Rejected, Mohanasunder 2026-10-17, OQ-018): the persona assumptions R-8 depended on.
- No new assumptions in this version.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
- None open.
- Answered 2026-10-17: OQ-033 (R-2, R-4, R-6: one pilot client organization); OQ-025 to OQ-032 (R-5; OQ-030 also R-4); OQ-024 (R-2, R-6, R-8: internal pilot, Applexus staff as client users); OQ-001, OQ-020, OQ-023 (R-4); OQ-004 (R-4, R-5); OQ-005, OQ-015, OQ-017 (R-5); OQ-016 (R-4, R-5); OQ-006 (R-8); OQ-007 (R-2, R-3, R-6); OQ-008, OQ-010, OQ-011 (R-7); OQ-013 (R-2); OQ-014 (R-1, DEC-020); OQ-018, OQ-019, OQ-022 (R-8); OQ-021 (R-3).

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason'.
     Cite individual risks as RSK R-N (e.g. RSK R-2). -->
- Upstream: PIB-001 v0.1 § Readiness Verdict; INT-001 v0.1; IRC-002 v0.1; `project.md`; `docs/logs/decision-log.md` (single-approver decision).
- Related Phase 1: BRF-001 (goals G-1 to G-4); SCP-001 (IS-1 to IS-5, OS-1 to OS-4); PER-001 (PER P-1 to P-4); PRC-001.
- Index: RSK R-1 to RSK R-8 rows in `docs/logs/risk-register.md`.
- Downstream: Phase 2 business rules and NFRs (R-4, R-5, R-6), Phase 3 input brief (R-3, R-6), Phase 5 plan (R-2), Phase 7 UAT (R-8) - not yet created.

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Every risk has a unique R-N ID; IDs are consecutive and never reused
- [x] Every risk has an owner (named role) and a mitigation
- [x] Each risk is recorded in docs/logs/risk-register.md as RSK R-N
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
