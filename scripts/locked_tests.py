#!/usr/bin/env python3
"""Locked tests: approved test files that agents may not change (principle: agents never edit approved tests).

A test file is locked when it is listed under '## Test Files' in a feature test set
(docs/06-build/FEAT-NNN-TESTS.md, template feature-test-set) whose status is Approved.
To change a locked test, a named human rejects that test set version with /approve (the reason is
recorded in docs/logs/approval-log.md); the builder revises it, and the new version is validated and approved.

Usage:
  python3 scripts/locked_tests.py list    # show locked test sets and files
  python3 scripts/locked_tests.py check   # CI / automated gate: locked files unchanged since each Test Commit
Exit code 1 on any violation.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sdlc_lib import ROOT, read_artifact, sections, strip_comments  # noqa: E402

TEST_SET_DIR = ROOT / "docs" / "06-build"
SHA = re.compile(r"\b[0-9a-f]{7,40}\b")
BACKTICK = re.compile(r"`([^`]+)`")


def norm(path):
    """Repo-relative, forward-slash, case-normalized path (or None if outside the repo)."""
    p = Path(path)
    if not p.is_absolute():
        p = ROOT / p
    try:
        rel = p.resolve().relative_to(ROOT.resolve())
    except (ValueError, OSError):
        return None
    return os.path.normcase(rel.as_posix()).replace("\\", "/")


def test_sets():
    """Yield dicts for every feature test set: path, id, version, status, files, commit."""
    for p in sorted(TEST_SET_DIR.glob("*-TESTS.md")):
        try:
            fm, body, _ = read_artifact(p)
        except Exception:
            continue
        if not fm or fm.get("template") != "feature-test-set":
            continue
        secs = {h: strip_comments(c) for h, c in sections(body)}
        files = []
        for ln in secs.get("Test Files", "").splitlines():
            s = ln.strip().lstrip("-*").strip()
            if not s or s.lower().startswith("not applicable"):
                continue
            files.extend(t.strip() for t in (BACKTICK.findall(s) or [s.split()[0]]) if t.strip())
        sha = SHA.search(secs.get("Test Commit", ""))
        yield {
            "path": p, "id": fm.get("id"), "version": fm.get("version"), "status": fm.get("status"),
            "files": files, "commit": sha.group(0) if sha else None,
        }


def approved_sets():
    return [s for s in test_sets() if s["status"] == "Approved"]


def locked_paths():
    """Map normalized path -> owning test set ID, for locked test files and the approved test set files themselves."""
    out = {}
    for s in approved_sets():
        out[norm(s["path"])] = s["id"]
        for f in s["files"]:
            n = norm(f)
            if n:
                out[n] = s["id"]
    return out


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=30)


def check():
    problems = []
    sets = approved_sets()
    for s in sets:
        label = f"{s['id']} v{s['version']}"
        if not s["files"]:
            problems.append(f"{label}: Approved but lists no Test Files")
            continue
        if not s["commit"]:
            problems.append(f"{label}: Approved but has no Test Commit SHA")
            continue
        if git("cat-file", "-e", f"{s['commit']}^{{commit}}").returncode != 0:
            problems.append(f"{label}: Test Commit {s['commit']} not found (history rewritten, or CI checkout is shallow)")
            continue
        for f in s["files"]:
            if not (ROOT / f).exists():
                problems.append(f"{label}: locked test file missing: {f}")
        changed = git("diff", "--name-only", s["commit"], "--", *s["files"]).stdout.split()
        for f in changed:
            problems.append(f"{label}: locked test file changed since {s['commit'][:10]}: {f}")
    for p in problems:
        print(f"FAIL  {p}")
    print(f"Locked tests: {len(sets)} approved test set(s), {len(problems)} violation(s).")
    return 1 if problems else 0


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "list":
        for s in approved_sets():
            print(f"{s['id']} v{s['version']} @ {s['commit'] or '-'}")
            for f in s["files"]:
                print(f"  {f}")
        return 0
    if cmd == "check":
        return check()
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
