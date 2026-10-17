#!/usr/bin/env python3
"""Deterministic validation of SDLC artifacts against their templates.

Usage:
  python3 scripts/validate_artifact.py docs/02-requirements/REQ-001.md [more paths or folders]
  python3 scripts/validate_artifact.py docs/02-requirements --json --check-links

Verdict rules: any Blocker or Major finding -> Fail; only Minor -> Pass with warnings; none -> Pass.
Exit code: 0 for Pass / Pass with warnings, 1 for Fail, 2 for usage errors.
"""
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sdlc_lib import (  # noqa: E402
    FILL, ID_TOKEN, REQUIRED_KEYS, STATUS_VALUES, TEMPLATES, VALIDATION_VALUES,
    all_artifact_ids, read_artifact, sections, strip_comments,
)

VAGUE = [r"\betc\.?", r"\bas needed\b", r"\bappropriate(ly)?\b", r"\band so on\b", r"\bsome kind of\b"]
PLACEHOLDER = [r"\bTBD\b", r"\bTODO\b", r"\bFIXME\b", r"\blorem ipsum\b"]


def finding(sev, where, msg, fix=""):
    return {"severity": sev, "location": where, "description": msg, "suggested_fix": fix}


def collect(paths):
    files = []
    for p in paths:
        pp = Path(p)
        if pp.is_dir():
            files += sorted(x for x in pp.rglob("*.md")
                            if x.name.lower() not in {"readme.md", "checklist.md"}
                            and not ({"logs", "inputs"} & set(x.parts)))  # logs and raw inputs are not artifacts
        elif pp.is_file():
            files.append(pp)
    return files


def validate(path, known_ids, check_links):
    f = []
    fm, body, _ = read_artifact(path)
    if fm is None:
        return [finding("Blocker", "front matter", "Missing YAML front matter", "Create the artifact with scripts/new_artifact.py")]
    for k in REQUIRED_KEYS:
        if k not in fm or not fm[k]:
            f.append(finding("Blocker", f"front matter:{k}", f"Required metadata '{k}' is missing or empty", f"Set '{k}'"))
    for k, v in fm.items():
        if FILL.search(v):
            f.append(finding("Blocker", f"front matter:{k}", "Unfilled placeholder in metadata", f"Fill '{k}'"))
    if fm.get("status") and fm["status"] not in STATUS_VALUES:
        f.append(finding("Major", "front matter:status", f"Invalid status '{fm['status']}'", f"Use one of {STATUS_VALUES}"))
    if fm.get("validation") and fm["validation"] not in VALIDATION_VALUES:
        f.append(finding("Major", "front matter:validation", f"Invalid validation value '{fm['validation']}'", f"Use one of {VALIDATION_VALUES}"))
    if fm.get("date"):
        try:
            datetime.strptime(fm["date"], "%Y-%m-%d")
        except ValueError:
            f.append(finding("Major", "front matter:date", "Date must be YYYY-MM-DD"))
    if fm.get("version") and not re.fullmatch(r"\d+\.\d+", fm["version"]):
        f.append(finding("Minor", "front matter:version", "Version should look like 0.1 or 1.0"))

    tpl_slug = fm.get("template")
    tpl_path = TEMPLATES / f"{tpl_slug}.md" if tpl_slug else None
    if not tpl_path or not tpl_path.exists():
        f.append(finding("Blocker", "front matter:template", f"Unknown template '{tpl_slug}'", "Use a slug from .ai/templates"))
        return f
    tfm, tbody, _ = read_artifact(tpl_path)
    if tfm.get("template_version") and fm.get("template_version") != tfm["template_version"]:
        f.append(finding("Major", "front matter:template_version",
                         f"Artifact used template v{fm.get('template_version')} but current is v{tfm['template_version']}",
                         "Regenerate or migrate to the current template"))
    prefix = tfm.get("id_prefix")
    if prefix and fm.get("id") and not re.fullmatch(rf"{re.escape(prefix)}-\d{{3}}(-[A-Z0-9]+)?", fm["id"]):
        f.append(finding("Major", "front matter:id", f"ID '{fm['id']}' does not match {prefix}-NNN", f"Use {prefix}-001 style"))

    required = [h for h, _ in sections(tbody)]
    found = sections(body)
    # Collection templates use headings like "Persona P-1: <fill: name>"; a filled heading matches by its prefix.
    for t in required:
        if FILL.search(t):
            prefix = FILL.split(t)[0].rstrip()
            found = [(t if h.startswith(prefix) and not FILL.search(h) else h, c) for h, c in found]
    found_map = {h: c for h, c in found}
    order = [h for h, _ in found if h in required]
    for h in required:
        if h not in found_map:
            f.append(finding("Blocker", f"section:{h}", "Required section is missing", f"Add '## {h}' (use 'Not applicable - reason' if it does not apply)"))
            continue
        content = strip_comments(found_map[h])
        if not content:
            f.append(finding("Major", f"section:{h}", "Section is empty", "Fill it or write 'Not applicable - <reason>'"))
            continue
        if FILL.search(content):
            f.append(finding("Blocker", f"section:{h}", "Unfilled <fill: ...> placeholder remains", "Replace the placeholder with real content"))
        if h == "Quality Checklist" and re.search(r"^\s*- \[ \]", content, re.M):
            f.append(finding("Major", "section:Quality Checklist", "Producer self-check has unchecked items", "Complete or justify every item"))
        if h in ("Quality Checklist", "Approval Record"):
            continue  # boilerplate sections: skip placeholder and vague-word scans
        for pat in PLACEHOLDER:
            if re.search(pat, content, re.I):
                f.append(finding("Major", f"section:{h}", f"Placeholder text found ({pat.strip(chr(92)+'b')})", "Replace with content or log an open question"))
                break
        for pat in VAGUE:
            m = re.search(pat, content, re.I)
            if m:
                f.append(finding("Minor", f"section:{h}", f"Vague wording: '{m.group(0)}'", "Be specific or define the term"))
                break
    if order != [h for h in required if h in order]:
        f.append(finding("Minor", "structure", "Sections are not in template order"))

    if check_links and "Traceability Links" in found_map:
        text = strip_comments(found_map["Traceability Links"])
        if not re.match(r"\s*not applicable", text, re.I):
            for tok in sorted(set(ID_TOKEN.findall(text))):
                if tok != fm.get("id") and tok not in known_ids:
                    f.append(finding("Major", "section:Traceability Links", f"Linked ID '{tok}' does not resolve to an artifact", "Fix the ID or create the artifact"))
    return f


def verdict_of(findings):
    sev = {x["severity"] for x in findings}
    if "Blocker" in sev or "Major" in sev:
        return "Fail"
    return "Pass with warnings" if "Minor" in sev else "Pass"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--check-links", action="store_true", help="verify IDs in Traceability Links resolve")
    a = ap.parse_args()
    files = collect(a.paths)
    if not files:
        missing = [p for p in a.paths if not Path(p).exists()]
        if missing:
            print(f"Not found: {', '.join(missing)}", file=sys.stderr)
            return 2
        print("No artifacts to validate yet")
        return 0
    known = all_artifact_ids() if a.check_links else {}
    report, worst = [], "Pass"
    rank = {"Pass": 0, "Pass with warnings": 1, "Fail": 2}
    for p in files:
        fnd = validate(p, known, a.check_links)
        v = verdict_of(fnd)
        worst = max(worst, v, key=rank.get)
        report.append({"artifact": str(p), "verdict": v, "findings": fnd})
    if a.json:
        print(json.dumps({"overall": worst, "results": report}, indent=2))
    else:
        for r in report:
            counts = {s: sum(1 for x in r["findings"] if x["severity"] == s) for s in ("Blocker", "Major", "Minor")}
            print(f"{r['verdict']:<20} {r['artifact']}  (Blocker {counts['Blocker']}, Major {counts['Major']}, Minor {counts['Minor']})")
            for x in r["findings"]:
                print(f"    [{x['severity']}] {x['location']}: {x['description']}" + (f" -> {x['suggested_fix']}" if x["suggested_fix"] else ""))
        print(f"\nOverall: {worst}")
    return 1 if worst == "Fail" else 0


if __name__ == "__main__":
    sys.exit(main())
