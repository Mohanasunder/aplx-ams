---
id: OPR
id_prefix: OPR
title: <fill: title>
phase: 8
version: 0.1
template: operational-runbook
template_version: 1.0
status: Draft
author_agent: <fill: agent name>
approver: Release manager / DevOps
default_approver: Release manager / DevOps
default_folder: docs/08-deployment
date: <fill: YYYY-MM-DD>
validation: Pending
---

# <fill: title>

> **Single file.** There is exactly one operational runbook per project. Always use `--id OPR --out docs/08-deployment/operational-runbook.md` when calling `new_artifact.py`; never auto-name as `OPR-NNN.md`. Created in Phase 8 and kept current in Phase 9; a revision to an Approved version follows the living spec rule (SCR S-N). Cited as `OPR`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved): monitoring spec, architecture, deployment topology, deployment runbook, rollback plan, threat model -->
<fill: input references>

## Purpose And Scope
<!-- guidance: How the running system is operated and supported in production. Written before go-live (Phase 8) and kept current in Phase 9; changes after approval follow the living spec rule -->
<fill: purpose and scope>

## Service Overview
<!-- guidance: Components, internal and third-party dependencies (with their status pages), environments, and the owning team role -->
<fill: service overview>

## Monitoring
<!-- guidance: The monitoring spec (MON vX.Y) this runbook relies on: dashboards, SLOs, where logs and traces are -->
<fill: monitoring>

## Alert Responses
<!-- guidance: Table, one row per alert in the monitoring spec: alert, SLO, severity, first checks, actions (steps or a Common Operations entry), escalate to (role). Every alert has a row -->
<fill: alert responses>

## Support Procedures
<!-- guidance: Support tiers and hours, how users report problems, triage into an incident report (incident-triage) or a defect report (defect rule in .ai/standards/phase-loop.md), and user communication during an incident -->
<fill: support procedures>

## Escalation And On-Call
<!-- guidance: Roles in escalation order with response targets. Roles only: real names and contact details live in the on-call tool, referenced here -->
<fill: escalation and on-call>

## Common Operations
<!-- guidance: Numbered procedures: restart, scale, failover, backup and restore (with the last restore test date), secret rotation (secret manager references only). Data fixes only through an approved change -->
<fill: common operations>

## Known Issues And Workarounds
<!-- guidance: Defects released as Won't fix (DEF D-N, DEC-NNN), known limits, and their workarounds, or 'None' -->
<fill: known issues and workarounds>

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
