# Branching Standard

Trunk-based development with short-lived feature branches. `main` is always releasable and protected.

| Branch | Purpose | Lifetime |
| --- | --- | --- |
| `main` | Always deployable; protected | permanent |
| `feature/FEAT-NNN-slug` | One feature built by builder agents, including a Fix feature (`Type: Fix DEF D-N`) for a defect from testing or production (defect rule, `.ai/standards/phase-loop.md`) | days; deleted after merge |
| `hotfix/HOT-NNN-slug` | Urgent production fix, from the release tag | hours |
| `release/x.y` | Only if a release must be stabilized or patched | short |
| `spike/spk-S-N-slug` | Throwaway experiment that answers one architecture or design question | its time box (at most `max_spike_days`); deleted once its ADR is approved |

## Creation

Only after a human selects the feature: `scripts/create-feature-branch.sh FEAT-NNN [--push]` (also `/create-feature-branch`). The script requires: approved plan/tasks/acceptance, dependencies Merged, no collision with an open feature (In progress, In review, or Blocked: no file in common, and a feature that changes a Shared Path from `.ai/standards/coding-standards.md` runs alone; `check_feature_size.py start`), open feature branches under `max_open_feature_branches`, clean tree, fresh `main`. Because dependencies must be Merged first and parallel features share no files, merge order inside a wave does not matter. It then creates the branch, optionally pushes, and records it in `status.md`. Open a **draft PR** immediately with `gh pr create --draft`, linked to the story, plan, and acceptance criteria.

## Rules

- Builders commit only to their feature branch, small commits with the FEAT-ID in each message. Never to `main`.
- Sync `main` into the feature branch with `git merge main` before opening the PR and before merge (the only merge agents may run; rebasing a pushed branch would need a force push, which is blocked). Resolve conflicts on the branch; if a conflict touches a contract or another feature, stop and escalate to the human.
- One migration per change, never edit a merged migration; migrations must be reversible and apply on current `main`.
- Never commit secrets or generated artifacts that do not belong in the repo.
- Merge: a named human approves; the platform (or an authorized bot) squash/rebase-merges with a message referencing FEAT, REQ, and PR IDs. The authoring agent never merges. If a merge breaks `main`, revert first, then fix on a new branch.
- A branch with no activity for `stale_branch_days` is flagged by `/sdlc-status`.
- Branch protection (configured by humans on the Git platform): no direct pushes; at least one human approval (two for High, tech lead plus release manager for Critical, via CODEOWNERS); required checks green; dismiss approvals on new commits; linear history; the author cannot approve or merge.

## Spikes

- All spike records live in the single collection file `docs/03-architecture/spikes.md` as `## Spike S-N: [Title]` sections, cited as `SPK S-N`. Never create separate `SPK-NNN.md` files.
- Only after the phase approver approves the spike section: `python3 scripts/spike.py start SPK-S-N` creates `spike/spk-S-N-slug` from `main`.
- Commits start with `SPK-S-N:` and contain only spike code; the spike record and its ADR are phase documents and never go on the spike branch. A spike branch is **never** opened as a PR and **never** merged (the git guard hook and CI block both); spike code is never reused as production code.
- When the time box ends: record Findings and Recommendation in the spike's section in `spikes.md`, write the ADR citing `SPK S-N`, have both approved, then `python3 scripts/spike.py close SPK-S-N --delete`. A human deletes any remote copy (`git push origin --delete ...`).
- `python3 scripts/spike.py check` (CI and `/sdlc-status`) fails on a spike commit in `main`, an expired time box, a spike branch with no record, or a branch left after its ADR is approved.
- **Note:** `scripts/spike.py` must be updated by a human to read sections from `spikes.md` and use the `SPK-S-N` / `spike/spk-S-N-slug` naming convention.

## Releases and hotfixes

Releases are tagged on `main` (`v1.4.0`) with release notes from merged features. Hotfixes branch from the release tag, get a fast but still human-approved review, and merge back to `main`. Feature flags may hide unfinished work.
