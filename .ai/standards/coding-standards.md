# Coding Standards

Defaults apply until Phase 4 fills the project-specific sections (the `standards-author` agent does this; humans approve).

## Defaults for all code

- Follow the approved API contract (`docs/04-design/openapi.yaml`) and database design exactly; do not change a contract in a feature branch: raise an open question.
- Small functions, explicit names, no dead code, no commented-out code.
- Validate all external input; enforce authorization on every endpoint per the permission matrix.
- Add or upgrade a package only if the feature plan's New Packages section names it at that exact version. If the feature needs one the plan does not name, stop and write a blocker; never add it anyway.
- Never hardcode secrets; read from environment/secret manager references.
- Errors use the shared error model; log without personal data or secrets.
- Every acceptance criterion has at least one automated test; tests assert behavior.
- Migrations: one per change, reversible, never edited after merge.
- Commits: small, `FEAT-NNN: message`.

## Shared Paths

Files that many features depend on. A feature whose plan lists a matching file runs alone: it is alone in its wave (`python3 scripts/check_feature_size.py waves`) and its branch is created only while no other feature is In progress, In review, or Blocked (`check_feature_size.py start`, run by `create-feature-branch.sh`). One bullet per glob, the glob in backticks first on the line; `*` also matches `/`, and a leading `**/` also matches at the repository root. The `standards-author` adds the project's own shared modules in Phase 4 (for example auth middleware, the shared error model, the route registry, shared UI components).

- `docs/04-design/*` (contracts: OpenAPI spec, schema)
- `**/migrations/*` (data model)
- `**/package.json`
- `**/package-lock.json`
- `**/yarn.lock`
- `**/pnpm-lock.yaml`
- `**/requirements*.txt`
- `**/pyproject.toml`
- `**/poetry.lock`
- `.github/*` (CI)
- `CLAUDE.md`
- `.ai/*` (standards and the charter's sources)

## Production Configuration

Files that hold production environment settings. Builders never read or change them, and no feature plan may list one (`python3 scripts/check_feature_size.py size` fails). Only the `devops-engineer` drafts them, in Phase 8, with secret references only; the tech lead and the release manager review every change (Critical tier) and a human applies it. Same glob rules as Shared Paths. The `standards-author` replaces these defaults in Phase 4 with the project's real paths.

- `**/*.prod.*`
- `**/*.production.*`
- `**/*prod*.tfvars`
- `**/environments/prod/*`
- `**/environments/production/*`
- `**/overlays/prod/*` (Kubernetes)
- `**/config/production*`
- `.env.production*`

## Project-specific (filled in Phase 4)

| Item | Value |
| --- | --- |
| Backend language and framework | Python 3.13 + Django 5.2 LTS + DRF 3.x (Gunicorn WSGI server) |
| Frontend language and framework | React 18.x + TypeScript 5.x + Vite 5.x + MUI v6 |
| Database | PostgreSQL 18 |
| Folder layout | `src/aplx_ams_django/` (project), `src/<app>/` (accounts, organizations, tickets, sla, effort, reports, audit), `src/frontend/src/` (React) |
| Naming conventions | Python: snake_case modules/funcs/vars, PascalCase classes, UPPER_SNAKE_CASE constants; TypeScript: PascalCase components, camelCase funcs/vars, UPPER_SNAKE_CASE constants |
| Coverage targets | Backend Python: 80% line coverage; frontend TypeScript: 70% line coverage |
| Logging format | `%(asctime)s %(levelname)s %(name)s %(message)s` UTC; never log secrets or passwords |
