---
id: LRN
id_prefix: LRN
title: Learned Rules
phase: 6
version: 0.1
template: learned-rule
template_version: 2.0
status: Draft
author_agent: standards-author
approver: Tech lead
default_approver: Tech lead
default_folder: docs/logs
date: <fill: YYYY-MM-DD>
validation: Pending
---

# Learned Rules

<!-- Collection file. All learned rules are appended as `## LRN L-N: [title]` sections (L-1, L-2, …). Never create a separate file per rule. Sub-IDs are consecutive and never reused. Cite a specific rule as `LRN L-N`. Per-rule status stored as HTML comments within each section. Approve each section individually with `/approve docs/logs/learned-rules.md --sub-id L-N`. Run `python3 scripts/learned_rules.py build` after approval to regenerate .ai/standards/learned-rules.md. -->

## LRN L-1: <fill: title>

<!-- lrn_status: Draft -->
<!-- lrn_date: <fill: YYYY-MM-DD> -->
<!-- lrn_category: <fill: kebab-case-slug> -->

### Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved), for example the coding standards or ADR A-N the rule refines -->
<fill: input references>

### Purpose And Scope
<!-- guidance: The recurring mistake this rule prevents, in one sentence -->
<fill: purpose and scope>

### Category
<!-- guidance: The review category slug this rule covers, exactly as in docs/logs/review-feedback-log.md (for example missing-authz-check) -->
<fill: category>

### Rule
<!-- guidance: One or two imperative sentences written for the agent (for example 'Check the caller's permission from the permission matrix in every handler before reading data.') -->
<fill: rule>

### Applies To
<!-- guidance: Which agents, layers, or paths (for example backend-builder; src/backend/**) -->
<fill: applies to>

### Evidence
<!-- guidance: From 'python3 scripts/learned_rules.py recurring' and the review feedback log: dates, FEAT-IDs, source (human, ai-code-reviewer, checker), one-line issue each -->
<fill: evidence>

### Example
<!-- guidance: Wrong and right, a few lines each -->
<fill: example>

### How It Is Checked
<!-- guidance: Automated where possible (lint rule, test, or checker rule, with the command or file), otherwise 'AI pre-review and PR reviewer checklist' -->
<fill: how it is checked>

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
- [ ] The rule is one or two imperative sentences an agent can follow without interpretation
- [ ] Evidence shows the category in at least learned_rule_threshold features
