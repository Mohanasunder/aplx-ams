---
id: SSR
id_prefix: SSR
title: Security Scan Reports
phase: 6
version: 0.1
template: security-scan-report
template_version: 2.0
status: Draft
author_agent: security-scanner
approver: Human developer reviewer
default_approver: Human developer reviewer
default_folder: docs/06-build
date: <fill: YYYY-MM-DD>
validation: Pending
---

# Security Scan Reports

<!-- Collection file. All security scan reports are appended as `## SSR FEAT-NNN: [title]` sections. Never create a separate file per feature. Per-report status stored as HTML comments within each section. Approve each section individually with `/approve docs/06-build/security-scan-reports.md --sub-id FEAT-NNN`. -->

## SSR FEAT-000: <fill: title>

<!-- ssr_status: Draft -->
<!-- ssr_author: <fill: agent name> -->
<!-- ssr_date: <fill: YYYY-MM-DD> -->
<!-- ssr_verdict: <fill: Clean | Findings to fix | Blocked> -->

### Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

### Purpose And Scope
<!-- guidance: What this report covers and what it does not -->
<fill: purpose and scope>

### Scan Tools And Scope
<!-- guidance: Commands run and what they covered -->
<fill: scan tools and scope>

### Findings
<!-- guidance: Table: tool, finding, severity, file -->
<fill: findings>

### Secrets Check
<!-- guidance: Result of the secrets scan -->
<fill: secrets check>

### Verdict
<!-- guidance: Clean | Findings to fix | Blocked (non-overridable) -->
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
