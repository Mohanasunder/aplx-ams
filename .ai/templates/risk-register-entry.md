---
id: RSK
id_prefix: RSK
title: <fill: "Project Name: Phase N Risks">
phase: <fill: number of the phase that raised the risks>
version: 0.1
template: risk-register-entry
template_version: 2.0
status: Draft
author_agent: <fill: agent name>
approver: Phase approver (.ai/standards/review-and-approval.md)
default_approver: Phase approver (.ai/standards/review-and-approval.md)
default_folder: docs/01-discovery
date: <fill: YYYY-MM-DD>
validation: Pending
---

# <fill: title>

> **Collection file.** All risks raised in this phase live in this one file. Add one `## Risk R-N` section per risk; never create a separate RSK-NNN file for an additional risk in the same phase. The risk-register index (`docs/logs/risk-register.md`) references each risk as `RSK R-N` (e.g. `RSK R-2`). The live status of each risk lives there, not here.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What risks this artifact covers and what it does not. One collection per phase. -->
<fill: purpose and scope>

---

## Risk R-1: <fill: risk title>

### Risk Description
<!-- guidance: Cause, event, consequence -->
<fill: risk description>

### Likelihood And Impact
<!-- guidance: Low/Medium/High each, with reasoning -->
<fill: likelihood and impact>

### Mitigation
<!-- guidance: Actions and owner -->
<fill: mitigation>

### Owner
<!-- guidance: Named role -->
<fill: owner>

---

<!-- Repeat the block above (from "## Risk R-N:" to the closing ---) for each additional risk.
     Increment the number: R-2, R-3, … Never reuse a number.
     Add a row to docs/logs/risk-register.md for each new risk using ID format RSK R-N. -->

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
<fill: assumptions>

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
<fill: open questions>

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason'.
     Cite individual risks as RSK R-N (e.g. RSK R-2). -->
<fill: traceability links>

## Quality Checklist
- [ ] Every template section is filled, or marked "Not applicable - <reason>"
- [ ] Inputs referenced are Approved artifacts at the stated versions
- [ ] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [ ] Every risk has a unique R-N ID; IDs are consecutive and never reused
- [ ] Every risk has an owner (named role) and a mitigation
- [ ] Each risk is recorded in docs/logs/risk-register.md as RSK R-N
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
