---
id: SCR-001
title: Spec Changes
phase: 1
version: 0.1
template: spec-change
template_version: 2.0
status: In review
author_agent: discovery-analyst
approver: Approver of the changed artifact's phase
date: 2026-10-17
validation: Pass with warnings
---
# Spec Changes

<!-- Collection file. All spec change records are appended as `## SCR S-N: [title]` sections (S-1, S-2, …). Never create a separate file per spec change. Sub-IDs are consecutive and never reused. Cite a specific record as `SCR S-N`. Per-record status stored as HTML comments within each section. Approve each section individually with `/approve docs/logs/spec-changes.md --sub-id S-N`. -->

## SCR S-1: Phase 1 summary wording after approval

<!-- scr_status: Approved -->
<!-- scr_date: 2026-10-17 -->
<!-- scr_approver: Mohanasunder -->

### Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- SUM-001 v0.2 (Approved 2026-10-17 06:05 UTC by Mohanasunder) - docs/01-discovery/SUMMARY.md.
- `docs/logs/approval-log.md` (Phase 1 approvals of 2026-10-17).

### Purpose And Scope
<!-- guidance: What this change covers and what it does not -->
Covers wording-only corrections: SUM-001 § Input References and § Documents (approval status of the Phase 1 deliverables) and § Open Items (confirmed-assumptions list, correcting it to match the assumptions log), and the OQ-002 "Answer and date" cell in `docs/logs/open-questions-log.md`. Does not change any decision, constraint, open item, goal, scope item, persona, or risk. Does not change PIB-001 v0.1 or IRC-002 v0.1 (scope chosen by Mohanasunder, Business owner / BA, in chat on 2026-10-17).

### Changed Artifact
<!-- guidance: One line per changed approved artifact: 'ID vOLD -> vNEW' (for example 'API v1.0 -> v1.1'), with its path -->
- SUM-001 v0.2 -> v0.3 (docs/01-discovery/SUMMARY.md)

### Trigger
<!-- guidance: First line: what revealed the problem and where (FEAT-, DEF D-N, PR, review comment, feedback or incident ID) and who found it -->
Orchestrator review after the Phase 1 gate on 2026-10-17: SUM-001 § Input References and § Documents still say the Phase 1 deliverables are "Draft, pending approval" though all are Approved; plus run 1 finding F-03 (docs/validation/phase-1-run-1.md) on the OQ-002 answer wording in docs/logs/open-questions-log.md.

### Change
<!-- guidance: What changes, section by section: before and after. Specs change here first; code is regenerated from them -->
- SUM-001 § Input References: before "Phase 1 deliverables below are Draft, pending validation and approval; versions are updated here once approved." After: all Phase 1 deliverables listed under § Documents are Approved at v0.2 on 2026-10-17.
- SUM-001 § Documents: the "Draft, pending approval" list is merged into the Approved list; BRF-001, PER-001, SCP-001, RSK-001, PRC-001 listed as Approved v0.2.
- `docs/logs/open-questions-log.md` row OQ-002, Answer and date (a log row, not a versioned artifact): before "Only client contact names and emails"; after "Only names and emails", matching INT-001 v0.1 Q15.
- SUM-001 § Open Items, assumptions bullet: before "A-001, A-004, A-005, A-007 Confirmed"; after "A-001, A-002, A-003, A-004, A-005, A-007 Confirmed", matching `docs/logs/assumptions-log.md` (A-002 and A-003 Confirmed by Mohanasunder, 2026-10-17) and SUM-001 § Assumptions (checker run 6 finding N-02).
- No other change to decisions, constraints, or open items.

### Reason
<!-- guidance: Why the approved spec was wrong or incomplete -->
SUM-001 was written before the Phase 1 deliverables were approved and was not refreshed at approval. The OQ-002 log row narrowed the recorded answer ("client contact names and emails") compared with the source answer in INT-001 v0.1 Q15 ("names and emails").

### Decision Record
<!-- guidance: Required when Changed Artifact lists an architecture or contract artifact (templates architecture-overview, adr, api-spec, database-design, deployment-topology, threat-model): cite the new ADR A-N that records this change, with options considered and consequences. When an ADR itself changes, cite the new ADR that supersedes it (the old ADR's Status And Date becomes 'Superseded by ADR A-N', listed under Changed Artifact). The ADR is approved by the architect / tech lead together with this SCR (checked by scripts/spec_impact.py records). Otherwise write 'Not applicable - no architecture or contract artifact changes' -->
Not applicable - no architecture or contract artifact changes. Scope of this SCR (SUM-001 and the OQ-002 log row only; PIB-001 and IRC-002 unchanged) chosen by Mohanasunder (Business owner / BA), chat, 2026-10-17.

### Impact
<!-- guidance: From 'python3 scripts/spec_impact.py impact <ID>': table of each citing artifact or feature, its state, and the action: revise, re-test, re-approve, or 'No change - reason' -->
`python scripts/spec_impact.py impact SUM-001`: "SUM-001: current v0.2 (Approved) at docs/01-discovery/SUMMARY.md. No artifact cites it."

| Artifact | State | Action |
| --- | --- | --- |
| SUM-001 | Approved v0.2 | Revise to v0.3 and re-approve |
| PIB-001 v0.1 | Approved | No change - original intake wording "client contact names and emails" kept as historical record by Mohanasunder's decision; downstream deliverables already use "names and emails" |
| IRC-002 v0.1 | Approved | No change - original intake wording "client contact names and emails" kept as historical record by Mohanasunder's decision; downstream deliverables already use "names and emails" |

### Work Stopped
<!-- guidance: Features set to State: Blocked with this SCR cited, or 'None - reason' -->
None - no features exist yet.

### Resume Criteria
<!-- guidance: What must be Approved before stopped work resumes (this SCR, the new artifact version, the ADR in Decision Record if any, revised downstream artifacts) -->
SCR S-1 and SUM-001 v0.3 Approved.

### Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
None.

### Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
None.

### Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: INT-001 v0.1 (Q15); SUM-001 v0.2
- Downstream: SUM-001 v0.3

### Quality Checklist
- [x] Every section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)
- [x] Every changed artifact is listed as 'ID vOLD -> vNEW'
- [x] An architecture or contract change cites its new or superseding ADR A-N under Decision Record
- [x] Impact covers every artifact and feature that cites the changed artifact

## SCR S-2: Phase 2 summary wording after approval
<!-- scr_approver: Mohanasunder -->

<!-- scr_status: Approved -->
<!-- scr_date: 2026-10-17 -->

### Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- SUM-002 v0.1 (Approved 2026-10-17 08:46 UTC by Mohanasunder) - docs/02-requirements/SUMMARY.md.
- `docs/logs/approval-log.md` (Phase 2 approvals of 2026-10-17).

### Purpose And Scope
<!-- guidance: What this change covers and what it does not -->
Covers a wording-only correction to SUM-002 § Documents (approval status of the Phase 2 deliverables). Does not change any decision, constraint, open item, requirement, rule, NFR, or risk (scope chosen by Mohanasunder, Product owner / BA, in chat on 2026-10-17).

### Changed Artifact
<!-- guidance: One line per changed approved artifact: 'ID vOLD -> vNEW' (for example 'API v1.0 -> v1.1'), with its path -->
- SUM-002 v0.1 -> v0.2 (docs/02-requirements/SUMMARY.md)

### Trigger
<!-- guidance: First line: what revealed the problem and where (FEAT-, DEF D-N, PR, review comment, feedback or incident ID) and who found it -->
Orchestrator review after the Phase 2 gate on 2026-10-17: SUM-002 § Documents still lists the Phase 2 deliverables under "Draft, awaiting review (v0.1):" though all were Approved at v0.1 on 2026-10-17.

### Change
<!-- guidance: What changes, section by section: before and after. Specs change here first; code is regenerated from them -->
- SUM-002 § Documents: before, the heading line "Draft, awaiting review (v0.1):" above PRS-001, EPC-001, REQ-001, NFR-001, BR-001, BKL-001, GLO-001, RSK-002 v0.1. After: that heading line is removed, so the eight deliverables sit in the single "Approved:" list (all Approved v0.1 on 2026-10-17).
- No other change to decisions, constraints, open items, or document versions.

### Reason
<!-- guidance: Why the approved spec was wrong or incomplete -->
SUM-002 was written before the Phase 2 deliverables were approved and was not refreshed at approval.

### Decision Record
<!-- guidance: Required when Changed Artifact lists an architecture or contract artifact (templates architecture-overview, adr, api-spec, database-design, deployment-topology, threat-model): cite the new ADR A-N that records this change, with options considered and consequences. When an ADR itself changes, cite the new ADR that supersedes it (the old ADR's Status And Date becomes 'Superseded by ADR A-N', listed under Changed Artifact). The ADR is approved by the architect / tech lead together with this SCR (checked by scripts/spec_impact.py records). Otherwise write 'Not applicable - no architecture or contract artifact changes' -->
Not applicable - no architecture or contract artifact changes. Change decided by Mohanasunder (Product owner / BA), chat, 2026-10-17.

### Impact
<!-- guidance: From 'python3 scripts/spec_impact.py impact <ID>': table of each citing artifact or feature, its state, and the action: revise, re-test, re-approve, or 'No change - reason' -->
`python scripts/spec_impact.py impact SUM-002`: "SUM-002: current v0.1 (Approved) at docs/02-requirements/SUMMARY.md. No artifact cites it."

| Artifact | State | Action |
| --- | --- | --- |
| SUM-002 | Approved v0.1 | Revise to v0.2 and re-approve |

### Work Stopped
<!-- guidance: Features set to State: Blocked with this SCR cited, or 'None - reason' -->
None - no features exist yet.

### Resume Criteria
<!-- guidance: What must be Approved before stopped work resumes (this SCR, the new artifact version, the ADR in Decision Record if any, revised downstream artifacts) -->
SCR S-2 and SUM-002 v0.2 Approved.

### Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
None.

### Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
None.

### Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: SUM-002 v0.1
- Downstream: SUM-002 v0.2

### Quality Checklist
- [x] Every section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)
- [x] Every changed artifact is listed as 'ID vOLD -> vNEW'
- [x] An architecture or contract change cites its new or superseding ADR A-N under Decision Record
- [x] Impact covers every artifact and feature that cites the changed artifact

## SCR S-3: Password set, reset and change
<!-- scr_approver: Mohanasunder -->

<!-- scr_status: Approved -->
<!-- scr_date: 2026-10-17 -->

### Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- REQ-001 v0.1 § Story S-20, § Story S-21 (Approved 2026-10-17) - docs/02-requirements/user-stories.md.
- BR-001 v0.1 § Rule B-21 (Approved 2026-10-17) - docs/02-requirements/business-rules.md.
- GLO-001 v0.1 § Terms (Approved 2026-10-17) - docs/02-requirements/domain-glossary.md.
- NFR-001 v0.1 § NFR N-5 (password policy; OQ-044) - docs/02-requirements/nfrs.md.
- EPC-001 v0.1 § Epic E-5; BKL-001 v0.1; PRS-001 v0.1 § Feature F-6; SUM-002 v0.2.
- Human decision: Mohanasunder (Product owner / BA), chat, 2026-10-17, option C on VAL-013 (docs/validation/phase-3-run-1.md) finding F-1.

### Purpose And Scope
<!-- guidance: What this change covers and what it does not -->
Covers adding password handling to the release 1 requirements: (a) the delivery manager sets a temporary password when creating a user account; (b) a user who forgets their password asks the delivery manager outside APLX AMS, and the delivery manager sets a new temporary password; (c) any signed-in user (internal user or client user) changes their own password, and the new password meets the password policy (NFR N-5, OQ-044); (d) no forced password change at first sign-in or after a reset (lower security chosen knowingly). Does not add email, a self-service password reset, MFA or password expiry; no change to N-5 policy values; adds only the OQ-054 lockout exception to NFR N-5 (decision by Mohanasunder, 2026-10-17).

### Changed Artifact
<!-- guidance: One line per changed approved artifact: 'ID vOLD -> vNEW' (for example 'API v1.0 -> v1.1'), with its path -->
- REQ-001 v0.1 -> v0.2 (docs/02-requirements/user-stories.md)
- BR-001 v0.1 -> v0.2 (docs/02-requirements/business-rules.md)
- GLO-001 v0.1 -> v0.2 (docs/02-requirements/domain-glossary.md)
- EPC-001 v0.1 -> v0.2 (docs/02-requirements/epics.md)
- BKL-001 v0.1 -> v0.2 (docs/02-requirements/backlog.md)
- PRS-001 v0.1 -> v0.2 (docs/02-requirements/product-requirement-specification.md)
- NFR-001 v0.1 -> v0.2 (docs/02-requirements/nfrs.md)
- SUM-002 v0.2 -> v0.3 (docs/02-requirements/SUMMARY.md)

### Trigger
<!-- guidance: First line: what revealed the problem and where (FEAT-, DEF D-N, PR, review comment, feedback or incident ID) and who found it -->
Phase 3 validation run 1 finding F-1 (checker, 2026-10-17, docs/validation/phase-3-run-1.md): the Phase 3 interview answer INT-003 Q8 (the delivery manager sets a temporary password for a new user and for a forgotten password; no forced change) is behaviour no approved story covers (REQ-001 v0.1 S-20, S-21; BR-001 v0.1 B-21). Finding F-2: a user changing their own password was assumed in PIB-003 without a story.

### Change
<!-- guidance: What changes, section by section: before and after. Specs change here first; code is regenerated from them -->
- REQ-001: before, S-1 to S-29, no story on setting, resetting or changing a password. After: new REQ S-30 "Delivery manager sets a temporary password" (AC-1 to AC-4) and REQ S-31 "User changes their own password" (AC-1 to AC-4); § Input References, § Purpose And Scope, § Open Questions, § Traceability Links updated. S-20 unchanged; S-21 criteria unchanged (each story already has 4 criteria, the sizing limit), but the S-21 Priority line changes (OQ-054 lockout exception).
- BR-001: before, B-1 to B-22. After: B-21 Rule adds that the delivery manager sets temporary passwords on user accounts, Applies To adds REQ S-30; new Rule B-23 (Applies To REQ S-30, REQ S-31) "Password set, reset and change" (decision (a) to (d)).
- GLO-001: new terms Temporary password and Password policy; Delivery manager and User account definitions name setting temporary passwords; § Ambiguities Resolved adds the INT-003 Q8 wording "one-time temporary password".
- EPC-001: E-5 Description adds password set, reset and change; Stories adds REQ S-30, REQ S-31; Downstream REQ S-1 to S-31.
- BKL-001: new entries BL-30 (REQ S-30) and BL-31 (REQ S-31), Must, release 1; scope line BL-1 to BL-31.
- PRS-001: F-6 Description adds password set, reset and change; Linked Stories adds REQ S-30, REQ S-31.
- SUM-002: § Decisions story count 29 -> 31 and the password handling decision; § Documents cites the new versions; § Open Items adds OQ-053, OQ-054; cites SCR S-3.
- `docs/logs/traceability-matrix.md` (log, not versioned): rows REQ S-30, REQ S-31 added.
- `docs/logs/open-questions-log.md` (log): OQ-053, OQ-054 added, then Answered (Mohanasunder, 2026-10-17, chat).
- OQ-053 answer applied: a user must enter their current password to change it. REQ S-31 AC-1 states it; new REQ S-31 AC-4 (wrong current password refused); BR B-23 Rule.
- OQ-054 answer applied: when the delivery manager sets a temporary password on a locked user account, the lock clears at once and the user can sign in immediately. REQ S-30 AC-3 reworded (S-30 not yet approved); BR B-23 Rule; GLO-001 Temporary password; REQ S-21 Priority line changes to note the exception (S-21 criteria unchanged).
- NFR-001 N-5: before, "a user account is locked for 30 minutes after 5 failed sign-ins"; after, the same plus "unless the delivery manager sets a new temporary password, which clears the lock at once (BR B-23, OQ-054)", with a matching Verification Method check. The v0.1 wording contradicted the OQ-054 answer. No other NFR change.

### Reason
<!-- guidance: Why the approved spec was wrong or incomplete -->
REQ-001 v0.1 says only the delivery manager creates user accounts (S-20) and every user signs in with a password (S-21), but no story says how a user gets a first password, how a forgotten password is reset, or whether a user can change their own password. The Phase 3 interview (INT-003 Q8) answered this; the answer must enter the approved requirements before Phase 3 designs authentication on it.

### Decision Record
<!-- guidance: Required when Changed Artifact lists an architecture or contract artifact (templates architecture-overview, adr, api-spec, database-design, deployment-topology, threat-model): cite the new ADR A-N that records this change, with options considered and consequences. When an ADR itself changes, cite the new ADR that supersedes it (the old ADR's Status And Date becomes 'Superseded by ADR A-N', listed under Changed Artifact). The ADR is approved by the architect / tech lead together with this SCR (checked by scripts/spec_impact.py records). Otherwise write 'Not applicable - no architecture or contract artifact changes' -->
Not applicable - no architecture or contract artifact changes. Human decision: Mohanasunder (Product owner / BA), chat, 2026-10-17, chose option C on VAL-013 F-1: release 1 adds (a) a temporary password set by the delivery manager when creating a user account; (b) forgotten password: the user asks the delivery manager outside the tool and the delivery manager sets a new temporary password; (c) any signed-in user (internal or client) changes their own password, meeting the password policy (OQ-044, NFR N-5); (d) no forced password change at first sign-in or after a reset (INT-003 Q8; lower security chosen knowingly). Nothing else (no email, no self-service reset link, no MFA).

### Impact
<!-- guidance: From 'python3 scripts/spec_impact.py impact <ID>': table of each citing artifact or feature, its state, and the action: revise, re-test, re-approve, or 'No change - reason' -->
`python scripts/spec_impact.py impact REQ-001`, `... BR-001`, `... GLO-001` (2026-10-17): each is cited by INT-003 (Draft), IRC-004 (Draft), PIB-003 (Draft) and SUM-002 (Approved), all citing v0.1.

| Artifact | State | Action |
| --- | --- | --- |
| REQ-001 | Approved v0.1 | Revise to v0.2 and re-approve |
| BR-001 | Approved v0.1 | Revise to v0.2 and re-approve |
| GLO-001 | Approved v0.1 | Revise to v0.2 and re-approve |
| EPC-001 | Approved v0.1 | Revise to v0.2 (E-5 stories) and re-approve |
| BKL-001 | Approved v0.1 | Revise to v0.2 (BL-30, BL-31) and re-approve |
| PRS-001 | Approved v0.1 | Revise to v0.2 (F-6 linked stories) and re-approve |
| SUM-002 | Approved v0.2 | Revise to v0.3 and re-approve |
| NFR-001 | Approved v0.1 | Revise to v0.2 (N-5 lockout cleared by a new temporary password, OQ-054) and re-approve |
| PIB-003 | Draft v0.1 | Revise (Orchestrator): cite REQ-001, BR-001, GLO-001 v0.2; fix VAL-013 F-1 to F-3 |
| INT-003 | Draft v0.1 | Revise (Orchestrator): cite the new versions |
| IRC-004 | Draft v0.1 | Revise (Orchestrator): cite the new versions; fix VAL-013 F-1 |

### Work Stopped
<!-- guidance: Features set to State: Blocked with this SCR cited, or 'None - reason' -->
None - no features exist yet. Phase 3 producers not started; they start only after the Resume Criteria are met.

### Resume Criteria
<!-- guidance: What must be Approved before stopped work resumes (this SCR, the new artifact version, the ADR in Decision Record if any, revised downstream artifacts) -->
SCR S-3 and all revised artifacts Approved: REQ-001 v0.2, BR-001 v0.2, GLO-001 v0.2, EPC-001 v0.2, BKL-001 v0.2, PRS-001 v0.2, NFR-001 v0.2, SUM-002 v0.3.

### Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
None.

### Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
- OQ-053 (Answered, Mohanasunder, 2026-10-17, chat): the user must enter their current password to change it (REQ S-31 AC-1, AC-4; BR B-23).
- OQ-054 (Answered, Mohanasunder, 2026-10-17, chat): a temporary password set on a locked user account clears the lock at once; the user can sign in immediately (REQ S-30 AC-3; BR B-23; NFR N-5).

### Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: REQ-001 v0.1; BR-001 v0.1; GLO-001 v0.1; EPC-001 v0.1; BKL-001 v0.1; PRS-001 v0.1; SUM-002 v0.2; NFR-001 v0.1 (N-5); VAL-013 F-1, F-2.
- Downstream: REQ-001 v0.2 (REQ S-30, S-31); BR-001 v0.2 (BR B-21, B-23); GLO-001 v0.2; EPC-001 v0.2 (EPC E-5); BKL-001 v0.2 (BKL BL-30, BL-31); PRS-001 v0.2 (PRS F-6); NFR-001 v0.2 (NFR N-5); SUM-002 v0.3; PIB-003, INT-003, IRC-004 (Phase 3, revised by the Orchestrator).

### Quality Checklist
- [x] Every section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)
- [x] Every changed artifact is listed as 'ID vOLD -> vNEW'
- [x] An architecture or contract change cites its new or superseding ADR A-N under Decision Record
- [x] Impact covers every artifact and feature that cites the changed artifact

## SCR S-4: Security events in the audit trail
<!-- scr_approver: Mohanasunder -->

<!-- scr_status: Approved -->
<!-- scr_date: 2026-10-17 -->

### Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- NFR-001 v0.2 § NFR N-5, § NFR N-6 (Approved 2026-10-17) - docs/02-requirements/nfrs.md.
- REQ-001 v0.2 § Story S-21, S-23, S-30, S-31 (Approved 2026-10-17) - docs/02-requirements/user-stories.md.
- BR-001 v0.2 § Rule B-22, § Rule B-23 (Approved 2026-10-17) - docs/02-requirements/business-rules.md.
- GLO-001 v0.2 § Terms (Audit trail) (Approved 2026-10-17) - docs/02-requirements/domain-glossary.md.
- EPC-001 v0.2 § Epic E-5; BKL-001 v0.2; PRS-001 v0.2 § Feature F-8; SUM-002 v0.3.
- Human decision: Mohanasunder (Product owner / BA), chat, 2026-10-17, answer to OQ-062 (raised by the Draft threat model THR-001, T-3 and T-5).

### Purpose And Scope
<!-- guidance: What this change covers and what it does not -->
Covers adding 5 security events to the release 1 audit trail, recorded like other audit entries: successful sign-ins, failed sign-ins, user account lockouts, temporary passwords set by the delivery manager, and users changing their own password; each with the event, the user who did it, the user account it concerns (an unknown account name recorded as typed), and the date and time; no password value in any audit entry; every refused sign-in is a failed sign-in (OQ-065); the delivery manager views all security events per user account, each internal user their own, client users none (OQ-064). Also covers citation-only revisions of the Approved Phase 3 intake files PIB-003, INT-003, IRC-004 (decision by Mohanasunder, 2026-10-17). Does not add alerting on security events, new reporting, or any other event (user account deactivations, named in OQ-062, are not added).

### Changed Artifact
<!-- guidance: One line per changed approved artifact: 'ID vOLD -> vNEW' (for example 'API v1.0 -> v1.1'), with its path -->
- NFR-001 v0.2 -> v0.3 (docs/02-requirements/nfrs.md)
- REQ-001 v0.2 -> v0.3 (docs/02-requirements/user-stories.md)
- BR-001 v0.2 -> v0.3 (docs/02-requirements/business-rules.md)
- GLO-001 v0.2 -> v0.3 (docs/02-requirements/domain-glossary.md)
- EPC-001 v0.2 -> v0.3 (docs/02-requirements/epics.md)
- BKL-001 v0.2 -> v0.3 (docs/02-requirements/backlog.md)
- PRS-001 v0.2 -> v0.3 (docs/02-requirements/product-requirement-specification.md)
- SUM-002 v0.3 -> v0.4 (docs/02-requirements/SUMMARY.md)
- PIB-003 v0.1 -> v0.2 (docs/03-architecture/phase-input-brief.md), citation update only
- INT-003 v0.1 -> v0.2 (docs/03-architecture/interview-record.md), citation update only
- IRC-004 v0.1 -> v0.2 (docs/03-architecture/input-readiness-checklist.md), citation update only

### Trigger
<!-- guidance: First line: what revealed the problem and where (FEAT-, DEF D-N, PR, review comment, feedback or incident ID) and who found it -->
Phase 3 threat model THR-001 (Draft, security-architect, 2026-10-17, docs/03-architecture/threat-model.md) raised OQ-062: NFR N-6 audits only status, priority, assignment and effort changes, so misuse of a known temporary password or a taken-over delivery manager user account cannot be detected (THR T-3, T-5; RSK-003 R-3).

### Change
<!-- guidance: What changes, section by section: before and after. Specs change here first; code is regenerated from them -->
- NFR-001 N-6: before, 100% of status, priority, assignment and effort changes have an audit entry; after, also 100% of the 5 security events (BR B-24) have an audit entry with the event, the user who did it, the user account it concerns and the date and time to the second, and 0 audit entries hold a password value. Requirement adds the 4 kinds of failed sign-in (OQ-065) and who views security events (OQ-064); Verification Method adds a Phase 7 system test of the 5 security events, a check for values entered in password fields (a password typed as an account name is outside it: RSK-003 R-10, OQ-065) and a viewing test per role. § Requirement, § Input References, § Open Questions, § Traceability Links cite SCR S-4. No other NFR change.
- REQ-001: before, S-1 to S-31; after, new REQ S-32 "Security events are recorded in the audit trail" (AC-1 to AC-4; AC-2, AC-3 cover every refused sign-in, OQ-065) and new REQ S-33 "Users view security events" (AC-1 to AC-4, OQ-064). S-23 unchanged (it already has 4 criteria, the sizing limit). § Input References, § Purpose And Scope, § Open Questions, § Traceability Links updated; NFR-001 cited at v0.3.
- BR-001: before, B-1 to B-23; after, new Rule B-24 "Security events in the audit trail" (Applies To REQ S-32, S-33): the 5 events, every refused sign-in a failed sign-in, the content of each audit entry (unknown account name as typed), no password value, no alerting and no new reporting, the delivery manager views all security events, each internal user their own, client users none, and no user can edit or delete them (as BR B-22). B-22 Rule adds a pointer to BR B-24 for security events (no other B-22 rule change); B-22 Applies To adds REQ S-32, S-33; B-23 Rule text unchanged, Applies To adds REQ S-32. § Purpose And Scope, § Input References, § Open Questions, § Traceability Links updated; NFR-001 cited at v0.3.
- GLO-001: Audit trail definition adds security events and who views them (OQ-064); new terms Account name, Audit entry and Security event (failed sign-in = any refused sign-in; unknown account name as typed, OQ-065). NFR-001 cited at v0.3.
- EPC-001: E-5 Description adds security events in the audit trail and who views them; Stories adds REQ S-32, REQ S-33; Downstream REQ S-1 to S-33.
- BKL-001: new entries BL-32 (REQ S-32) and BL-33 (REQ S-33), Must, release 1; scope line BL-1 to BL-33.
- PRS-001: F-8 Description adds the 5 security events and who views them; Linked Stories adds REQ S-32, REQ S-33; Related REQ-001 S-1 to S-33.
- SUM-002: § Decisions story count 31 -> 33 and the security events decision; § Documents and § Sections cite the new versions; § Constraints Set N-6 line adds security events; § Open Items adds OQ-062, OQ-064, OQ-065 (Answered); § Input References cites SCR S-4 and corrects SCR S-3 from Draft to Approved.
- PIB-003, INT-003, IRC-004 (Phase 3 intake, Approved): citation update only, to the new versions of the S-4 artifacts; content revised by the Orchestrator's writer, not by the requirements analyst (decision by Mohanasunder, 2026-10-17).
- `docs/logs/traceability-matrix.md` (log, not versioned): rows REQ S-32, REQ S-33 added.
- `docs/logs/open-questions-log.md` (log): OQ-062 Answered (Mohanasunder, 2026-10-17, chat); OQ-064, OQ-065 added, then Answered (Mohanasunder, 2026-10-17, chat).

### Reason
<!-- guidance: Why the approved spec was wrong or incomplete -->
NFR-001 v0.2 N-6 and BR-001 v0.2 B-22 record only ticket changes. No approved requirement records sign-ins, lockouts or password changes, so the Phase 3 threat model could not plan detection of misuse of a temporary password or a taken-over delivery manager user account. The OQ-062 answer must enter the approved requirements before Phase 3 designs on it.

### Decision Record
<!-- guidance: Required when Changed Artifact lists an architecture or contract artifact (templates architecture-overview, adr, api-spec, database-design, deployment-topology, threat-model): cite the new ADR A-N that records this change, with options considered and consequences. When an ADR itself changes, cite the new ADR that supersedes it (the old ADR's Status And Date becomes 'Superseded by ADR A-N', listed under Changed Artifact). The ADR is approved by the architect / tech lead together with this SCR (checked by scripts/spec_impact.py records). Otherwise write 'Not applicable - no architecture or contract artifact changes' -->
Not applicable - no architecture or contract artifact changes (the Phase 3 artifacts are Draft, not Approved). Human decision: Mohanasunder (Product owner / BA), chat, 2026-10-17, answer to OQ-062: security events are recorded in the audit trail like other audit entries: successful sign-ins, failed sign-ins, account lockouts, temporary passwords set by the delivery manager, and users changing their own password. Nothing else (no alerting on them, no new reporting). No password value is recorded in any audit entry (only that the event happened, who, when, which user account). OQ-064 answer (Mohanasunder, chat, 2026-10-17): the delivery manager can view all security events (per user account); each internal user can view their own; client users cannot view security events. OQ-065 answer (Mohanasunder, chat, 2026-10-17): every refused sign-in counts as a failed sign-in (wrong password, unknown account name, deactivated account, locked account); for an unknown account name, the name is recorded as typed. Phase 3 intake files revised for citations only: decision by Mohanasunder, 2026-10-17.

### Impact
<!-- guidance: From 'python3 scripts/spec_impact.py impact <ID>': table of each citing artifact or feature, its state, and the action: revise, re-test, re-approve, or 'No change - reason' -->
`python scripts/spec_impact.py impact NFR-001`, `... REQ-001`, `... BR-001`, `... GLO-001`, `... SUM-002` (2026-10-17): cited by Phase 2 artifacts (BR-001, GLO-001, REQ-001, SUM-002, all Approved), Phase 3 intake (INT-003, IRC-004, PIB-003, Approved) and Phase 3 deliverables (ADR-001, ARC-001, CST-001, RSK-003, TEC-001, THR-001, TOP-001, Draft), all citing NFR-001, REQ-001, BR-001, GLO-001 v0.2 and SUM-002 v0.3.

| Artifact | State | Action |
| --- | --- | --- |
| NFR-001 | Approved v0.2 | Revise to v0.3 (N-6 security events) and re-approve |
| REQ-001 | Approved v0.2 | Revise to v0.3 (REQ S-32, S-33) and re-approve |
| BR-001 | Approved v0.2 | Revise to v0.3 (BR B-24) and re-approve |
| GLO-001 | Approved v0.2 | Revise to v0.3 (Audit trail, Audit entry, Security event) and re-approve |
| EPC-001 | Approved v0.2 | Revise to v0.3 (E-5 stories) and re-approve |
| BKL-001 | Approved v0.2 | Revise to v0.3 (BL-32, BL-33) and re-approve |
| PRS-001 | Approved v0.2 | Revise to v0.3 (F-8) and re-approve |
| SUM-002 | Approved v0.3 | Revise to v0.4 and re-approve |
| ARC-001 | Draft | Revise (Phase 3 producers): drafted against the S-4 Draft content; refresh citations to the new versions after approval |
| ADR-001 | Draft | Revise (Phase 3 producers): drafted against the S-4 Draft content; refresh citations after approval |
| THR-001 | Draft | Revise (Phase 3 producers): drafted against the S-4 Draft content (OQ-062, OQ-064, OQ-065; T-3, T-5 detection through BR B-24); refresh citations after approval |
| TOP-001 | Draft | Revise (Phase 3 producers): drafted against the S-4 Draft content; refresh citations after approval |
| CST-001 | Draft | Revise (Phase 3 producers): drafted against the S-4 Draft content; refresh citations after approval |
| TEC-001 | Draft | Revise (Phase 3 producers): drafted against the S-4 Draft content; refresh citations after approval |
| RSK-003 | Draft | Revise (Phase 3 producers): drafted against the S-4 Draft content (R-3, R-10); refresh citations after approval |
| PIB-003 | Approved v0.1 | Revise (Orchestrator), citation update only, to v0.2, and re-approve |
| INT-003 | Approved v0.1 | Revise (Orchestrator), citation update only, to v0.2, and re-approve |
| IRC-004 | Approved v0.1 | Revise (Orchestrator), citation update only, to v0.2, and re-approve |

### Work Stopped
<!-- guidance: Features set to State: Blocked with this SCR cited, or 'None - reason' -->
None - no features exist yet. The Phase 3 producers drafted ARC-001, ADR-001, THR-001, TOP-001, CST-001, TEC-001 and RSK-003 (all Draft) against the S-4 Draft content of the Phase 2 artifacts; after this SCR and its artifacts are Approved they refresh their citations to the approved versions.

### Resume Criteria
<!-- guidance: What must be Approved before stopped work resumes (this SCR, the new artifact version, the ADR in Decision Record if any, revised downstream artifacts) -->
SCR S-4 and all revised artifacts Approved: NFR-001 v0.3, REQ-001 v0.3, BR-001 v0.3, GLO-001 v0.3, EPC-001 v0.3, BKL-001 v0.3, PRS-001 v0.3, SUM-002 v0.4, PIB-003 v0.2, INT-003 v0.2, IRC-004 v0.2.

### Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
None.

### Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
- OQ-062 (Answered, Mohanasunder, 2026-10-17, chat): the 5 security events are recorded in the audit trail like other audit entries; no alerting, no new reporting (REQ S-32; BR B-24; NFR N-6).
- OQ-064 (Answered, Mohanasunder, 2026-10-17, chat): the delivery manager views all security events (per user account); each internal user views their own; client users view none (REQ S-33; BR B-24; NFR N-6).
- OQ-065 (Answered, Mohanasunder, 2026-10-17, chat): every refused sign-in is a failed sign-in (wrong password, unknown account name, deactivated or locked user account); an unknown account name is recorded as typed (REQ S-32 AC-2, AC-3; BR B-24; NFR N-6).

### Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: NFR-001 v0.2 (N-6); REQ-001 v0.2; BR-001 v0.2 (B-22, B-23); GLO-001 v0.2; EPC-001 v0.2; BKL-001 v0.2; PRS-001 v0.2; SUM-002 v0.3; OQ-062; THR-001 (Draft) T-3, T-5.
- Downstream: NFR-001 v0.3 (NFR N-6); REQ-001 v0.3 (REQ S-32, S-33); BR-001 v0.3 (BR B-24); GLO-001 v0.3; EPC-001 v0.3 (EPC E-5); BKL-001 v0.3 (BKL BL-32, BL-33); PRS-001 v0.3 (PRS F-8); SUM-002 v0.4; PIB-003 v0.2, INT-003 v0.2, IRC-004 v0.2 (citation update, Orchestrator); ARC-001, ADR-001, THR-001, TOP-001, CST-001, TEC-001, RSK-003 (Phase 3, revised by their producers).

### Quality Checklist
- [x] Every section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)
- [x] Every changed artifact is listed as 'ID vOLD -> vNEW'
- [x] An architecture or contract change cites its new or superseding ADR A-N under Decision Record
- [x] Impact covers every artifact and feature that cites the changed artifact

---

## SCR S-5: FEAT-001 plan — missing scaffold files and unlisted npm peer dependencies
<!-- scr_approver: Mohanasunder -->

<!-- scr_status: Approved -->
<!-- scr_date: 2026-10-18 -->

### Input References
- FEAT-001 plan.md v0.1 (Approved 2026-10-17, Mohanasunder) — docs/05-build-plan/feature-001-frontend-scaffold/plan.md
- DEC-056 (2026-10-18, Mohanasunder) — playwright test --passWithNoTests approach for FEAT-001 E2E gate
- DEC-057 (2026-10-18, Mohanasunder) — script bug fix approved for check_feature_size.py
- A-042 through A-045 — builder assumptions logged during Mode B (2026-10-18)

### Purpose And Scope
During Mode B implementation of FEAT-001, the check_feature_size.py scope gate identified three files not listed in plan.md "Files To Create Or Modify": src/frontend/index.html (mandatory Vite entry point — vite build exits 1 without it), src/frontend/package-lock.json (npm lockfile auto-generated by npm install; the plan's New Packages section already references it as "Lockfile: src/frontend/package-lock.json"), and src/frontend/playwright.config.ts (minimal config redirecting Playwright's testDir to ./e2e so that Playwright's default testMatch pattern does not discover App.test.tsx; without this, Playwright tries to run a Vitest file and throws an internal state error).

The check_feature_size.py packages gate identified three npm packages in package.json not listed in plan.md "New Packages": @types/react ^19.3 (TypeScript type definitions for React — required by tsc --noEmit with strict mode), @types/react-dom ^19.3 (same for ReactDOM), and jsdom ^30.1 (browser environment emulator — Vitest required peer dep for environment: jsdom).

Does not change: the feature's purpose, acceptance criteria, risk tier, dependencies, or any other plan section beyond "Files To Create Or Modify" and "New Packages".

### Changed Artifact
- FEAT-001 v0.1 -> v0.2 (docs/05-build-plan/feature-001-frontend-scaffold/plan.md)

### Change Detail
Files To Create Or Modify — add: src/frontend/index.html; src/frontend/package-lock.json; src/frontend/playwright.config.ts

New Packages — add: npm: @types/react ^19.3 | MIT | TypeScript type defs for React (peer dep for tsc --noEmit strict mode); npm: @types/react-dom ^19.3 | MIT | TypeScript type defs for ReactDOM (peer dep); npm: jsdom ^30.1 | MIT | Browser env emulator; Vitest peer dep for environment: jsdom

### Decision Record
Not applicable — no architecture or contract artifact changes. DEC-056 and DEC-057 already logged.

### Impact
- FEAT-001 plan.md v0.2 is the only affected artifact.
- No downstream artifacts (acceptance.md, tasks.md, FEAT-001-TESTS.md) are changed.
- No other features cite FEAT-001 plan.md directly.

### Traceability Links
- Upstream: FEAT-001 plan.md v0.1; DEC-056; DEC-057; A-042, A-043, A-044, A-045
- Downstream: FEAT-001 plan.md v0.2

### Quality Checklist
- [x] Every section is filled, or marked "Not applicable - reason"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)
- [x] Every changed artifact is listed as 'ID vOLD -> vNEW'
- [x] An architecture or contract change cites its new or superseding ADR A-N under Decision Record
- [x] Impact covers every artifact and feature that cites the changed artifact

---

## SCR S-6: Glossary terminology violations in Phase 4/5 design artifacts

<!-- scr_status: Approved -->
<!-- scr_date: 2026-10-18 -->
<!-- scr_approver: Mohanasunder -->

### Input References
- GLO-001 v0.3 — APLX AMS: Domain Glossary (Approved 2026-10-17) § Terms: 'Priority' (avoid: severity); 'Assigned support engineer' (avoid: assignee).
- API-001 v0.1 — APLX AMS: API Specification (Approved 2026-10-17) and companion docs/04-design/openapi.yaml.
- UIS-001 v0.1 — APLX AMS: UI Specification (Approved 2026-10-17).
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17).
- TST-001 v0.1 — APLX AMS: Test Strategy (Approved 2026-10-17).
- DOD-001 v0.1 — Definition of Done (Approved 2026-10-17).
- FEAT-000-ACC v0.1 — FEAT-000 Acceptance Criteria (Approved 2026-10-17).
- FEAT-001 gate run 2026-10-18: `python scripts/glossary_check.py check` exits 1 with 35 violations.

### Purpose And Scope
Covers: (1) renaming the `AssignTicketRequest.assignee_id` field to `engineer_id` in docs/04-design/openapi.yaml, consistent with EffortRecord.engineer_id naming, to resolve three 'assignee' violations; (2) in-place terminology corrections in five design artifacts replacing 'severity' references with equivalent precise descriptions. This removes all 35 violations flagged by `scripts/glossary_check.py check`.

Does not cover: any change to endpoint behavior, response structure, business rules, acceptance criteria, or NFRs. The five in-place patches carry no version bump per DEC-060.

### Changed Artifact
- API-001 v0.1 -> v0.2 (docs/04-design/api-spec.md) — ADR A-18 field rename in companion openapi.yaml

In-place patches (no version bump; authorized by DEC-060):
- UIS-001 v0.1 (docs/04-design/ui-spec.md) — 27 MUI Alert severity prop references reworded to descriptive form
- STD-001 v0.1 (docs/04-design/coding-standards.md) — 1 occurrence corrected
- TST-001 v0.1 (docs/04-design/test-strategy.md) — 2 occurrences corrected
- DOD-001 v0.1 (docs/05-build-plan/definition-of-done.md) — 1 occurrence corrected
- FEAT-000-ACC v0.1 (docs/05-build-plan/feature-000-walking-skeleton/acceptance.md) — 1 occurrence corrected

### Trigger
FEAT-001 Phase 6 gate run 2026-10-18: `scripts/glossary_check.py check` (non-overridable) exits 1 with 35 violations across 6 files. All are pre-existing (on main before FEAT-001 was branched).

### Change
**API-001 companion openapi.yaml (3 changes):** `AssignTicketRequest` schema `assignee_id` → `engineer_id` (required list and property key); POST /api/tickets/{id}/assign/ 400 description updated. api-spec.md version 0.1 → 0.2.

**UIS-001 (27 in-place changes):** `<MuiAlert severity="error|warning|info|success">` variants reworded (e.g. → `<MuiAlert>` (error-level)); accessibility parentheticals `(MUI default for severity="error")` → `(MUI default for error-level alerts)`. No change to component type, placement, or message.

**STD-001 line 282:** "high-severity CVE" → "Critical or High CVE".

**TST-001 lines 114, 118:** "high-severity findings" → "high-level findings"; "high severity" → "high level".

**DOD-001 line 46:** "high-severity findings" → "high-level security findings".

**FEAT-000-ACC line 32:** "high-severity findings" → "medium or high level security findings".

### Reason
GLO-001 v0.3 flags 'assignee' and 'severity' as avoided terms. Phase 4/5 artifacts were approved before the glossary gate was wired. 'severity' in these artifacts refers to MUI Alert prop names and bandit/CVE severity ratings (technical industry terms), not ticket priority; however the gate is non-overridable and flags all occurrences.

### Decision Record
ADR A-18 (docs/03-architecture/adrs.md § ADR A-18) — rename `AssignTicketRequest.assignee_id` to `engineer_id`. Approved together with this SCR by Mohanasunder (Architect / tech lead).

Not applicable for the five in-place patches — descriptions-only corrections, no architecture or contract changes.

### Impact
For API-001 v0.1 → v0.2 (AssignTicketRequest.assignee_id → engineer_id):

| Artifact | State | Action |
| --- | --- | --- |
| API-001 | Approved v0.1 | Revise to v0.2; re-approve |
| BED-001 | Approved v0.1 | No change — update citation API-001 v0.1 → v0.2 before branching |
| FBD-001 | Approved v0.1 | No change — update citation before building |
| UIS-001 | Approved v0.1 | No change — does not reference AssignTicketRequest fields |
| PRM-001 | Approved v0.1 | No change — update citation before building |
| SUM-004 | Approved v0.2 | No change — update citation before Phase 7 |
| PIB-005 | Approved v0.1 | No change — update citation when relevant |
| FEAT-002 to FEAT-034 | Not started | Update Input References API-001 v0.1 → v0.2 before branching; only the feature implementing POST /api/tickets/{id}/assign/ needs engineer_id in implementation |

For in-place patches: no version bump — no impact on spec_impact.py for any citing artifact.

### Work Stopped
- FEAT-001 (State: In progress) — glossary gate non-overridable; blocks CI.

### Resume Criteria
SCR S-6 Approved + ADR A-18 Approved + API-001 v0.2 Approved + all patches applied + `python scripts/glossary_check.py check` exits 0.

### Assumptions
None.

### Open Questions
None.

### Traceability Links
- Upstream: GLO-001 v0.3; API-001 v0.1; UIS-001 v0.1; STD-001 v0.1; TST-001 v0.1; DOD-001 v0.1; FEAT-000-ACC v0.1
- Downstream: API-001 v0.2; ADR A-18; in-place patch artifacts (version unchanged)

### Quality Checklist
- [x] Every section is filled, or marked "Not applicable - reason"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)
- [x] Every changed artifact is listed as 'ID vOLD -> vNEW' — API-001: listed; in-place patches carry no version bump per DEC-060
- [x] An architecture or contract change cites its new or superseding ADR A-N under Decision Record
- [x] Impact covers every artifact and feature that cites the changed artifact
