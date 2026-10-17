# Checker rules: Phase 8 (Deployment)

Applies after the producer(s) in `docs/08-deployment` finish. Apply the general layers in `.ai/standards/checker-and-fail-decision.md`, then:

## Phase-specific focus

- IaC validates and passes policy checks
- No secrets in config or code
- Rollback plan exists and is testable
- Release notes match merged features
- Environment parity checked
- Production configuration (Production Configuration in `.ai/standards/coding-standards.md`) changed only by the `devops-engineer`, with secret references only, and every change listed for Critical-tier review by the tech lead and the release manager
- Monitoring spec and operational runbook exist before go-live: every alert maps to an SLO and has an Alert Responses row (first checks, actions, escalation role); support procedures, escalation by role (no personal contact details), common operations including restore, and known issues are filled
- Go-live checklist names the release tag, target environment, and change window; every Go / No-Go criterion cites its evidence as `ID vX.Y`; `python3 scripts/go_live.py criteria` passes
- Deployment runbook's first pre-deployment check is `python3 scripts/go_live.py check` printing GO

## Non-overridable checks

If any of these fail, mark the finding **Blocker (non-overridable)**; the user may only send the artifact back.

- Secrets in configuration or IaC
- Failed IaC policy check
- A go-live checklist submitted for the Go decision while a criterion's evidence is not Approved (`go_live.py criteria` fails), or a criterion marked met without evidence
- An alert in the monitoring spec with no response in the operational runbook

## Who decides on a Fail

Release manager / DevOps (see `.ai/standards/review-and-approval.md`).
