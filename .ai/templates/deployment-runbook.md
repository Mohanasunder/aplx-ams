---
id: RUN
id_prefix: RUN
title: <fill: title>
phase: 8
version: 0.1
template: deployment-runbook
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

> **Single file.** There is exactly one deployment runbook per project. Always use `--id RUN --out docs/08-deployment/deployment-runbook.md` when calling `new_artifact.py`; never auto-name as `RUN-NNN.md`. Cited as `RUN`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
<fill: purpose and scope>

## Pre-Deployment Checks
<!-- guidance: Checklist. The first item is always: 'python3 scripts/go_live.py check GLC prints GO for release vX.Y.Z; on NO-GO, stop'. Run by the release manager, who performs the deployment; agents never deploy -->
<fill: pre-deployment checks>

## Steps
<!-- guidance: Numbered commands and who runs them -->
<fill: steps>

## Verification
<!-- guidance: Smoke tests and metrics to watch -->
<fill: verification>

## Rollback
<!-- guidance: Link to the rollback plan -->
<fill: rollback>

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
