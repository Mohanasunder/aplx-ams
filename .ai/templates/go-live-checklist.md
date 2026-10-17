---
id: GLC
id_prefix: GLC
title: <fill: title>
phase: 8
version: 0.1
template: go-live-checklist
template_version: 1.1
status: Draft
author_agent: <fill: agent name>
approver: Release manager / DevOps
default_approver: Release manager / DevOps
default_folder: docs/08-deployment
date: <fill: YYYY-MM-DD>
validation: Pending
---

# <fill: title>

> **Single file.** There is exactly one go-live checklist per project. Always use `--id GLC --out docs/08-deployment/go-live-checklist.md` when calling `new_artifact.py`; never auto-name as `GLC-NNN.md`. `/approve` on this file records the Go / No-go decision; a different release tag requires a new version and a new Go. Cited as `GLC`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
<fill: purpose and scope>

## Release
<!-- guidance: The release this decision is for: tag (vX.Y.Z, on main), commit, target environment, change window (date, time, time zone), release notes REL vX.Y. A different tag needs a new version of this checklist and a new Go -->
<fill: release>

## Checklist
<!-- guidance: Technical, operational, and communication items -->
<fill: checklist>

## Go / No-Go Criteria
<!-- guidance: Table: criterion, evidence (ID vX.Y), met (Yes or No). At least: release readiness report Approved; UAT signed off; no open Blocker defects and traceability.py check --phase 7 passes; deployment runbook and rollback plan Approved, rollback rehearsed; operational runbook and monitoring spec Approved, dashboards and alerts live in the target environment; config validation passes for the target environment; support and on-call staffed for the change window; stakeholders informed. scripts/go_live.py criteria checks the Approved evidence -->
<fill: go / no-go criteria>

## Go / No-Go Decision
<!-- guidance: How the decision is recorded: /approve on this checklist is the decision (Approve = Go; Approve with conditions = Go with the conditions stated; Reject = No-go, with the reason in its comments). Production deploys are Critical, so the release manager and the tech lead both record a Go. An edit after approval returns the checklist to Draft and needs a new Go. Before deploying, the release manager runs python3 scripts/go_live.py check; it must print GO. Agents never deploy -->
<fill: go / no-go decision>

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
<fill: assumptions>

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
<fill: open questions>

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
<fill: traceability links>

## Quality Checklist
- [ ] Every template section is filled, or marked "Not applicable - <reason>"
- [ ] Inputs referenced are Approved artifacts at the stated versions
- [ ] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [ ] Assumptions and open questions are logged and linked
- [ ] Traceability links are present upstream and downstream
- [ ] Terminology follows .ai/standards/glossary.md
- [ ] Vague words removed (etc., as needed, appropriate)

## Approval Record
| Field | Value |
| --- | --- |
| Decision | Pending |
| Approver | Pending |
| Role | Pending |
| Conditions | None |
| Comments | None |
| Timestamp | Pending |
