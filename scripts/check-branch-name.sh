#!/usr/bin/env bash
# Validate a branch name against the branching standard.
#   scripts/check-branch-name.sh feature/FEAT-004-ticket-triage
# Pattern: (feature|hotfix|spike)/<PREFIX>-NNN-<slug> where slug is 1 to 4 lowercase words joined by hyphens.
# Defect fixes are Fix features (FEAT-NNN, Type: Fix) on feature/ branches, so they get the same plan, test-first,
# scope, and package checks as any feature; there is no fix/ branch.
# spike/SPK-NNN-slug branches are throwaway: never merged, never a PR (scripts/spike.py).
# main, develop-free trunk: 'main' itself and release/x.y are allowed.
set -euo pipefail
name="${1:-}"
[ -n "$name" ] || { echo "usage: $0 <branch-name>" >&2; exit 2; }
if [[ "$name" == "main" || "$name" =~ ^release/[0-9]+\.[0-9]+$ ]]; then exit 0; fi
if [[ "$name" =~ ^(feature|hotfix|spike)/(FEAT|HOT|SPK)-[0-9]{3}-[a-z0-9]+(-[a-z0-9]+){0,3}$ ]]; then
  # feature/ must use FEAT, hotfix/ must use HOT, spike/ must use SPK
  case "$name" in
    feature/FEAT-*|hotfix/HOT-*|spike/SPK-*) exit 0 ;;
  esac
fi
echo "Invalid branch name: $name" >&2
echo "Expected feature/FEAT-NNN-slug, hotfix/HOT-NNN-slug, spike/SPK-NNN-slug or release/x.y (slug: 1 to 4 lowercase words)" >&2
echo "Defect fixes use feature/FEAT-NNN-slug for a Fix feature (plan.md 'Type: Fix DEF-NNN')." >&2
exit 1
