#!/usr/bin/env python3
"""PreToolUse hook (matcher: Bash). Blocks git actions that break the methodology's rules.

Receives the tool call as JSON on stdin. Exit code 2 blocks the call and returns stderr to Claude.
Blocks:
  - git commit / push / merge / rebase while on main or master
  - git merge, except 'git merge main' / 'git merge origin/main' to sync a feature, fix, or hotfix branch
  - 'gh pr merge' and approving reviews (agents never merge or approve)
  - git push --force / -f
  - committing files that look like secrets (.env, *.pem, *.key, id_rsa)
  - opening a PR from a spike/ branch, or merging a spike/ branch anywhere (spikes are throwaway)
"""
import json
import re
import subprocess
import sys


def current_branch():
    try:
        return subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True, timeout=5).stdout.strip()
    except Exception:
        return ""


def block(msg):
    print(f"BLOCKED by SDLC guard: {msg}", file=sys.stderr)
    sys.exit(2)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    cmd = (data.get("tool_input") or {}).get("command", "") or ""
    if not re.search(r"\b(git|gh)\b", cmd):
        return 0

    if re.search(r"\bgh\s+pr\s+merge\b", cmd) or re.search(r"\bgh\s+pr\s+review\b.*--approve", cmd):
        block("agents never merge or approve pull requests; a named human does this")
    if re.search(r"\bgit\s+merge\b.*\bspike/", cmd) or (re.search(r"\bgh\s+pr\s+create\b", cmd) and current_branch().startswith("spike/")):
        block("spike branches are throwaway: never opened as a PR or merged. Record findings, write the ADR, then scripts/spike.py close")
    if re.search(r"\bgit\s+merge\b", cmd):
        on_work_branch = re.match(r"(feature|fix|hotfix)/", current_branch() or "")
        sync_only = re.fullmatch(r"\s*git\s+merge\s+(--no-edit\s+)?(origin/)?main\s*", cmd)
        if not (on_work_branch and sync_only):
            block("agents never merge into main; the only allowed merge is syncing main into your feature branch (git merge main)")
    if re.search(r"\bgit\s+push\b.*(--force|--force-with-lease|\s-f\b)", cmd):
        block("force push is not allowed")
    if re.search(r"\bgit\s+push\b.*\b(origin\s+)?(main|master)\b", cmd):
        block("never push to main; push the feature branch and open a PR")

    branch = current_branch()
    if branch in ("main", "master") and re.search(r"\bgit\s+(commit|push|rebase|cherry-pick|am)\b", cmd):
        block(f"you are on '{branch}'. Create a feature branch with scripts/create-feature-branch.sh FEAT-NNN")

    if re.search(r"\bgit\s+add\b", cmd) and re.search(r"(\.env\b|\.pem\b|\.key\b|id_rsa|credentials)", cmd):
        block("looks like a secret file; secrets are never committed (use references/secret managers)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
