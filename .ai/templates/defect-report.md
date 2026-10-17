---
id: DEF
id_prefix: DEF
title: Defect Register
phase: 7
version: 0.1
template: defect-report
template_version: 2.0
status: Draft
author_agent: defect-triage
approver: QA lead
default_approver: QA lead
default_folder: docs/07-testing
date: <fill: YYYY-MM-DD>
validation: Pending
---

# Defect Register

<!-- Collection file. All defects are appended as `## Defect D-N: [title]` sections (D-1, D-2, …). Never create a separate file per defect. Sub-IDs are consecutive and never reused. Cite a specific defect as `DEF D-N`. Per-defect status stored as HTML comments within each section. -->

## Defect D-1: <fill: title>

<!-- def_status: Open -->
<!-- def_class: <fill: Code | Spec | Test | Environment> -->
<!-- def_date: <fill: YYYY-MM-DD> -->

### Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

### Purpose And Scope
<!-- guidance: What this defect covers and what it does not -->
<fill: purpose and scope>

### Description
<!-- guidance: What is wrong -->
<fill: description>

### Steps To Reproduce
<!-- guidance: Numbered -->
<fill: steps to reproduce>

### Severity
<!-- guidance: Blocker | Major | Minor with reason -->
<fill: severity>

### Suspected Cause
<!-- guidance: Likely area and whether code, plan, or design is at fault -->
<fill: suspected cause>

### Owner
<!-- guidance: Builder agent or upstream agent that should fix it -->
<fill: owner>

### Classification And Route
<!-- guidance: Three lines, read by scripts/traceability.py:
- Class: Code (the code fails an approved criterion) | Spec (a criterion, design, or contract is wrong or missing) | Test (the Phase 7 test case or suite is wrong; the product is right) | Environment (data, configuration, or infrastructure)
- Route: Code -> the Fix feature FEAT-NNN ('Type: Fix DEF D-N', planned by build-planner, approved by the tech lead); Spec -> SCR S-N (living spec rule); Test -> the test case TC TC-N or suite to revise; Environment -> the owner
- Status: Open | Fixing | Fixed (fix merged, retest pending) | Closed (retest passed in the newest execution report) | Won't fix (DEC-NNN, a named human's decision)
No builder changes code for a defect without an approved Fix plan -->
<fill: classification and route>

### Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
<fill: assumptions>

### Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
<fill: open questions>

### Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
<fill: traceability links>

### Quality Checklist
- [ ] Every section is filled, or marked "Not applicable - <reason>"
- [ ] Inputs referenced are Approved artifacts at the stated versions
- [ ] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [ ] Assumptions and open questions are logged and linked
- [ ] Traceability links are present upstream and downstream
- [ ] Terminology follows .ai/standards/glossary.md
- [ ] Vague words removed (etc., as needed, appropriate)
