---
id: THR
id_prefix: THR
title: <fill: title>
phase: 3
version: 0.1
template: threat-model
template_version: 2.0
status: Draft
author_agent: <fill: agent name>
approver: Architect / tech lead
default_approver: Architect / tech lead
default_folder: docs/03-architecture
date: <fill: YYYY-MM-DD>
validation: Pending
---

# <fill: title>

> **Single file.** There is exactly one threat model per project. Always use `--id THR --out docs/03-architecture/threat-model.md` when calling `new_artifact.py`; never auto-name as `THR-NNN.md`. Threats within the file use row IDs T-1, T-2, … and are cited elsewhere as `THR T-n`.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this artifact covers and what it does not -->
<fill: purpose and scope>

## Assets
<!-- guidance: Data and functions worth protecting -->
<fill: assets>

## Trust Boundaries
<!-- guidance: Where trust changes (Mermaid or table) -->
<fill: trust boundaries>

## Threats
<!-- guidance: STRIDE-style table: ID, threat, asset, likelihood, impact. The ID column holds T-1, T-2, ... and is cited elsewhere as THR T-n (Phase 7 Threat Model Coverage, checked by scripts/traceability.py), so never renumber after approval: add new threats at the end and mark a dropped one 'Removed - SCR S-N' -->
<fill: threats>

## Mitigations
<!-- guidance: Table: threat ID (T-n), control, how Phase 7 will verify it (test, scan, or review), residual risk -->
<fill: mitigations>

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
