---
id: PRS
id_prefix: PRS
title: <fill: "Project Name: Product Requirement Specification">
phase: 2
version: 0.1
template: product-requirement-specification
template_version: 1.0
status: Draft
author_agent: <fill: agent name>
approver: Product owner / BA
default_approver: Product owner / BA
default_folder: docs/02-requirements
date: <fill: YYYY-MM-DD>
validation: Pending
---

# <fill: title>

> **Single file.** One Product Requirement Specification per project. Create with:
> `python3 scripts/new_artifact.py --template product-requirement-specification --id PRS --title "<title>" --author <agent> --out docs/02-requirements/product-requirement-specification.md`
> Never create a separate `PRS-NNN.md` file. Downstream artifacts cite product goals as `PRS G-N`, non-goals as `PRS NG-N`, and features as `PRS F-N`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
<fill: purpose and scope>

---

## Product Goals

<!-- guidance: Table of product-level goals. ID is PRS G-N (G-1, G-2, …), never reused. Each goal must have a measurable success metric. Cite the upstream brief goal that this serves as BRF G-N; a PRS goal may serve more than one brief goal. A goal dropped in a later version keeps its row with 'Removed - SCR S-N' in the Goal column. -->

| ID | Goal | Success Metric | Brief Goal |
| --- | --- | --- | --- |
| PRS G-1 | <fill: goal statement> | <fill: number and unit> | BRF G-<fill> |

---

## Non-Goals

<!-- guidance: Table of explicit non-goals — capabilities the product intentionally will not address in this release. ID is PRS NG-N (NG-1, NG-2, …), never reused. Reason must name the decision or constraint that makes it a non-goal (a business constraint, out-of-scope decision, or named human decision DEC-NNN). -->

| ID | Non-Goal | Reason |
| --- | --- | --- |
| PRS NG-1 | <fill: what is not being built> | <fill: reason or DEC-NNN> |

---

## Product Scope

### In Scope
<!-- guidance: Bulleted capabilities included in this product release -->
<fill: in scope>

### Out Of Scope
<!-- guidance: Bulleted exclusions for this product release -->
<fill: out of scope>

---

## Feature F-1: <fill: feature title>

### Description
<!-- guidance: One to three sentences on what this feature delivers to the user -->
<fill: description>

### Priority
<!-- guidance: MoSCoW (Must / Should / Could / Won't) with a one-line reason -->
<fill: priority>

### Goals Served
<!-- guidance: PRS G-N references (at least one); the feature must move at least one product goal -->
<fill: goals served>

### Linked Stories
<!-- guidance: REQ S-N references; Won't priority features may list 'None - Won't priority' -->
<fill: linked stories>

---

<!-- Repeat the block above (from "## Feature F-N:" to the closing ---) for each additional feature.
     Increment the number: F-2, F-3, … Never reuse a number. -->

---

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
<fill: assumptions>

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
<fill: open questions>

## Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason'.
     Cite product goals as PRS G-N, non-goals as PRS NG-N, features as PRS F-N. -->
<fill: traceability links>

## Quality Checklist
- [ ] Every template section is filled, or marked "Not applicable - <reason>"
- [ ] Inputs referenced are Approved artifacts at the stated versions
- [ ] Nothing invented: no goals, features, or constraints without a source
- [ ] Every product goal has a unique G-N ID; IDs are consecutive and never reused
- [ ] Every product goal has a measurable success metric with a number and unit
- [ ] Every product goal cites at least one upstream brief goal as BRF G-N
- [ ] Every non-goal has a unique NG-N ID; IDs are consecutive and never reused
- [ ] Every non-goal has a named reason or references DEC-NNN
- [ ] In Scope and Out of Scope are both filled; no capability is ambiguously placed
- [ ] Every feature has a unique F-N ID; IDs are consecutive and never reused
- [ ] Every feature has a MoSCoW priority with a reason
- [ ] Every feature cites at least one product goal (PRS G-N) it serves
- [ ] Every Must or Should feature cites at least one linked story (REQ S-N)
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
