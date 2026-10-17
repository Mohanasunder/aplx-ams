---
id: FEAT-033-ACC
id_prefix: FEAT
title: "FEAT-033: S-32: Security Events Are Recorded in the Audit Trail â€” Acceptance Criteria"
phase: 5
version: 0.1
template: feature-acceptance
template_version: 1.1
status: Approved
author_agent: build-planner
approver: Mohanasunder
default_approver: Tech lead
default_folder: docs/05-build-plan
date: 2026-10-17
validation: Pass
---
# FEAT-033: S-32: Security Events Are Recorded in the Audit Trail â€” Acceptance Criteria

## Input References
- REQ-001 v0.3 â€” APLX AMS: User Stories (Approved 2026-10-17) Â§ S-32
- PIB-005 v0.1 â€” Phase 5 Build Planning Input Brief (Approved 2026-10-17)

## Purpose And Scope
Covers the 4 acceptance criteria for FEAT-033 (REQ S-32). Criteria are copied verbatim from REQ-001 v0.3 Â§ S-32.

## Acceptance Criteria
REQ-032 AC-1 REQ S-32 AC-1: Given active, unlocked user account X, when X signs in with the correct password at 10:00:05 IST and a sign-in on X with a wrong password is refused at 10:01:10 IST, then the audit trail holds a successful sign-in entry and a failed sign-in entry, each with user account X and its date and time to the second (BR B-24).
REQ-032 AC-2 REQ S-32 AC-2: Given user account X with 4 failed sign-ins, when a fifth sign-in with a wrong password is refused and X is locked (NFR N-5), and then a sign-in on X with the correct password is refused while X is locked, then the audit trail holds a failed sign-in entry, a user account lockout entry and a second failed sign-in entry for X, each with its date and time (BR B-24, OQ-065).
REQ-032 AC-3 REQ S-32 AC-3: Given deactivated user account Y and the account name "user.unknown", which matches no user account, when a sign-in on Y and a sign-in with "user.unknown" are each refused, then the audit trail holds a failed sign-in entry for user account Y and a failed sign-in entry holding the account name "user.unknown" as typed, each with its date and time (BR B-24, OQ-065).
REQ-032 AC-4 REQ S-32 AC-4: Given delivery manager D sets temporary password "Bcdefgh2" on user account X, and signed-in user Z changes their own password to "Cdefghi3", when each change is saved, then the audit trail holds a temporary password set entry with user D, user account X and the time, and an own password change entry with user Z, user account Z and the time; and a search of every audit entry for every password value entered during the test of AC-1 to AC-4 (the correct and wrong passwords entered at sign-in, "Bcdefgh2", "Cdefghi3" and the current password entered by Z) finds 0 matches (BR B-23, BR B-24).

## Test Scenarios
REQ-032 AC-1 REQ S-32 AC-1: Given active, unlocked user account X, when X signs in with the correct password... â€” verify Given/When/Then conditions as stated above.
REQ-032 AC-2 REQ S-32 AC-2: Given user account X with 4 failed sign-ins, when a fifth sign-in with a wrong p... â€” verify Given/When/Then conditions as stated above.
REQ-032 AC-3 REQ S-32 AC-3: Given deactivated user account Y and the account name "user.unknown", which matc... â€” verify Given/When/Then conditions as stated above.
REQ-032 AC-4 REQ S-32 AC-4: Given delivery manager D sets temporary password "Bcdefgh2" on user account X, a... â€” verify Given/When/Then conditions as stated above.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: REQ-001 v0.3 Â§ S-32; PIB-005 v0.1
- Downstream: FEAT-033-TASKS (builder task list); Phase 6 test set (created in Phase 6)

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
| Role | Architect / tech lead |
| Version | 0.1 |
| Conditions | None |
| Comments | None |
| Timestamp | 2026-10-17 18:47 UTC |
