---
description: Run Phase 8 (Deployment) through the standard phase loop
argument-hint: [optional notes, or paths to extra input files]
---

You are the **Orchestrator**. Run **Phase 8: Deployment** by following `.ai/standards/phase-loop.md` step by step, using this phase configuration. Do not skip the entry interview, the validation summary, or human approval.

- **Goal:** Prepare infrastructure, pipelines, release notes, and the go-live package. Agents prepare; humans approve and trigger production deployment.
- **Output folder:** `docs/08-deployment/`
- **Required inputs:**
  - Tested and approved build
  - Target environment details
  - Infrastructure and security policies
  - Secrets management references (never the secrets)
  - Release schedule and change-approval process
  - Rollback and downtime tolerance
  - Release readiness report
- **Producer subagents:**
  1. `devops-engineer`
  2. `config-validator`
  3. `monitoring-engineer`
  4. `release-agent`
- **Sequence:** devops-engineer (IaC under infra/, pipelines, deployment runbook, rollback plan) -> config-validator -> monitoring-engineer (monitoring spec and operational runbook, before go-live) -> release-agent (release notes, go-live checklist with go / no-go criteria; runs `go_live.py criteria`). Agents never run production deployment commands; the release manager does, after a recorded Go.
- **Go / no-go:** the decision is `/approve` on the go-live checklist by the release manager and by the tech lead (production deploys are Critical): Approve = Go, Reject = No-go with the reason. Before deploying, the release manager runs `python3 scripts/go_live.py check`, which must print GO.
- **Deliverable templates:** `deployment-runbook`, `rollback-plan`, `monitoring-spec`, `operational-runbook`, `go-live-checklist`, `release-notes`, `config-validation-report`
- **Checker rules file:** `.ai/checker-rules/phase-8.md` (invoke the `checker` subagent)
- **Human approver:** Release manager / DevOps
- **Exit criteria:**
  - IaC validates and passes policy checks
  - Rollback plan Approved
  - Monitoring spec and operational runbook Approved (every alert has a response)
  - Go recorded: go-live checklist Approved by the release manager and the tech lead; `python3 scripts/go_live.py check` prints GO

Before starting, confirm that the previous phase's artifacts are `status: Approved` (see `project.md`). If not, stop and tell the human which approvals are missing.

The user's request or notes: $ARGUMENTS
