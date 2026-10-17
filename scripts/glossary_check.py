#!/usr/bin/env python3
"""Domain glossary check: one meaning per business term, and avoided synonyms kept out of specs and contracts.

The Approved domain glossary (template domain-glossary, GLO-NNN, docs/02-requirements/) has a Terms table:
  | Term | Definition | Avoid | Example | Source |
'Avoid' lists synonyms that must not be used for the term (comma or semicolon separated).

Usage:
  python3 scripts/glossary_check.py check [--code]   # glossary well-formed; no avoided term in Approved artifacts or
                                                     # contract files (docs/04-design/*.yaml|yml|json|sql); --code also scans src/
Matching is word- and identifier-aware: avoiding 'case' flags 'case', 'cases', 'case_id', 'caseId', and 'Case ID'.
Exit code 1 on any violation; 0 (skipped) when no glossary is Approved yet.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sdlc_lib import COMMENT, DOCS, ROOT, read_artifact, sections, strip_comments  # noqa: E402

SKIP_TEMPLATES = {"domain-glossary", "validation-report", "spec-change", "phase-summary"}
CONTRACT_EXT = {".yaml", ".yml", ".json", ".sql"}
CODE_EXT = {".py", ".ts", ".tsx", ".js", ".jsx", ".java", ".cs", ".go", ".sql", ".html", ".json", ".yaml", ".yml"}
ID = re.compile(r"\b[A-Z]{2,5}-\d{3}\b")


def words(text):
    """Lowercase word tokens, splitting snake_case, kebab-case, and camelCase identifiers."""
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", text)
    text = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", text)
    return re.findall(r"[a-z0-9]+", text.lower())


def glossary():
    """(fm, rows) of the latest Approved domain glossary, rows as dicts; or None."""
    found = []
    for p in sorted(DOCS.rglob("*.md")):
        try:
            fm, body, _ = read_artifact(p)
        except Exception:
            continue
        if fm and fm.get("template") == "domain-glossary" and fm.get("status") == "Approved":
            found.append((fm, body))
    if not found:
        return None
    fm, body = found[-1]
    txt = strip_comments(dict(sections(body)).get("Terms", ""))
    rows = []
    for ln in txt.splitlines():
        if not ln.strip().startswith("|"):
            continue
        c = [x.strip() for x in ln.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", x) for x in c if x) or (c and c[0].lower() == "term"):
            continue
        c += [""] * (5 - len(c))
        avoid = [a.strip() for a in re.split(r"[,;]", c[2]) if a.strip() and a.strip() not in ("-", "None", "none")]
        rows.append({"term": c[0], "definition": c[1], "avoid": avoid, "source": c[4]})
    return fm, rows


def phrase_in(tokens, phrase):
    n = len(phrase)
    for i in range(len(tokens) - n + 1):
        window = tokens[i:i + n]
        if window[:-1] == phrase[:-1] and window[-1] in (phrase[-1], phrase[-1] + "s", phrase[-1] + "es"):
            return True
    return False


def targets(code):
    for p in sorted(DOCS.rglob("*.md")):
        try:
            fm, _, text = read_artifact(p)
        except Exception:
            continue
        if fm and fm.get("status") == "Approved" and fm.get("template") not in SKIP_TEMPLATES:
            yield p, COMMENT.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    design = DOCS / "04-design"
    for p in sorted(design.rglob("*")) if design.exists() else []:
        if p.is_file() and p.suffix.lower() in CONTRACT_EXT:
            yield p, p.read_text(encoding="utf-8", errors="replace")
    if code:
        src = ROOT / "src"
        for p in sorted(src.rglob("*")) if src.exists() else []:
            if p.is_file() and p.suffix.lower() in CODE_EXT:
                yield p, p.read_text(encoding="utf-8", errors="replace")


def check(code):
    g = glossary()
    if not g:
        print("Domain glossary: none Approved yet; skipping.")
        return 0
    fm, rows = g
    problems = []
    terms = {r["term"].lower(): r for r in rows}
    if not rows:
        problems.append(f"{fm['id']}: Terms table is empty")
    for r in rows:
        if not r["definition"]:
            problems.append(f"{fm['id']}: term '{r['term']}' has no definition")
        if not ID.search(r["source"]):
            problems.append(f"{fm['id']}: term '{r['term']}' has no source ID (BRF-, REQ-, PER-, BR-)")
        for a in r["avoid"]:
            if a.lower() in terms:
                problems.append(f"{fm['id']}: '{a}' is both a defined term and avoided for '{r['term']}'")
    avoid = [(words(a), a, r["term"]) for r in rows for a in r["avoid"] if words(a)]
    hits = 0
    for path, text in targets(code):
        rel = path.relative_to(ROOT).as_posix()
        for n, ln in enumerate(text.splitlines(), 1):
            toks = words(ln)
            for phrase, raw, term in avoid:
                if phrase_in(toks, phrase):
                    hits += 1
                    if hits <= 50:
                        problems.append(f"{rel}:{n}: '{raw}' is avoided; use '{term}' ({fm['id']})")
    if hits > 50:
        problems.append(f"... and {hits - 50} more")
    for p in problems:
        print(f"FAIL  {p}")
    print(f"Domain glossary {fm['id']} v{fm.get('version')}: {len(rows)} term(s), {len(problems)} problem(s).")
    return 1 if problems else 0


def main():
    a = sys.argv[1:]
    if not a or a[0] != "check":
        print(__doc__)
        return 2
    return check("--code" in a)


if __name__ == "__main__":
    sys.exit(main())
