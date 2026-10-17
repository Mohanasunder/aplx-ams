---
id: AIR
id_prefix: AIR
title: AI Pre-Review Reports
phase: 6
version: 0.1
template: ai-pre-review-report
template_version: 2.0
status: Draft
author_agent: ai-code-reviewer
approver: Human developer reviewer
default_approver: Human developer reviewer
default_folder: docs/06-build
date: <fill: YYYY-MM-DD>
validation: Pending
---

# AI Pre-Review Reports

<!-- Collection file. All AI pre-review reports are appended as `## AIR FEAT-NNN: [title]` sections. Never create a separate file per feature. Per-report status stored as HTML comments within each section. Approve each section individually with `/approve docs/06-build/ai-pre-review-reports.md --sub-id FEAT-NNN`. -->

## AIR FEAT-000: <fill: title>

<!-- air_status: Draft -->
<!-- air_author: <fill: agent name> -->
<!-- air_date: <fill: YYYY-MM-DD> -->
<!-- air_verdict: <fill: Ready for human review | Needs changes> -->

### Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

### Purpose And Scope
<!-- guidance: What this report covers and what it does not -->
<fill: purpose and scope>

### Plan Adherence
<!-- guidance: Does the code match plan.md, the contract, and acceptance criteria -->
<fill: plan adherence>

### Findings
<!-- guidance: Table: file, line, category (kebab-case slug, reuse one from docs/logs/review-feedback-log.md where it fits), issue, severity, suggested fix -->
<fill: findings>

### Learned Rules Check
<!-- guidance: For each rule in .ai/standards/learned-rules.md that applies to this diff: followed or violated (file and line). A violation is a Major finding. 'No learned rules yet' if the file has none -->
<fill: learned rules check>

### Security Observations
<!-- guidance: Auth, validation, secrets, data handling -->
<fill: security observations>

### Verdict
<!-- guidance: Advisory only: Ready for human review | Needs changes -->
<fill: verdict>

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
