---
id: RSK-003
title: APLX AMS: Phase 3 risks
phase: 3
version: 0.3
template: risk-register-entry
template_version: 2.0
status: Approved
author_agent: solution-architect
approver: Mohanasunder
date: 2026-10-17
validation: Pass with warnings
---
# APLX AMS: Phase 3 risks

> **Collection file.** All risks raised in this phase live in this one file. Add one `## Risk R-N` section per risk; never create a separate RSK-NNN file for an additional risk in the same phase. The risk-register index (`docs/logs/risk-register.md`) references each risk as `RSK R-N` (e.g. `RSK R-2`). The live status of each risk lives there, not here.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- PIB-003 v0.2 § Constraints (producer pointers: candidate risks (1) to (3)), § Interview Answers Q2, Q5, Q8, Q9, Q10, § Open Questions.
- INT-003 v0.2 Q2, Q5, Q8, Q9, Q10.
- NFR-001 v0.3 § NFR N-1, N-3, N-5, N-6; REQ-001 v0.3 § Story S-31, S-32, S-33; BR-001 v0.3 § Rule B-23, B-24; GLO-001 v0.3; SUM-002 v0.4 (SCR S-4 Approved).
- RSK-001 v0.2 (rating method); RSK-002 v0.1 § Risk R-1, R-2.
- Human answers, Mohanasunder, chat, 2026-10-17: OQ-052, OQ-055 to OQ-061, OQ-063, OQ-066; DEC-027 (public repository), DEC-028 (R-1 accepted for the pilot), DEC-029 (self-signed certificate), DEC-030 (session limits), DEC-031 (TLS certificate and key recovery copy on the test server), DEC-032 to DEC-036 (Phase 3 gate decisions).
- This phase (Draft): ADR-001 v0.3 (ADR A-5, A-7, A-11, A-13 to A-17), ARC-001 v0.3, THR-001 v0.2, TOP-001 v0.2, CST-001 v0.2.

## Purpose And Scope
<!-- guidance: What risks this artifact covers and what it does not. One collection per phase. -->
Covers: risks raised in Phase 3: R-1 single production server (`solution-architect`); R-2 manual deploy and personal github.com account (`solution-architect`); R-3 delivery manager knows temporary passwords and R-4 production data on the test server (`security-architect`, THR-001); R-5 self-signed certificate, R-6 public repository, R-10 passwords typed as account names (from THR-001 T-26, T-30 to T-34); R-7 test server disk, R-8 production memory headroom, R-9 Django LTS end of support (from TOP-001 and CST-001); R-11 single holder of the offline backup decryption key (`infra-cost-analyst`, from DEC-036 and DEC-020). Register rows use the ID form `RSK-003 R-N`. Rating method as in RSK-001 v0.2: High if either is High and the other at least Medium; Medium if both are Medium, or one is High and the other Low; otherwise Low.

Does not cover: risks already in the register (RSK R-1 to R-8, RSK-002 R-1, R-2), which are referenced, not repeated. The human decisions behind these risks are not changed.

---

## Risk R-1: Single production server against the 99% business-hours availability target

### Risk Description
- Cause: release 1 has exactly 2 servers, 1 production and 1 test (INT-003 Q2); production runs every container on one Ubuntu LTS VM (ADR A-5); the uptime checker runs on the test server (INT-003 Q10; ADR A-16).
- Event: the production VM, its disk or its host fails during business hours.
- Consequence: NFR N-1 allows about 1.9 hours of unavailability per month; recovery on the test server takes 3.75 business hours (including 0.25 hours to bring the offline decryption key, DEC-036) plus up to 2 hours for Applexus IT to move the host name, worst case 5.75 business hours, or 7.5 business hours if the sealed key copy must be fetched from Applexus IT (DEC-038) (TOP-001 RTO budget; OQ-059 answer), within the 9-business-hour RTO (NFR N-3) but breaching N-1 for that month; up to 7 days of data may be lost (RSK-002 R-2). While the test server is the stand-in, testing stops and Uptime Kuma checks a service on its own host.

### Likelihood And Impact
- Likelihood: Low. Existing on-prem VMs with no recorded failure history; container restarts cover application faults (ADR A-5).
- Impact: High. All 4 roles stop working; SLA timers keep counting business hours while users cannot act; NFR N-1 breached for the month.
- Overall rating: Medium (one High, the other Low).

### Mitigation
- Accepted for the pilot by the Architect / tech lead (DEC-028, Mohanasunder, 2026-10-17); residual: worst-case recovery 5.75 business hours, of which up to 2 hours is the Applexus IT host name move.
- Containers with restart policy and health checks (ADR A-5); deploys only outside business hours with the previous bundle kept for rollback (ADR A-13).
- Recovery runbook in Phase 8 per the TOP-001 RTO budget; the host name move is requested from Applexus IT at the first step; times measured in the restore drill (NFR N-3 verification).
- Uptime Kuma 60-second check with email alert to the Release manager / DevOps (ADR A-16).
- Revisit condition: VM-level snapshots or failover from Applexus IT (DEC-028 alternative).
- Owner of actions: Architect / tech lead (Mohanasunder).

### Owner
Architect / tech lead (Mohanasunder)

---

## Risk R-2: Manual deploy by one person, and company code on a personal github.com account

### Risk Description
- Cause: the human keeps the github.com repository and GitHub-hosted CI and deploys a built package manually (INT-003 Q5); the repository stays on the personal account `github.com/Mohanasunder/aplx-ams` for the pilot and is public (DEC-027; OQ-052 answer); Applexus has no written IT security policy (INT-003 Q9).
- Event: (a) the personal account is lost, taken over or leaves with its owner; (b) a manual deploy step is skipped or done wrong (wrong bundle, missed migration, no pre-deploy dump); (c) the one person who deploys is absent (DEC-020, no backup approver).
- Consequence: (a) loss of control of source code, CI and the bundle that is deployed (THR T-23); (b) a failed or partial deploy causing downtime (NFR N-1) or data problems; (c) fixes cannot be released. Public visibility itself is R-6.

### Likelihood And Impact
- Likelihood: Medium. Every release depends on one person's manual steps and one personal account.
- Impact: Medium. The repository holds no secrets or production data (ADR A-13, A-17); the previous bundle and pre-deploy dump allow rollback.
- Overall rating: Medium (both Medium).

### Mitigation
- Personal account kept for the pilot by human decision (DEC-027); revisit condition: move to an Applexus GitHub organization.
- Two-factor sign-in on the GitHub account; branch protection on `main` with required PR review and CI pass; bundle built only from protected `main` and checked by checksum before deploy (ADR A-13; THR T-23).
- Phase 8 deployment runbook with checksum verification, pre-deploy `pg_dump`, migration step and rollback to the kept previous bundle; deploy to the test server first.
- Owner of actions: Release manager / DevOps (Mohanasunder).

### Owner
Release manager / DevOps (Mohanasunder)

---

## Risk R-3: The delivery manager knows users' temporary passwords, with no forced change and no MFA

### Risk Description
- Cause: the delivery manager sets every temporary password, at user account creation and after a forgotten password reported outside APLX AMS; no user is asked or forced to change it (BR B-23; INT-003 Q8, human decision); no MFA (NFR N-5; RSK-002 R-1).
- Event: the delivery manager, or anyone who sees the hand-over or poses as the user when asking for a new temporary password, signs in as that user (THR T-3, T-4).
- Consequence: tickets, comments, status, priority, assignment and effort changes are made under another user's name and recorded so in the audit trail (NFR N-6); a client user's own client organization data is exposed to whoever holds the password.

### Likelihood And Impact
- Likelihood: Medium. Every user account starts with a password the delivery manager knows, and changing it is optional (REQ S-31).
- Impact: Medium. The delivery manager already sees every client organization's data as an internal user; the harm is wrong attribution and, once external client organizations join, access by a person posing as a client user.
- Overall rating: Medium (both Medium).

### Mitigation
- Users can change their own password at any time (REQ S-31); Phase 8 user documentation tells users so (information only, no prompt in APLX AMS, BR B-23).
- Temporary passwords are never shown again, logged or returned by the API; setting one ends the user's other sessions (ADR A-7, A-8; THR T-3).
- Security events (BR B-24; ADR A-11): every successful sign-in, temporary password set and own password change is recorded with user, user account and time; the delivery manager sees all security events and each internal user sees their own, so an internal user can spot a sign-in they did not make; client users cannot see their own security events (REQ S-33 AC-4), so misuse of a client user's account is visible only to the delivery manager.
- Phase 8 operational runbook: the delivery manager confirms a forgotten-password request through a channel already on record for that user before setting a temporary password (THR T-4).
- Accepted by the Architect / tech lead at the Phase 3 gate (DEC-033, Mohanasunder, 2026-10-17); revisit condition: forced password change at first sign-in (SCR), re-decided together with MFA (RSK-002 R-1) before the first external client organization's users sign in.
- Owner of actions: Architect / tech lead (Mohanasunder).

### Owner
Architect / tech lead (Mohanasunder)

---

## Risk R-4: The test server holds production data

### Risk Description
- Cause: the weekly `pg_dump` is copied to the test server, the only other server, which also runs the restore drill, test deployments and Uptime Kuma (INT-003 Q2, Q7, Q10; ADR A-15; A-031), and holds a root-only recovery copy of the production TLS certificate and key (DEC-031; ADR A-14, A-17); OS-level access (SSH, sudo, Docker) to both servers is held by Mohanasunder and Applexus IT administrators (OQ-063 answer).
- Event: a person with access to the test server, a test deployment pointed at production data, a restore drill database left running, or a compromise of the test server reads the dump (THR T-20, T-21), or reads the TLS key copy and impersonates APLX AMS on the network with a certificate every user's machine trusts, so no warning appears (THR T-36).
- Consequence: names and emails (NFR N-9), every client organization's tickets, reports and effort entries, audit entries (including any password typed as an account name, R-10) and Argon2id password hashes are exposed; the client data separation of NFR N-7 does not protect a dump file.

### Likelihood And Impact
- Likelihood: Medium. Test servers change more often than production, and access includes Applexus IT administrators beyond the APLX AMS team.
- Impact: High. All client organizations' data at once.
- Overall rating: High (one High, the other Medium).

### Mitigation
- Test server OS access matches production: Mohanasunder and Applexus IT administrators only, named accounts, no shared account (OQ-063 answer); dump directory root-only; dedicated backup account that can only write new files (ADR A-15; THR T-20, T-22).
- Test deployments use generated test data only and their own certificate; the restore drill database publishes no port and is dropped after the drill (ADR A-15; THR T-21).
- TLS key copy: root-owned, mode 0400, own directory apart from the dumps, never mounted into any container, checksum recorded; used only in a recovery or restore drill; certificate replaced and trust re-installed by Applexus IT on suspected exposure or when an administrator with access leaves (THR T-36).
- Weekly and pre-deploy dumps and the TLS certificate and key recovery copy encrypted at rest with age or GnuPG (free, open source); the private decryption key is held offline by the Release manager / DevOps (Mohanasunder), brought to the test server only for a restore or restore drill, and removed afterwards (DEC-036) (DEC-034, Mohanasunder, 2026-10-17; ADR A-15, A-17). Residual: a database restored for a drill or recovery, and the decrypted files during a restore, are readable by OS-level administrators while present (THR T-21, T-36).
- Owner of actions: Release manager / DevOps (Mohanasunder).

### Owner
Release manager / DevOps (Mohanasunder)

---

## Risk R-5: Self-signed certificate: warnings clicked through, or the certificate expires

### Risk Description
- Cause: the pilot uses a self-signed TLS certificate instead of an internal-CA certificate (DEC-029; ADR A-14).
- Event: (a) a user's machine lacks the installed trust, the user clicks through the browser warning, and a person on the Applexus network or VPN presents their own certificate (THR T-30); (b) the certificate expires or its key is lost, and no browser accepts the site until a new certificate is made and trusted again (THR T-26).
- Consequence: (a) passwords and session cookies captured or changed in transit; (b) no user can sign in (NFR N-1).

### Likelihood And Impact
- Likelihood: Low. Applexus IT installs the certificate as trusted on every user's machine before go-live, all pilot users being Applexus staff (OQ-066 answer); expiry is warned by Uptime Kuma.
- Impact: High. Credential capture, or a full outage until the certificate is replaced.
- Overall rating: Medium (one High, the other Low).

### Mitigation
- Applexus IT installs the certificate as trusted on every user's machine before go-live (OQ-066 answer); Phase 7 checks each of the 4 browser versions opens the sign-in page with no warning (NFR N-8); users told that any certificate warning means stop and report (ADR A-14).
- Validity period and renewal date recorded in the Phase 8 runbook with a renewal reminder; Uptime Kuma warns before expiry and emails the Release manager / DevOps (ADR A-16); renewal scheduled with Applexus IT so the new certificate is installed before the old one expires.
- Key kept on the production server plus the recovery copy named in the Phase 8 runbook (ADR A-17).
- Revisit condition: internal-CA certificate (DEC-029 alternative), and before external client users join.
- Owner of actions: Release manager / DevOps (Mohanasunder).

### Owner
Release manager / DevOps (Mohanasunder)

---

## Risk R-6: Public repository: secret leak and workflow abuse

### Risk Description
- Cause: the repository is public on the personal github.com account for the pilot (DEC-027); anyone can read every commit, CI log and artifact, fork it and open pull requests (THR T-31 to T-33).
- Event: (a) a secret, server address, host name or production data is committed or printed in a CI log; (b) a workflow runs pull request code from a fork with write permissions, takes user-controlled text into a script, or uses an altered third-party action.
- Consequence: (a) the value is harvested at once and stays exposed even if history is rewritten; (b) the repository, caches or the bundle a human deploys are altered (THR T-23).

### Likelihood And Impact
- Likelihood: Medium. Automated scanners watch public repositories; 3 builder agents commit to it.
- Impact: High. A leaked server secret or an altered bundle reaches production.
- Overall rating: High (one High, the other Medium).

### Mitigation
- Exposure of the design accepted by DEC-027; no secret is ever needed in GitHub: secrets are root-only files on the servers (ADR A-17).
- GitHub secret scanning with push protection; full-history secret scan before the repository is made public and in CI on every push; any committed secret is rotated (ADR A-13; THR T-32).
- Workflow rules: no `pull_request_target` or `workflow_run` job running pull request code; read-only default `GITHUB_TOKEN`; approval before workflows run for outside contributors; user-controlled values only through environment variables; actions pinned by commit SHA; bundle built only from protected `main`; workflow changes reviewed by the Architect / tech lead (ADR A-13; THR T-33).
- No server address, host name or server user name in the repository; review before each release (THR T-31).
- Owner of actions: Architect / tech lead (Mohanasunder).

### Owner
Architect / tech lead (Mohanasunder)

---

## Risk R-7: Test server disk fills up and weekly backup copies fail

### Risk Description
- Cause: at the 5-year ceiling the test server disk is about 77% used (30.9 of 40 GB: 8 weekly dumps 16 GB, restore drill database 6 GB, test stack, Uptime Kuma, images) (TOP-001; A-033).
- Event: dumps grow beyond 2 GB, more dumps are kept, a daily dump is chosen later (CST-001: up to about 96 GB more), or drill databases are left behind.
- Consequence: the weekly copy fails, so the RPO of 7 days is no longer met (NFR N-3), and the restore drill or a recovery stand-in cannot run.

### Likelihood And Impact
- Likelihood: Low. Year-1 use is far lower (database under 1 GB, TOP-001).
- Impact: Medium. One or more weekly restore points lost until disk is freed.
- Overall rating: Low.

### Mitigation
- A failed dump or copy sends an email alert (ADR A-15, A-16); disk use of both servers checked in the monthly Phase 9 review.
- Drill database dropped after each drill (ADR A-15); keep fewer dumps or ask Applexus IT for more disk on the existing platform if use passes 85%.
- Owner of actions: Release manager / DevOps (Mohanasunder).

### Owner
Release manager / DevOps (Mohanasunder)

---

## Risk R-8: Production server memory headroom on the minimum server size

### Risk Description
- Cause: the production server has 4 GB RAM (OQ-055 answer); the estimated use at the 5-year ceiling is about 3.0 GB (75%) with 5 Gunicorn workers, PostgreSQL `shared_buffers` 1 GB and PDF generation peaks (TOP-001; A-034); the figures are producer estimates, not measurements.
- Event: real memory use per worker, PDF rendering (WeasyPrint, ADR A-12) or Argon2id hashing at sign-in peaks (ADR A-8) is higher than estimated.
- Consequence: swapping or a container killed for lack of memory; p95 above 2 s (NFR N-2) or short outages (NFR N-1).

### Likelihood And Impact
- Likelihood: Low. Peak load is at most 15 API requests per second (A-034), about 38% of CPU.
- Impact: Medium. Slower pages or restarts during business hours.
- Overall rating: Low.

### Mitigation
- Phase 7 load test on the test server (same size as production) includes sign-in and PDF download; measured values replace the estimates.
- Scaling path in TOP-001: tune workers and PostgreSQL memory, then ask Applexus IT for more RAM on the existing VM.
- Owner of actions: Architect / tech lead (Mohanasunder).

### Owner
Architect / tech lead (Mohanasunder)

---

## Risk R-9: Django 5.2 LTS security support ends April 2028

### Risk Description
- Cause: the backend uses Django 5.2 LTS, with security fixes until April 2028 (ADR A-2; TEC-001 T-1).
- Event: the upgrade to the next LTS (6.2, due April 2027) is not planned and done before April 2028.
- Consequence: framework vulnerabilities stay unpatched in a tool that holds every client organization's data; upgrade effort hours are not in CST-001.

### Likelihood And Impact
- Likelihood: Medium. 1 reviewer and no planned maintenance capacity after go-live.
- Impact: Medium. Unpatched framework on an internal network.
- Overall rating: Medium (both Medium).

### Mitigation
- Plan the LTS upgrade as a Phase 9 backlog item after Django 6.2 is released, well before April 2028; CI dependency scan flags unsupported versions (THR T-24).
- Owner of actions: Architect / tech lead (Mohanasunder).

### Owner
Architect / tech lead (Mohanasunder)

---

## Risk R-10: Passwords typed as account names are kept in the audit trail and dumps

### Risk Description
- Cause: a refused sign-in with an account name that matches no user account is recorded with the account name as typed (BR B-24; OQ-065, human decision); audit entries are never deleted (NFR N-4).
- Event: a user types their password into the account-name field (THR T-34).
- Consequence: that password is stored in the audit trail, visible to the delivery manager with the time of the attempt, and copied into every dump, including those on the test server (R-4); such a password is not covered by the NFR N-6 target "0 audit entries hold a value entered in a password field" (NFR-001 v0.3 N-6).

### Likelihood And Impact
- Likelihood: Medium. A common typing slip.
- Impact: Medium. Exposure of one user's password to the delivery manager and server administrators.
- Overall rating: Medium (both Medium).

### Mitigation
- Within the human decision: entries for unknown account names visible only to the delivery manager (ADR A-11; REQ S-33); the account-name field is not echoed on screen after a refused sign-in; Phase 8 user documentation asks users who typed a password into the account-name field to change it (REQ S-31) (THR T-34).
- Accepted by the Architect / tech lead at the Phase 3 gate (DEC-032, Mohanasunder, 2026-10-17); revisit condition: change BR B-24 through an SCR (for example, do not record unknown account names as typed).
- Owner of actions: Architect / tech lead (Mohanasunder).

### Owner
Architect / tech lead (Mohanasunder)

---

## Risk R-11: Single holder of the offline backup decryption key

### Risk Description
- Cause: the weekly and pre-deploy dumps and the TLS certificate and key recovery copy are encrypted at rest, and the private decryption key is held offline by the Release manager / DevOps (Mohanasunder) only (DEC-036); there is no backup approver or second key holder (DEC-020). Raised by the `infra-cost-analyst` (TOP-001).
- Event: the key is lost or damaged, or its holder is unavailable when a restore or restore drill is needed.
- Consequence: no dump and no TLS key copy can be decrypted, so no restore or drill is possible; after a production server loss the 9-business-hour RTO of NFR N-3 is broken (TOP-001 RTO step 4 needs the key), and if the key is lost every backup is unusable.

### Likelihood And Impact
- Likelihood: Low. One holder; key loss and absence at the moment of a needed restore are both uncommon.
- Impact: High. Recovery impossible or delayed beyond the RTO; with a lost key, all backups lost.
- Overall rating: Medium (one High, the other Low).

### Mitigation
- Decided by the Architect / tech lead (DEC-037, Mohanasunder, 2026-10-17): a sealed second copy of the private key in a tamper-evident envelope is held by Applexus IT in a locked safe, used only if the Release manager / DevOps is unavailable; the restore drill checks the sealed copy once a year (and the primary key at every drill).
- Hand-over time (DEC-038, Mohanasunder, 2026-10-17): Applexus IT hands over the sealed copy within 2 business hours, so the worst-case RTO is 7.5 business hours when the key holder is unavailable (5.75 business hours when present), both within the 9-business-hour RTO of NFR N-3 (TOP-001).
- Residual rating (RSK-001 v0.2 method): Low. Likelihood Low (both copies would have to be lost or unreachable); Impact Medium (up to 2 business hours of delay while Applexus IT hands over the sealed copy, still within the RTO, not a lost backup set).
- Owner of actions: Release manager / DevOps (Mohanasunder).

### Owner
Release manager / DevOps (Mohanasunder)

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
- A-030 (Confirmed by the OQ-055 answer): server size and SSH from production to test (R-1, R-7, R-8).
- A-031 (Open): the weekly dump is copied to the test server (R-1, R-4).
- A-033, A-034 (Open, infra-cost-analyst): dump count and size; peak load (R-7, R-8).
- A-037 (Rejected by the OQ-063 answer): OS-level access is held by Mohanasunder and Applexus IT administrators, not one person (R-4).
- A-038 (Open, security-architect): no secret manager; secrets as root-only files (R-6).

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
- Answered by Mohanasunder, 2026-10-17, chat: OQ-052 (R-2, R-6), OQ-055 (R-1, R-8), OQ-056 (R-1, R-5), OQ-057 (R-5), OQ-059 (R-1), OQ-063 (R-4), OQ-066 (R-5); OQ-062, OQ-064, OQ-065 through SCR S-4 (R-3, R-10).
- No open question remains for these risks.

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason'.
     Cite individual risks as RSK R-N (e.g. RSK R-2). -->
- Upstream: PIB-003; INT-003; NFR-001 (N-1, N-2, N-3, N-5, N-6, N-8); REQ-001 (S-31, S-32, S-33); BR-001 (B-23, B-24); RSK-001 (rating method); RSK-002 (R-1, R-2).
- Same phase: ADR-001 (ADR A-2, A-5, A-7, A-11 to A-17); ARC-001; THR-001 (THR T-3, T-4, T-20 to T-23, T-26, T-30 to T-34, T-36); TOP-001; CST-001.
- Downstream: `docs/logs/risk-register.md` rows RSK-003 R-1 to R-11; Phase 7 load test and restore drill; Phase 8 deployment runbook, rollback plan, operational runbook, user documentation; Phase 9 reviews.

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions (exception: same-phase Drafts ADR-001, ARC-001, THR-001, TOP-001, CST-001 are cited as context, not as approved input)
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
| Role | Architect / tech lead |
| Version | 0.3 |
| Conditions | None |
| Comments | Reviewed after validation run 6; gate decisions DEC-027 to DEC-038 applied; THR-001 envelope-opening log proposal adopted as DEC-039. |
| Timestamp | 2026-10-17 11:25 UTC |
