---
description: Run Phase 3 (Solution Architecture) through the standard phase loop
argument-hint: [optional notes, or paths to extra input files]
---

You are the **Orchestrator**. Run **Phase 3: Solution Architecture** by following `.ai/standards/phase-loop.md` step by step, using this phase configuration. Do not skip the entry interview, the validation summary, or human approval.

- **Goal:** Choose the stack, structure, integrations, security model, and deployment topology.
- **Output folder:** `docs/03-architecture/`
- **Required inputs:**
  - Approved requirements (especially NFRs and integrations)
  - Enterprise architecture standards and approved technology list
  - Team skills and preferred stack
  - Hosting and cloud constraints
  - Documentation of systems to integrate with
  - Security policies
  - Budget limits
  - Expected scale: users, data volume, traffic
- **Producer subagents:**
  1. `solution-architect`
  2. `security-architect`
  3. `infra-cost-analyst`
- **Spikes (optional):** if a decision needs evidence from running code, solution-architect appends a `## Spike S-N:` section to `docs/03-architecture/spikes.md` (template `spike`): question, options, time box, success criteria. Show it to the architect / tech lead for `/approve`, run `python3 scripts/spike.py start SPK-S-N`, let solution-architect build on the `spike/spk-S-N-slug` branch, then record findings in the spike's section, write the ADR citing `SPK S-N`, get both approved, and run `python3 scripts/spike.py close SPK-S-N --delete`. The phase does not close with an open spike.
- **Sequence:** solution-architect first (overview, technology comparison, ADRs); then security-architect (threat model) and infra-cost-analyst (topology, cost) in parallel; the checker applies the architecture review rules.
- **Deliverable files (friendly filenames):**
  | File | Template | Contents |
  | --- | --- | --- |
  | `docs/03-architecture/architecture-overview.md` | `architecture-overview` | Single architecture overview (ARC) |
  | `docs/03-architecture/adrs.md` | `adr` | All ADRs as `## ADR A-N:` sections |
  | `docs/03-architecture/technology-comparison.md` | `technology-comparison` | Single technology comparison (TEC) |
  | `docs/03-architecture/spikes.md` *(if needed)* | `spike` | All spikes as `## Spike S-N:` sections (SPK) |
  | `docs/03-architecture/threat-model.md` | `threat-model` | Single threat model (THR); threats as T-1, T-2, … rows |
  | `docs/03-architecture/deployment-topology.md` | `deployment-topology` | Single deployment topology (TOP) |
  | `docs/03-architecture/cost-estimate.md` | `cost-estimate` | Single cost estimate (CST) |
- **Checker rules file:** `.ai/checker-rules/phase-3.md` (invoke the `checker` subagent)
- **Human approver:** Architect / tech lead
- **Exit criteria:**
  - Every NFR mapped to an architectural answer
  - Every significant decision has an ADR
  - No open spikes: `python3 scripts/spike.py check` passes
  - Architecture package Approved by the architect / tech lead

Before starting, confirm that the previous phase's artifacts are `status: Approved` (see `project.md`). If not, stop and tell the human which approvals are missing.

The user's request or notes: $ARGUMENTS
