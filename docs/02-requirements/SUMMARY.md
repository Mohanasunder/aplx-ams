---
id: SUM-002
title: Phase 2 summary
phase: 2
version: 0.4
template: phase-summary
template_version: 1.0
status: Approved
author_agent: requirements-analyst
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# Phase 2 summary

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- PIB-002 v0.1, INT-002 v0.1, IRC-003 v0.1 (Approved 2026-10-17).
- SUM-001 v0.3 and the Phase 1 artifacts it indexes (BRF-001, PER-001, SCP-001, RSK-001, PRC-001 v0.2).
- `project.md`; DEC-018, DEC-020, DEC-022, DEC-025, DEC-026 (`docs/logs/decision-log.md`).
- SCR S-3 (`docs/logs/spec-changes.md`, Approved): password set, reset and change, decided by Mohanasunder (Product owner / BA), chat, 2026-10-17; revised PRS-001, EPC-001, REQ-001, BR-001, BKL-001, GLO-001, NFR-001 to v0.2.
- SCR S-4 (`docs/logs/spec-changes.md`, Draft): security events in the audit trail, OQ-062 answered by Mohanasunder (Product owner / BA), chat, 2026-10-17; revises PRS-001, EPC-001, REQ-001, BR-001, BKL-001, GLO-001, NFR-001 to v0.3.

## Purpose And Scope
<!-- guidance: One or two sentences: which phase this summarizes. File docs/0N-*/SUMMARY.md -->
Summarises Phase 2 (Requirements) of APLX AMS so Phase 3 (Architecture) can start from this page and open full documents only for the sections listed.

## Decisions
<!-- guidance: Bullets: the decision, the reason in one clause, and its source 'ID vX.Y § section'. Only decisions later phases must respect -->
- Release 1 = 8 features (PRS F-1 to F-8), 5 epics, 33 stories (REQ S-30, S-31 added by SCR S-3; REQ S-32, S-33 by SCR S-4), all Must for go-live 2027-01-17 (INT-002 v0.1 Q1; DEC-026; PRS-001, BKL-001).
- Intake is portal only; no mailbox, no ITSM integration, desktop browser only (INT-002 Q5; PRS-001 § Non-Goals NG-3 to NG-5). Client users add comments on their own organization's tickets; internal users add comments visible to the client user, which do not clear awaiting client (DEC-026, part of IS-4; OQ-051). Closure: client user sees Closed in the tool, no message (OQ-037).
- SLA: standard SLA on 09:00 to 18:00 IST Monday to Friday minus the Applexus company holiday list, maintained yearly by the delivery manager; changes apply from the change onward, no recalculation (OQ-041, OQ-050); SLA timers start at raise; the response clock stops at the first L1 action of any kind (acknowledgement; a priority change as first action is judged against the new priority's response target, OQ-046); the resolution clock stops at Resolved; paused while awaiting client (set by the assigned support engineer, cleared by a client user's comment, OQ-045); at risk 90%, breached at 100% (a stop at exactly 100% is breached; met only below 100%); in-app only; escalation flag at 50% of the resolution target (BR-001 B-1 to B-10; Phase 2 gate answers, Mohanasunder, 2026-10-17).
- Priority change (L1 only, with a reason, not after Resolved): only running SLA timers recalculate from the raise time; stopped timers keep met or breached; the escalation point moves to 50% of the new resolution target, and a flag below the new point clears and reappears when reached (BR-001 B-7, B-10; Phase 2 gate and review answers, 2026-10-17).
- Resolved by L1 or L2/L3 returns the ticket to the L1 queue; only L1 closes (BR-001 B-11).
- BRF-001 G-1 is measured by resolution % (BR-001 B-12); the 80% baseline is kept as stated although not like-for-like (DEC-025). G-2 MTTR = mean business time raise to Resolved, paused time excluded, in business days of 9 business hours, over tickets Resolved in the month; the 3-day baseline was in business days, like-for-like (OQ-039, OQ-049; BR-001 B-13).
- Monthly client report: the delivery manager generates, reviews and publishes; client users see it once published (OQ-047; BR-001 B-14).
- SLA targets in days: 1 day = 9 business hours (OQ-040 answered; BR-001 B-1).
- Goals are cited as `BRF-001 G-n` because `scripts/traceability.py` matches that form only (EPC-001 § Purpose And Scope).
- One active contract per client organization, ended and replaced by the delivery manager; no effort without an active contract; hours bank balance = contracted hours - recorded hours, may go negative with a warning to the delivery manager; fixed fee hours for visibility only; effort only on tickets assigned to the support engineer, own entries editable until month end, delivery manager corrects any, all audited; monthly finance export as Excel or CSV with the month-end balance, downloaded by the delivery manager and emailed to finance outside the tool, no finance role (BR-001 B-15 to B-18; OQ-038, OQ-042, OQ-043, OQ-048).
- Client data boundary built and tested with two client organizations (BR-001 B-20; DEC-022).
- Passwords: the delivery manager sets a temporary password on a new user account and a new temporary password for a user who forgot their password (asked outside APLX AMS); any signed-in user changes their own password after entering their current password, meeting the password policy (OQ-053); a new temporary password clears a lock at once (OQ-054; NFR-001 v0.3 N-5); no forced password change at first sign-in or after a reset (lower security chosen knowingly); no email or self-service password reset (SCR S-3; BR-001 v0.3 B-23; REQ-001 v0.3 S-30, S-31).
- Security events in the audit trail like other audit entries: successful sign-ins, failed sign-ins, user account lockouts, temporary passwords set by the delivery manager, users changing their own password, each with the user, the user account (or an unknown account name as typed) and the time; every refused sign-in is a failed sign-in; no password value in any audit entry; the delivery manager views all security events, each internal user their own, client users none; no alerting, no new reporting (OQ-062, OQ-064, OQ-065 answered, Mohanasunder, 2026-10-17; SCR S-4; BR-001 v0.3 B-24; REQ-001 v0.3 S-32, S-33; NFR-001 v0.3 N-6).
- No MFA; weekly backup, RPO 7 days, RTO 1 business day; retention indefinite (NFR-001 N-3 to N-5; human decisions INT-002 Q7, Q10).

## Constraints Set
<!-- guidance: Bullets: limits later phases must work within (technology, NFR targets, scope exclusions, compliance), each with its source ID -->
- Availability 99% of business hours per month (NFR-001 N-1).
- Page p95 under 2 s at 30 concurrent users, 10 engineer and 20 client user sessions (NFR-001 N-2).
- Backup every 7 days, RPO 7 days, RTO 9 business hours (NFR-001 N-3); 0 automatic deletions (N-4).
- Password at least 8 characters with upper-case, lower-case and digit, locked 30 minutes after 5 failed sign-ins, no MFA (NFR-001 N-5; OQ-044); 100% audit of status, priority, assignment and effort changes and of the 5 security event types, 0 audit entries with a password value (N-6); 0 cross-organization records (N-7); Chrome and Edge current and previous major versions (N-8; A-008); personal data limited to name and email per user account (N-9).
- Existing on-prem servers, no new paid licences (SUM-001 v0.3 § Constraints Set).

## Open Items
<!-- guidance: Open questions (OQ-), assumptions (A-), and risks (RSK-) still open, with owner; or 'None' -->
All owned by Mohanasunder.
- Open OQs: none. OQ-037 to OQ-051 Answered; OQ-053 (current password needed to change a password) and OQ-054 (a new temporary password clears the lock), raised by SCR S-3, Answered; OQ-062 (security events in the audit trail), OQ-064 (who views security events) and OQ-065 (every refused sign-in is a failed sign-in), SCR S-4, Answered (Mohanasunder, 2026-10-17, chat).
- Open assumptions: A-008, A-014 to A-016, A-019 to A-022 (A-009 to A-011, A-013, A-017, A-018, A-023 to A-025 Confirmed; A-012 Rejected).
- Risks: new RSK-002 R-1 (no MFA; Low in the pilot, Medium once external clients join) and R-2 (RPO 7 days, Medium), Open; RSK R-2 (MoSCoW: all Must, no scope-cut lever), R-3, R-6, R-8 Open; R-4, R-5 Mitigating; all eight Open or Mitigating rows confirmed as stated at the Phase 2 gate risk review (Mohanasunder, 2026-10-17) (`docs/logs/risk-register.md`).
- G-1 baseline settled: 80% kept (DEC-025; BR-001 B-12; RSK R-4).
- BR-001 B-12 formulas confirmed as written (Mohanasunder, Phase 2 review answers, 2026-10-17).

## Documents
<!-- guidance: One line per Approved artifact of the phase: 'ID vX.Y - title - path'. Checked by scripts/context_pack.py summaries -->
Phase 2 deliverables (PRS-001, EPC-001, REQ-001, BR-001, BKL-001, GLO-001 and NFR-001 at v0.3 under SCR S-4; each is Approved once its approval is recorded in `docs/logs/approval-log.md`):
- PIB-002 v0.1 - Phase 2 input brief - docs/02-requirements/phase-input-brief.md
- INT-002 v0.1 - Phase 2 interview - docs/02-requirements/interview-record.md
- IRC-003 v0.1 - Phase 2 readiness - docs/02-requirements/input-readiness-checklist.md
- PRS-001 v0.3 - APLX AMS: Product Requirement Specification - docs/02-requirements/product-requirement-specification.md
- EPC-001 v0.3 - APLX AMS: Epics - docs/02-requirements/epics.md
- REQ-001 v0.3 - APLX AMS: User Stories - docs/02-requirements/user-stories.md
- NFR-001 v0.3 - APLX AMS: Non-Functional Requirements - docs/02-requirements/nfrs.md
- BR-001 v0.3 - APLX AMS: Business Rules - docs/02-requirements/business-rules.md
- BKL-001 v0.3 - APLX AMS: Backlog - docs/02-requirements/backlog.md
- GLO-001 v0.3 - APLX AMS: Domain Glossary - docs/02-requirements/domain-glossary.md
- RSK-002 v0.1 - APLX AMS: Phase 2 risks - docs/02-requirements/risks.md

## What The Next Phase Needs
<!-- guidance: The few documents or sections the next phase should open in full, as 'ID vX.Y § section'; everything else is covered above -->
- NFR-001 v0.3 § NFR N-1 to N-9.
- BR-001 v0.3 § Rule B-1 to B-11 (SLA timers), § Rule B-20 (data boundary), § Rule B-22 (audit), § Rule B-23 (passwords), § Rule B-24 (security events).
- REQ-001 v0.3 § Story S-20, S-21, S-30, S-31, S-32, S-33 (user accounts, sign-in, passwords, security events).
- RSK-002 v0.1 § Risk R-1, R-2; RSK-001 v0.2 § Risk R-3, R-6.
- PRS-001 v0.3 § Product Scope; GLO-001 v0.3 § Terms.

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-008, A-014 to A-016, A-019 to A-022 (Open), A-009 to A-011, A-013, A-017, A-018, A-023 to A-025 (Confirmed), A-012 (Rejected), listed under § Open Items; logged in `docs/logs/assumptions-log.md`.

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
- OQ-037 to OQ-051, OQ-053, OQ-054, OQ-062, OQ-064, OQ-065 Answered; none Open; listed under § Open Items; logged in `docs/logs/open-questions-log.md`.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: PIB-002; INT-002; IRC-003; SCR S-3; SCR S-4; SUM-001; BRF-001; SCP-001; PER-001; PRC-001; RSK-001.
- Indexes: PRS-001; EPC-001; REQ-001; NFR-001; BR-001; BKL-001; GLO-001; RSK-002.
- Downstream: Phase 3 input brief PIB-003 (docs/03-architecture/phase-input-brief.md).

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
| Role | Product owner / BA |
| Version | 0.4 |
| Conditions | None |
| Comments | Security events in the audit trail per SCR S-4 (OQ-062, OQ-064, OQ-065); R-10 accepted. |
| Timestamp | 2026-10-17 10:59 UTC |
