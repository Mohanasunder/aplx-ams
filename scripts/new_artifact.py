#!/usr/bin/env python3
"""Create an artifact from a template with correct metadata.

Usage:
  python3 scripts/new_artifact.py --template user-story --title "Customer can raise a ticket" \
      --author requirements-analyst [--id REQ-007 | --id auto] [--out docs/02-requirements/REQ-007.md]

If --id is omitted or 'auto', the next free ID for the template's prefix is used.
If --out is omitted, the file goes to the template's default folder as <ID>.md.
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sdlc_lib import ROOT, TEMPLATES, next_id, read_artifact  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--template", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--author", required=True, help="agent name, e.g. requirements-analyst")
    ap.add_argument("--id", default="auto")
    ap.add_argument("--out")
    a = ap.parse_args()

    tpl = TEMPLATES / f"{a.template}.md"
    if not tpl.exists():
        print(f"Unknown template '{a.template}'. Available: " + ", ".join(sorted(p.stem for p in TEMPLATES.glob('*.md'))), file=sys.stderr)
        return 2
    tfm, _, text = read_artifact(tpl)
    prefix = tfm["id_prefix"]
    aid = next_id(prefix) if a.id == "auto" else a.id
    if not re.fullmatch(rf"{re.escape(prefix)}-\d{{3}}(-[A-Z0-9]+)?", aid):
        print(f"ID must look like {prefix}-001", file=sys.stderr)
        return 2
    out = Path(a.out) if a.out else ROOT / tfm["default_folder"] / f"{aid}.md"
    if out.exists():
        print(f"{out} already exists; refusing to overwrite", file=sys.stderr)
        return 2

    lines = text.splitlines()
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    fm_out = [
        f"id: {aid}", f"title: {a.title}", f"phase: {tfm['phase']}", "version: 0.1",
        f"template: {a.template}", f"template_version: {tfm['template_version']}",
        "status: Draft", f"author_agent: {a.author}", f"approver: {tfm['default_approver']}",
        f"date: {date.today().isoformat()}", "validation: Pending",
    ]
    body = "\n".join(lines[end + 1:]).replace("# <fill: title>", f"# {a.title}")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("---\n" + "\n".join(fm_out) + "\n---\n" + body.lstrip("\n") + "\n", encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
