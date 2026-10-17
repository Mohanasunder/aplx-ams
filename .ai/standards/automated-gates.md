# Automated Gates

Run before any PR reaches a human. Failing tests, security scans, or secrets findings are **non-overridable**. The `standards-author` fills the exact commands in Phase 4 for the chosen stack. **Task 0** (`FEAT-000`, the walking skeleton) makes every command run green in CI and corrects any that do not work; after it merges, no gate may be left unset (`check_feature_size.py task0`). Until then builders must stop and raise an open question if a gate has no command.

| Gate | Command | Required |
| --- | --- | --- |
| Build | `docker compose build app && npm --prefix src/frontend ci && npm --prefix src/frontend run build` | yes |
| Run locally (app starts, health check answers) | `docker compose up -d && curl --fail http://localhost/api/health/` | yes |
| Lint (Python) | `ruff check src/ && ruff format --check src/` | yes |
| Lint (TypeScript) | `eslint src/frontend/src/ --max-warnings=0` | yes |
| Type check (Python) | `mypy src/ --strict` | yes |
| Type check (TypeScript) | `tsc --noEmit --project src/frontend/tsconfig.json` | yes |
| Unit + integration tests with coverage (Python, 80% gate) | `pytest src/ --cov=src --cov-fail-under=80 --timeout=600` | yes |
| Unit tests with coverage (TypeScript, 70% gate) | `vitest run --coverage --coverage.threshold.lines=70` | yes |
| E2E tests (separate CI job) | `playwright test` | yes |
| SAST | `bandit -r src/ -ll` | yes (non-overridable) |
| Dependency scan | `pip-audit` | yes (non-overridable) |
| Secrets scan | `detect-secrets scan` | yes (non-overridable) |
| Migration check (apply and reverse on a scratch DB) | `python manage.py migrate --run-syncdb` then `python manage.py migrate <app> zero` (finalized in FEAT-000) | yes |
| Locked tests unchanged | `python3 scripts/locked_tests.py check` | yes (non-overridable) |
| Feature size (Phase 5) | `python3 scripts/check_feature_size.py size` | yes (non-overridable) |
| Wave plan collision-free (Phase 5) | `python3 scripts/check_feature_size.py waves` | yes (non-overridable) |
| Files in scope (Phase 6) | `python3 scripts/check_feature_size.py scope` | yes |
| New packages approved (Phase 6) | `python3 scripts/check_feature_size.py packages` | yes (non-overridable) |
| Spec change records | `python3 scripts/spec_impact.py records` | yes (non-overridable) |
| Feature cites current approved specs (Phase 6) | `python3 scripts/spec_impact.py check` | yes (non-overridable) |
| Context pack resolves, within budget (Phase 5 and 6) | `python3 scripts/context_pack.py check` | yes (non-overridable) |
| Phase summary indexes the phase (at each phase gate) | `python3 scripts/context_pack.py summaries N` | yes |
| Learned rules index matches approved rules | `python3 scripts/learned_rules.py check` | yes (non-overridable) |
| Task 0 first; gates set after it merges | `python3 scripts/check_feature_size.py task0` | yes (non-overridable) |
| Spikes never merged; time boxes; branches deleted | `python3 scripts/spike.py check` | yes (non-overridable) |
| Change summary complete and accurate (Phase 6) | `python3 scripts/pr_summary.py check` | yes (non-overridable) |
| Decision log well-formed and append-only | `python3 scripts/log_decision.py check --base origin/main` | yes (non-overridable) |
| Agent charter matches its sources | `python3 scripts/build_charter.py check` | yes (non-overridable) |
| Domain terms used consistently | `python3 scripts/glossary_check.py check` (add `--code` once src/ exists) | yes (non-overridable) |
| Artifact validation | `python3 scripts/validate_artifact.py docs --check-links` | yes |
| Branch name | `scripts/check-branch-name.sh "$(git branch --show-current)"` | yes |
| IaC validate and policy check (Phase 8) | <set in Phase 8> | yes (non-overridable) |
| Go recorded before production deploy (Phase 8) | `python3 scripts/go_live.py check` | yes (non-overridable) |
| Feedback and incident log matches the Phase 9 artifacts | `python3 scripts/feedback_log.py check` | yes |
| Every incident and feedback item triaged; every improvement item decided (Phase 9 gate) | `python3 scripts/feedback_log.py check --gate` | yes |

