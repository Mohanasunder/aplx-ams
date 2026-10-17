#!/usr/bin/env bash
# Create a feature branch for an approved feature, checking all preconditions first.
#   scripts/create-feature-branch.sh FEAT-004 [--push]
# Run by the Orchestrator after a human has selected the feature to build.
set -euo pipefail

feat="${1:-}"; push="${2:-}"
[[ "$feat" =~ ^FEAT-[0-9]{3}$ ]] || { echo "usage: $0 FEAT-NNN [--push]" >&2; exit 2; }
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"
num="${feat#FEAT-}"
plan_root="docs/05-build-plan"

fail() { echo "PRECONDITION FAILED: $*" >&2; exit 1; }
fmget() { grep -m1 "^$2:" "$1" | sed "s/^$2:[[:space:]]*//" || true; }

# 1. Feature folder and approved plan files
folder="$(ls -d "$plan_root"/feature-"$num"-* 2>/dev/null | head -n1 || true)"
[ -n "$folder" ] || fail "no folder $plan_root/feature-$num-<slug>/"
for f in plan.md tasks.md acceptance.md status.md; do
  [ -f "$folder/$f" ] || fail "$folder/$f is missing"
done
for f in plan.md tasks.md acceptance.md; do
  [ "$(fmget "$folder/$f" status)" = "Approved" ] || fail "$folder/$f is not Approved"
done

# 2. Branch name
slug="${folder##*/feature-$num-}"
branch="feature/$feat-$slug"
"$root/scripts/check-branch-name.sh" "$branch" || fail "derived branch name '$branch' is invalid"
if git show-ref --verify --quiet "refs/heads/$branch"; then fail "branch $branch already exists"; fi

# 3. Dependencies merged
deps="$(grep -m1 '^- Depends on:' "$folder/plan.md" | sed 's/^- Depends on:[[:space:]]*//' || true)"
for d in $(echo "$deps" | grep -oE 'FEAT-[0-9]{3}' || true); do
  dn="${d#FEAT-}"
  dfolder="$(ls -d "$plan_root"/feature-"$dn"-* 2>/dev/null | head -n1 || true)"
  [ -n "$dfolder" ] || fail "dependency $d has no plan folder"
  grep -q '^- State: Merged' "$dfolder/status.md" || fail "dependency $d is not Merged"
done

# 3b. No collision with open features: no two change the same files; one that changes a shared path runs alone
python3 "$root/scripts/check_feature_size.py" start "$feat" || fail "$feat collides with an open feature (details above)"

# 4. Review capacity
max="$(grep -m1 -E '^max_open_feature_branches:' project.md | sed 's/^[^:]*:[[:space:]]*//' || true)"
if [[ "$max" =~ ^[0-9]+$ ]]; then
  open="$(git branch --list 'feature/*' | wc -l | tr -d ' ')"
  [ "$open" -lt "$max" ] || fail "$open open feature branches; limit is $max (review capacity)"
fi

# 5. Clean tree, fresh main
git diff --quiet && git diff --cached --quiet || fail "working tree has uncommitted changes"
if git remote | grep -q .; then git fetch origin --quiet; fi
git switch main --quiet
if git remote | grep -q .; then git pull --ff-only --quiet; fi

# 6. Create branch (and optionally push)
git switch -c "$branch" --quiet
base="$(git rev-parse --short HEAD)"
if [ "$push" = "--push" ] && git remote | grep -q .; then git push -u origin "$branch" --quiet; fi

# 7. Record in status.md
today="$(date -u +%Y-%m-%d)"
sed -i.bak -e "s|^- Branch:.*|- Branch: $branch|" -e "s|^- Base commit:.*|- Base commit: $base|" \
  -e "s|^- Started:.*|- Started: $today|" -e "s|^- State:.*|- State: In progress|" "$folder/status.md" && rm -f "$folder/status.md.bak"

echo "Created $branch from main@$base"
echo "Next: builders commit only to this branch; open a draft PR; never merge or push to main."
