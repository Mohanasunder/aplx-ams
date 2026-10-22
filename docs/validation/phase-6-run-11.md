---
id: VAL-037
title: Phase 6 validation run 11
phase: 6
version: 0.1
template: validation-report
template_version: 2.0
status: Draft
author_agent: checker
approver: Tech lead
date: 2026-10-22
validation: Pending
---
# Phase 6 Validation Run 11

Artifacts validated: `docs/06-build/pr-descriptions.md` (§ PR FEAT-010), `docs/06-build/ai-pre-review-reports.md` (§ AIR FEAT-010), `docs/06-build/security-scan-reports.md` (§ SSR FEAT-010). Branch: `feature/FEAT-010-holiday-list`.

## Input References
- FEAT-010 plan.md v0.5 (Approved, Mohanasunder, 2026-10-21) — docs/05-build-plan/feature-010-holiday-list/plan.md
- FEAT-010-ACC v0.1 (Approved, Mohanasunder, 2026-10-17) — docs/05-build-plan/feature-010-holiday-list/acceptance.md
- FEAT-010-TESTS v0.2 (Approved, Mohanasunder, 2026-10-21) — docs/06-build/FEAT-010-TESTS.md
- REQ-001 v0.4 § S-24; API-001 v0.3 § Company holiday list; DBD-001 v0.1 § Module: sla; PRM-001 v0.1; UIS-001 v0.1 § REQ S-24
- .ai/standards/learned-rules.md (LRN L-1); .ai/checker-rules/phase-6.md
- DEC-090 (Mohanasunder, 2026-10-21) — pip-audit scoped to requirements.txt

## Purpose And Scope
Covers Phase 6 review documents for FEAT-010 (S-24: Delivery Manager Maintains the Company Holiday List): the PR description, AI pre-review report, and security scan report. Also validates the implementation code on the branch against the approved plan and learned rules, as prompted by findings in AIR FEAT-010. Does not re-validate the test set (FEAT-010-TESTS v0.2, already validated in run-10).

## Verdict
**FAIL**

Deterministic script result: `Pass with warnings` (2 pre-existing Minor in FEAT-000 stubs). Checker adds 4 Major findings confirmed via AIR FEAT-010 and independent code inspection.

## Scorecard

| Layer | PR FEAT-010 | AIR FEAT-010 | SSR FEAT-010 |
|---|---|---|---|
| Structural | Pass — all required sections present | Pass — all sections present | Pass |
| Input conformance | Pass — plan v0.5, test set v0.2, SCRs cited | Pass — inputs cited at Approved versions | Pass |
| Completeness | Pass — 4 ACs listed; 22 tests listed; gate table present | Pass — all 4 ACs assessed | Pass — all gate commands present |
| Consistency | **Fail** — frontend types inconsistent with DBD-001 / backend serializer (F-002, F-003); App.tsx routing broken (F-004) | Pass — findings internally consistent | Pass — 3 gate commands all exit 0 |
| Traceability | Pass — upstream/downstream links present | Pass | Pass |
| Content quality | **Fail** — LRN L-1 violation confirmed in views.py (F-001); PR change summary omits AIR finding status (F-005); incorrect file path (F-006); misleading gate characterization (F-007) | Pass (advisory) — 4 Major findings cite file:line:category; LRN L-1 check performed | Pass — LOW findings documented; no production findings |

## Findings

| ID | Artifact | Location | Severity | Category | Description |
|---|---|---|---|---|---|
| F-001 | Code on branch (confirmed via AIR F-4) | `src/aplx_ams_django/sla/views.py` lines 64–67, 85 | **Major** | missing-input-validation / LRN L-1 | `views.create()` catches only `ValueError`; `views.destroy()` has no exception handler. Both call `model.save()` on `HolidayEntry` subject to `chk_removed_consistent` with no `try/except IntegrityError`. Per LRN L-1 any IntegrityError propagates as HTTP 500. Fix: add `except django.db.IntegrityError` → HTTP 400 to both. |
| F-002 | Code on branch (confirmed via AIR F-1) | `src/frontend/src/api/holidays.ts` lines 15–27; `HolidayList.tsx` line 94 | **Major** | api-contract-field-mismatch | `HolidayEntry.date` does not match backend serializer field `holiday_date`. `HolidayList.tsx:94` renders `h.date` (always undefined). `addHoliday()` sends `{date}` but backend expects `{holiday_date}` — every POST from the UI returns HTTP 400. Fix: rename `date` → `holiday_date` in TypeScript types and component. |
| F-003 | Code on branch (confirmed via AIR F-2) | `src/frontend/src/api/holidays.ts` lines 19, 26; `HolidayList.tsx` line 95 | **Major** | invented-field | `description` field in `HolidayEntry` and `CreateHolidayPayload` has no backing in DBD-001 v0.1, Django model, or serializer. PR Quality Checklist "Nothing invented" is incorrectly marked [x]. Fix: remove `description` from TypeScript types, form state, form render, and handleAdd payload. |
| F-004 | Code on branch (confirmed via AIR F-3) | `src/frontend/src/App.tsx` line 43 | **Major** | missing-context-provider | `/admin/holidays` route has no `UserContext.Provider` wrapper. `HolidayList.tsx:32` calls `useContext(UserContext)`; without provider `role` is undefined and redirect sentinel always renders. DM can never access the holiday list at runtime. Tests pass because they mock context directly. Fix: add `UserContext.Provider` wrapper for the holiday route in App.tsx. |
| F-005 | PR FEAT-010 | `### Known Gaps`, `### Deviations From Plan` | Minor | incomplete-change-summary | PR description doesn't document whether 4 Major AIR findings were fixed or deferred. Reviewer cannot determine status from PR alone. Fix: add AI Pre-Review Findings subsection listing each finding with its fix commit or deferral decision. |
| F-006 | PR FEAT-010 | `### Changes` > Backend boilerplate | Minor | incorrect-file-path | PR states `src/aplx_ams_django/sla/settings/base.py` — path does not exist. Correct path is `src/aplx_ams_django/settings/base.py` (root settings dir). Fix: correct the path. |
| F-007 | PR FEAT-010 | `### Gate Results` — scope row | Minor | misleading-gate-characterization | States scope gate is "overridable" which is incorrect per phase rules. Two deviations (pyproject.toml, .secrets.baseline) have no recorded DEC. Fix: state actual exit code; record DECs or note they were pre-approved; remove "overridable" characterization. |
| F-008 | AIR FEAT-010 | `### Quality Checklist` | Minor | quality-checklist-format-deviation | AIR Quality Checklist omits standard items present in prior AIRs: "Inputs referenced are Approved artifacts at the stated versions," "Nothing invented," "Assumptions and open questions are logged and linked," "Terminology follows .ai/standards/glossary.md." Fix: add missing standard checklist items. |
| DET-001 | pr-descriptions.md (pre-existing) | `## PR FEAT-000` section | Minor (pre-existing) | vague-wording | Script: 'etc.' in FEAT-000 stub. Pre-existing; not from FEAT-010 producer. |
| DET-002 | ai-pre-review-reports.md (pre-existing) | `## AIR FEAT-000` section | Minor (pre-existing) | vague-wording | Script: 'etc.' in FEAT-000 stub. Pre-existing; not from FEAT-010 producer. |

## Top Issues

1. **F-001 — LRN L-1 violation in views.py:** `views.create()` and `views.destroy()` lack `try/except IntegrityError`. A constraint violation propagates as HTTP 500. Contained fix in two places in views.py.
2. **F-002 — Field name mismatch:** `HolidayEntry.date` vs. backend `holiday_date`. Every add from the UI returns HTTP 400; GET list renders undefined dates. AC-1 and AC-2 non-functional via UI.
3. **F-003 — Invented field `description`:** No backing in DBD-001 or backend. PR quality checklist incorrectly marks "Nothing invented" as done.
4. **F-004 — Missing UserContext.Provider:** DM can never access /admin/holidays in a running application; tests are insulated by their inline context mock. AC-3 broken at runtime (DM sees redirect sentinel).
5. **F-005 — PR missing AIR finding status:** Reviewer cannot determine from the PR alone whether F-1 through F-4 were fixed before the PR was finalized.

## Unresolved From Earlier Runs
Not applicable — this is the first checker run on these three documents for FEAT-010.

## Recommendation
**Send back to producer (Option A).** The 4 Major findings (F-001 through F-004) are concrete, contained code-level defects with clear fixes. The backend logic (DAL `as_of` semantics, permissions, soft-delete) is correctly implemented. The SSR is clean. Fix F-001 to F-004 in the builders; also fix F-005 to F-007 in the PR description in the same pass.

## Decision Record
<fill: decision record — to be filled by the Orchestrator after the human decides>

## Assumptions
- A-CHK-010-01: Code-level findings F-001 through F-004 are confirmed via AIR FEAT-010 (2026-10-22) and independently validated against Phase 6 learned-rule requirements and input conformance standards.

## Open Questions
None.

## Traceability Links
- Upstream: FEAT-010 plan.md v0.5; FEAT-010-ACC v0.1; FEAT-010-TESTS v0.2; REQ-001 v0.4 § S-24; API-001 v0.3; DBD-001 v0.1; PRM-001 v0.1; UIS-001 v0.1; .ai/standards/learned-rules.md LRN L-1; AIR FEAT-010
- Downstream: Builders (F-001 to F-004 fix pass); docs/06-build/pr-descriptions.md (F-005 to F-007 fix); docs/06-build/ai-pre-review-reports.md (F-008 fix)

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
