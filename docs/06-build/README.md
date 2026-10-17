# Phase 6: Build

Write tests first, have a human approve them, then generate code for one approved feature at a time on its own branch; humans review and approve the PR.

- **Command:** `/run-build-feature`
- **Human approver:** Human developer reviewer
- **Output folder:** `docs/06-build/`

## Required inputs

- Approved feature plan, tasks, and acceptance files
- API contract and DB schema
- UI specs
- Coding standards and automated gate commands (.ai/standards)
- Existing codebase and merged dependencies
- Non-production environment access
- Human feedback from earlier PR iterations

## Producer agents

- `database-builder`
- `backend-builder`
- `frontend-builder`
- `integration-builder`
- `documentation-writer`
- `ai-code-reviewer`
- `security-scanner`

## Deliverable templates

- `.ai/templates/feature-test-set.md`
- `.ai/templates/pr-description.md` → all PRs collected in `docs/06-build/pr-descriptions.md` (`## PR FEAT-NNN:` sections)
- `.ai/templates/ai-pre-review-report.md`
- `.ai/templates/security-scan-report.md`

## How it runs

See .claude/commands/run-build-feature.md: branch, tests first (builders in Mode A), test set validated and approved by a human, implement (builders in Mode B, tests locked), automated gates, AI pre-review and security scan, validation summary, draft PR, human review.

Every phase follows `.ai/standards/phase-loop.md`: entry interview, Phase Input Brief approved, producers build, validation (script and checker), validation summary to the user, human review and approval.
