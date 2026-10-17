#!/usr/bin/env python3
"""Minimal context per session: feature context packs and phase summaries.

Context pack: the 'Context Pack' section of a feature's plan.md, one entry per line ('::' may replace '§'):
  API-001 v1.1 § POST /tickets          (artifact ID, cited version, section or heading text)
  ADR-003 v1.0                          (a whole artifact; keep for short ones)
  docs/04-design/openapi.yaml § /tickets (a file path and a selector)
  src/backend/tickets/service.py        (an existing file the feature changes)
Builders and the AI reviewer load only the rendered pack, CLAUDE.md, the standards, and the feature folder.

Usage:
  python3 scripts/context_pack.py check [FEAT-NNN]   # entries resolve to current Approved artifacts and sections;
                                                     # rendered size within max_context_pack_lines (project.md)
                                                     # (FEAT-NNN from the branch or GITHUB_HEAD_REF when omitted)
  python3 scripts/context_pack.py render FEAT-NNN    # print the pack excerpts (what the Orchestrator passes to builders)
  python3 scripts/context_pack.py summaries [N ...]  # phase SUMMARY.md exists and indexes every Approved artifact
                                                     # in the phase folder at its current version
Exit code 1 on any violation.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sdlc_lib import DOCS, ROOT, read_artifact, sections, strip_comments  # noqa: E402
from spec_impact import CITE, git_branch, load, ver  # noqa: E402

PLAN_DIR = DOCS / "05-build-plan"
ENTRY = re.compile(r"^(?P<ref>[A-Z]{2,5}-\d{3}(?:-[A-Z0-9]+)?\s+v\d+\.\d+|[^\s§:]+)\s*(?:(?:§|::)\s*(?P<sel>.+))?$")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
SUMMARY_PHASES = [1, 2, 3, 4, 5, 7, 8, 9]  # Phase 0: project.md; Phase 6: per-feature PR descriptions
NOT_INDEXED = {"phase-summary", "phase-input-brief", "interview-record", "input-readiness-checklist",
               "validation-report", "feature-status", "feature-tasks"}


def budget():
    pm = ROOT / "project.md"
    m = re.search(r"^max_context_pack_lines:\s*(\d+)", pm.read_text(encoding="utf-8"), re.M) if pm.exists() else None
    return int(m.group(1)) if m else 400


def feature_dir(fid):
    hits = sorted(PLAN_DIR.glob(f"feature-{fid[5:]}-*"))
    return hits[0] if hits else None


def pack_entries(fid):
    d = feature_dir(fid)
    if not d or not (d / "plan.md").exists():
        return None
    _, body, _ = read_artifact(d / "plan.md")
    txt = strip_comments(dict(sections(body)).get("Context Pack", ""))
    out = []
    for ln in txt.splitlines():
        s = ln.strip().lstrip("-*").strip().replace("`", "")
        if not s or s.lower().startswith("not applicable"):
            continue
        m = ENTRY.match(s)
        if m:
            out.append((s, m.group("ref").strip(), (m.group("sel") or "").strip()))
        else:
            out.append((s, None, None))
    return out


def extract(lines, sel):
    """Return the lines for a selector: a heading block, else a line plus its indented (YAML) or contiguous block."""
    low = sel.lower()
    for i, ln in enumerate(lines):
        h = HEADING.match(ln)
        if h and low in h.group(2).lower():
            lvl = len(h.group(1))
            j = i + 1
            while j < len(lines):
                h2 = HEADING.match(lines[j])
                if h2 and len(h2.group(1)) <= lvl:
                    break
                j += 1
            return lines[i:j]
    for i, ln in enumerate(lines):
        if low in ln.lower():
            ind = len(ln) - len(ln.lstrip())
            j = i + 1
            while j < len(lines) and lines[j].strip() and (len(lines[j]) - len(lines[j].lstrip()) > ind or ind == 0 and not HEADING.match(lines[j])):
                j += 1
            return lines[i:j]
    return None


def resolve(fid):
    """[(entry, excerpt_lines or None, problem or None)]"""
    entries = pack_entries(fid)
    if entries is None:
        return None
    arts = load()
    out = []
    for raw, ref, sel in entries:
        if ref is None:
            out.append((raw, None, "unreadable entry (use 'ID vX.Y § section' or 'path § selector')"))
            continue
        cm = CITE.fullmatch(ref)
        if cm:
            aid, cv = cm.group(1), cm.group(2)
            a = arts.get(aid)
            if not a:
                out.append((raw, None, f"{aid} does not exist"))
                continue
            if a["status"] != "Approved":
                out.append((raw, None, f"{aid} is {a['status']} at v{a['version']} (not Approved)"))
                continue
            if ver(cv) != ver(a["version"]):
                out.append((raw, None, f"{aid} cited at v{cv}; approved version is v{a['version']}"))
                continue
            lines = a["path"].read_text(encoding="utf-8").splitlines()
        else:
            p = ROOT / ref
            if not p.exists():
                out.append((raw, None, f"file not found: {ref}"))
                continue
            lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
        if sel:
            ex = extract(lines, sel)
            if ex is None:
                out.append((raw, None, f"section or selector not found: '{sel}'"))
                continue
        else:
            ex = lines
        out.append((raw, ex, None))
    return out


def feature_from_branch(fid):
    if fid:
        return fid
    m = re.match(r"(?:feature|fix|hotfix)/(FEAT-\d{3})", git_branch())
    return m.group(1) if m else None


def cmd_check(fid):
    fid = feature_from_branch(fid)
    if not fid:
        print("check: no FEAT-NNN given and the branch is not feature/FEAT-NNN-slug; skipping")
        return 0
    res = resolve(fid)
    if res is None:
        print(f"FAIL  {fid}: no plan.md found")
        return 1
    problems = [f"{fid}: {raw}: {prob}" for raw, _, prob in res if prob]
    if not res:
        problems.append(f"{fid}: Context Pack is empty")
    total = sum(len(ex) for _, ex, _ in res if ex)
    lim = budget()
    if total > lim:
        problems.append(f"{fid}: rendered pack is {total} lines > max_context_pack_lines {lim}: narrow the selectors or split the feature")
    for p in problems:
        print(f"FAIL  {p}")
    print(f"Context pack {fid}: {len(res)} entr(ies), {total} lines (limit {lim}), {len(problems)} problem(s).")
    return 1 if problems else 0


def cmd_render(fid):
    res = resolve(fid)
    if res is None:
        print(f"{fid}: no plan.md found", file=sys.stderr)
        return 1
    print(f"# Context pack for {fid}\n\nLoad only this pack, CLAUDE.md, the standards, and the feature folder. "
          f"If something you need is missing, stop and report it as a plan gap.\n")
    bad = 0
    for raw, ex, prob in res:
        print(f"## {raw}\n")
        if prob:
            bad += 1
            print(f"UNRESOLVED: {prob}\n")
        else:
            print("\n".join(ex).rstrip() + "\n")
    return 1 if bad else 0


def cmd_summaries(phases):
    arts = load()
    problems = []
    for n in phases or SUMMARY_PHASES:
        folders = sorted(DOCS.glob(f"{n:02d}-*"))
        if not folders:
            continue
        folder = folders[0]
        approved = {aid: a for aid, a in arts.items()
                    if folder in a["path"].parents and a["status"] == "Approved" and a["template"] not in NOT_INDEXED}
        summ = folder / "SUMMARY.md"
        if not approved:
            continue
        if not summ.exists():
            problems.append(f"Phase {n}: {len(approved)} Approved artifact(s) but no {summ.relative_to(ROOT).as_posix()}")
            continue
        fm, body, _ = read_artifact(summ)
        docs = strip_comments(dict(sections(body)).get("Documents", ""))
        cited = dict(CITE.findall(docs))
        for aid, a in sorted(approved.items()):
            if aid not in cited:
                problems.append(f"Phase {n}: SUMMARY.md Documents does not list {aid} v{a['version']}")
            elif ver(cited[aid]) != ver(a["version"]):
                problems.append(f"Phase {n}: SUMMARY.md lists {aid} v{cited[aid]}; current is v{a['version']}")
        lines = len(body.splitlines())
        if lines > 120:
            problems.append(f"Phase {n}: SUMMARY.md body is {lines} lines; keep it to about half a page (decisions, constraints, open items, index)")
    for p in problems:
        print(f"FAIL  {p}")
    print(f"Phase summaries: {len(problems)} problem(s).")
    return 1 if problems else 0


def main():
    a = sys.argv[1:]
    if not a or a[0] not in ("check", "render", "summaries"):
        print(__doc__)
        return 2
    if a[0] == "check":
        return cmd_check(a[1] if len(a) > 1 else None)
    if a[0] == "render":
        if len(a) < 2:
            print("render needs FEAT-NNN")
            return 2
        return cmd_render(a[1])
    return cmd_summaries([int(x) for x in a[1:]])


if __name__ == "__main__":
    sys.exit(main())
