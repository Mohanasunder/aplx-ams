---
id: RSK-002
title: APLX AMS: Phase 2 risks
phase: 2
version: 0.1
template: risk-register-entry
template_version: 2.0
status: Approved
author_agent: requirements-analyst
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# APLX AMS: Phase 2 risks

> **Collection file.** All risks raised in this phase live in this one file. Add one `## Risk R-N` section per risk; never create a separate RSK-NNN file for an additional risk in the same phase. The risk-register index (`docs/logs/risk-register.md`) references each risk as `RSK R-N` (e.g. `RSK R-2`). The live status of each risk lives there, not here.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- PIB-002 v0.1 § Constraints (candidate risks: no MFA on client log-in; RPO 7 days), § Interview Answers Q7, Q10.
- INT-002 v0.1 Q7, Q10, Q10a.
- SUM-001 v0.3 § Decisions (internal pilot; external clients after release 1), § Constraints Set (names and emails only).
- RSK-001 v0.2 (rating method; R-6 data boundary).

## Purpose And Scope
<!-- guidance: What risks this artifact covers and what it does not. One collection per phase. -->
Covers: new risks raised in Phase 2 from human decisions the requirements record as stated: R-1 no MFA on the client log-in once external clients join (INT-002 Q7) and R-2 up to 7 days of data lost on a restore (INT-002 Q10, Q10a). The decisions themselves are not changed (PIB-002 § Constraints).

Does not cover: changes to Phase 1 risks (row updates in `docs/logs/risk-register.md`), or technical security design (Phase 3 threat model). Register rows use the ID form `RSK-002 R-N` so they do not clash with the Phase 1 rows `RSK R-1` to `RSK R-8` (RSK-001). Rating method as in RSK-001 v0.2.

---

## Risk R-1: No MFA on the client log-in once external clients join

### Risk Description
- Cause: every user, including client users, signs in with a user account and password only; no MFA, by the human's security decision (INT-002 Q7; NFR N-5). Release 1 is an internal pilot, but external client organizations come after release 1 (SUM-001 § Decisions), and the tool holds every client organization's tickets with names and emails.
- Event: a client user's password is guessed, reused from another breach, or phished after external clients join.
- Consequence: an attacker sees and acts on that client organization's tickets and reports; with a data boundary defect (RSK R-6) exposure could reach other client organizations.

### Likelihood And Impact
- Likelihood: Low during the internal pilot (Applexus staff only, about 20 client users); Medium once external client users sign in from outside the company.
- Impact: Medium. Data is names, emails and ticket content, no regulatory obligation known (INT-001 Q11, Q15); a breach still harms client trust.
- Overall rating (RSK-001 v0.2 method): Low during the internal pilot (Low likelihood, Medium impact: neither is High and they are not both Medium); Medium once external clients join (Medium likelihood, Medium impact). Both ratings are recorded; the gate risk review decides which one the register carries.

### Mitigation
- Record the decision as stated (NFR N-5, PRS NG-7); password policy and lockout per NFR N-5 (OQ-044 answered 2026-10-17: at least 8 characters with an upper-case letter, a lower-case letter and a digit; locked 30 minutes after 5 failed sign-ins).
- Carry into the Phase 3 threat model; re-decide MFA before the first external client organization goes live, as a named human decision.
- Owner of actions: Architect / tech lead (Mohanasunder).

### Owner
Architect / tech lead (Mohanasunder)

---

## Risk R-2: Up to 7 days of ticket and effort data lost on a restore

### Risk Description
- Cause: backup is weekly, RPO 7 days, RTO 1 business day, by the human's compliance decision (INT-002 Q10, Q10a; NFR N-3).
- Event: data loss (server failure or corruption) just before the next weekly backup, with restore from the last backup.
- Consequence: up to 7 days of tickets, acknowledgement and Resolved times, effort entries and audit entries are lost; SLA timer results, the monthly client report and the finance export for that period are wrong or must be rebuilt by hand.

### Likelihood And Impact
- Likelihood: Low. Hosting is on existing on-prem servers (OQ-021); no failure history is recorded.
- Impact: High. Lost effort entries affect hours bank balances in the finance export; lost timer data affects resolution % (BRF-001 G-1).
- Overall rating (RSK-001 v0.2 method): Medium (one High, the other Low).

### Mitigation
- Record the decision as stated (NFR N-3); restore drill before go-live (NFR N-3 verification).
- Phase 3 states the backup approach on the existing servers; the human may revisit backup frequency if the restore drill or Phase 3 shows a lower RPO at no extra cost.
- Owner of actions: Business owner / BA (Mohanasunder).

### Owner
Business owner / BA (Mohanasunder)

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-012 (Rejected 2026-10-17): replaced by the OQ-044 answer in the R-1 mitigation.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
- OQ-044 (Answered, Mohanasunder, 2026-10-17): password policy values (R-1). No open question for these risks.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason'.
     Cite individual risks as RSK R-N (e.g. RSK R-2). -->
- Upstream: PIB-002 v0.1 § Constraints; INT-002 v0.1 (Q7, Q10, Q10a); SUM-001 v0.3; RSK-001 v0.2.
- Related Phase 2: NFR-001 (N-3, N-5); PRS-001 (NG-7).
- Index: rows `RSK-002 R-1` and `RSK-002 R-2` in `docs/logs/risk-register.md`.
- Downstream: Phase 3 threat model and deployment topology (not yet created).

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
| Role | Product owner / BA |
| Version | 0.1 |
| Conditions | None |
| Comments | Reviewed after validation run 4; all open questions answered; R4 findings fixed. |
| Timestamp | 2026-10-17 08:46 UTC |
