---
id: SCR-002
title: FEAT-005: add settings/base.py to plan file scope
phase: 0
version: 0.1
template: spec-change
template_version: 2.0
status: Draft
author_agent: build-planner
approver: Approver of the changed artifact's phase
date: 2026-10-18
validation: Pending
---
# Spec Changes

<!-- Collection file. All spec change records are appended as `## SCR S-N: [title]` sections (S-1, S-2, …). Never create a separate file per spec change. Sub-IDs are consecutive and never reused. Cite a specific record as `SCR S-N`. Per-record status stored as HTML comments within each section. Approve each section individually with `/approve docs/logs/spec-changes.md --sub-id S-N`. -->

## SCR S-1: Add settings/base.py to FEAT-005 plan.md file scope

<!-- scr_status: Draft -->
<!-- scr_date: 2026-10-18 -->
<!-- scr_approver: -->

### Input References
- FEAT-005 plan.md v0.1 (Approved 2026-10-17, Mohanasunder) — artifact being amended
- VAL-027 (Draft, 2026-10-18) — validation report identifying F-002 (Minor)

### Purpose And Scope
Adds `src/aplx_ams_django/settings/base.py` to FEAT-005 plan.md § Files To Create Or Modify. Covers only the plan.md file list amendment and Size Check table update. No requirements, contracts, or architecture artifacts change.

### Changed Artifact
FEAT-005 plan.md v0.1 → v0.2; `docs/05-build-plan/feature-005-user-accounts/plan.md`

### Trigger
VAL-027 F-002 (Minor) — checker subagent during Mode A validation run on 2026-10-18. `settings/base.py` was modified in commit `6248aa5` (database-builder test commit, Mode A) but was not listed in plan.md § Files To Create Or Modify. The Mode B scope gate (`check_feature_size.py scope`) would fail when `settings/base.py` is re-modified during implementation unless the plan is updated.

### Change
**§ Files To Create Or Modify** — add one entry:

Before (10 files):
```
- `src/aplx_ams_django/accounts/models.py`
- `src/aplx_ams_django/accounts/migrations/0001_initial.py`
- `src/aplx_ams_django/accounts/serializers.py`
- `src/aplx_ams_django/accounts/services.py`
- `src/aplx_ams_django/accounts/dal.py`
- `src/aplx_ams_django/accounts/views.py`
- `src/aplx_ams_django/accounts/urls.py`
- `src/aplx_ams_django/urls.py`
- `src/frontend/src/pages/UserManagement.tsx`
- `src/frontend/src/api/users.ts`
```

After (11 files) — `settings/base.py` added after `urls.py`:
```
- `src/aplx_ams_django/accounts/models.py`
- `src/aplx_ams_django/accounts/migrations/0001_initial.py`
- `src/aplx_ams_django/accounts/serializers.py`
- `src/aplx_ams_django/accounts/services.py`
- `src/aplx_ams_django/accounts/dal.py`
- `src/aplx_ams_django/accounts/views.py`
- `src/aplx_ams_django/accounts/urls.py`
- `src/aplx_ams_django/urls.py`
- `src/aplx_ams_django/settings/base.py`
- `src/frontend/src/pages/UserManagement.tsx`
- `src/frontend/src/api/users.ts`
```

**§ Size Check** table row — source file count:

Before: `| Source files (non-test) | 10 | 10 |`
After: `| Source files (non-test) | 11 | 30 |`

(The feature-level limit is `max_source_files_per_feature: 30` from project.md; 11 is within limit.)

### Reason
`settings/base.py` must be modified to register `aplx_ams_django.accounts` in `INSTALLED_APPS` and set `AUTH_USER_MODEL = "accounts.User"`. Without these entries Django cannot discover the model, run migrations, or resolve the `AUTH_USER_MODEL` reference. This is a mandatory Django convention for any custom user model. The modification was an oversight in the Phase 5 plan: the plan described creating the accounts app but did not enumerate the settings file that must be updated to activate it.

### Decision Record
Not applicable — no architecture or contract artifact changes. FEAT-005 plan.md is a build plan (template `feature-plan`), not an architecture-overview, adr, api-spec, database-design, deployment-topology, or threat-model artifact.

### Impact
| Artifact / Feature | State | Action |
|---|---|---|
| FEAT-005 plan.md v0.1 | Approved | Revise to v0.2; re-approve (this SCR's direct output) |
| FEAT-005-STATUS v0.1 | Approved | No change — references plan.md by ID, not by file list |
| FEAT-005-TESTS v0.1 | Draft | No change — test files unchanged; plan scope amendment only |
| FEAT-005 branch scope gate | In progress | Will pass once plan.md v0.2 is Approved and scope re-run |

### Work Stopped
None — `settings/base.py` modification was already committed in Mode A (`6248aa5`); Mode A test-fix work continues in parallel. Mode B cannot start until FEAT-005-TESTS is Approved (the separate test approval gate); this SCR unblocks the Mode B scope gate, not the test approval gate.

### Resume Criteria
1. This SCR (SCR-002, SCR S-1) Approved by Mohanasunder (tech lead).
2. FEAT-005 plan.md v0.2 Approved by Mohanasunder (tech lead).
3. FEAT-005-TESTS Approved (Mode A completion gate, separate process).

### Assumptions
None.

### Open Questions
None.

### Traceability Links
- Upstream: FEAT-005 plan.md v0.1; VAL-027 (F-002 finding)
- Downstream: FEAT-005 plan.md v0.2; FEAT-005-TESTS (scope gate unblocked for Mode B)

### Quality Checklist
- [x] Every section is filled, or marked "Not applicable - <reason>"
- [x] Inputs referenced are Approved artifacts at the stated versions
- [x] Nothing invented: no requirements, systems, users, endpoints, or libraries without a source
- [x] Assumptions and open questions are logged and linked
- [x] Traceability links are present upstream and downstream
- [x] Terminology follows .ai/standards/glossary.md
- [x] Vague words removed (etc., as needed, appropriate)
- [x] Every changed artifact is listed as 'ID vOLD -> vNEW'
- [x] An architecture or contract change cites its new or superseding ADR A-N under Decision Record (Not applicable)
- [x] Impact covers every artifact and feature that cites the changed artifact
