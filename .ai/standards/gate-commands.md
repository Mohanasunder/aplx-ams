# Gate Commands

Exact CI commands for every automated gate. Set in Phase 4 by `standards-author` (STD-001 v0.1).
Every builder and the `ai-code-reviewer` loads this file. Every command must exit 0 for a PR to be mergeable.
Task 0 (`FEAT-000`) makes all commands run green in CI; after it merges, no gate may remain unset.

## Lint and format

```
ruff check src/
ruff format --check src/
eslint src/frontend/src/ --max-warnings=0
```

## Type check

```
mypy src/ --strict
tsc --noEmit --project src/frontend/tsconfig.json
```

## Unit and integration tests with coverage

```
# Backend — 80% line coverage gate; 10-minute timeout
pytest src/ --cov=src --cov-fail-under=80 --timeout=600

# Frontend — 70% line coverage gate
vitest run --coverage --coverage.threshold.lines=70
```

## End-to-end tests (separate CI job)

```
playwright test
```

## SAST (non-overridable)

```
bandit -r src/ -ll
```

## Dependency vulnerability scan (non-overridable)

```
pip-audit
```

## Secret scan (non-overridable)

```
detect-secrets scan
```

## Migration check

```
# Finalized in FEAT-000 once database container and credentials are configured.
# Provisional:
python manage.py migrate --run-syncdb
python manage.py migrate <app> zero
```

## Build

```
docker compose build app
npm --prefix src/frontend ci
npm --prefix src/frontend run build
```

## Health check (local)

```
docker compose up -d
curl --fail http://localhost/api/health/
```

## SDLC process gates (always run)

```
python3 scripts/locked_tests.py check
python3 scripts/check_feature_size.py size
python3 scripts/check_feature_size.py waves
python3 scripts/check_feature_size.py scope
python3 scripts/check_feature_size.py packages
python3 scripts/spec_impact.py records
python3 scripts/spec_impact.py check
python3 scripts/context_pack.py check
python3 scripts/learned_rules.py check
python3 scripts/check_feature_size.py task0
python3 scripts/spike.py check
python3 scripts/pr_summary.py check
python3 scripts/log_decision.py check --base origin/main
python3 scripts/build_charter.py check
python3 scripts/glossary_check.py check
python3 scripts/validate_artifact.py docs --check-links
scripts/check-branch-name.sh "$(git branch --show-current)"
```

## Coverage thresholds

| Layer | Type | Threshold | Command |
| --- | --- | --- | --- |
| Backend Python | Line | 80% | `pytest --cov-fail-under=80` |
| Frontend TypeScript | Line | 70% | `vitest --coverage.threshold.lines=70` |

Thresholds set by DEC-045 (Mohanasunder, 2026-10-17). A change requires a new human decision in `docs/logs/decision-log.md`.
