# Phase 8: Deployment

Prepare infrastructure, pipelines, release notes, and the go-live package. Agents prepare; humans approve and trigger production deployment.

- **Command:** `/run-deployment`
- **Human approver:** Release manager / DevOps
- **Output folder:** `docs/08-deployment/`

## Required inputs

- Tested and approved build
- Target environment details
- Infrastructure and security policies
- Secrets management references (never the secrets)
- Release schedule and change-approval process
- Rollback and downtime tolerance
- Release readiness report

## Producer agents

- `devops-engineer`
- `config-validator`
- `release-agent`

## Deliverable templates

- `.ai/templates/deployment-runbook.md`
- `.ai/templates/rollback-plan.md`
- `.ai/templates/go-live-checklist.md`
- `.ai/templates/release-notes.md`
- `.ai/templates/config-validation-report.md`

## How it runs

devops-engineer (IaC under infra/, pipelines, runbook, rollback plan) -> config-validator -> release-agent (release notes, go-live checklist). Agents never run production deployment commands; the release manager does, after approval.

Every phase follows `.ai/standards/phase-loop.md`: entry interview, Phase Input Brief approved, producers build, validation (script and checker), validation summary to the user, human review and approval.
