---
id: VAL-024
title: Phase 5 Build Planning — Validation Report Run 3
phase: 5
version: 0.1
template: validation-report
template_version: 2.0
status: Draft
author_agent: checker
approver: Tech lead
date: 2026-10-18
validation: Pass
---
> **One file per validation run per phase.** Each phase validation run produces one `phase-N-run-M.md` in `docs/validation/`. Use `--out docs/validation/phase-N-run-M.md` when calling `new_artifact.py`; never auto-name as `VAL-NNN.md`. M increments with each re-run of the same phase.

# Phase 5 Build Planning — Validation Report Run 3

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- FBD-001 v0.1 — APLX AMS: Feature Breakdown (Approved 2026-10-17)
- DOD-001 v0.1 — APLX AMS: Definition of Done (Approved 2026-10-17)
- WAV-001 v0.1 — APLX AMS: Build Wave Plan (Approved 2026-10-17)
- ENV-001 v0.1 — APLX AMS: Environment Plan (Approved 2026-10-17)
- FEAT-000 through FEAT-035 plan.md — all 36 feature plans (Approved 2026-10-17)
- FEAT-000 through FEAT-035 acceptance.md — 36 acceptance criteria files (status: In review)
- FEAT-000 through FEAT-035 tasks.md — 36 task checklists (status: In review)
- FEAT-000 through FEAT-035 status.md — 36 feature status files (status: In review)
- VAL-022 (Run 1 report) and VAL-023 (Run 2 report) — prior validation reports
- .ai/checker-rules/phase-5.md — Phase 5 checker rules
- .ai/standards/checker-and-fail-decision.md — validation layers and verdict rules

## Purpose And Scope
This is validation run 3 of Phase 5 (Build Planning) for APLX AMS, expanded at human request to cover the supplementary per-feature files out of scope in runs 1 and 2:
- acceptance.md (36 files, FEAT-000 through FEAT-035)
- tasks.md (36 files, FEAT-000 through FEAT-035)
- status.md (36 files, FEAT-000 through FEAT-035)

Also re-checks the 4 Minor findings left open at run 2 close (N-F1 through N-F4). Does not re-validate items confirmed Pass in run 2 (plan.md files, FBD-001, DOD-001, WAV-001, ENV-001) unless a change signal exists.

## Verdict
**FAIL** — 0 Blockers, 1 Major, 2 Minors.

Automated gate checks all pass:
- `python scripts/check_feature_size.py size` → PASS — 36 features, 0 violations
- `python scripts/check_feature_size.py task0` → PASS — 36 features, 0 problems
- `python scripts/check_feature_size.py waves` → PASS — 28 waves, 36 features, 0 problems

## Scorecard

| Layer | Result | Notes |
|---|---|---|
| Structural | Pass | All 108 sub-files conform to templates (feature-acceptance v1.1, feature-tasks v1.0, feature-status v1.1). Required sections present and populated. Metadata complete. No unfilled placeholders. |
| Input conformance | Pass | All inputs cited at Approved versions. No Phase 6 content. All Open design decisions say "None." No production configuration paths. |
| Completeness | Pass | All 36 features have all 3 supplementary files. Acceptance criteria in acceptance.md match plan.md Test Plan entries (verified for FEAT-000, FEAT-001, FEAT-011, FEAT-019, FEAT-035). Tasks mirror plan.md Implementation Steps. Status files correctly reflect "Not started." |
| Consistency | Pass | Enabling features cite STD/TST IDs; story features cite REQ IDs. No contradictions across sampled files. |
| Traceability | **Fail** | R3-F1 (Major): Compound IDs FEAT-NNN-ACC, FEAT-NNN-TASKS, FEAT-NNN-STATUS don't resolve — actual files carry `id: FEAT-NNN` (no compound suffix). R3-F2 (Minor): FEAT-NNN-TESTS are expected Phase 6 forward references, correctly labeled. |
| Content quality | Pass | All acceptance criteria testable Given/When/Then. Tasks name specific files. Status files use controlled vocabulary. No vague language. |
| Automated gates | Pass | All three check_feature_size.py gates pass. |
| Producer self-check | Partially fail | Quality checklists marked [x] for traceability, but R3-F1 shows downstream compound ID links don't resolve. |

| Severity | Run 2 open | Resolved | Newly found | Still open |
|---|---|---|---|---|
| Blocker | 0 | 0 | 0 | 0 |
| Major | 0 | 0 | 1 | 1 |
| Minor | 4 | 4 | 2 | 2 |
| **Total** | **4** | **4** | **3** | **3** |

## Findings

### R3-F1 (Major) — Compound ID mismatch in all 108 supplementary sub-files

**Severity:** Major
**Files:** acceptance.md (Downstream) for all 36 features; tasks.md (Downstream) for all 36 features; status.md (Upstream) for all 36 features; plan.md (Downstream) for FEAT-001 through FEAT-035

Compound IDs FEAT-NNN-ACC, FEAT-NNN-TASKS, and FEAT-NNN-STATUS appear in Traceability Links sections as cross-references but no artifact in the registry has these IDs. The actual sub-files carry `id: FEAT-NNN` (no compound suffix). DOD-001 uses the compound suffix convention, confirming it is the intended naming — but it was never applied to the sub-files' `id:` fields.

**Suggested fix (Option A — recommended):** Update the `id:` field in every acceptance.md to `FEAT-NNN-ACC`, every tasks.md to `FEAT-NNN-TASKS`, and every status.md to `FEAT-NNN-STATUS`. Apply to all 36 features (108 files total). No content changes needed — only `id:` field values.

**Suggested fix (Option B):** Replace compound suffix references in all Traceability Links sections with file-qualified references (e.g., "FEAT-NNN tasks.md (builder task list)"). Tech lead decides.

---

### R3-F2 (Minor) — Phase 6 forward references to FEAT-NNN-TESTS

**Severity:** Minor (downgraded from Major; see note)
**Files:** acceptance.md (Downstream) and tasks.md (Downstream) for all 36 features

References to "Phase 6 test set FEAT-NNN-TESTS" are forward references to artifacts that don't yet exist. validate_artifact.py --check-links flags these as broken links; checker downgrades to Minor because (a) Phase 6 test sets cannot exist at the Phase 5 gate by definition, (b) references are correctly labeled "Phase 6 test set" making the forward nature explicit, and (c) phase-5.md checker rules require test sets only in Phase 6.

**Suggested fix:** No action required in Phase 5. Record as accepted forward reference if proceeding.

---

### R3-F3 (Minor) — FEAT-001 tasks.md T-12 and T-13 redundant and omit frontend gates

**Severity:** Minor
**File:** docs/05-build-plan/feature-001-frontend-scaffold/tasks.md

T-12 ("Run all gate commands locally; confirm each exits 0") is vague and redundant with T-13 ("Run all gate commands locally (ruff, mypy, pytest --cov, bandit, pip-audit, detect-secrets); confirm each exits 0"). Neither explicitly calls out the frontend gate commands introduced by FEAT-001 (eslint, tsc --noEmit, vitest coverage).

**Suggested fix:** Replace T-12 with "Run frontend gate commands: `npx eslint src/frontend/src/`, `npx tsc --noEmit`, `npm run test -- --run --coverage`; assert each exits 0." Retitle T-13 "Run backend gate commands: ruff, mypy, pytest --cov, bandit, pip-audit, detect-secrets; assert each exits 0."

---

## Top Issues

1. **R3-F1 (Major):** All 108 sub-files reference companion artifacts using compound suffix IDs that don't exist in the registry. The fix is mechanical (update `id:` fields) and low-risk; no content changes needed.
2. **R3-F2 (Minor):** 72 FEAT-NNN-TESTS forward references are expected and correctly labeled. No Phase 5 action required.
3. **R3-F3 (Minor):** FEAT-001 tasks.md omits explicit frontend gate verification steps; low risk given the acceptance criteria cover gate outcomes.

## Unresolved From Earlier Runs

| Finding | Run | Prior status | Current status |
|---|---|---|---|
| N-F1: DOD-001 said "FEAT-000 through FEAT-034" | Run 2 (VAL-023) | Open Minor | **Resolved** — now reads "FEAT-000 through FEAT-035" |
| N-F2: WAV-001 Input References said "35 features FEAT-000 to FEAT-034" | Run 2 (VAL-023) | Open Minor | **Resolved** — now reads "36 features FEAT-000 to FEAT-035" |
| N-F3: FEAT-001 plan.md Test Plan missing "See acceptance.md" pointer | Run 2 (VAL-023) | Open Minor | **Resolved** — pointer now appended |
| N-F4: FEAT-000 plan.md Traceability Downstream excluded FEAT-035 | Run 2 (VAL-023) | Open Minor | **Resolved** — now reads "FEAT-001 through FEAT-035" |

All 4 run 2 Minors fully resolved. No prior findings remain open.

## Recommendation

**Send back (Option A).** Fix R3-F1 before proceeding to human review.

R3-F1 is a genuine traceability failure affecting all 108 supplementary sub-files. The fix is clear, mechanical, and non-destructive: update the `id:` fields in all acceptance.md/tasks.md/status.md files to include the compound suffix, aligning with the convention already used in DOD-001 and all cross-references throughout the plan.

If the tech lead chooses to proceed to human review (Option B): the physical files exist, are correctly located, and contain correct content. The compound ID gap is a naming convention inconsistency only — a builder locating files by folder path in Phase 6 is not affected. R3-F1 is not a non-overridable finding. If proceeding, the tech lead must record a reason in docs/logs/fail-decisions-log.md.

**Loop limit note:** loop_limit_failed_validations = 3. Run 1 was a Fail (counted). Runs 2 and 3 are distinct scopes — run 2 passed with warnings; run 3 is a human-requested scope expansion. Failed-validation loop count stands at 1. Loop limit not in play.

## Decision Record

| Field | Value |
|---|---|
| Decision | Pending — tech lead (Mohanasunder) decides |
| Decided by | Pending |
| Timestamp | Pending |
| Reason | Pending |

## Assumptions

None.

## Open Questions

None.

## Traceability Links
- Upstream: VAL-022 (Run 1); VAL-023 (Run 2); FBD-001 v0.1; DOD-001 v0.1; WAV-001 v0.1; ENV-001 v0.1; FEAT-000–FEAT-035 plan.md; FEAT-000–FEAT-035 acceptance.md / tasks.md / status.md; .ai/checker-rules/phase-5.md; .ai/standards/checker-and-fail-decision.md
- Downstream: Human review of Phase 5 supplementary artifacts; approval decision for FEAT-000–FEAT-035 sub-files

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
| Decision | Pending |
| Approver | Pending |
| Role | Pending |
| Conditions | None |
| Comments | None |
| Timestamp | Pending |
