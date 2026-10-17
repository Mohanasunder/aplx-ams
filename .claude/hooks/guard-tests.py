#!/usr/bin/env python3
"""PreToolUse hook (matcher: Edit|Write|MultiEdit|NotebookEdit|Bash). Blocks changes to locked tests.

Locked = test files listed in an Approved feature test set (docs/06-build/FEAT-NNN-TESTS.md), plus the
approved test set file itself (its status changes only through /approve). See scripts/locked_tests.py.
Exit code 2 blocks the call and returns stderr to Claude. The CI check (scripts/locked_tests.py check)
is the backstop for anything this hook cannot see.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

FILE_TOOLS = {"Edit", "Write", "MultiEdit", "NotebookEdit"}
# Bash commands that can change a file named anywhere in the command
WRITERS = re.compile(
    r"\bsed\s+(-[a-zA-Z]*i|--in-place)|\bperl\s+-[a-zA-Z]*i|\b(rm|mv|cp|truncate|tee|dd|unlink|install)\b"
    r"|\bgit\s+(checkout|restore|rm|mv|reset|stash|apply|am)\b|\bfm\.py\b"
    r"|\b(Set-Content|Add-Content|Out-File|Remove-Item|Move-Item|Copy-Item|Clear-Content|New-Item)\b",
    re.I,
)
REDIRECT = re.compile(r"(?<![0-9&])>{1,2}\s*[\"']?([^\s\"';|&)]+)")
UNLOCK_HINT = ("To change an approved test, stop and tell the human the test, the reason, and the proposed change. "
               "Only a named human can unlock it: /approve <test set> with Reject and the reason; then revise it in Mode A, "
               "and the new test set version is validated and approved.")


def block(owner, what):
    print(f"BLOCKED by SDLC guard: {what} is locked by approved test set {owner}. {UNLOCK_HINT}", file=sys.stderr)
    sys.exit(2)


def main():
    try:
        data = json.load(sys.stdin)
        tool = data.get("tool_name", "")
        inp = data.get("tool_input") or {}
        from locked_tests import locked_paths, norm
        locked = locked_paths()
    except Exception:
        return 0  # never break the session on a hook error; CI still checks
    if not locked:
        return 0

    if tool in FILE_TOOLS:
        target = norm(inp.get("file_path") or inp.get("notebook_path") or "")
        if target in locked:
            block(locked[target], target)
        return 0

    if tool == "Bash":
        cmd = inp.get("command", "") or ""
        if "log_approval.py" in cmd:
            return 0  # human decision via /approve; the permission prompt is the human's confirmation
        for m in REDIRECT.finditer(cmd):
            t = norm(m.group(1))
            if t in locked:
                block(locked[t], t)
        if WRITERS.search(cmd):
            low = cmd.replace("\\", "/").lower()
            for path, owner in locked.items():
                if path.lower() in low:
                    block(owner, path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
