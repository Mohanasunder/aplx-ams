#!/usr/bin/env python3
"""Decision log: decisions too small for an ADR, and overrides, each with a named human owner and a reason.

Append-only. Rows are added only by this script (the Orchestrator runs it after a human decides; the permission
prompt is the human's confirmation). Significant or hard-to-reverse decisions still need an ADR.

Usage:
  python3 scripts/log_decision.py add --decision "..." --owner "Name" --reason "..." \\
      [--kind Decision|Override] [--context "FEAT-004, API-001"] [--alternatives "..."]
  python3 scripts/log_decision.py check [--base origin/main]   # well-formed rows, named owners, IDs resolve;
                                                                 # with --base: nothing removed or edited (append-only)
"""
import argparse
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sdlc_lib import ROOT, all_artifact_ids  # noqa: E402

LOG = ROOT / "docs" / "logs" / "decision-log.md"
HEADER = ("# Decision Log\n\nDecisions too small for an ADR, and overrides, each owned by a named human. Append-only: "
          "rows are added only by `python3 scripts/log_decision.py add`. Significant or hard-to-reverse decisions need an ADR instead.\n\n"
          "| ID | Date (UTC) | Kind | Decision | Owner | Reason | Context | Alternatives considered |\n"
          "| --- | --- | --- | --- | --- | --- | --- | --- |\n")
ID_TOKEN = re.compile(r"\b[A-Z]{2,5}-\d{3}(?:-[A-Z0-9]+)?\b")
LOG_IDS = re.compile(r"^(OQ|A|RSK)-\d+$")  # IDs that live in logs, not artifacts


def cell(s):
    return (s or "-").replace("|", "/").replace("\n", " ").strip() or "-"


def rows(text):
    out = []
    for ln in text.splitlines():
        if ln.startswith("| DEC-"):
            out.append([c.strip() for c in ln.strip().strip("|").split("|")])
    return out


def approvers():
    pm = ROOT / "project.md"
    if not pm.exists():
        return set()
    txt = pm.read_text(encoding="utf-8")
    m = re.search(r"## Approvers.*?\n\| Role \| Name \|\n\| --- \| --- \|\n(.*?)(?:\n\n|\Z)", txt, re.S)
    names = set()
    for ln in (m.group(1).splitlines() if m else []):
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        if len(c) >= 2 and c[1]:
            names.update(n.strip() for n in re.split(r"[,;/]", c[1]) if n.strip())
    return names


def cmd_add(a):
    names = approvers()
    if names and a.owner not in names:
        print(f"Refusing: owner '{a.owner}' is not a named approver in project.md ({', '.join(sorted(names))})", file=sys.stderr)
        return 1
    if not names:
        print("WARN  project.md names no approvers yet; recording the owner as given", file=sys.stderr)
    if not LOG.exists():
        LOG.write_text(HEADER, encoding="utf-8")
    existing = rows(LOG.read_text(encoding="utf-8"))
    n = max([int(r[0][4:]) for r in existing if re.fullmatch(r"DEC-\d{3}", r[0])] or [0]) + 1
    did = f"DEC-{n:03d}"
    row = "| " + " | ".join([did, datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"), a.kind, cell(a.decision), cell(a.owner),
                             cell(a.reason), cell(a.context), cell(a.alternatives)]) + " |\n"
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(row)
    print(f"{did}: {a.kind} by {a.owner} recorded in {LOG.relative_to(ROOT).as_posix()}")
    return 0


def cmd_check(base):
    if not LOG.exists():
        print("Decision log: not created yet.")
        return 0
    text = LOG.read_text(encoding="utf-8")
    problems = []
    names = approvers()
    known = set(all_artifact_ids())
    seen = set()
    for r in rows(text):
        if len(r) < 8:
            problems.append(f"{r[0]}: row has {len(r)} columns; expected 8")
            continue
        did, _, kind, decision, owner, reason, context, _ = r[:8]
        if did in seen:
            problems.append(f"{did}: duplicate ID")
        seen.add(did)
        if kind not in ("Decision", "Override"):
            problems.append(f"{did}: kind must be Decision or Override")
        for label, v in (("decision", decision), ("owner", owner), ("reason", reason)):
            if v in ("", "-"):
                problems.append(f"{did}: {label} is empty")
        if names and owner not in names:
            problems.append(f"{did}: owner '{owner}' is not a named approver in project.md")
        for tok in ID_TOKEN.findall(context):
            if tok not in known and not LOG_IDS.match(tok):
                problems.append(f"{did}: context ID {tok} does not resolve to an artifact")
    if base:
        d = subprocess.run(["git", "diff", base, "--", str(LOG.relative_to(ROOT))], cwd=ROOT, capture_output=True, text=True, timeout=30)
        if d.returncode == 0:
            removed = [ln for ln in d.stdout.splitlines() if ln.startswith("-") and not ln.startswith("---")]
            if removed:
                problems.append(f"decision log is append-only: {len(removed)} line(s) removed or edited since {base}")
    for p in problems:
        print(f"FAIL  {p}")
    print(f"Decision log: {len(seen)} decision(s), {len(problems)} problem(s).")
    return 1 if problems else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    ad = sub.add_parser("add")
    ad.add_argument("--decision", required=True)
    ad.add_argument("--owner", required=True)
    ad.add_argument("--reason", required=True)
    ad.add_argument("--kind", choices=["Decision", "Override"], default="Decision")
    ad.add_argument("--context", default="")
    ad.add_argument("--alternatives", default="")
    ck = sub.add_parser("check")
    ck.add_argument("--base")
    a = ap.parse_args()
    return cmd_add(a) if a.cmd == "add" else cmd_check(a.base)


if __name__ == "__main__":
    sys.exit(main())
