---
id: SCR-001
title: Spec Changes
phase: 1
version: 0.1
template: spec-change
template_version: 2.0
status: In review
author_agent: discovery-analyst
approver: Approver of the changed artifact's phase
date: 2026-10-17
validation: Pass with warnings
---
# Spec Changes

<!-- Collection file. All spec change records are appended as `## SCR S-N: [title]` sections (S-1, S-2, …). Never create a separate file per spec change. Sub-IDs are consecutive and never reused. Cite a specific record as `SCR S-N`. Per-record status stored as HTML comments within each section. Approve each section individually with `/approve docs/logs/spec-changes.md --sub-id S-N`. -->

## SCR S-1: Phase 1 summary wording after approval

<!-- scr_status: Approved -->
<!-- scr_date: 2026-10-17 -->
<!-- scr_approver: Mohanasunder -->

### Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- SUM-001 v0.2 (Approved 2026-10-17 06:05 UTC by Mohanasunder) - docs/01-discovery/SUMMARY.md.
- `docs/logs/approval-log.md` (Phase 1 approvals of 2026-10-17).

### Purpose And Scope
<!-- guidance: What this change covers and what it does not -->
Covers wording-only corrections: SUM-001 § Input References and § Documents (approval status of the Phase 1 deliverables) and § Open Items (confirmed-assumptions list, correcting it to match the assumptions log), and the OQ-002 "Answer and date" cell in `docs/logs/open-questions-log.md`. Does not change any decision, constraint, open item, goal, scope item, persona, or risk. Does not change PIB-001 v0.1 or IRC-002 v0.1 (scope chosen by Mohanasunder, Business owner / BA, in chat on 2026-10-17).

### Changed Artifact
<!-- guidance: One line per changed approved artifact: 'ID vOLD -> vNEW' (for example 'API v1.0 -> v1.1'), with its path -->
- SUM-001 v0.2 -> v0.3 (docs/01-discovery/SUMMARY.md)

### Trigger
<!-- guidance: First line: what revealed the problem and where (FEAT-, DEF D-N, PR, review comment, feedback or incident ID) and who found it -->
Orchestrator review after the Phase 1 gate on 2026-10-17: SUM-001 § Input References and § Documents still say the Phase 1 deliverables are "Draft, pending approval" though all are Approved; plus run 1 finding F-03 (docs/validation/phase-1-run-1.md) on the OQ-002 answer wording in docs/logs/open-questions-log.md.

### Change
<!-- guidance: What changes, section by section: before and after. Specs change here first; code is regenerated from them -->
- SUM-001 § Input References: before "Phase 1 deliverables below are Draft, pending validation and approval; versions are updated here once approved." After: all Phase 1 deliverables listed under § Documents are Approved at v0.2 on 2026-10-17.
- SUM-001 § Documents: the "Draft, pending approval" list is merged into the Approved list; BRF-001, PER-001, SCP-001, RSK-001, PRC-001 listed as Approved v0.2.
- `docs/logs/open-questions-log.md` row OQ-002, Answer and date (a log row, not a versioned artifact): before "Only client contact names and emails"; after "Only names and emails", matching INT-001 v0.1 Q15.
- SUM-001 § Open Items, assumptions bullet: before "A-001, A-004, A-005, A-007 Confirmed"; after "A-001, A-002, A-003, A-004, A-005, A-007 Confirmed", matching `docs/logs/assumptions-log.md` (A-002 and A-003 Confirmed by Mohanasunder, 2026-10-17) and SUM-001 § Assumptions (checker run 6 finding N-02).
- No other change to decisions, constraints, or open items.

### Reason
<!-- guidance: Why the approved spec was wrong or incomplete -->
SUM-001 was written before the Phase 1 deliverables were approved and was not refreshed at approval. The OQ-002 log row narrowed the recorded answer ("client contact names and emails") compared with the source answer in INT-001 v0.1 Q15 ("names and emails").

### Decision Record
<!-- guidance: Required when Changed Artifact lists an architecture or contract artifact (templates architecture-overview, adr, api-spec, database-design, deployment-topology, threat-model): cite the new ADR A-N that records this change, with options considered and consequences. When an ADR itself changes, cite the new ADR that supersedes it (the old ADR's Status And Date becomes 'Superseded by ADR A-N', listed under Changed Artifact). The ADR is approved by the architect / tech lead together with this SCR (checked by scripts/spec_impact.py records). Otherwise write 'Not applicable - no architecture or contract artifact changes' -->
Not applicable - no architecture or contract artifact changes. Scope of this SCR (SUM-001 and the OQ-002 log row only; PIB-001 and IRC-002 unchanged) chosen by Mohanasunder (Business owner / BA), chat, 2026-10-17.

### Impact
<!-- guidance: From 'python3 scripts/spec_impact.py impact <ID>': table of each citing artifact or feature, its state, and the action: revise, re-test, re-approve, or 'No change - reason' -->
`python scripts/spec_impact.py impact SUM-001`: "SUM-001: current v0.2 (Approved) at docs/01-discovery/SUMMARY.md. No artifact cites it."

| Artifact | State | Action |
| --- | --- | --- |
| SUM-001 | Approved v0.2 | Revise to v0.3 and re-approve |
| PIB-001 v0.1 | Approved | No change - original intake wording "client contact names and emails" kept as historical record by Mohanasunder's decision; downstream deliverables already use "names and emails" |
| IRC-002 v0.1 | Approved | No change - original intake wording "client contact names and emails" kept as historical record by Mohanasunder's decision; downstream deliverables already use "names and emails" |

### Work Stopped
<!-- guidance: Features set to State: Blocked with this SCR cited, or 'None - reason' -->
None - no features exist yet.

### Resume Criteria
<!-- guidance: What must be Approved before stopped work resumes (this SCR, the new artifact version, the ADR in Decision Record if any, revised downstream artifacts) -->
SCR S-1 and SUM-001 v0.3 Approved.

### Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
None.

### Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
None.

### Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: INT-001 v0.1 (Q15); SUM-001 v0.2
- Downstream: SUM-001 v0.3

### Quality Checklist
- [x] Every section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)
- [x] Every changed artifact is listed as 'ID vOLD -> vNEW'
- [x] An architecture or contract change cites its new or superseding ADR A-N under Decision Record
- [x] Impact covers every artifact and feature that cites the changed artifact

## SCR S-2: Phase 2 summary wording after approval
<!-- scr_approver: Mohanasunder -->

<!-- scr_status: Approved -->
<!-- scr_date: 2026-10-17 -->

### Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
- SUM-002 v0.1 (Approved 2026-10-17 08:46 UTC by Mohanasunder) - docs/02-requirements/SUMMARY.md.
- `docs/logs/approval-log.md` (Phase 2 approvals of 2026-10-17).

### Purpose And Scope
<!-- guidance: What this change covers and what it does not -->
Covers a wording-only correction to SUM-002 § Documents (approval status of the Phase 2 deliverables). Does not change any decision, constraint, open item, requirement, rule, NFR, or risk (scope chosen by Mohanasunder, Product owner / BA, in chat on 2026-10-17).

### Changed Artifact
<!-- guidance: One line per changed approved artifact: 'ID vOLD -> vNEW' (for example 'API v1.0 -> v1.1'), with its path -->
- SUM-002 v0.1 -> v0.2 (docs/02-requirements/SUMMARY.md)

### Trigger
<!-- guidance: First line: what revealed the problem and where (FEAT-, DEF D-N, PR, review comment, feedback or incident ID) and who found it -->
Orchestrator review after the Phase 2 gate on 2026-10-17: SUM-002 § Documents still lists the Phase 2 deliverables under "Draft, awaiting review (v0.1):" though all were Approved at v0.1 on 2026-10-17.

### Change
<!-- guidance: What changes, section by section: before and after. Specs change here first; code is regenerated from them -->
- SUM-002 § Documents: before, the heading line "Draft, awaiting review (v0.1):" above PRS-001, EPC-001, REQ-001, NFR-001, BR-001, BKL-001, GLO-001, RSK-002 v0.1. After: that heading line is removed, so the eight deliverables sit in the single "Approved:" list (all Approved v0.1 on 2026-10-17).
- No other change to decisions, constraints, open items, or document versions.

### Reason
<!-- guidance: Why the approved spec was wrong or incomplete -->
SUM-002 was written before the Phase 2 deliverables were approved and was not refreshed at approval.

### Decision Record
<!-- guidance: Required when Changed Artifact lists an architecture or contract artifact (templates architecture-overview, adr, api-spec, database-design, deployment-topology, threat-model): cite the new ADR A-N that records this change, with options considered and consequences. When an ADR itself changes, cite the new ADR that supersedes it (the old ADR's Status And Date becomes 'Superseded by ADR A-N', listed under Changed Artifact). The ADR is approved by the architect / tech lead together with this SCR (checked by scripts/spec_impact.py records). Otherwise write 'Not applicable - no architecture or contract artifact changes' -->
Not applicable - no architecture or contract artifact changes. Change decided by Mohanasunder (Product owner / BA), chat, 2026-10-17.

### Impact
<!-- guidance: From 'python3 scripts/spec_impact.py impact <ID>': table of each citing artifact or feature, its state, and the action: revise, re-test, re-approve, or 'No change - reason' -->
`python scripts/spec_impact.py impact SUM-002`: "SUM-002: current v0.1 (Approved) at docs/02-requirements/SUMMARY.md. No artifact cites it."

| Artifact | State | Action |
| --- | --- | --- |
| SUM-002 | Approved v0.1 | Revise to v0.2 and re-approve |

### Work Stopped
<!-- guidance: Features set to State: Blocked with this SCR cited, or 'None - reason' -->
None - no features exist yet.

### Resume Criteria
<!-- guidance: What must be Approved before stopped work resumes (this SCR, the new artifact version, the ADR in Decision Record if any, revised downstream artifacts) -->
SCR S-2 and SUM-002 v0.2 Approved.

### Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md -->
None.

### Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md -->
None.

### Traceability Links
<!-- guidance: Upstream and downstream IDs, or 'Not applicable - reason' -->
- Upstream: SUM-002 v0.1
- Downstream: SUM-002 v0.2

### Quality Checklist
- [x] Every section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)
- [x] Every changed artifact is listed as 'ID vOLD -> vNEW'
- [x] An architecture or contract change cites its new or superseding ADR A-N under Decision Record
- [x] Impact covers every artifact and feature that cites the changed artifact
