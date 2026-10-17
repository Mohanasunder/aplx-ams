---
id: NFR-001
title: APLX AMS: Non-Functional Requirements
phase: 2
version: 0.3
template: nfr
template_version: 2.0
status: Approved
author_agent: requirements-analyst
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# APLX AMS: Non-Functional Requirements

> **Collection file.** All non-functional requirements for this project live in this one file. Add one `## NFR N-N` section per NFR; never create a separate NFR-NNN file. Downstream artifacts reference a specific NFR as `NFR N-N` (e.g. `NFR N-3`).

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- PIB-002 v0.1 § Interview Answers (Q7, Q9, Q9a, Q10, Q10a, Q11), § Constraints, § Assumptions (A-008).
- INT-002 v0.1 § Questions And Answers (Q7, Q9, Q9a, Q10, Q10a, Q11).
- SUM-001 v0.3 § Constraints Set (desktop web browser only; existing on-prem servers; names and emails only).
- SCP-001 v0.2 § In Scope IS-5, § Out Of Scope OS-4.
- RSK-001 v0.2 § Risk R-6; DEC-022.
- SCR S-3 (`docs/logs/spec-changes.md`): N-5 lockout cleared by a new temporary password (OQ-054 answered, Mohanasunder, 2026-10-17, chat).
- SCR S-4 (`docs/logs/spec-changes.md`): N-6 security events in the audit trail (OQ-062 answered, Mohanasunder, 2026-10-17, chat).

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
Covers: measurable non-functional requirements for APLX AMS release 1: availability, performance, backup and recovery, data retention, sign-in and password policy, audit trail (ticket changes and security events, SCR S-4), client data separation, browser support, and personal data limited to names and emails (N-9). Release 1 scale: about 10 engineers, about 20 client users, up to about 10 SAP applications, one pilot client organization (SUM-001 v0.3 § Decisions).

Does not cover: technology, hosting design or monitoring tools (Phases 3 and 8). Q7 (no MFA) and Q10 (weekly backup, RPO 7 days) are human decisions recorded as stated; their risks are RSK-002 R-1 and R-2.

---

## NFR N-1: Availability within business hours

### Category
Availability

### Requirement
APLX AMS is available to signed-in users during business hours (09:00 to 18:00 IST, Monday to Friday, excluding the company holiday list; BR B-2). No availability target applies outside business hours.

### Measurable Target
At least 99% of business hours per calendar month (about 1.9 hours of unavailability allowed in a month of 21 business days x 9 hours = 189 hours).

### Verification Method
Automated availability check of the sign-in page once per minute during business hours from go-live; monthly availability = available minutes / business-hours minutes x 100; reviewed monthly in Phase 9. Source: INT-002 Q9.

---

## NFR N-2: Page response time under pilot load

### Category
Performance

### Requirement
Each page meets the response-time target below at the release 1 load. A "page" is one user action in the browser that loads a page or submits a form; its response time runs from the user's action until the page content is fully shown.

### Measurable Target
95th percentile (p95) page response time under 2 seconds for each page, with 30 concurrent users (10 engineer sessions and 20 client user sessions).

### Verification Method
Load test in Phase 7 with 30 concurrent simulated users (10 engineer, 20 client user) running the release 1 journeys (raise ticket, view tickets, acknowledge, change priority, assign, set Resolved, close, record effort, add comment, view live dashboard, view monthly client report) for at least 30 minutes; p95 computed per page from the test results. Source: INT-002 Q9, Q9a.

---

## NFR N-3: Backup and recovery

### Category
Reliability (backup and recovery)

### Requirement
All APLX AMS data (tickets, comments, effort entries, contracts, user accounts, audit entries, the company holiday list) is backed up weekly and can be restored after a loss.

### Measurable Target
Backup at least once every 7 days; RPO 7 days or less (at most 7 days of data lost); RTO 1 business day (9 business hours) or less from the decision to restore until users can sign in and work.

### Verification Method
Restore drill before go-live (Phase 7 or 8): restore the latest weekly backup to a separate environment, time the restore, and check that ticket, effort and audit data up to the backup time are present. Source: INT-002 Q10, Q10a (human compliance decision); risk RSK-002 R-2.

---

## NFR N-4: Data retention

### Category
Compliance (data retention)

### Requirement
APLX AMS keeps all tickets, comments, effort entries, contracts, monthly client reports, audit entries, company holiday list dates and user accounts (deactivated accounts included) with no end date.

### Measurable Target
Retention period: unlimited; 0 records deleted automatically by APLX AMS.

### Verification Method
Review in Phase 7 that no automatic deletion or purge job exists, and test that a ticket Closed 13 or more months earlier (seeded test data) is still retrievable. Source: INT-002 Q10.

---

## NFR N-5: Sign-in and password policy

### Category
Security

### Requirement
Every user (staff and client users) signs in with an APLX AMS user account and a password that meets the password policy. No multi-factor authentication (MFA) in release 1 (human security decision, INT-002 Q7). Policy values: OQ-044 answered (Mohanasunder, 2026-10-17, chat); they replace assumption A-012 (Rejected). The answer names no password expiry rule.

### Measurable Target
Password at least 8 characters, with at least 1 upper-case letter, 1 lower-case letter and 1 digit; a user account is locked for 30 minutes after 5 failed sign-ins, unless the delivery manager sets a new temporary password, which clears the lock at once (BR B-23, OQ-054); 0 second factors required; 100% of sign-ins use a user account.

### Verification Method
Phase 6 feature tests and Phase 7 security tests: a password of 7 characters is refused; 8-character passwords lacking an upper-case letter, a lower-case letter or a digit are each refused; "Abcdefg1" is accepted; the 6th sign-in within 30 minutes after 5 failures is refused even with the correct password, and the correct password is accepted after 30 minutes; a new temporary password set by the delivery manager on a locked user account is accepted at once (OQ-054); sign-in succeeds with no second factor. Risk RSK-002 R-1.

---

## NFR N-6: Audit trail completeness

### Category
Security (audit)

### Requirement
Every change to a ticket's status, priority, assignment or effort entries creates an audit entry (BR B-22), visible to internal users only. Every security event (successful sign-in, failed sign-in, user account lockout, temporary password set by the delivery manager, user changing their own password) also creates an audit entry, with no value entered in a password field in it (BR B-24; OQ-062 answered, SCR S-4). Every refused sign-in is a failed sign-in (wrong password, unknown account name recorded as typed, deactivated or locked user account; OQ-065). The delivery manager views all security events, each internal user their own, client users none (OQ-064).

### Measurable Target
100% of status, priority, assignment and effort changes have an audit entry with user, date and time to the second, old value and new value; 100% of security events of the 5 types have an audit entry with the event, the user who did it, the user account it concerns (or the account name as typed) and the date and time to the second; 100% of refused sign-ins of the 4 kinds (wrong password, unknown account name, deactivated, locked) have a failed sign-in entry; 0 security events visible to a client user, and 0 security events of another user account visible to an internal user who is not the delivery manager; 0 audit entries hold a value entered in a password field (a password entered at sign-in, a temporary password, a current or new password); a password typed into the account name field is recorded as typed (OQ-065) and is not covered by this target (risk RSK-003 R-10); 0 audit entries editable or deletable by any user.

### Verification Method
Phase 6 feature tests per change type and per security event type, and a Phase 7 system test that makes each of the 4 change types and each of the 5 security event types (failed sign-ins of all 4 kinds) and compares the actions made with the audit entries; the same test searches every audit entry for every value entered in a password field during the test (passwords entered at sign-in, temporary, current and new passwords) and expects 0 matches; it also views security events as the delivery manager, an L1 support engineer and a client user and compares what is shown with OQ-064. Source: INT-002 Q11; OQ-062, OQ-064, OQ-065 answered (Mohanasunder, 2026-10-17, chat).

---

## NFR N-7: Client data separation

### Category
Security (data separation)

### Requirement
A client user never sees or acts on another client organization's tickets, monthly client reports, SAP applications, names or emails (BR B-20). Tested with at least two client organizations' data although the pilot has one.

### Measurable Target
0 records of another client organization visible or changeable by a client user, across tests with at least 2 client organizations.

### Verification Method
Phase 6 feature tests and Phase 7 system tests with client organizations A and B: list, open by reference, report view and download, raise against the other organization's SAP application; re-run before the first external client organization goes live. Source: INT-001 Q14; DEC-022; RSK-001 R-6.

---

## NFR N-8: Supported browsers

### Category
Compatibility

### Requirement
APLX AMS works on desktop web browsers: the current and previous major versions of Google Chrome and Microsoft Edge (assumption A-008). No mobile access (SCP OS-4).

### Measurable Target
100% of release 1 acceptance tests pass on each of the 4 browser versions (Chrome current and previous major, Edge current and previous major) on desktop.

### Verification Method
Phase 7 runs the acceptance test suite on each of the 4 browser versions. Source: A-008 (producer default, PIB-002); SCP-001 OS-4.

---

## NFR N-9: Personal data limited to names and emails

### Category
Compliance (data minimisation)

### Requirement
The only personal data APLX AMS asks for and holds about a person in their user account is their name and email address. This carries the Phase 1 constraint "personal data limited to names and emails; no specific data-protection obligations known". Free text that users type into a ticket description or a comment is not covered by this target.

### Measurable Target
2 personal data fields per user account (name, email address); 0 other personal data fields in user accounts, client organizations, contracts or effort entries.

### Verification Method
Phase 4 design review of every data field held for user accounts, client organizations, contracts and effort entries against this list; Phase 7 review of the user account setup form fields. Source: SCP-001 v0.2 § Constraints (Data); INT-001 Q15; SUM-001 v0.3 § Constraints Set.

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-008 (Open): supported browsers are the current and previous major versions of Chrome and Edge on desktop (NFR N-8).
- A-012 (Rejected 2026-10-17): the producer's password policy default is replaced by the OQ-044 answer (NFR N-5).
- A-016 (Open): audit entries hold old and new value and cannot be edited or deleted (NFR N-6).

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
- OQ-044 (Answered, Mohanasunder, 2026-10-17): password policy values (NFR N-5).
- OQ-054 (Answered, Mohanasunder, 2026-10-17, chat; SCR S-3): a new temporary password set by the delivery manager clears the lock at once (NFR N-5).
- OQ-041 (Answered, Mohanasunder, 2026-10-17): the Applexus company holiday list, maintained by the delivery manager (NFR N-1 business hours).
- OQ-062 (Answered, Mohanasunder, 2026-10-17, chat; SCR S-4): the 5 security event types are recorded in the audit trail, with no password value (NFR N-6).
- OQ-064 (Answered, Mohanasunder, 2026-10-17, chat; SCR S-4): the delivery manager views all security events, each internal user their own, client users none (NFR N-6).
- OQ-065 (Answered, Mohanasunder, 2026-10-17, chat; SCR S-4): every refused sign-in is a failed sign-in; an unknown account name is recorded as typed (NFR N-6).

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason'.
     Cite individual NFRs downstream as NFR N-N (e.g. NFR N-2). -->
- Upstream: SCR S-3; SCR S-4; PIB-002 v0.1; INT-002 v0.1 (Q7, Q9, Q9a, Q10, Q10a, Q11); SUM-001 v0.3; SCP-001 v0.2 (IS-5, OS-4, § Constraints Data); INT-001 v0.1 Q15; RSK-001 v0.2 (R-6).
- Related Phase 2: REQ-001 (stories cite NFR N-N; N-6 by REQ S-23, S-32, S-33); BR-001 (B-2, B-20, B-22, B-24); RSK-002 (R-1, R-2).
- Downstream: Phase 3 architecture and threat model; Phase 7 NFR test report (not yet created).

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Every NFR has a unique N-N ID; IDs are consecutive and never reused
- [x] Every NFR has a measurable target with a number and unit
- [x] Every NFR has a verification method
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
| Version | 0.3 |
| Conditions | None |
| Comments | Security events in the audit trail per SCR S-4 (OQ-062, OQ-064, OQ-065); R-10 accepted. |
| Timestamp | 2026-10-17 10:59 UTC |
