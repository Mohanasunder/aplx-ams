#!/usr/bin/env python3
"""PreToolUse hook (matcher: Edit|Write|MultiEdit|NotebookEdit|Bash). Blocks agent changes to Approved artifacts.

An artifact under docs/ whose front matter says status: Approved changes only through the living spec rule
(.ai/standards/phase-loop.md): an open spec change record (template spec-change, status Draft or In review, in
docs/logs/spec-changes/) must name the artifact's ID before its producer revises it. This also covers
'scripts/fm.py set' on an Approved artifact, so its status cannot be reset to Draft to get around the rule.
/approve (scripts/log_approval.py) is a human decision and is not blocked. Exit code 2 blocks the call and returns
stderr to Claude. The CI check (scripts/spec_impact.py records) is the backstop for anything this hook cannot see.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

FILE_TOOLS = {"Edit", "Write", "MultiEdit", "NotebookEdit"}
WRITERS = re.compile(
    r"\bsed\s+(-[a-zA-Z]*i|--in-place)|\bperl\s+-[a-zA-Z]*i|\b(rm|mv|cp|truncate|tee|dd|unlink|install)\b"
    r"|\bgit\s+(checkout|restore|rm|mv|reset|stash|apply|am)\b|\bfm\.py\s+set\b"
    r"|\b(Set-Content|Add-Content|Out-File|Remove-Item|Move-Item|Copy-Item|Clear-Content|New-Item)\b",
    re.I,
)
REDIRECT = re.compile(r"(?<![0-9&])>{1,2}\s*[\"']?([^\s\"';|&)]+)")
ID = re.compile(r"\b[A-Z]{2,5}-\d{3}(?:-[A-Z0-9]+)?\b")


def norm(p):
    if not p:
        return ""
    path = Path(p)
    if not path.is_absolute():
        path = ROOT / path
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except Exception:
        return str(p).replace("\\", "/")


def approved():
    from sdlc_lib import read_artifact
    out = {}
    for p in (ROOT / "docs").rglob("*.md"):
        try:
            fm, _, _ = read_artifact(p)
        except Exception:
            continue
        if fm and fm.get("status") == "Approved" and fm.get("id"):
            out[p.relative_to(ROOT).as_posix()] = (fm["id"], fm.get("version", ""))
    return out


def open_scr_ids():
    from sdlc_lib import read_artifact
    named = set()
    for p in (ROOT / "docs" / "logs" / "spec-changes").glob("*.md"):
        try:
            fm, body, _ = read_artifact(p)
        except Exception:
            continue
        if fm and fm.get("template") == "spec-change" and fm.get("status") in ("Draft", "In review"):
            named |= set(ID.findall(body))
    return named


def block(path, aid, ver):
    print(f"BLOCKED by SDLC guard: {path} ({aid} v{ver}) is Approved. Change flows backward: under the living spec "
          f"rule (.ai/standards/phase-loop.md) the artifact's producer first creates a spec change record naming {aid} "
          f"(scripts/new_artifact.py --template spec-change), then revises it and bumps its version. If this phase does "
          f"not own {aid}, stop and report the problem to the Orchestrator instead.", file=sys.stderr)
    sys.exit(2)


def main():
    try:
        data = json.load(sys.stdin)
        tool = data.get("tool_name", "")
        inp = data.get("tool_input") or {}
        appr = approved()
    except Exception:
        return 0  # never break the session on a hook error; CI still checks
    if not appr:
        return 0
    targets = []
    if tool in FILE_TOOLS:
        targets.append(norm(inp.get("file_path") or inp.get("notebook_path") or ""))
    elif tool == "Bash":
        cmd = inp.get("command", "") or ""
        if "log_approval.py" in cmd:
            return 0  # human decision via /approve; the permission prompt is the human's confirmation
        targets += [norm(m.group(1)) for m in REDIRECT.finditer(cmd)]
        if WRITERS.search(cmd):
            low = cmd.replace("\\", "/").lower()
            targets += [p for p in appr if p.lower() in low]
    hits = [t for t in targets if t in appr]
    if hits:
        scr = open_scr_ids()
        for t in hits:
            aid, ver = appr[t]
            if aid not in scr:
                block(t, aid, ver)
    return 0


if __name__ == "__main__":
    sys.exit(main())
