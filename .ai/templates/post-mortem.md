---
id: PMT
id_prefix: PMT
title: <fill: "Project Name: Post-Mortems">
phase: 9
version: 0.1
template: post-mortem
template_version: 2.0
status: Draft
author_agent: <fill: agent name>
approver: Product owner / ops lead
default_approver: Product owner / ops lead
default_folder: docs/09-operate
date: <fill: YYYY-MM-DD>
validation: Pending
---

# <fill: title>

> **Collection file.** All post-mortems for this project live in this one file at `docs/09-operate/post-mortems.md`. The `incident-triage` agent appends one `## PMT PM-N: [title]` section per incident; never create a separate `PMT-NNN.md` file. A specific post-mortem is cited elsewhere as `PMT PM-N` (e.g. `PMT PM-2`). Sub-IDs start at PM-1, are consecutive, and are never reused.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this collection covers and what it does not -->
<fill: purpose and scope>

---

## PMT PM-1: <fill: post-mortem title>

### What Happened
<!-- guidance: Blameless narrative of the incident (INC I-N) this post-mortem covers -->
<fill: what happened>

### Root Cause
<!-- guidance: Contributing factors, not blame; cite evidence -->
<fill: root cause>

### What Went Well
<!-- guidance: Things to keep and reinforce -->
<fill: what went well>

### What Went Wrong
<!-- guidance: Things to fix or improve -->
<fill: what went wrong>

### Action Items
<!-- guidance: Each item has an owner and due date; each becomes an IMP IM-N improvement backlog item -->
<fill: action items>

### Traceability Links
<!-- guidance: The incident this post-mortem covers (INC I-N) and improvement items created (IMP IM-N) -->
<fill: traceability links>

---

<!-- Repeat the block above (from "## PMT PM-N:" to the closing ---) for each additional post-mortem.
     Increment the number: PM-2, PM-3, … Never reuse a number. -->

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
<fill: assumptions>

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
<fill: open questions>

## Quality Checklist
- [ ] Every template section is filled, or marked "Not applicable - <reason>"
- [ ] Inputs referenced are Approved artifacts at the stated versions
- [ ] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [ ] Assumptions and open questions are logged and linked
- [ ] PMT sub-IDs (PM-1, PM-2, …) are consecutive from 1 with no gaps; never renumbered after approval
- [ ] Every post-mortem is blameless: no personal accusations
- [ ] Every action item has an owner and due date, and links to an IMP IM-N item
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
