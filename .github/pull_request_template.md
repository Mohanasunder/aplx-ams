## Summary
<!-- 3 sentences: what changed and why -->

## Linked artifacts
FEAT: · REQ: · API/DBD/UIS: · Plan: docs/05-build-plan/feature-NNN-slug/plan.md

## Change summary
- Requirements covered (criterion -> passing test): 
- Known gaps (or None): 
- Deviations from plan (or None): 
- Blockers (must be None for review): 

## Risk tier and review depth
- [ ] Standard (1 human developer): depth Standard, or Light only for docs, UI copy, or test-covered refactors
- [ ] High (2 approvers incl. tech lead): depth Deep
- [ ] Critical (tech lead + release manager): depth Deep

Depth checklist (reviewer ticks the items for the depth above; see `.ai/standards/review-and-approval.md`):
- [ ] Deep: every changed line of logic read; security reviewed against the threat model; ran locally incl. failure paths; migrations and rollback checked
- [ ] Standard: every criterion checked on the running feature; contract and UI spec followed; logic and edge cases spot-checked
- [ ] Light: description and test results read; diff skimmed and stays docs, copy, or covered refactor

## Automated gates and reviews
- [ ] Lint, types, tests, SAST, dependency scan, secrets scan green
- [ ] Checker validation summary attached (verdict: ____ ; "Proceeded on Fail"? yes/no)
- [ ] AI pre-review and security scan reports attached (advisory)

## Reviewer checklist (human approver ticks each item)
- [ ] Ran or previewed the feature
- [ ] Every acceptance criterion met
- [ ] No changes outside the plan
- [ ] Tests assert behavior
- [ ] Auth, validation, secrets, data handling checked
- [ ] Migrations reversible; contract and UI spec followed
