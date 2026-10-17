# Phase 9: Operate and Feedback

Monitor, learn from incidents and feedback, and feed improvements back into Phase 2.

- **Command:** `/run-operate`
- **Human approver:** Product owner / ops lead
- **Output folder:** `docs/09-operate/`

## Required inputs

- Production logs, metrics, and traces
- Incident and alert history
- User feedback and usage analytics
- SLO and SLA targets
- KPI results versus original goals
- Cost reports

## Producer agents

- `monitoring-engineer`
- `incident-triage`
- `feedback-analyst`
- `backlog-curator`

## Deliverable templates

- `.ai/templates/monitoring-spec.md`
- `.ai/templates/incident-report.md`
- `.ai/templates/post-mortem.md`
- `.ai/templates/feedback-summary.md`
- `.ai/templates/improvement-backlog-item.md`

## How it runs

monitoring-engineer first; incident-triage and feedback-analyst as events and feedback arrive; backlog-curator turns their findings into improvement backlog items that re-enter Phase 2.

Every phase follows `.ai/standards/phase-loop.md`: entry interview, Phase Input Brief approved, producers build, validation (script and checker), validation summary to the user, human review and approval.
