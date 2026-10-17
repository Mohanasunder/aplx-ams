---
id: FEAT-000
id_prefix: FEAT
title: <fill: title>
phase: 5
version: 0.1
template: feature-plan
template_version: 1.6
status: Draft
author_agent: <fill: agent name>
approver: Tech lead
default_approver: Tech lead
default_folder: docs/05-build-plan
date: <fill: YYYY-MM-DD>
validation: Pending
---

# <fill: title>

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
<fill: purpose and scope>

## Feature Type
<!-- guidance: 'Type: Feature' (delivers stories; criteria cite REQ S-N AC-n) or 'Type: Enabling' (delivers no story; criteria cite NFR-, TST-, or STD- IDs, for example Task 0 = FEAT-000, the walking skeleton) or 'Type: Fix DEF D-N' (fixes a Code defect; cite the defect as `DEF D-N`; its criteria are the failed criteria copied unchanged; its test set starts with a regression test that reproduces the defect and fails before the fix; built on a feature/ branch like any feature). A fix that needs a criterion, design, or contract changed is not a Fix: it goes through a spec change record first -->
<fill: feature type>

## Objective
<!-- guidance: What this feature delivers; stories covered -->
<fill: objective>

## Dependencies
<!-- guidance: - Depends on: FEAT-IDs or 'none' -->
<fill: dependencies>

## Inputs And Contracts
<!-- guidance: API endpoints, schema, UI specs this feature builds against (IDs and versions) -->
<fill: inputs and contracts>

## Context Pack
<!-- guidance: Exactly what builders and the AI reviewer load for this feature, nothing more. One entry per line: 'ID vX.Y § section or heading' (for example 'API v1.1 § POST /tickets', 'DBD v1.0 § tickets'), 'ID vX.Y' for a short artifact such as an ADR, 'path § selector' for contract files (for example 'docs/04-design/openapi.yaml § /tickets'), or the path of an existing file the feature changes ('::' may replace '§'). Checked and rendered by scripts/context_pack.py; rendered size within max_context_pack_lines (project.md) -->
<fill: context pack>

## Files To Create Or Modify
<!-- guidance: The feature's files in scope: one path per line in backticks, grouped by database, backend, frontend, tests. Builders may change only these files (checked by scripts/check_feature_size.py scope). Source files, excluding tests, must not exceed max_source_files_per_feature (project.md) -->
<fill: files to create or modify>

## New Packages
<!-- guidance: Every package this feature adds or upgrades, one per line: '- npm: zod ^3.23.8 | MIT | why it is needed; alternatives considered'. Ecosystem is npm or pypi; the version spec exactly as it will appear in the manifest. When not 'None', list the manifest and lockfile under Files To Create Or Modify. Write 'None' if the feature adds no packages. Approving this plan approves these packages; any other package needs a revised plan (checked by scripts/check_feature_size.py packages) -->
<fill: new packages>

## Out Of Scope
<!-- guidance: What this feature must not touch or deliver: neighbouring features, criteria left to other FEAT-IDs, shared contracts or schema not listed above -->
<fill: out of scope>

## Risk Tier
<!-- guidance: First line exactly 'Tier: Standard', 'Tier: High', or 'Tier: Critical', then the reason in one sentence. High for auth, permissions, data migrations, integrations, payments, or personal data; Critical for infrastructure, production configuration, or security configuration; Standard otherwise (see .ai/standards/review-and-approval.md). The tier sets the test set approver and the PR review depth; the PR description must state the same tier (checked by scripts/pr_summary.py check). The tech lead confirms it by approving this plan -->
<fill: risk tier>

## Implementation Steps
<!-- guidance: Numbered, small enough to review -->
<fill: implementation steps>

## Test Plan
<!-- guidance: Tests per acceptance criterion -->
<fill: test plan>

## Size Check
<!-- guidance: Table: acceptance criteria (count / max_acceptance_criteria_per_feature), source files (count / max_source_files_per_feature). Then the line 'Expected test runtime: N minutes' (N at most max_test_runtime_minutes in project.md; the feature's own tests, not the full suite). Then the line 'Open design decisions: None'. If a limit is exceeded, split the feature; if a design decision is open, raise an OQ and send it back to Phase 4 -->
<fill: size check>

## Definition Of Done
<!-- guidance: Checklist from the Definition of Done template -->
<fill: definition of done>

## Risks
<!-- guidance: Technical and review risks (the tier itself goes under Risk Tier) -->
<fill: risks>

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
