---
id: TC
id_prefix: TC
title: Test Cases
phase: 7
version: 0.1
template: test-case
template_version: 2.0
status: Draft
author_agent: test-designer
approver: QA lead
default_approver: QA lead
default_folder: docs/07-testing
date: <fill: YYYY-MM-DD>
validation: Pending
---

# Test Cases

<!-- Collection file. All test cases are appended as `## Test Case TC-N: [title]` sections (TC-1, TC-2, …). Never create a separate file per test case. Sub-IDs are consecutive and never reused. Cite a specific test case as `TC TC-N`. -->

## Test Case TC-1: <fill: title>

<!-- tc_status: Draft -->
<!-- tc_date: <fill: YYYY-MM-DD> -->

### Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

### Purpose And Scope
<!-- guidance: What this case covers and what it does not -->
<fill: purpose and scope>

### Objective
<!-- guidance: What this proves -->
<fill: objective>

### Preconditions
<!-- guidance: State and data -->
<fill: preconditions>

### Steps
<!-- guidance: Numbered -->
<fill: steps>

### Expected Result
<!-- guidance: Observable outcome -->
<fill: expected result>

### Linked Criteria
<!-- guidance: Every acceptance criterion this case proves, one per line as 'REQ S-N AC-n' (or NFR N-n/TST/STD for Enabling criteria). scripts/traceability.py reads this section to find criteria with no test case -->
<fill: linked criteria>

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
