# Review Feedback Log

Every Phase 6 review finding that leads to a change, appended by the Orchestrator: human PR comments (request changes or reject), and Major or Blocker findings from the AI pre-review and the checker. `python3 scripts/learned_rules.py recurring` counts categories across features; a category seen in `learned_rule_threshold` features (project.md) becomes a learned rule proposal.

Category: kebab-case slug; reuse an existing one when it fits (see `.ai/standards/review-and-approval.md`).

| Date | Feature | Source | Category | Severity | Issue | Reviewer |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-10-18 | FEAT-000 | ai-code-reviewer | missing-wsgi-module | Major | `src/aplx_ams_django/wsgi.py` is absent; Dockerfile CMD `gunicorn aplx_ams_django.wsgi:application` will raise ModuleNotFoundError at container start — application cannot run despite docker build passing | ai-code-reviewer |
| 2026-10-18 | FEAT-000 | ai-code-reviewer | production-allowed-hosts-wildcard | Major | `ALLOWED_HOSTS = ["*"]` from base.py not overridden in production.py; with DEBUG=False Django accepts any Host header, enabling host header injection — requires human decision on FEAT-000 vs FEAT-001 scope | ai-code-reviewer |
| 2026-10-18 | FEAT-000 | security-scanner | insecure-default | Medium | `ALLOWED_HOSTS: ["*"]` in `src/aplx_ams_django/settings/base.py` line 23 is not overridden in `settings/production.py`; all Host headers accepted in production | security-scanner |
| 2026-10-18 | FEAT-000 | security-scanner | insecure-default | Medium | `SECRET_KEY` falls back to literal string `"insecure-dev-key-replace-in-production"` in `src/aplx_ams_django/settings/base.py` line 19 when no secret file or env var is present; should raise `ImproperlyConfigured` | security-scanner |
