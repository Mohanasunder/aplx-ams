---
id: INC
id_prefix: INC
title: <fill: "Project Name: Incident Reports">
phase: 9
version: 0.1
template: incident-report
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

> **Collection file.** All incident reports for this project live in this one file at `docs/09-operate/incidents.md`. The `incident-triage` agent appends one `## INC I-N: [title]` section per incident; never create a separate `INC-NNN.md` file. A specific incident is cited elsewhere as `INC I-N` (e.g. `INC I-2`). Sub-IDs start at I-1, are consecutive, and are never reused.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this collection covers and what it does not -->
<fill: purpose and scope>

---

## INC I-1: <fill: incident title>

### Summary
<!-- guidance: What happened in 3 sentences -->
<fill: summary>

### Timeline
<!-- guidance: Timestamped events from evidence -->
<fill: timeline>

### Impact
<!-- guidance: Users affected, data affected, duration -->
<fill: impact>

### Cause
<!-- guidance: Known or suspected root cause -->
<fill: cause>

### Actions
<!-- guidance: Immediate actions taken and follow-up items; each follow-up becomes an IMP IM-N improvement backlog item -->
<fill: actions>

### Traceability Links
<!-- guidance: Triggering alert, post-mortem (PMT PM-N), and improvement items (IMP IM-N) that arose from this incident -->
<fill: traceability links>

---

<!-- Repeat the block above (from "## INC I-N:" to the closing ---) for each additional incident.
     Increment the number: I-2, I-3, … Never reuse a number. -->

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
- [ ] INC sub-IDs (I-1, I-2, …) are consecutive from 1 with no gaps; never renumbered after approval
- [ ] Every incident section has a summary, timeline, impact, and cause
- [ ] Follow-up actions that produce improvement items cite the resulting IMP IM-N
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
