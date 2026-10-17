---
id: SCR
id_prefix: SCR
title: Spec Changes
phase: 0
version: 0.1
template: spec-change
template_version: 2.0
status: Draft
author_agent: <fill: agent name>
approver: Approver of the changed artifact's phase
default_approver: Approver of the changed artifact's phase
default_folder: docs/logs
date: <fill: YYYY-MM-DD>
validation: Pending
---

# Spec Changes

<!-- Collection file. All spec change records are appended as `## SCR S-N: [title]` sections (S-1, S-2, …). Never create a separate file per spec change. Sub-IDs are consecutive and never reused. Cite a specific record as `SCR S-N`. Per-record status stored as HTML comments within each section. Approve each section individually with `/approve docs/logs/spec-changes.md --sub-id S-N`. -->

## SCR S-1: <fill: title>

<!-- scr_status: Draft -->
<!-- scr_date: <fill: YYYY-MM-DD> -->
<!-- scr_approver: -->

### Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

### Purpose And Scope
<!-- guidance: What this change covers and what it does not -->
<fill: purpose and scope>

### Changed Artifact
<!-- guidance: One line per changed approved artifact: 'ID vOLD -> vNEW' (for example 'API v1.0 -> v1.1'), with its path -->
<fill: changed artifact>

### Trigger
<!-- guidance: First line: what revealed the problem and where (FEAT-, DEF D-N, PR, review comment, feedback or incident ID) and who found it -->
<fill: trigger>

### Change
<!-- guidance: What changes, section by section: before and after. Specs change here first; code is regenerated from them -->
<fill: change>

### Reason
<!-- guidance: Why the approved spec was wrong or incomplete -->
<fill: reason>

### Decision Record
<!-- guidance: Required when Changed Artifact lists an architecture or contract artifact (templates architecture-overview, adr, api-spec, database-design, deployment-topology, threat-model): cite the new ADR A-N that records this change, with options considered and consequences. When an ADR itself changes, cite the new ADR that supersedes it (the old ADR's Status And Date becomes 'Superseded by ADR A-N', listed under Changed Artifact). The ADR is approved by the architect / tech lead together with this SCR (checked by scripts/spec_impact.py records). Otherwise write 'Not applicable - no architecture or contract artifact changes' -->
<fill: decision record>

### Impact
<!-- guidance: From 'python3 scripts/spec_impact.py impact <ID>': table of each citing artifact or feature, its state, and the action: revise, re-test, re-approve, or 'No change - reason' -->
<fill: impact>

### Work Stopped
<!-- guidance: Features set to State: Blocked with this SCR cited, or 'None - reason' -->
<fill: work stopped>

### Resume Criteria
<!-- guidance: What must be Approved before stopped work resumes (this SCR, the new artifact version, the ADR in Decision Record if any, revised downstream artifacts) -->
<fill: resume criteria>

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
- [ ] Every changed artifact is listed as 'ID vOLD -> vNEW'
- [ ] An architecture or contract change cites its new or superseding ADR A-N under Decision Record
- [ ] Impact covers every artifact and feature that cites the changed artifact
