"""Shared helpers for the AI-enabled SDLC scripts (standard library only)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / ".ai" / "templates"
DOCS = ROOT / "docs"

STATUS_VALUES = ["Draft", "In review", "Approved", "Rejected"]
VALIDATION_VALUES = ["Pending", "Pass", "Pass with warnings", "Fail", "Proceeded on Fail"]
ID_TOKEN = re.compile(r"\b[A-Z]{2,5}-\d{3}(?:-[A-Z0-9]+)?\b")
FILL = re.compile(r"<fill:[^>]*>")
COMMENT = re.compile(r"<!--.*?-->", re.S)

REQUIRED_KEYS = [
    "id", "title", "phase", "version", "template", "template_version",
    "status", "author_agent", "approver", "date", "validation",
]


def split_front_matter(text):
    """Return (front_matter_dict, body_text, raw_front_matter_lines) or (None, text, [])."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text, []
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            fm_lines = lines[1:i]
            fm = {}
            for ln in fm_lines:
                if not ln.strip() or ln.lstrip().startswith("#") or ":" not in ln:
                    continue
                k, v = ln.split(":", 1)
                fm[k.strip()] = v.strip().strip('"').strip("'")
            return fm, "\n".join(lines[i + 1:]), fm_lines
    return None, text, []


def read_artifact(path):
    text = Path(path).read_text(encoding="utf-8")
    fm, body, _ = split_front_matter(text)
    return fm, body, text


def set_front_matter(path, updates):
    """Update (or add) front matter keys in-place, preserving order and everything else."""
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path}: no front matter")
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        raise ValueError(f"{path}: unterminated front matter")
    remaining = dict(updates)
    for i in range(1, end):
        if ":" in lines[i]:
            k = lines[i].split(":", 1)[0].strip()
            if k in remaining:
                lines[i] = f"{k}: {remaining.pop(k)}"
    for k, v in remaining.items():
        lines.insert(end, f"{k}: {v}")
        end += 1
    p.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""), encoding="utf-8")


def sections(body):
    """Split a markdown body into ordered [(heading, content)] on '## ' headings."""
    out, current, buf = [], None, []
    for ln in body.splitlines():
        if ln.startswith("## "):
            if current is not None:
                out.append((current, "\n".join(buf)))
            current, buf = ln[3:].strip(), []
        elif current is not None:
            buf.append(ln)
    if current is not None:
        out.append((current, "\n".join(buf)))
    return out


def strip_comments(s):
    return COMMENT.sub("", s).strip()


def all_artifact_ids():
    ids = {}
    for p in DOCS.rglob("*.md"):
        try:
            fm, _, _ = read_artifact(p)
        except Exception:
            continue
        if fm and fm.get("id"):
            ids[fm["id"]] = p
    return ids


def next_id(prefix):
    nums = []
    for aid in all_artifact_ids():
        m = re.fullmatch(rf"{re.escape(prefix)}-(\d{{3}})(?:-[A-Z0-9]+)?", aid)
        if m:
            nums.append(int(m.group(1)))
    return f"{prefix}-{(max(nums) + 1 if nums else 1):03d}"
