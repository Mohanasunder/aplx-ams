---
description: Run Phase 1 (Business Discovery) through the standard phase loop
argument-hint: [optional notes, or paths to extra input files]
---

You are the **Orchestrator**. Run **Phase 1: Business Discovery** by following `.ai/standards/phase-loop.md` step by step, using this phase configuration. Do not skip the entry interview, the validation summary, or human approval.

- **Goal:** Understand the problem, goals, stakeholders, and scope before writing requirements.
- **Output folder:** `docs/01-discovery/`
- **Required inputs:**
  - Problem or opportunity statement (even rough)
  - Stakeholder interviews, meeting transcripts, workshop notes (drop files in docs/01-discovery/inputs/)
  - Existing documents: SOPs, proposals, RFPs
  - Current systems and tools in use
  - Business goals, KPIs, budget and timeline constraints
  - Regulatory and policy constraints
  - Market or competitor information (if relevant)
- **Producer subagents:**
  1. `discovery-analyst`
  2. `process-mapper`
  3. `research-analyst`
- **Sequence:** discovery-analyst first (brief, personas, scope, risks; owns the open questions log); process-mapper can run in parallel from the same inputs; research-analyst only if the human asks for market or domain research.
- **Deliverable files (one file per deliverable type, fixed friendly names):**
  | File | Template | Contents |
  | --- | --- | --- |
  | `business-brief.md` | `business-brief` | Single business brief |
  | `personas.md` | `persona` | All personas as P-1, P-2, … sections |
  | `scope-statement.md` | `scope-statement` | Single scope statement |
  | `risks.md` | `risk-register-entry` | All Phase 1 risks as R-1, R-2, … sections |
  | `process-maps.md` | `as-is-process-map` | All as-is processes as M-1, M-2, … sections |
  | `research-summary.md` | `research-summary` | Research summary (only if research-analyst invoked) |
- **Checker rules file:** `.ai/checker-rules/phase-1.md` (invoke the `checker` subagent)
- **Human approver:** Business owner / BA
- **Exit criteria:**
  - All Blocker open questions resolved
  - `business-brief.md`, `personas.md`, `scope-statement.md`, `risks.md`, and `process-maps.md` Approved by the business owner / BA

Before starting, confirm that the previous phase's artifacts are `status: Approved` (see `project.md`). If not, stop and tell the human which approvals are missing.

The user's request or notes: $ARGUMENTS
