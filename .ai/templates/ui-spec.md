---
id: UIS
id_prefix: UIS
title: <fill: title>
phase: 4
version: 0.1
template: ui-spec
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

> **Single file.** There is exactly one UI spec per project. Always use `--id UIS --out docs/04-design/ui-spec.md` when calling `new_artifact.py`; never auto-name as `UIS-NNN.md`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
<fill: purpose and scope>

## Pages And Routes
<!-- guidance: Table: route, page, story ID, roles -->
<fill: pages and routes>

## User Flows
<!-- guidance: One flow per user-facing story, headed with the story ID (for example '### REQ-014 Create order'). A Mermaid flowchart or numbered steps from entry point to outcome, naming the page or route at each step and the API call it makes. Include the error and empty paths from the story's acceptance criteria (validation failure, not found, no permission) -->
<fill: user flows>

## Wireframes
<!-- guidance: One wireframe per page in Pages And Routes, headed with the route. ASCII or Mermaid block showing layout regions, every field and action with its label (domain glossary terms), and the loading, empty, and error states. Fields must exist in the API spec. Link an external design file only in addition, never instead -->
<fill: wireframes>

## Component Tree
<!-- guidance: Components and props -->
<fill: component tree>

## State Management
<!-- guidance: Approach and data fetching -->
<fill: state management>

## Design Tokens
<!-- guidance: Colors, type, spacing -->
<fill: design tokens>

## Accessibility
<!-- guidance: Target level and key requirements -->
<fill: accessibility>

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
- [ ] Every user-facing story has a user flow, including its error paths
- [ ] Every page has a wireframe with loading, empty, and error states
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
