#!/usr/bin/env python3
"""Change summary check: the PR description reports what the reviewer needs, accurately.

All PR descriptions live in a single collection file docs/06-build/pr-descriptions.md.
Each feature's PR description is a ## PR FEAT-NNN: section with ### sub-headings.
The section must have:
  Requirements Covered   every criterion in acceptance.md ('ID AC-n'), each with a test name in backticks that
                         appears in the approved test set FEAT-NNN-TESTS
  Known Gaps             gaps, or 'None'
  Deviations From Plan   changes beyond the plan, or 'None' (must not be 'None' if files changed outside the plan)
  Blockers               must be 'None' before the PR goes to human review
  Risk Tier And Review Depth
                        the same tier (Standard, High, Critical) as the 'Tier:' line in plan.md's Risk Tier section,
                        so the review depth that log_approval.py enforces comes from the approved plan

Usage:
  python3 scripts/pr_summary.py check [FEAT-NNN] [--base main]   # FEAT-NNN from the branch or GITHUB_HEAD_REF when omitted
Exit code 1 on any violation; 0 (skipped) when the feature has no PR description yet.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sdlc_lib import DOCS, ROOT, read_artifact, sections, strip_comments  # noqa: E402
from check_feature_size import ALWAYS_IN_SCOPE, AC_LINE, feature_dirs, plan_files, section_map, test_set_files, plan_tier  # noqa: E402

BUILD = DOCS / "06-build"
PRD_FILE = BUILD / "pr-descriptions.md"
REQUIRED = ["Requirements Covered", "Known Gaps", "Deviations From Plan", "Blockers"]
PR_TIER = re.compile(r"\b(Critical|High|Standard)\b")


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=30)


def feature_id(arg):
    if arg:
        return arg
    branch = os.environ.get("GITHUB_HEAD_REF") or git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    m = re.match(r"(?:feature|fix|hotfix)/(FEAT-\d{3})", branch)
    return m.group(1) if m else None


def _subsections(content):
    """Split PR section content on '### ' headings → [(heading, content)]."""
    out, current, buf = [], None, []
    for ln in content.splitlines():
        if ln.startswith("### "):
            if current is not None:
                out.append((current, "\n".join(buf)))
            current, buf = ln[4:].strip(), []
        elif current is not None:
            buf.append(ln)
    if current is not None:
        out.append((current, "\n".join(buf)))
    return out


def pr_for(fid):
    """Find the ## PR FEAT-NNN: section in pr-descriptions.md; return (path, pseudo-fm, sections-dict) or None."""
    if not PRD_FILE.exists():
        return None
    fm_file, body, _ = read_artifact(PRD_FILE)
    if not fm_file or fm_file.get("template") != "pr-description":
        return None
    for heading, content in sections(body):
        m = re.match(r"^PR (FEAT-\d{3}):\s*(.*)", heading)
        if m and m.group(1) == fid:
            s = {h: strip_comments(c) for h, c in _subsections(content)}
            pseudo_fm = {"id": f"PRD {fid}", "template": "pr-description"}
            return (PRD_FILE, pseudo_fm, s)
    return None


def is_none(txt):
    return bool(re.fullmatch(r"(none|n/a|not applicable)\b.*", txt.strip(), re.I | re.S))


def check(fid, base):
    fid = feature_id(fid)
    if not fid:
        print("check: no FEAT-NNN given and the branch is not feature/FEAT-NNN-slug; skipping")
        return 0
    pr = pr_for(fid)
    if not pr:
        print(f"{fid}: no PR description yet (docs/06-build/pr-descriptions.md, ## PR {fid}: section); skipping")
        return 0
    path, fm, s = pr
    problems = []
    for sec in REQUIRED:
        txt = s.get(sec, "")
        if not txt or "<fill" in txt:
            problems.append(f"{fm['id']}: section '{sec}' missing or empty (write 'None' when there is nothing to report)")
    dirs = feature_dirs([fid])
    rc = s.get("Requirements Covered", "")
    if dirs and (dirs[0] / "acceptance.md").exists():
        crit = {m.group(0) for m in AC_LINE.finditer(section_map(dirs[0] / "acceptance.md").get("Acceptance Criteria", ""))}
        tests_txt = ""
        tp = BUILD / f"{fid}-TESTS.md"
        if tp.exists():
            tests_txt = tp.read_text(encoding="utf-8")
        for c in sorted(crit):
            line = next((ln for ln in rc.splitlines() if c in ln), None)
            if not line:
                problems.append(f"{fm['id']}: Requirements Covered does not list {c}")
                continue
            names = re.findall(r"`([^`]+)`", line)
            if not names:
                problems.append(f"{fm['id']}: {c} has no test name in backticks")
            elif tests_txt and not any(n in tests_txt for n in names):
                problems.append(f"{fm['id']}: {c} cites {', '.join(names)}, not found in {fid}-TESTS")
    if dirs and (dirs[0] / "plan.md").exists():
        want = plan_tier(section_map(dirs[0] / "plan.md"))
        got = PR_TIER.search(s.get("Risk Tier And Review Depth", "") or s.get("Risk Level", ""))
        if not want:
            problems.append(f"{fm['id']}: {fid} plan.md has no 'Tier: Standard|High|Critical' line under Risk Tier")
        elif not got:
            problems.append(f"{fm['id']}: Risk Tier And Review Depth states no tier; the plan says {want}")
        elif got.group(1) != want:
            problems.append(f"{fm['id']}: PR states tier {got.group(1)}, but the approved plan says {want} "
                            "(a tier change goes through a revised plan, not the PR)")
    blockers = s.get("Blockers", "")
    if blockers and "<fill" not in blockers and not is_none(blockers):
        problems.append(f"{fm['id']}: Blockers listed; resolve them (or route upstream) before human review")
    dev = s.get("Deviations From Plan", "")
    if dirs and dev and is_none(dev):
        allowed = {f.replace("\\", "/") for f in plan_files(dirs[0]) + test_set_files(fid)}
        diff = git("diff", "--name-only", f"{base}...HEAD")
        if diff.returncode == 0:
            outside = [f for f in diff.stdout.split() if f not in allowed and not ALWAYS_IN_SCOPE.search(f)]
            if outside:
                problems.append(f"{fm['id']}: Deviations From Plan says None, but files changed outside the plan: {', '.join(outside)}")
    for p in problems:
        print(f"FAIL  {p}")
    print(f"Change summary {fm['id']}: {len(problems)} problem(s).")
    return 1 if problems else 0


def main():
    a = sys.argv[1:]
    if not a or a[0] != "check":
        print(__doc__)
        return 2
    rest = a[1:]
    base = "main"
    if "--base" in rest:
        i = rest.index("--base")
        base = rest[i + 1]
        rest = rest[:i] + rest[i + 2:]
    return check(rest[0] if rest else None, base)


if __name__ == "__main__":
    sys.exit(main())
