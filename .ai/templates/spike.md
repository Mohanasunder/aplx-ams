---
id: SPK
id_prefix: SPK
title: <fill: title>
phase: 3
version: 0.1
template: spike
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

> **Collection file.** All spike records for the project live in this single file. Always use `--out docs/03-architecture/spikes.md` when calling `new_artifact.py`. Each spike is a `## Spike S-N: [Title]` section (S-1, S-2, …). A specific spike is cited downstream as `SPK S-N`. Never renumber after approval — append new spikes at the end; mark a closed one `Closed - ADR A-N` in the section heading.

## Input References
<!-- guidance: Exact IDs and versions of the approved artifacts used as input (status: Approved) -->
<fill: input references>

## Purpose And Scope
<!-- guidance: What this collection covers: all throwaway experiments on spike/spk-S-N-slug branches that answer architecture or design questions; never merged; deleted once their ADR is approved -->
<fill: purpose and scope>

---

## Spike S-1: <fill: spike title>

### Question
<!-- guidance: The one architectural or design question this spike answers -->
<fill: question>

### Options To Test
<!-- guidance: Two or more options, and what will be built for each (minimum code to answer the question) -->
<fill: options to test>

### Time Box
<!-- guidance: Number of days, for example '3 days'. At most max_spike_days (project.md). When it ends, decide with what is known -->
<fill: time box>

### Success Criteria
<!-- guidance: Measurable results that decide the question (latency, effort, compatibility, cost) -->
<fill: success criteria>

### Findings
<!-- guidance: Plan stage: 'Pending - recorded after the spike'. After: results per option against the success criteria, with numbers and the spike commit SHAs -->
<fill: findings>

### Recommendation
<!-- guidance: Plan stage: 'Pending - recorded after the spike'. After: the recommended option and why; the human decides in the ADR -->
<fill: recommendation>

### Resulting ADR
<!-- guidance: Plan stage: 'Pending'. After: the ADR ID that records the decision and cites this spike -->
<fill: resulting adr>

### Traceability Links
<!-- guidance: Upstream IDs (NFR N-N, REQ S-N) and downstream ADR A-N -->
<fill: traceability links>

---
<!-- Add further ## Spike S-N: sections here as new spikes arise -->

## Assumptions
<!-- guidance: Each labeled A-NNN and logged in docs/logs/assumptions-log.md (collection-level) -->
<fill: assumptions>

## Open Questions
<!-- guidance: Each labeled OQ-NNN and logged in docs/logs/open-questions-log.md (collection-level) -->
<fill: open questions>

## Quality Checklist
- [ ] Every template section is filled, or marked "Not applicable - <reason>"
- [ ] Inputs referenced are Approved artifacts at the stated versions
- [ ] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [ ] Assumptions and open questions are logged and linked
- [ ] Traceability links are present upstream and downstream
- [ ] Terminology follows .ai/standards/glossary.md
- [ ] Vague words removed (etc., as needed, appropriate)
- [ ] Every spike has a time box in days, within max_spike_days (project.md)
- [ ] Every spike's success criteria let the human decide between the options
- [ ] Spike sub-IDs (S-1, S-2, …) are consecutive from 1 with no gaps
- [ ] No separate SPK-NNN.md files exist; all spikes are sections in this file

## Approval Record
| Field | Value |
| --- | --- |
| Decision | Pending |
| Approver | Pending |
| Role | Pending |
| Conditions | None |
| Comments | None |
| Timestamp | Pending |
