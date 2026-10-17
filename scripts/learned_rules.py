#!/usr/bin/env python3
"""Learned rules: recurring review findings become human-approved rules that every builder and reviewer loads.

Flow: every review finding is logged with a category in docs/logs/review-feedback-log.md ->
'recurring' lists categories seen in at least learned_rule_threshold features (project.md) with no rule yet ->
standards-author appends a `## LRN L-N:` section to docs/logs/learned-rules.md (template learned-rule) ->
a human approves it with `/approve docs/logs/learned-rules.md --sub-id L-N` ->
'build' regenerates .ai/standards/learned-rules.md from Approved rules only.

Usage:
  python3 scripts/learned_rules.py recurring   # categories that recur across features and have no rule (exit 1 if any)
  python3 scripts/learned_rules.py build       # regenerate .ai/standards/learned-rules.md from Approved LRN sections
  python3 scripts/learned_rules.py check       # CI: learned-rules.md matches the Approved rules exactly
  python3 scripts/learned_rules.py stats       # rules approved per ISO week, findings per category
"""
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sdlc_lib import DOCS, ROOT, strip_comments  # noqa: E402

FEEDBACK_LOG = DOCS / "logs" / "review-feedback-log.md"
APPROVAL_LOG = DOCS / "logs" / "approval-log.md"
RULES_FILE = DOCS / "logs" / "learned-rules.md"
INDEX = ROOT / ".ai" / "standards" / "learned-rules.md"
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

LRN_SECTION_RE = re.compile(r"^## LRN (L-\d+):\s*(.+)$", re.M)
LRN_META_RE = re.compile(r"<!--\s*lrn_(\w+):\s*(.*?)\s*-->")


def threshold():
    pm = ROOT / "project.md"
    m = re.search(r"^learned_rule_threshold:\s*(\d+)", pm.read_text(encoding="utf-8"), re.M) if pm.exists() else None
    return int(m.group(1)) if m else 2


def table_rows(path):
    """Data rows of the first markdown table in a file, as lists of cells (header and separator skipped)."""
    if not path.exists():
        return []
    rows = []
    for ln in path.read_text(encoding="utf-8").splitlines():
        if not ln.strip().startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", c) for c in cells if c):
            continue
        rows.append(cells)
    return rows[1:] if rows else []


def _section_text(content, sub_id):
    """Return the text of a ## LRN L-N: section, or '' if not found."""
    m = re.search(rf"^## LRN {re.escape(sub_id)}:.*$", content, re.M)
    if not m:
        return ""
    start = m.end()
    nxt = re.search(r"^## LRN L-\d+:", content[start:], re.M)
    return content[start: start + (nxt.start() if nxt else len(content))]


def _heading_text(section_text, heading):
    """Return text under '### Heading' within a section."""
    m = re.search(rf"^### {re.escape(heading)}\s*\n(.*?)(?=\n###|\Z)", section_text, re.S | re.M)
    return m.group(1) if m else ""


def feedback():
    """[{date, feature, source, category, severity, issue}] from the review feedback log."""
    out = []
    for c in table_rows(FEEDBACK_LOG):
        if len(c) >= 6:
            out.append(dict(zip(["date", "feature", "source", "category", "severity", "issue"], c[:6])))
    return out


def rules():
    """[{id, version, status, category, rule, applies, check}] for every learned-rule section."""
    if not RULES_FILE.exists():
        return []
    content = RULES_FILE.read_text(encoding="utf-8")
    out = []
    for m in LRN_SECTION_RE.finditer(content):
        sub_id = m.group(1)
        rid = f"LRN {sub_id}"
        section_text = _section_text(content, sub_id)
        meta = {k: v for k, v in LRN_META_RE.findall(section_text)}
        first = lambda k: next((ln.strip().lstrip("-* ").strip()  # noqa: E731
                                 for ln in strip_comments(_heading_text(section_text, k)).splitlines() if ln.strip()), "")
        out.append({"id": rid, "sub_id": sub_id, "status": meta.get("status", "Draft"),
                    "category": first("Category").strip("`"),
                    "rule": " ".join(strip_comments(_heading_text(section_text, "Rule")).split()),
                    "applies": " ".join(strip_comments(_heading_text(section_text, "Applies To")).split()),
                    "check": " ".join(strip_comments(_heading_text(section_text, "How It Is Checked")).split())})
    return out


def cmd_recurring():
    fb = feedback()
    th = threshold()
    feats = defaultdict(set)
    count = Counter()
    bad = []
    for r in fb:
        cat = r["category"].strip("`").lower()
        if not SLUG.match(cat):
            bad.append(f"{r['date']} {r['feature']}: category '{r['category']}' is not a kebab-case slug")
            continue
        feats[cat].add(r["feature"])
        count[cat] += 1
    covered = {r["category"] for r in rules() if r["status"] != "Rejected"}
    cands = sorted((c for c in feats if len(feats[c]) >= th and c not in covered), key=lambda c: (-len(feats[c]), c))
    for b in bad:
        print(f"WARN  {b}")
    for c in cands:
        print(f"RECUR {c}: {count[c]} finding(s) in {len(feats[c])} feature(s) ({', '.join(sorted(feats[c]))}); no learned rule yet")
    print(f"Recurring categories without a rule: {len(cands)} (threshold: {th} features). Findings logged: {len(fb)}.")
    return 1 if cands else 0


def render():
    approved = [r for r in rules() if r["status"] == "Approved"]
    lines = ["# Learned Rules", "",
             "Generated by `python3 scripts/learned_rules.py build` from Approved LRN sections "
             "in `docs/logs/learned-rules.md`. Do not edit by hand: a rule appears here only after a human approves it with `/approve`.",
             "", "Every builder and the AI reviewer load this file. A violation of a rule here is a Major finding.", ""]
    if not approved:
        lines.append("No learned rules yet.")
    for r in approved:
        lines += [f"## {r['id']}: {r['category']}", "",
                  f"- **Rule:** {r['rule']}", f"- **Applies to:** {r['applies']}", f"- **Checked by:** {r['check']}", ""]
    return "\n".join(lines).rstrip() + "\n"


def cmd_build():
    INDEX.write_text(render(), encoding="utf-8")
    n = sum(1 for r in rules() if r["status"] == "Approved")
    print(f"Wrote {INDEX.relative_to(ROOT).as_posix()} ({n} approved rule(s)).")
    return 0


def cmd_check():
    want = render()
    have = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
    if have.replace("\r\n", "\n") != want:
        print(f"FAIL  {INDEX.relative_to(ROOT).as_posix()} does not match the Approved learned rules. "
              "Run 'python3 scripts/learned_rules.py build'; only Approved rules may appear and the file is never hand-edited.")
        return 1
    print("Learned rules index matches the Approved rules.")
    return 0


def cmd_stats():
    ids = {r["id"] for r in rules()}
    weeks = Counter()
    for c in table_rows(APPROVAL_LOG):
        if len(c) >= 4 and c[1] in ids and c[3].startswith("Approve"):
            try:
                y, m, d = (int(x) for x in c[0][:10].split("-"))
                iso = date(y, m, d).isocalendar()
                weeks[f"{iso[0]}-W{iso[1]:02d}"] += 1
            except ValueError:
                continue
    print("Learned rules approved per week:")
    for w in sorted(weeks):
        print(f"  {w}: {weeks[w]}")
    if not weeks:
        print("  none yet")
    cats = Counter(r["category"].strip("`").lower() for r in feedback())
    print("Review findings per category:")
    for c, n in cats.most_common():
        print(f"  {c}: {n}")
    if not cats:
        print("  none yet")
    return 0


def main():
    cmds = {"recurring": cmd_recurring, "build": cmd_build, "check": cmd_check, "stats": cmd_stats}
    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        print(__doc__)
        return 2
    return cmds[sys.argv[1]]()


if __name__ == "__main__":
    sys.exit(main())
