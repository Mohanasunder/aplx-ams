#!/usr/bin/env python3
"""Throwaway spikes: time-boxed experiments on spike/spk-S-N-slug branches that are never merged.

A spike tests an architectural or design option in code before its ADR is written. All spike
records live in the single collection file docs/03-architecture/spikes.md as ## Spike S-N: sections.
Lifecycle:
  1. A producer appends a ## Spike S-N: section to docs/03-architecture/spikes.md:
     question, options, time box, success criteria.
  2. The phase approver approves it with /approve.
  3. 'start' creates spike/spk-S-N-slug from main. Spike commits start with 'SPK-S-N:'. No PR, no merge.
  4. The producer records Findings and Recommendation in the spike's section, then writes the ADR
     that cites SPK S-N.
  5. The human approves the spike section and the ADR. 'close --delete' deletes the branch.

Usage:
  python3 scripts/spike.py start SPK-S-N           (e.g. SPK-S-1)
  python3 scripts/spike.py check                   # CI and /sdlc-status: no spike work in main, time boxes, branches deleted
  python3 scripts/spike.py close SPK-S-N [--delete]  # Approved ADR cites the spike; delete the local branch
Exit code 1 on any violation.
"""
import re
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sdlc_lib import DOCS, ROOT, read_artifact, sections, strip_comments  # noqa: E402

SPIKE_FILE = DOCS / "03-architecture" / "spikes.md"

_SPIKE_META_RE = re.compile(r"<!--\s*spike_(\w+):\s*(.*?)\s*-->")


def _subsections(content):
    """Split spike section content on '### ' headings → [(heading, content)]."""
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


def _spike_meta(content):
    """Return dict of spike_* keys from <!-- spike_key: value --> comments in section content."""
    return {m.group(1): m.group(2) for m in _SPIKE_META_RE.finditer(content)}


def _set_spike_meta(sub_id, updates):
    """Update or insert <!-- spike_key: value --> comments in the ## Spike sub_id: section."""
    text = SPIKE_FILE.read_text(encoding="utf-8")
    lines = text.splitlines()
    header_pat = re.compile(rf"^## Spike {re.escape(sub_id)}:", re.I)
    header_idx = next((i for i, ln in enumerate(lines) if header_pat.match(ln)), None)
    if header_idx is None:
        raise ValueError(f"Section '## Spike {sub_id}:' not found in {SPIKE_FILE}")
    remaining = dict(updates)
    # Update existing comment lines within this section
    i = header_idx + 1
    while i < len(lines) and not lines[i].startswith("## "):
        m = _SPIKE_META_RE.match(lines[i].strip())
        if m and m.group(1) in remaining:
            lines[i] = f"<!-- spike_{m.group(1)}: {remaining.pop(m.group(1))} -->"
        i += 1
    # Insert new keys just after the section header
    insert_at = header_idx + 1
    for k, v in remaining.items():
        lines.insert(insert_at, f"<!-- spike_{k}: {v} -->")
        insert_at += 1
    SPIKE_FILE.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""), encoding="utf-8")


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=30)


def max_days():
    pm = ROOT / "project.md"
    m = re.search(r"^max_spike_days:\s*(\d+)", pm.read_text(encoding="utf-8"), re.M) if pm.exists() else None
    return int(m.group(1)) if m else 5


def spikes():
    """Read all ## Spike S-N: sections from SPIKE_FILE; return dict keyed by 'SPK-S-N'."""
    if not SPIKE_FILE.exists():
        return {}
    fm_file, body, _ = read_artifact(SPIKE_FILE)
    if not fm_file or fm_file.get("template") != "spike":
        return {}
    out = {}
    for heading, content in sections(body):
        m = re.match(r"^Spike (S-\d+):\s*(.+)", heading)
        if not m:
            continue
        sub_id, title = m.group(1), m.group(2).strip()  # "S-1", "Cache test"
        sid = f"SPK-{sub_id}"                            # "SPK-S-1"
        meta = _spike_meta(content)
        s = {h: strip_comments(c) for h, c in _subsections(content)}
        tb = re.search(r"(\d+)\s*(?:working\s+|business\s+)?days?", s.get("Time Box", ""), re.I)
        out[sid] = {
            "path": SPIKE_FILE,
            "sub_id": sub_id,
            "fm": {
                "id": sid,
                "title": title,
                "status": meta.get("status", "Draft"),
                "spike_branch": meta.get("branch", ""),
                "spike_started": meta.get("started", ""),
                "spike_closed": meta.get("closed", ""),
            },
            "s": s,
            "days": int(tb.group(1)) if tb else None,
        }
    return out


def slug(title):
    words = re.findall(r"[a-z0-9]+", title.lower())[:4]
    return "-".join(words) or "spike"


def adr_citing(sid):
    """Approved ADRs that cite the spike (citation format: SPK S-N with space)."""
    cite = sid.replace("SPK-S-", "SPK S-")  # "SPK-S-1" → "SPK S-1"
    hits = []
    for p in DOCS.rglob("*.md"):
        try:
            fm, body, _ = read_artifact(p)
        except Exception:
            continue
        if fm and fm.get("template") == "adr" and fm.get("status") == "Approved" and re.search(rf"\b{re.escape(cite)}\b", body):
            hits.append(fm["id"])
    return hits


def branches():
    local = [b.strip().lstrip("* ").strip() for b in git("branch", "--list", "spike/*").stdout.splitlines() if b.strip()]
    remote = [b.strip().replace("origin/", "", 1) for b in git("branch", "-r", "--list", "origin/spike/*").stdout.splitlines() if b.strip()]
    return set(local), set(remote)


def spike_branches(sid, fm, local, remote):
    """Branches of a spike: the recorded one plus any named spike/spk-S-N-*, local or on origin."""
    prefix = "spike/" + sid.replace("SPK-S-", "spk-s-").lower() + "-"  # "spike/spk-s-1-"
    names = {b for b in local | remote if b.startswith(prefix)}
    if fm.get("spike_branch"):
        names.add(fm["spike_branch"])
    return {b for b in names if b in local or b in remote}


def cmd_start(sid):
    sp = spikes().get(sid)
    if not sp:
        print(f"FAIL  {sid}: no '## Spike {sid.replace('SPK-', '')}:' section in {SPIKE_FILE.relative_to(ROOT).as_posix()}")
        return 1
    fm = sp["fm"]
    problems = []
    if fm.get("status") != "Approved":
        problems.append(f"{sid} is {fm.get('status')}; the phase approver must approve the spike plan first (/approve)")
    if fm.get("spike_branch"):
        problems.append(f"{sid} already started on {fm['spike_branch']}")
    if sp["days"] is None:
        problems.append(f"{sid}: Time Box must state a number of days")
    elif sp["days"] > max_days():
        problems.append(f"{sid}: time box {sp['days']} days > max_spike_days {max_days()} (project.md)")
    if git("status", "--porcelain").stdout.strip():
        problems.append("working tree has uncommitted changes")
    if problems:
        for p in problems:
            print(f"FAIL  {p}")
        return 1
    br = f"spike/{sid.replace('SPK-S-', 'spk-s-').lower()}-{slug(fm.get('title', ''))}"
    if git("rev-parse", "--verify", "--quiet", f"refs/heads/{br}").returncode == 0:
        print(f"FAIL  branch {br} already exists")
        return 1
    for args in (("switch", "main", "--quiet"), ("switch", "-c", br, "--quiet")):
        r = git(*args)
        if r.returncode != 0:
            print(f"FAIL  git {' '.join(args)}: {r.stderr.strip()}")
            return 1
    today = date.today().isoformat()
    _set_spike_meta(sp["sub_id"], {"branch": br, "started": today})
    print(f"Started {br} ({sp['days']} day time box, ends {date.today() + timedelta(days=sp['days'])}).")
    print(f"Commit messages start with '{sid}:'. Never open a PR or merge; close with: python3 scripts/spike.py close {sid} --delete")
    return 0


def cmd_check():
    problems, warns = [], []
    sp = spikes()
    local, remote = branches()
    for b in sorted(local | remote):
        m = re.match(r"spike/(spk-s-\d+)-", b, re.I)
        sid_from_branch = m.group(1).upper().replace("SPK-S-", "SPK-S-") if m else None
        if not m or sid_from_branch not in sp:
            problems.append(f"branch {b} has no spike record (## Spike S-N:) in {SPIKE_FILE.relative_to(ROOT).as_posix()}")
    leaked = git("log", "main", "--oneline", "-E", "--grep=^SPK-S-[0-9]+:")
    if leaked.returncode == 0 and leaked.stdout.strip():
        for ln in leaked.stdout.strip().splitlines():
            problems.append(f"spike commit reached main (spikes are never merged): {ln}")
    today = date.today()
    for sid, s in sorted(sp.items()):
        fm = s["fm"]
        brs = spike_branches(sid, fm, local, remote)
        br = ", ".join(sorted(brs)) or fm.get("spike_branch", "")
        exists = bool(brs)
        if fm.get("spike_closed"):
            if exists:
                problems.append(f"{sid} is closed but {br} still exists: delete it")
            continue
        if not fm.get("spike_branch") and not exists:
            continue  # planned, not started
        try:
            started = date.fromisoformat(fm.get("spike_started", ""))
        except ValueError:
            started = None
        if started and s["days"] is not None and today > started + timedelta(days=s["days"]):
            problems.append(f"{sid}: time box of {s['days']} days ended {started + timedelta(days=s['days'])}; record findings, write the ADR, close the spike")
        if adr_citing(sid) and exists:
            problems.append(f"{sid}: its ADR ({', '.join(adr_citing(sid))}) is Approved but {br} still exists: run spike.py close {sid} --delete")
        if not exists:
            warns.append(f"{sid}: {br} not found locally or on origin, but the spike is not closed")
    for w in warns:
        print(f"WARN  {w}")
    for p in problems:
        print(f"FAIL  {p}")
    print(f"Spikes: {len(sp)} record(s), {len(local | remote)} spike branch(es), {len(problems)} problem(s).")
    return 1 if problems else 0


def cmd_close(sid, delete):
    sp = spikes().get(sid)
    if not sp:
        print(f"FAIL  {sid}: no spike record")
        return 1
    fm, s = sp["fm"], sp["s"]
    problems = []
    for sec in ("Findings", "Recommendation"):
        txt = s.get(sec, "")
        if not txt or txt.lower().startswith("pending") or "<fill" in txt:
            problems.append(f"{sid}: {sec} not recorded")
    if fm.get("status") != "Approved":
        problems.append(f"{sid} is {fm.get('status')}: the human approves the findings with /approve before closing")
    adrs = adr_citing(sid)
    if not adrs:
        problems.append(f"{sid}: no Approved ADR cites {sid.replace('SPK-S-', 'SPK S-')}; the spike closes only once its decision is recorded")
    if problems:
        for p in problems:
            print(f"FAIL  {p}")
        return 1
    local, remote = branches()
    brs = spike_branches(sid, fm, local, remote)
    if not delete:
        print(f"Ready to close {sid} (ADR: {', '.join(adrs)}). Re-run with --delete to delete {', '.join(sorted(brs)) or 'its branch (none found)'}.")
        return 0
    for br in sorted(b for b in brs if b in local):
        if git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip() == br:
            sw = git("switch", "main", "--quiet")
            if sw.returncode != 0:
                print(f"FAIL  still on {br} and cannot switch to main: {sw.stderr.strip().splitlines()[0] if sw.stderr.strip() else 'unknown error'}. "
                      "Commit or stash local changes (the spike record belongs with the other phase docs, not on the spike branch), switch to main, and re-run.")
                return 1
        r = git("branch", "-D", br)
        if r.returncode != 0:
            print(f"FAIL  could not delete {br}: {r.stderr.strip()}")
            return 1
        print(f"Deleted local branch {br}.")
    _set_spike_meta(sp["sub_id"], {"closed": date.today().isoformat()})
    for br in sorted(b for b in brs if b in remote):
        print(f"Remote branch remains. A human runs (push needs confirmation): git push origin --delete {br}")
    print(f"Closed {sid}; decision recorded in {', '.join(adrs)}.")
    return 0


def main():
    a = sys.argv[1:]
    if not a or a[0] not in ("start", "check", "close"):
        print(__doc__)
        return 2
    if a[0] == "check":
        return cmd_check()
    if len(a) < 2:
        print(f"{a[0]} needs SPK-S-N (e.g. SPK-S-1)")
        return 2
    return cmd_start(a[1]) if a[0] == "start" else cmd_close(a[1], "--delete" in a)


if __name__ == "__main__":
    sys.exit(main())
