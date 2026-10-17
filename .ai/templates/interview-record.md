---
id: INT
id_prefix: INT
title: <fill: title>
phase: 0
version: 0.1
template: interview-record
template_version: 2.0
status: Draft
author_agent: <fill: agent name>
approver: Tech lead
default_approver: Tech lead
default_folder: docs/00-setup
date: <fill: YYYY-MM-DD>
validation: Pending
---

# <fill: title>

> **One file per phase.** Each phase produces exactly one `interview-record.md` in its own folder. Use `--out docs/0N-<phase-slug>/interview-record.md` when calling `new_artifact.py`; never let it auto-name as `INT-NNN.md`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
<fill: purpose and scope>

## Questions And Answers
<!-- guidance: Table: ID, question, why it matters (template section affected), answer, answered by, date -->
<fill: questions and answers>

## Deferred Items
<!-- guidance: Questions answered with 'defer' or 'don't know yet'; each links to an assumption (A-xxx) or open question (OQ-xxx) -->
<fill: deferred items>

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
