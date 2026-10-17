#!/usr/bin/env python3
"""Living specifications: spec change records, impact of a spec change, and stale-spec checks.

Artifacts cite their inputs as 'ID vX.Y' (for example 'API v1.0'). An artifact changed after it was
approved (approval-log.md has an approval of it at another version) needs a spec change record
(template spec-change, SCR S-N in docs/logs/spec-changes.md) naming 'ID vOLD -> vNEW'.

Usage:
  python3 scripts/spec_impact.py impact <ARTIFACT-ID>   # who cites it, at which version; affected features
  python3 scripts/spec_impact.py check [FEAT-NNN]       # feature plan/acceptance/test set cite current, Approved versions
                                                        # (FEAT-NNN from the branch or GITHUB_HEAD_REF when omitted)
  python3 scripts/spec_impact.py records                # every artifact changed after approval has an SCR; an SCR that
                                                        # changes an architecture or contract artifact cites a new ADR A-N
  python3 scripts/spec_impact.py stale                  # Approved artifacts that cite outdated versions (re-check list)
  python3 scripts/spec_impact.py log                    # regenerate docs/logs/spec-change-log.md from the SCRs
Exit code 1 on any violation (log: never).
"""
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sdlc_lib import DOCS, ROOT, read_artifact, sections, strip_comments  # noqa: E402

ID = r"[A-Z]{2,5}(?:-\d{3}(?:-[A-Z0-9]+)?|(?:\s+[A-Z0-9]+-\d+)?)"
CITE = re.compile(r"\b([A-Z]{2,5}(?:-\d{3}(?:-[A-Z0-9]+)?)?(?:\s+[A-Z0-9]+-\d+)?)\s+v(\d+\.\d+)\b")
CHANGE = re.compile(r"\b([A-Z]{2,5}(?:-\d{3}(?:-[A-Z0-9]+)?)?(?:\s+[A-Z0-9]+-\d+)?)\s+v(\d+\.\d+)\s*(?:->|→|to)\s*v(\d+\.\d+)\b")
HISTORICAL = {"spec-change", "validation-report", "spike"}  # cite old versions on purpose
ADR_REQUIRED = {"architecture-overview", "adr", "api-spec", "database-design", "deployment-topology", "threat-model"}
APPROVAL_LOG = DOCS / "logs" / "approval-log.md"
SCR_FILE = DOCS / "logs" / "spec-changes.md"
SCR_LOG = DOCS / "logs" / "spec-change-log.md"
PLAN_DIR = DOCS / "05-build-plan"

# Regex for SCR section headings in the collection file
SCR_SECTION_RE = re.compile(r"^## SCR (S-\d+):\s*(.+)$", re.M)
SCR_META_RE = re.compile(r"<!--\s*scr_(\w+):\s*(.*?)\s*-->")
# Regex for ADR sub-ID citations (new format: ADR A-N)
ADR_SUBID_RE = re.compile(r"\bADR\s+(A-\d+)\b")


def ver(v):
    try:
        return tuple(int(x) for x in str(v).split("."))
    except ValueError:
        return (0,)


def load():
    """id -> {path, version, status, template, body}"""
    arts = {}
    for p in sorted(DOCS.rglob("*.md")):
        try:
            fm, body, _ = read_artifact(p)
        except Exception:
            continue
        if fm and fm.get("id"):
            arts[fm["id"]] = {"path": p, "version": fm.get("version", ""), "status": fm.get("status", ""),
                              "template": fm.get("template", ""), "date": fm.get("date", ""),
                              "approver": fm.get("approver", ""), "body": body}
    return arts


def _scr_section_text(content, sub_id):
    """Return the text of a ## SCR S-N: section, or '' if not found."""
    m = re.search(rf"^## SCR {re.escape(sub_id)}:.*$", content, re.M)
    if not m:
        return ""
    start = m.end()
    nxt = re.search(r"^## SCR S-\d+:", content[start:], re.M)
    return content[start: start + (nxt.start() if nxt else len(content))]


def _scr_section_heading_text(content, sub_id, heading):
    """Return text under '### Heading' within an SCR section."""
    section = _scr_section_text(content, sub_id)
    m = re.search(rf"^### {re.escape(heading)}\s*\n(.*?)(?=\n###|\Z)", section, re.S | re.M)
    return m.group(1) if m else ""


def scr_changes():
    """[(scr_id, scr_status, changed_id, from_v, to_v, trigger_line, date, approver)]"""
    if not SCR_FILE.exists():
        return []
    content = SCR_FILE.read_text(encoding="utf-8")
    out = []
    for m in SCR_SECTION_RE.finditer(content):
        sub_id = m.group(1)
        sid = f"SCR {sub_id}"
        section_text = _scr_section_text(content, sub_id)
        meta = {k: v for k, v in SCR_META_RE.findall(section_text)}
        status = meta.get("status", "Draft")
        date = meta.get("date", "")
        approver = meta.get("approver", "-")
        ch_text = strip_comments(_scr_section_heading_text(content, sub_id, "Changed Artifact"))
        trig = strip_comments(_scr_section_heading_text(content, sub_id, "Trigger")).splitlines()
        trigger_line = (trig[0] if trig else "-").replace("|", "/")[:80]
        for cid, fv, tv in CHANGE.findall(ch_text):
            out.append((sid, status, cid, fv, tv, trigger_line, date, approver))
    return out


def body_without_record(body):
    return strip_comments("\n".join(c for h, c in sections(body) if h != "Approval Record"))


def citations(art):
    """[(cited_id, cited_version)] excluding self-references."""
    if art["template"] in HISTORICAL:
        return []
    return [(i, v) for i, v in CITE.findall(body_without_record(art["body"]))]


def rel(p):
    return p.relative_to(ROOT).as_posix()


def git_branch():
    if os.environ.get("GITHUB_HEAD_REF"):
        return os.environ["GITHUB_HEAD_REF"]
    try:
        return subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, timeout=10).stdout.strip()
    except Exception:
        return ""


def feature_of(path):
    m = re.search(r"05-build-plan/feature-(\d{3})-", path.as_posix()) or re.search(r"06-build/FEAT-(\d{3})-", path.as_posix())
    return f"FEAT-{m.group(1)}" if m else None


def feature_state(fid):
    for d in PLAN_DIR.glob(f"feature-{fid[5:]}-*"):
        s = d / "status.md"
        if s.exists():
            m = re.search(r"^- State:\s*(.+)$", s.read_text(encoding="utf-8"), re.M)
            if m:
                return m.group(1).strip()
    return "unknown"


def approvals():
    """id -> set of versions approved (Approve or Approve with conditions)."""
    out = {}
    if not APPROVAL_LOG.exists():
        return out
    # Match both old-style IDs (AAA-NNN) and new space-separated sub-IDs (AAA X-N)
    id_re = re.compile(r"^[A-Z]{2,5}(?:-\d{3}(?:-[A-Z0-9]+)?)?(?:\s+[A-Z0-9]+-\d+)?$")
    for ln in APPROVAL_LOG.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) >= 4 and cells[3].startswith("Approve") and id_re.fullmatch(cells[1] or ""):
            out.setdefault(cells[1], set()).add(cells[2])
    return out


def cmd_impact(target):
    arts = load()
    t = arts.get(target)
    if not t:
        print(f"FAIL  {target}: no artifact with this ID under docs/")
        return 1
    print(f"{target}: current v{t['version']} ({t['status']}) at {rel(t['path'])}")
    rows, feats = [], {}
    for aid, a in arts.items():
        for cid, cv in citations(a):
            if cid == target and aid != target:
                stale = ver(cv) != ver(t["version"])
                rows.append((aid, cv, a["status"], stale, rel(a["path"])))
                f = feature_of(a["path"])
                if f:
                    feats.setdefault(f, []).append(aid)
    if not rows:
        print("No artifact cites it.")
        return 0
    print("\nCited by:")
    for aid, cv, st, stale, p in sorted(set(rows)):
        print(f"  {aid:<18} cites v{cv:<5} {st:<10} {'OUTDATED' if stale else 'current':<9} {p}")
    if feats:
        print("\nAffected features (action by state):")
        action = {"In progress": "stop: set State to Blocked, cite the SCR in Blockers",
                  "In review": "stop review: set State to Blocked; re-test after the change",
                  "Merged": "re-check merged code and tests against the new version; defect or new feature if needed",
                  "Not started": "re-plan before branching"}
        for f in sorted(feats):
            st = feature_state(f)
            print(f"  {f}  [{st}]  {action.get(st, 'review')}  (via {', '.join(sorted(set(feats[f])))})")
    return 0


def cmd_check(fid):
    if not fid:
        m = re.match(r"(?:feature|fix|hotfix)/(FEAT-\d{3})", git_branch())
        if not m:
            print("check: no FEAT-NNN given and the branch is not feature/FEAT-NNN-slug; skipping")
            return 0
        fid = m.group(1)
    arts = load()
    mine = {aid: a for aid, a in arts.items() if feature_of(a["path"]) == fid and not a["path"].name == "status.md"}
    if not mine:
        print(f"FAIL  {fid}: no plan artifacts found")
        return 1
    problems = []
    for aid, a in sorted(mine.items()):
        for cid, cv in citations(a):
            if cid == aid or cid.startswith(f"{fid}-") or cid == fid:
                continue  # the feature's own files
            t = arts.get(cid)
            if not t:
                problems.append(f"{aid}: cites {cid} v{cv}, which does not exist")
            elif t["status"] != "Approved":
                problems.append(f"{aid}: cites {cid}, which is {t['status']} at v{t['version']} (a spec change is in progress: stop)")
            elif ver(cv) != ver(t["version"]):
                problems.append(f"{aid}: cites {cid} v{cv} but the approved version is v{t['version']} (re-plan against the new version)")
    for p in problems:
        print(f"FAIL  {p}")
    print(f"Spec versions for {fid}: {len(mine)} artifact(s) checked, {len(problems)} stale or unapproved citation(s).")
    return 1 if problems else 0


def cmd_records():
    arts = load()
    appr = approvals()
    changes = scr_changes()
    problems = []
    for aid, a in sorted(arts.items()):
        if a["template"] in HISTORICAL or aid not in appr:
            continue
        cur = a["version"]
        if appr[aid] == {cur}:
            continue
        older = [v for v in appr[aid] if ver(v) < ver(cur)]
        if not older:
            continue
        recs = [c for c in changes if c[2] == aid and ver(c[4]) == ver(cur)]
        if not recs:
            problems.append(f"{aid}: v{cur} changes an approved version (v{max(older, key=ver)}) but no spec change record names '{aid} vOLD -> v{cur}'")
        elif a["status"] == "Approved" and not any(r[1] == "Approved" for r in recs):
            problems.append(f"{aid}: v{cur} is Approved but its spec change record ({', '.join(r[0] for r in recs)}) is not")

    if SCR_FILE.exists():
        content = SCR_FILE.read_text(encoding="utf-8")
        for m in SCR_SECTION_RE.finditer(content):
            sub_id = m.group(1)
            sid = f"SCR {sub_id}"
            section_text = _scr_section_text(content, sub_id)
            meta = {k: v for k, v in SCR_META_RE.findall(section_text)}
            status = meta.get("status", "Draft")
            changed = {c[2] for c in changes if c[0] == sid}
            needs = sorted(c for c in changed if arts.get(c, {}).get("template") in ADR_REQUIRED)
            if not needs:
                continue
            rec_text = strip_comments(_scr_section_heading_text(content, sub_id, "Decision Record"))
            # Look for ADR A-N citations (new format)
            adrs = sorted(set(ADR_SUBID_RE.findall(rec_text)))
            changed_adr_subids = {c.split()[-1] for c in changed if c.startswith("ADR ")}
            adrs = [a for a in adrs if a not in changed_adr_subids]
            if not adrs:
                problems.append(f"{sid}: changes {', '.join(needs)} (architecture or contract) but its Decision Record "
                                "cites no new or superseding ADR A-N")
            for a_sub in adrs:
                adr_id = f"ADR A-{a_sub[2:]}" if a_sub.startswith("A-") else f"ADR {a_sub}"
                t = arts.get("ADR")
                if not t or t.get("template") != "adr":
                    # ADR is a collection; check if section exists
                    adr_file = DOCS / "03-architecture" / "adrs.md"
                    if adr_file.exists():
                        adr_content = adr_file.read_text(encoding="utf-8")
                        if not re.search(rf"^## ADR {re.escape(a_sub)}:", adr_content, re.M):
                            problems.append(f"{sid}: Decision Record cites ADR {a_sub}, which is not in docs/03-architecture/adrs.md")
                else:
                    if status == "Approved" and t["status"] != "Approved":
                        problems.append(f"{sid}: is Approved but its ADR {a_sub} is {t['status']}; approve them together")

    for p in problems:
        print(f"FAIL  {p}")
    print(f"Spec change records: {len(changes)} recorded change(s), {len(problems)} unrecorded or unapproved.")
    return 1 if problems else 0


def cmd_stale():
    arts = load()
    rows = []
    for aid, a in sorted(arts.items()):
        if a["status"] != "Approved":
            continue
        for cid, cv in citations(a):
            t = arts.get(cid)
            if t and cid != aid and ver(cv) != ver(t["version"]):
                rows.append(f"{aid} cites {cid} v{cv}; current is v{t['version']} ({t['status']})  {rel(a['path'])}")
    for r in sorted(set(rows)):
        print(f"STALE {r}")
    print(f"Stale citations in Approved artifacts: {len(set(rows))}.")
    return 1 if rows else 0


def cmd_log():
    changes = scr_changes()
    lines = ["# Spec Change Log", "",
             "Generated by `python3 scripts/spec_impact.py log` from the spec change records (docs/logs/spec-changes.md). Do not edit by hand.", "",
             "| SCR | Changed artifact | From | To | Trigger | Status | Date | Approver |",
             "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for sid, st, cid, fv, tv, trig, date, approver in sorted(changes, key=lambda r: r[0]):
        lines.append(f"| {sid} | {cid} | v{fv} | v{tv} | {trig} | {st} | {date} | {approver if st == 'Approved' else '-'} |")
    SCR_LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {rel(SCR_LOG)} ({len(lines) - 6} change(s)).")
    return 0


def main():
    a = sys.argv[1:]
    if not a or a[0] not in ("impact", "check", "records", "stale", "log"):
        print(__doc__)
        return 2
    if a[0] == "impact":
        if len(a) < 2:
            print("impact needs an artifact ID")
            return 2
        return cmd_impact(a[1])
    if a[0] == "check":
        return cmd_check(a[1] if len(a) > 1 else None)
    return {"records": cmd_records, "stale": cmd_stale, "log": cmd_log}[a[0]]()


if __name__ == "__main__":
    sys.exit(main())
