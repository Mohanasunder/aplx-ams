---
id: DOD-001
title: APLX AMS: Definition of Done
phase: 5
version: 0.1
template: definition-of-done
template_version: 1.0
status: Approved
author_agent: build-planner
approver: Mohanasunder
default_approver: Tech lead
default_folder: docs/05-build-plan
date: 2026-10-17
validation: Pass
---
# APLX AMS: Definition of Done

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- STD-001 v0.1 — APLX AMS: Coding Standards (Approved 2026-10-17) § Automated Gate Commands, § Security Rules
- TST-001 v0.1 — APLX AMS: Test Strategy (Approved 2026-10-17) § Test Levels
- .ai/standards/automated-gates.md — full gate command list
- CLAUDE.md — non-negotiable SDLC rules (Rule 3: tests before code; Rule 6: decisions recorded)

## Purpose And Scope
Applies to every feature branch (FEAT-000 through FEAT-035) in Phase 6. The builder checks all items before requesting human review. The AI reviewer confirms all items before recommending merge. The human reviewer confirms before approving the PR. Items marked "(CI-enforced)" are checked automatically by GitHub Actions; the PR cannot be merged if they fail.

Does not cover: deployment readiness (Phase 8) or system testing criteria (Phase 7).

## Checklist

### Code and Tests
- [ ] All acceptance criteria in the feature's `FEAT-NNN-ACC` are implemented and pass.
- [ ] Tests are written for every acceptance criterion BEFORE implementation code (Rule 3).
- [ ] Test coverage gate passes: `pytest src/ --cov=src --cov-fail-under=80` exits 0 for backend; `npm run test -- --run --coverage` with ≥70% for frontend (DEC-045). (CI-enforced)
- [ ] All tests run within the `Expected test runtime` stated in the feature's plan.md.
- [ ] No test that was approved in `FEAT-NNN-TESTS` has been modified; `python3 scripts/locked_tests.py check` exits 0. (CI-enforced)

### Code Quality
- [ ] `ruff check src/ && ruff format --check src/` exit 0. (CI-enforced)
- [ ] `mypy src/ --strict` exits 0. (CI-enforced)
- [ ] `npx eslint src/frontend/src/ && npx tsc --noEmit` exit 0. (CI-enforced)
- [ ] No unfilled template placeholders (`<fill:`) or unresolved code markers remain in any file on the branch.

### Security
- [ ] `bandit -r src/ -ll` exits 0 with no high-severity findings. (CI-enforced)
- [ ] `pip-audit` exits 0 with no known vulnerable dependencies. (CI-enforced)
- [ ] `detect-secrets scan` exits 0; no new secrets detected. (CI-enforced)
- [ ] No secret value committed; no production configuration path touched (STD-001 § Production Configuration paths).
- [ ] No password, token, or key written to any log, audit entry, or database field.

### Scope and Plan Compliance
- [ ] Only files listed in the feature's `plan.md` Files To Create Or Modify section are changed; `python3 scripts/check_feature_size.py scope FEAT-NNN` exits 0. (CI-enforced)
- [ ] Only packages listed in the feature's `plan.md` New Packages section are added or upgraded; `python3 scripts/check_feature_size.py packages FEAT-NNN` exits 0. (CI-enforced)
- [ ] `python3 scripts/check_feature_size.py size FEAT-NNN` exits 0.
- [ ] No endpoint, model, or UI element outside the feature's scope is added.

### Build and Docker
- [ ] `docker compose build app` exits 0 on a clean environment. (CI-enforced)
- [ ] `python manage.py migrate --run-syncdb` then reverse to zero (exact command finalized in FEAT-000) exits 0. (CI-enforced)

### Traceability
- [ ] The PR description includes the FEAT-ID, a reference to `FEAT-NNN-ACC`, and states the Risk Tier.
- [ ] Acceptance criteria ID labels (e.g. `REQ-018 AC-1`) appear in test function names or docstrings.
- [ ] Any assumption made during build is logged in `docs/logs/assumptions-log.md` with an A-NNN label.
- [ ] Any open question raised during build is logged in `docs/logs/open-questions-log.md` with an OQ-NNN label before the PR is opened.

### Review
- [ ] AI code review (`ai-code-reviewer` agent) has reviewed the PR and its report is saved.
- [ ] AI security scan (`security-scanner` agent) has reviewed the PR and its report is saved.
- [ ] No Major or Critical finding from the AI reviewer is unresolved.
- [ ] Human developer reviewer has approved the PR via `/approve`.
- [ ] For High or Critical tier features: tech lead has reviewed the risk sections before merge.

## Assumptions
None beyond those logged in docs/logs/assumptions-log.md.

## Open Questions
None.

## Traceability Links
- Upstream: PIB-005 v0.1; STD-001 v0.1; TST-001 v0.1; CLAUDE.md; .ai/standards/automated-gates.md
- Downstream: All FEAT-000 through FEAT-035 plan.md files (each references this document under Definition Of Done)

## Quality Checklist
- [x] Every template section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)

## Approval Record
| Field | Value |
| --- | --- |
| Decision | Approve |
| Approver | Mohanasunder |
| Role | Architect / tech lead |
| Version | 0.1 |
| Conditions | None |
| Comments | Phase 5 validation passed (VAL-023). |
| Timestamp | 2026-10-17 16:50 UTC |
