---
description: Run Phase 4 (Solution Design) through the standard phase loop
argument-hint: [optional notes, or paths to extra input files]
---

You are the **Orchestrator**. Run **Phase 4: Solution Design** by following `.ai/standards/phase-loop.md` step by step, using this phase configuration. Do not skip the entry interview, the validation summary, or human approval.

- **Goal:** Specify the schema, APIs, backend and UI design, permissions, coding standards, and test strategy that builders will follow.
- **Output folder:** `docs/04-design/`
- **Required inputs:**
  - Approved architecture, ADRs, and stack
  - Approved requirements and acceptance criteria
  - Brand and UX guidelines or design system
  - Existing database schemas (for migrations)
  - Third-party API documentation
  - Role and permission definitions
  - Organization coding standards
- **Producer subagents:**
  1. `database-designer`
  2. `api-designer`
  3. `backend-designer`
  4. `ux-ui-designer`
  5. `standards-author`
- **Sequence:** database-designer and api-designer in parallel; then backend-designer (backend design, permission matrix) and ux-ui-designer; standards-author last (coding standards, automated gate commands, test strategy). The checker applies the design consistency rules across all artifacts. standards-author also fills the project-specific files in .ai/standards that builders, testers, and reviewers read.
- **Deliverable files (friendly filenames — one file per type):**
  | File | Template | ID | Created by |
  | --- | --- | --- | --- |
  | `docs/04-design/database-design.md` | `database-design` | DBD | `database-designer` |
  | `docs/04-design/api-spec.md` | `api-spec` | API | `api-designer` |
  | `docs/04-design/openapi.yaml` | (hand-written) | n/a | `api-designer` |
  | `docs/04-design/backend-design.md` | `backend-design` | BED | `backend-designer` |
  | `docs/04-design/ui-spec.md` | `ui-spec` | UIS | `ux-ui-designer` |
  | `docs/04-design/permission-matrix.md` | `permission-matrix` | PRM | `backend-designer` |
  | `docs/04-design/coding-standards.md` | `coding-standards` | STD | `standards-author` |
  | `docs/04-design/test-strategy.md` | `test-strategy` | TST | `standards-author` |
- **Spikes (optional):** a design question that needs evidence from running code follows the spike process in `.ai/standards/branching-standard.md` (template `spike`, approved by the tech lead, closed before the phase ends).
- **Agent charter:** after `standards-author` finishes, run `python3 scripts/build_charter.py build` and include `.ai/standards/agent-charter.md` in the human review: the tech lead reads it as the builders will see it. Fix anything wrong in its source files, not in the charter.
- **Checker rules file:** `.ai/checker-rules/phase-4.md` (invoke the `checker` subagent)
- **Human approver:** Tech lead + UX
- **Exit criteria:**
  - Schema, API, and UI cross-consistent
  - Every story has the endpoints and screens it needs
  - Design package Approved by the tech lead and UX

Before starting, confirm that the previous phase's artifacts are `status: Approved` (see `project.md`). If not, stop and tell the human which approvals are missing.

The user's request or notes: $ARGUMENTS
