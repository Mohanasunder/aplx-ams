---
id: VAL-022
title: Phase 5 Build Planning — Validation Report Run 1
phase: 5
version: 0.1
template: validation-report
template_version: 2.0
status: Draft
author_agent: checker
approver: Tech lead
date: 2026-10-17
validation: Fail
---
> **One file per validation run per phase.** Each phase validation run produces one `phase-N-run-M.md` in `docs/validation/`. Use `--out docs/validation/phase-N-run-M.md` when calling `new_artifact.py`; never auto-name as `VAL-NNN.md`. M increments with each re-run of the same phase.

# Phase 5 Build Planning — Validation Report Run 1

## Input References
- PIB-005 v0.1 — Phase 5 Build Planning Input Brief (Approved 2026-10-17)
- FBD-001 v0.1 — APLX AMS: Feature Breakdown (In review 2026-10-17)
- DOD-001 v0.1 — Definition of Done (In review 2026-10-17)
- WAV-001 v0.1 — Wave Plan (In review 2026-10-17)
- ENV-001 v0.1 — Environment Plan (In review 2026-10-17)
- FEAT-000 through FEAT-034 plan.md (35 files, all In review 2026-10-17)
- REQ-001 v0.3, API-001 v0.1, DBD-001 v0.1, STD-001 v0.1, BED-001 v0.1, UIS-001 v0.1, PRM-001 v0.1, TST-001 v0.1 (all Approved 2026-10-17)
- .ai/checker-rules/phase-5.md
- .ai/standards/checker-and-fail-decision.md

## Purpose And Scope
Verify all Phase 5 Build Planning deliverables against the checker rules. Covers FBD-001, DOD-001, WAV-001, ENV-001, and all 35 feature plan.md files. Does not cover Phase 6 code or tests. This report does not fix any artifact; it records findings for producer action or human override.

## Verdict
**FAIL** — 0 Blockers, 1 Major, 8 Minors.

Deterministic pre-run scripts all pass:
- `check_feature_size.py size` → 35 features, 0 violations
- `check_feature_size.py task0` → 35 features, 0 problems
- `check_feature_size.py waves` → 27 waves, 35 features, 0 problems
- `context_pack.py check FEAT-NNN` (all 35) → 0 problems each

## Scorecard

| Layer | Result | Notes |
|---|---|---|
| Structural | Pass | All artifacts have required sections, complete metadata, valid IDs, and controlled values. |
| Input conformance | Pass with warnings | PIB-005 Approved; all Phase 1–4 upstream Approved. WAV-001 cites FBD-001 as "In review" (F-03). |
| Completeness | Fail | e2e.yml listed in ENV-001 is owned by no feature plan (F-01 — Major). |
| Consistency | Pass with warnings | Wave 24 Alone description mismatches FEAT-007 plan (F-04); FBD-001 AC count wrong by 1 (F-02); FEAT-000 TST-001 numbering inconsistency (F-06); DOD-001 vs ENV-001 migration command mismatch (F-09). |
| Traceability | Pass | S-1 to S-33 each in exactly one feature; dependency graph verified; OQ-067 logged. |
| Content quality | Pass with warnings | Test Plan entries truncated across feature plans (F-07); FEAT-001 Objective has boilerplate (F-05); .secrets.baseline absent from FEAT-000 file list (F-08). |
| Producer self-check | Pass | Three quality checklist spot-checks pass. |

| Severity | Count |
|---|---|
| Blocker | 0 |
| Major | 1 |
| Minor | 8 |
| **Total** | **9** |

## Findings

### F-01 (Major) — e2e.yml and playwright.config.ts assigned to no feature

**Severity:** Major
**Files:** ENV-001 v0.1 § GitHub Actions workflow structure; FEAT-000 through FEAT-034 plan.md § Files To Create Or Modify

ENV-001 explicitly states `.github/workflows/e2e.yml` should be created in FEAT-000: "e2e.yml — Playwright E2E job (separate, runs after ci.yml)." No feature plan lists `.github/workflows/e2e.yml` or `playwright.config.ts` in its Files To Create Or Modify section. FEAT-001 installs the `playwright` npm package but creates neither. Any Phase 6 builder who creates these files will trigger a CI-enforced scope check failure.

**Suggested fix:** Add `.github/workflows/e2e.yml` and `playwright.config.ts` to an eligible feature's file list. FEAT-000 and FEAT-001 are both at the 10-source-file limit; options are: (a) confirm these are configuration files not counted toward the source-file limit and add to FEAT-001 (already alone in Wave 2), or (b) create a new small Enabling feature for E2E CI scaffolding, alone in its wave (`.github/*` is a Shared Path).

---

### F-02 (Minor) — FBD-001 AC total off by 1

**Severity:** Minor
**File:** FBD-001 v0.1 § Feature List "Totals" line

Stated total is 140 AC. Correct count: FEAT-000 (4) + FEAT-001 (4) + FEAT-002 (3) + FEAT-003 to FEAT-034 (32 × 4 = 128) = **139**. The formula also evaluates to 139.

**Suggested fix:** Change "140" to "139" in the Totals line and correct the formula result.

---

### F-03 (Minor) — WAV-001 cites FBD-001 as "In review"

**Severity:** Minor
**File:** WAV-001 v0.1 § Input References

WAV-001 cites FBD-001 v0.1 as "In review" — an in-phase co-produced dependency. The label is accurate but unexplained.

**Suggested fix:** Add a note: "FBD-001 v0.1 (in-phase co-produced artifact; consumed as In review — approved at the Phase 5 gate)."

---

### F-04 (Minor) — WAV-001 Wave 24 Alone description uses stale migration number; OQ-067 still listed as open

**Severity:** Minor
**Files:** WAV-001 v0.1 § Waves Wave 24; FEAT-007/plan.md § Files To Create Or Modify; docs/logs/open-questions-log.md

WAV-001 Wave 24 states: "Alone: `audit/migrations/0002_roles_and_rls.py` matches Shared Paths." FEAT-007/plan.md lists `src/aplx_ams_django/audit/migrations/0003_roles_and_rls.py`. OQ-067 remains listed as open despite being resolved in FEAT-007/plan.md.

**Suggested fix:** Update WAV-001 Wave 24 Alone description to `0003_roles_and_rls.py`. Mark OQ-067 Answered in docs/logs/open-questions-log.md citing FEAT-007/plan.md v0.1 (DEC-048).

---

### F-05 (Minor) — FEAT-001 Objective carries story-feature boilerplate

**Severity:** Minor
**File:** FEAT-001/plan.md § Objective

Objective reads "Deliver all 4 acceptance criteria of this Enabling feature end-to-end: backend models, migrations, serializers, services, DAL, views, URLs, and frontend pages." FEAT-001 delivers a React 18 scaffold and Nginx container — not backend models or migrations.

**Suggested fix:** Replace with a specific Enabling-feature objective describing the React 18 + TypeScript + Vite + MUI v6 frontend scaffold and frontend CI gates.

---

### F-06 (Minor) — FBD-001 FEAT-000 Criteria Covered inconsistent with FEAT-000 plan Test Plan

**Severity:** Minor
**Files:** FBD-001 v0.1 § FEAT-000 row Criteria Covered; FEAT-000/plan.md § Test Plan

FBD-001 cites "STD-001 AC-1..4; TST-001 AC-1..2" (implies 6 items) vs AC Count 4. FEAT-000/plan.md references TST-001 AC-3, not AC-1 or AC-2.

**Suggested fix:** Align FBD-001 FEAT-000 Criteria Covered with the 4 actual test items in the plan. Verify TST-001 AC numbering is consistent.

---

### F-07 (Minor) — Test Plan entries truncated in feature plans

**Severity:** Minor
**Files:** FEAT-001, FEAT-002, FEAT-007, FEAT-011 (and likely all 33 story feature plans) § Test Plan

Test Plan entries are truncated mid-sentence. A builder cannot determine the full Given/When/Then from the plan.

**Suggested fix:** Provide complete acceptance criterion text in each Test Plan entry verbatim from REQ-001, or confirm that the feature's acceptance.md carries the full text and direct builders there explicitly.

---

### F-08 (Minor) — .secrets.baseline absent from FEAT-000 Files To Create Or Modify

**Severity:** Minor
**File:** FEAT-000/plan.md § Files To Create Or Modify; FEAT-000/plan.md § Risks

FEAT-000 § Risks and tasks.md T-10 require creating `.secrets.baseline` with `detect-secrets scan`, but this file is absent from Files To Create Or Modify. Phase 6 scope check (`check_feature_size.py scope FEAT-000`) blocks creation of unlisted files.

**Suggested fix:** Add `.secrets.baseline` to FEAT-000 § Files To Create Or Modify; if dotfiles are excluded from scope checks, document that in the plan.

---

### F-09 (Minor) — Migration check command differs between DOD-001 and ENV-001

**Severity:** Minor
**Files:** DOD-001 v0.1 § Build and Docker; ENV-001 v0.1 § CI Skeleton Gate 13

DOD-001 migration check uses `--fake organizations` flag. ENV-001 Gate 13 uses `--run-syncdb` with a different app placeholder. Both documents should reference the same command.

**Suggested fix:** Align DOD-001 migration check wording with ENV-001 Gate 13. Both should state the exact command is finalized in FEAT-000 and reference the same pattern.

## Top Issues

1. **F-01 (Major) — e2e.yml and playwright.config.ts are design elements with no feature owner.** No builder can create these files without a plan entry due to CI-enforced scope checks.
2. **F-04 (Minor) — WAV-001 Wave 24 Alone uses stale migration number (0002) and OQ-067 is still open** despite being resolved in FEAT-007/plan.md (DEC-048 records the decision).
3. **F-02 (Minor) — FBD-001 AC total is 140; correct count is 139.** Phase 7 test planning depends on accurate counts.
4. **F-05 (Minor) — FEAT-001 Objective has story-feature boilerplate** that could mislead a builder into creating backend models that belong to later features.
5. **F-07 (Minor) — Test Plan entries are truncated** across all sampled feature plans; if acceptance.md carries full text, the plan should say so.

## Unresolved From Earlier Runs

None. This is Run 1.

## Recommendation

**Send back to producers.** F-01 (Major) is a concrete Phase 6 blocker: no builder can create `.github/workflows/e2e.yml` or `playwright.config.ts` without a plan entry. All 8 Minors should be included in the same pass to avoid a Run 3 later. This is Run 1 of 3 allowed.

Decision authority: Tech lead (Mohanasunder), per `.ai/standards/checker-and-fail-decision.md`.

## Decision Record

| Field | Value |
|---|---|
| Options offered | A (send back to producers — fix Major + all Minors), B (proceed to human review with findings), C (send back with specific instructions) |
| Option chosen | A — send back to producers, fix Major + all Minors |
| Decided by | Mohanasunder (Tech lead) |
| Timestamp | 2026-10-17 |
| Reason | F-01 is a Phase 6 blocker; fix all 9 findings in one pass. DEC-049. |

## Assumptions

None raised.

## Open Questions

None raised beyond those already in artifacts.

## Traceability Links
- Upstream: PIB-005 v0.1; FBD-001 v0.1; DOD-001 v0.1; WAV-001 v0.1; ENV-001 v0.1; FEAT-000 through FEAT-034 plan.md v0.1
- Rules: .ai/checker-rules/phase-5.md; .ai/standards/checker-and-fail-decision.md

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
