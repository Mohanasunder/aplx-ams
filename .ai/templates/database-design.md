---
id: DBD
id_prefix: DBD
title: <fill: title>
phase: 4
version: 0.1
template: database-design
template_version: 2.0
status: Draft
author_agent: <fill: agent name>
approver: Tech lead + UX
default_approver: Tech lead + UX
default_folder: docs/04-design
date: <fill: YYYY-MM-DD>
validation: Pending
---

# <fill: title>

> **Single file.** There is exactly one database design per project. Always use `--id DBD --out docs/04-design/database-design.md` when calling `new_artifact.py`; never auto-name as `DBD-NNN.md`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
<fill: purpose and scope>

## Entity Model
<!-- guidance: Mermaid erDiagram -->
<fill: entity model>

## Schema DDL
<!-- guidance: SQL for tables, keys, constraints -->
<fill: schema ddl>

## Indexing Strategy
<!-- guidance: Index per query pattern -->
<fill: indexing strategy>

## Migration Approach
<!-- guidance: Order, reversibility, data backfill -->
<fill: migration approach>

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
