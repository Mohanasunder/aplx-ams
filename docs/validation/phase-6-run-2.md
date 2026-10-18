---
id: VAL-027
title: Phase 6 validation run 2
phase: 6
version: 0.1
template: validation-report
template_version: 2.0
status: Draft
author_agent: checker
approver: Tech lead
date: 2026-10-18
validation: Fail
---

# Phase 6 validation run 2 — FEAT-005-TESTS

## Input References
- FEAT-005-TESTS v0.1 (Draft, 2026-10-18) — artifact under review
- FEAT-005-ACC v0.1 (Approved 2026-10-17) — acceptance criteria source
- FEAT-005 plan.md v0.1 (Approved 2026-10-17) — risk tier, file scope
- `.ai/checker-rules/phase-6.md` — checker rules applied

## Purpose And Scope
Validation of FEAT-005-TESTS v0.1 (test set, pre-implementation check). Covers test-set completeness, criterion coverage, red-run evidence, and test-commit content. Does not cover code review, PR description, or SAST (post-implementation checks).

## Verdict
**Fail** — 1 Major finding, 2 Minor findings, 1 Advisory.

## Scorecard
| Layer | Result | Notes |
|---|---|---|
| Structural | Pass | All front-matter fields present; template sections filled; correct phase folder |
| Input conformance | Pass | All cited artifacts verified Approved at stated versions |
| Completeness | Pass with warnings | All 4 ACs have at least one test; AC-3 sign-in gap documented |
| Consistency | Fail | Backend tests use P-code tier IDs ("P3") as role values; model uses role slugs ("delivery_manager") |
| Traceability | Pass | Upstream/downstream links present; test commits verified on branch |
| Content quality | Pass | Tests assert observable behavior; red run evidence is behavioral |

## Findings

### F-001 — Major (overridable)
**Category:** Behavioral validity / Consistency
**Location:** `src/aplx_ams_django/accounts/tests/test_api.py` — `_make_user` helper

Backend test helper creates users with PRM tier codes as the role attribute (`_make_user("P3")` for DM, `_make_user("P1")` for L1 etc.). The User model stores role slugs (`delivery_manager`, `l1_support_engineer`). Any Mode B `HasRolePermission` implementation will check `request.user.role == "delivery_manager"` — it will not match "P3". All four DM happy-path tests will stay red in Mode B even with a correct implementation, making the locked tests un-passable.

**Fix:** Replace tier codes with role slugs in `test_api.py`: `"P3"` → `"delivery_manager"`, `"P1"` → `"l1_support_engineer"`, `"P2"` → `"l2_l3_support_engineer"`, `"P4"` → `"client_user"`.

### F-002 — Minor (overridable)
**Category:** Scope / Plan conformance
**Location:** `src/aplx_ams_django/settings/base.py`; FEAT-005 plan.md § Files To Create Or Modify

`settings/base.py` was modified in commit `6248aa5` (the database test commit) but is not listed in plan.md § Files To Create Or Modify. The Mode B scope check (`check_feature_size.py scope`) will fail when it is modified again during implementation.

**Fix:** Add `src/aplx_ams_django/settings/base.py` to plan.md § Files To Create Or Modify (requires plan revision and re-approval by tech lead).

### F-003 — Minor (overridable)
**Category:** Completeness / Edge case coverage
**Location:** `test_api.py` AC-4 rows; `UserManagement.test.tsx` AC-4 row

AC-4 ("a user who is not a delivery manager") tests PATCH and deactivate refusals for P1 only; P2 and P4 are not verified for those operations. Frontend tests cover redirect for P1 only.

**Fix:** Add `test_l2_l3_cannot_patch_user`, `test_client_user_cannot_patch_user`, `test_l2_l3_cannot_deactivate_user`, `test_client_user_cannot_deactivate_user` to `test_api.py`.

### F-004 — Advisory
**Category:** Deferred scope / AC coverage gap
**Location:** FEAT-005-TESTS § Purpose And Scope; § Criteria To Tests Map AC-3

AC-3's THEN clause ("can no longer sign in") is deferred to FEAT-006. The deactivation persistence is covered; the sign-in refusal gate is not. Documented clearly in the artifact. No action required here; FEAT-006-TESTS must close the gap.

## Top Issues
1. **Role identifier mismatch (F-001 — Major):** DM happy-path backend tests use "P3" as role value; the model stores "delivery_manager". Tests locked in this state cannot turn green in Mode B.
2. **settings/base.py not in plan scope (F-002 — Minor):** Will cause Mode B scope gate failure unless plan is updated.
3. **AC-4 partial coverage for PATCH/deactivate (F-003 — Minor):** P2 and P4 refusals on PATCH and deactivate untested.
4. **AC-3 sign-in refusal deferred (F-004 — Advisory):** Documented scope boundary; FEAT-006-TESTS must close.

## Unresolved From Earlier Runs
None — first validation run for this artifact.

## Recommendation
**Send back to producer.** F-001 is a blocking defect: locking tests that cannot turn green even with correct implementation violates the purpose of the test-set approval gate. Fix F-001, F-002, and F-003 in the same revision to avoid a second send-back loop.

## Decision Record
<fill: decision record — to be completed after human decision>

## Assumptions
None new.

## Open Questions
None new.

## Traceability Links
- Upstream: FEAT-005-TESTS v0.1; FEAT-005-ACC v0.1; FEAT-005 plan.md v0.1
- Downstream: FEAT-005-TESTS revised version (after fix); FEAT-005 Phase 6 PR

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
