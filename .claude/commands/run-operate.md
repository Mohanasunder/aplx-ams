---
description: Run Phase 9 (Operate and Feedback) through the standard phase loop
argument-hint: [optional notes, or paths to extra input files]
---

You are the **Orchestrator**. Run **Phase 9: Operate and Feedback** by following `.ai/standards/phase-loop.md` step by step, using this phase configuration. Do not skip the entry interview, the validation summary, or human approval.

- **Goal:** Monitor, learn from incidents and feedback, and feed improvements back into Phase 2.
- **Output folder:** `docs/09-operate/`
- **Required inputs:**
  - Production logs, metrics, and traces
  - Incident and alert history
  - User feedback and usage analytics
  - SLO and SLA targets
  - KPI results versus original goals
  - Cost reports
- **Producer subagents:**
  1. `monitoring-engineer`
  2. `incident-triage`
  3. `feedback-analyst`
  4. `backlog-curator`
- **Sequence:** monitoring-engineer first (revises the Phase 8 monitoring spec and operational runbook from production data; changes to Approved versions follow the living spec rule); incident-triage and feedback-analyst as events and feedback arrive; backlog-curator turns their findings into improvement backlog items that re-enter Phase 2. Production defects follow the defect rule (`.ai/standards/phase-loop.md`).
- **Deliverable templates:** `monitoring-spec`, `operational-runbook`, `incident-report`, `post-mortem`, `feedback-summary`, `improvement-backlog-item`
- **Checker rules file:** `.ai/checker-rules/phase-9.md` (invoke the `checker` subagent)
- **Human approver:** Product owner / ops lead
- **Exit criteria:**
  - Alerts map to SLOs, and the operational runbook has a response for every alert (including alerts added after incidents)
  - Improvement backlog prioritized by the product owner
  - `python3 scripts/feedback_log.py check --gate` passes: every incident, feedback summary, and production defect has an outcome, and every improvement backlog item is Approved or Rejected

Before starting, confirm that the previous phase's artifacts are `status: Approved` (see `project.md`). If not, stop and tell the human which approvals are missing.

The user's request or notes: $ARGUMENTS
