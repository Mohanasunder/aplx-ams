#!/usr/bin/env python3
"""Go / no-go: a production release needs its evidence Approved and a recorded Go decision.

Usage:
  python3 scripts/go_live.py criteria   # Phase 8 checker, before approval: evidence Approved, release tag
                                        # named, traceability.py check --phase 7 passes
  python3 scripts/go_live.py check      # before any production deployment: criteria, the release tag exists
                                        # in git, and a Go is recorded at the checklist's current version
Default: the go-live checklist at docs/08-deployment/go-live-checklist.md (template go-live-checklist, id: GLC).
Exit 1 means NO-GO: do not deploy.

Evidence (at least one Approved artifact each): release readiness report, UAT sign-off, deployment runbook, rollback
plan, operational runbook, monitoring spec, release notes, config validation report.
Release: the checklist's Release section names the tag (vX.Y.Z).
Go: approval-log rows for the checklist's ID at its current version with Decision Approve or 'Approve with conditions',
one by a role naming the release manager and one naming the tech lead (production deploys are Critical), with no
Reject at that version after them. A No-go is a Reject with the reason in its comments.
"""
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sdlc_lib import DOCS, ROOT, read_artifact, sections, strip_comments  # noqa: E402

EVIDENCE = [
    ("release-readiness-report", "release readiness report"), ("uat-signoff", "UAT sign-off"),
    ("deployment-runbook", "deployment runbook"), ("rollback-plan", "rollback plan"),
    ("operational-runbook", "operational runbook"), ("monitoring-spec", "monitoring spec"),
    ("release-notes", "release notes"), ("config-validation-report", "config validation report"),
]
ROLES = {"release manager": re.compile(r"release\s+manager", re.I), "tech lead": re.compile(r"tech(nical)?\s+lead", re.I)}
GO = ("Approve", "Approve with conditions")
TAG = re.compile(r"\bv\d+\.\d+\.\d+\b")


def all_artifacts():
    out = []
    for p in sorted(DOCS.rglob("*.md")):
        fm, body, _ = read_artifact(p)
        if fm and fm.get("template") and fm.get("id"):
            out.append((fm, {h: strip_comments(c) for h, c in sections(body)}))
    return out


def traceability_ok():
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "traceability.py"), "check", "--phase", "7"],
                       capture_output=True, text=True, cwd=ROOT)
    lines = r.stdout.strip().splitlines()
    return r.returncode == 0, lines[-1] if lines else r.stderr.strip()


def criteria(arts, gl):
    approved = {fm["template"] for fm, _ in arts if fm.get("status") == "Approved"}
    problems = [f"no Approved {label}" for t, label in EVIDENCE if t not in approved]
    tag = TAG.search(gl[1].get("Release", ""))
    if not tag:
        problems.append(f"{gl[0]['id']}: the Release section names no release tag (vX.Y.Z)")
    ok, summary = traceability_ok()
    if not ok:
        problems.append(f"traceability.py check --phase 7 fails ({summary})")
    return problems, tag.group(0) if tag else None


def recorded_go(fm):
    gid, ver = fm["id"], fm.get("version")
    problems = []
    if fm.get("status") != "Approved":
        problems.append(f"{gid} v{ver} is {fm.get('status')}, not Approved: no Go recorded")
    log = DOCS / "logs" / "approval-log.md"
    rows = []
    if log.exists():
        for ln in log.read_text(encoding="utf-8").splitlines():
            c = [x.strip() for x in ln.strip().strip("|").split("|")]
            if len(c) >= 6 and c[1] == gid and c[2] == ver:
                rows.append(c)
    last_reject = max((i for i, c in enumerate(rows) if c[3] == "Reject"), default=-1)
    goes = [c for c in rows[last_reject + 1:] if c[3] in GO]
    for role, rx in ROLES.items():
        if not any(rx.search(c[5]) for c in goes):
            problems.append(f"{gid} v{ver}: no Go recorded by the {role} in docs/logs/approval-log.md")
    return problems


def main():
    args = sys.argv[1:]
    if not args or args[0] not in ("criteria", "check"):
        print(__doc__)
        return 2
    arts = all_artifacts()
    # GLC is a fixed single-instance file; prefer the canonical path
    glc_path = DOCS / "08-deployment" / "go-live-checklist.md"
    gls = [a for a in arts if a[0]["template"] == "go-live-checklist"]
    if not gls:
        print("NO-GO  no go-live checklist under docs/")
        return 1
    gl = max(gls, key=lambda a: a[0].get("date", "") + a[0]["id"])
    problems, tag = criteria(arts, gl)
    if args[0] == "check":
        problems += recorded_go(gl[0])
        if tag and subprocess.run(["git", "rev-parse", "--verify", "--quiet", f"refs/tags/{tag}"],
                                  cwd=ROOT, capture_output=True).returncode != 0:
            problems.append(f"release tag {tag} does not exist in git")
    for p in problems:
        print(f"FAIL  {p}")
    what = "Go criteria" if args[0] == "criteria" else "GO" if not problems else "NO-GO"
    verdict = ("met" if not problems else "not met") if args[0] == "criteria" else ""
    print(f"{what} {verdict}".strip() + f": {gl[0]['id']} v{gl[0].get('version')}, release {tag or 'unnamed'}, "
          f"{len(problems)} problem(s).")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
