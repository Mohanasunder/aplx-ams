#!/usr/bin/env python3
"""Record a human approval decision. Run only on behalf of a named human approver (see /approve).

Usage:
  python3 scripts/log_approval.py --artifact docs/02-requirements/REQ-001.md \
      --decision Approve --approver "Priya N" --role "Product owner" [--comments "..."] [--conditions "..."]

  # Per-spike approval (plan or findings) — --sub-id names the spike section:
  python3 scripts/log_approval.py --artifact docs/03-architecture/spikes.md --sub-id S-1 \
      --decision Approve --approver "Priya N" --role "Architect / tech lead"

  # Per-PR approval — --sub-id names the feature whose PR section to approve:
  python3 scripts/log_approval.py --artifact docs/06-build/pr-descriptions.md --sub-id FEAT-001 \
      --decision Approve --approver "Priya N" --role "Human developer reviewer" \
      --depth Standard --review-minutes 45

  # Per-spec-change approval — --sub-id names the SCR section:
  python3 scripts/log_approval.py --artifact docs/logs/spec-changes.md --sub-id S-1 \
      --decision Approve --approver "Priya N" --role "Architect / tech lead"

  # Per-learned-rule approval — --sub-id names the LRN section:
  python3 scripts/log_approval.py --artifact docs/logs/learned-rules.md --sub-id L-1 \
      --decision Approve --approver "Priya N" --role "Tech lead"

Decisions: Approve | "Approve with conditions" | Reject
PR descriptions (template pr-description): approving requires --depth matching the PR's risk tier
(High or Critical: Deep; Standard: Standard or Deep, or Light for docs, UI copy, or test-covered refactors only);
the confirmed depth is recorded in the approval log comments. PR decisions (approve or reject) also require
--review-minutes: the reviewer's own estimate of time spent reviewing (a pilot measure).
All PR descriptions now live in a single collection file (docs/06-build/pr-descriptions.md); each PR is a
## PR FEAT-NNN: section. Pass --sub-id FEAT-NNN to approve a specific PR section; status is written as
<!-- pr_status: ... --> inside that section. Artifact ID in the approval log is 'PRD FEAT-NNN'.
Approve is refused while validation is Pending or Fail (a user override must first set
validation to 'Proceeded on Fail' via the fail-decision step). This guard is skipped for per-section
approvals (--sub-id), which have no separate file-level validation step.
Updates the artifact's front matter, fills its Approval Record table (decision, approver, role, version, conditions,
comments, timestamp; a second decision at the same version, such as a High or Critical second approver, is appended
after '; '), and appends a row to docs/logs/approval-log.md, which stays the authoritative record.
For per-section approvals (--sub-id), the status is written as an HTML comment inside the section.
"""
import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sdlc_lib import COMMENT, ROOT, read_artifact, set_front_matter  # noqa: E402

LOG = ROOT / "docs" / "logs" / "approval-log.md"
HEADER = (
    "# Approval Log\n\nAppend-only record of human approval decisions (written by scripts/log_approval.py).\n\n"
    "| Timestamp (UTC) | Artifact ID | Version | Decision | Approver | Role | Validation | Conditions | Comments |\n"
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
)


RECORD_FIELDS = ["Decision", "Approver", "Role", "Version", "Conditions", "Comments", "Timestamp"]
RECORD = re.compile(r"^## Approval Record[ \t]*\n(.*?)(?=^## |\Z)", re.M | re.S)
SEPARATOR = re.compile(r":?-{3,}:?")

_SPIKE_META_RE = re.compile(r"<!--\s*spike_(\w+):\s*(.*?)\s*-->")
_PR_META_RE = re.compile(r"<!--\s*pr_(\w+):\s*(.*?)\s*-->")
_SCR_META_RE = re.compile(r"<!--\s*scr_(\w+):\s*(.*?)\s*-->")
_LRN_META_RE = re.compile(r"<!--\s*lrn_(\w+):\s*(.*?)\s*-->")


def cell(s):
    return (s or "-").replace("|", "/").replace("\n", " ")


def fill_record(path, values):
    text = path.read_text(encoding="utf-8")
    m = RECORD.search(text)
    if not m:
        return False
    rows = {}
    for ln in m.group(1).splitlines():
        c = [x.strip() for x in ln.strip().strip("|").split("|")] if ln.strip().startswith("|") else []
        if len(c) >= 2 and c[0] and c[0] != "Field" and not SEPARATOR.fullmatch(c[0]):
            rows[c[0]] = c[1]
    same_version = rows.get("Version") == values["Version"] and rows.get("Decision", "Pending") != "Pending"
    for k in RECORD_FIELDS:
        rows[k] = f"{rows[k]}; {values[k]}" if same_version and k != "Version" else values[k]
    order = RECORD_FIELDS + [k for k in rows if k not in RECORD_FIELDS]
    table = "| Field | Value |\n| --- | --- |\n" + "".join(f"| {k} | {rows[k]} |\n" for k in order)
    rest = text[m.end(1):]
    path.write_text(text[:m.start(1)] + table + ("\n" if rest else "") + rest, encoding="utf-8")
    return True


def _spike_section_meta(text, sub_id):
    """Return {key: value} from <!-- spike_key: ... --> comments in the ## Spike sub_id: section."""
    header_pat = re.compile(rf"^## Spike {re.escape(sub_id)}:", re.I | re.M)
    m = header_pat.search(text)
    if not m:
        return {}
    section = text[m.end():]
    next_h2 = re.search(r"^## ", section, re.M)
    section = section[:next_h2.start()] if next_h2 else section
    return {mm.group(1): mm.group(2) for mm in _SPIKE_META_RE.finditer(section)}


def _set_spike_meta(path, sub_id, updates):
    """Update or insert <!-- spike_key: value --> comments inside the ## Spike sub_id: section."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    header_pat = re.compile(rf"^## Spike {re.escape(sub_id)}:", re.I)
    header_idx = next((i for i, ln in enumerate(lines) if header_pat.match(ln)), None)
    if header_idx is None:
        raise ValueError(f"Section '## Spike {sub_id}:' not found in {path}")
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
    path.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""), encoding="utf-8")


def _extract_pr_section(text, feat_id):
    """Return raw text of the ## PR FEAT-NNN: section."""
    pat = re.compile(rf"^## PR {re.escape(feat_id)}:", re.I | re.M)
    m = pat.search(text)
    if not m:
        return ""
    section = text[m.end():]
    next_h2 = re.search(r"^## ", section, re.M)
    return section[:next_h2.start()] if next_h2 else section


def _pr_subsection(section_text, heading):
    """Return content of ### heading within a PR section."""
    pat = re.compile(rf"^### {re.escape(heading)}\s*$", re.I | re.M)
    m = pat.search(section_text)
    if not m:
        return ""
    rest = section_text[m.end():]
    next_h = re.search(r"^### ", rest, re.M)
    return rest[:next_h.start()] if next_h else rest


def _set_pr_meta(path, feat_id, updates):
    """Update or insert <!-- pr_key: value --> comments inside the ## PR FEAT-NNN: section."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    header_pat = re.compile(rf"^## PR {re.escape(feat_id)}:", re.I)
    header_idx = next((i for i, ln in enumerate(lines) if header_pat.match(ln)), None)
    if header_idx is None:
        raise ValueError(f"Section '## PR {feat_id}:' not found in {path}")
    remaining = dict(updates)
    i = header_idx + 1
    while i < len(lines) and not lines[i].startswith("## "):
        m = _PR_META_RE.match(lines[i].strip())
        if m and m.group(1) in remaining:
            lines[i] = f"<!-- pr_{m.group(1)}: {remaining.pop(m.group(1))} -->"
        i += 1
    insert_at = header_idx + 1
    for k, v in remaining.items():
        lines.insert(insert_at, f"<!-- pr_{k}: {v} -->")
        insert_at += 1
    path.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""), encoding="utf-8")


def _set_scr_meta(path, sub_id, updates):
    """Update or insert <!-- scr_key: value --> comments inside the ## SCR S-N: section."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    header_pat = re.compile(rf"^## SCR {re.escape(sub_id)}:", re.I)
    header_idx = next((i for i, ln in enumerate(lines) if header_pat.match(ln)), None)
    if header_idx is None:
        raise ValueError(f"Section '## SCR {sub_id}:' not found in {path}")
    remaining = dict(updates)
    i = header_idx + 1
    while i < len(lines) and not lines[i].startswith("## "):
        m = _SCR_META_RE.match(lines[i].strip())
        if m and m.group(1) in remaining:
            lines[i] = f"<!-- scr_{m.group(1)}: {remaining.pop(m.group(1))} -->"
        i += 1
    insert_at = header_idx + 1
    for k, v in remaining.items():
        lines.insert(insert_at, f"<!-- scr_{k}: {v} -->")
        insert_at += 1
    path.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""), encoding="utf-8")


def _set_lrn_meta(path, sub_id, updates):
    """Update or insert <!-- lrn_key: value --> comments inside the ## LRN L-N: section."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    header_pat = re.compile(rf"^## LRN {re.escape(sub_id)}:", re.I)
    header_idx = next((i for i, ln in enumerate(lines) if header_pat.match(ln)), None)
    if header_idx is None:
        raise ValueError(f"Section '## LRN {sub_id}:' not found in {path}")
    remaining = dict(updates)
    i = header_idx + 1
    while i < len(lines) and not lines[i].startswith("## "):
        m = _LRN_META_RE.match(lines[i].strip())
        if m and m.group(1) in remaining:
            lines[i] = f"<!-- lrn_{m.group(1)}: {remaining.pop(m.group(1))} -->"
        i += 1
    insert_at = header_idx + 1
    for k, v in remaining.items():
        lines.insert(insert_at, f"<!-- lrn_{k}: {v} -->")
        insert_at += 1
    path.write_text("\n".join(lines) + ("\n" if text.endswith("\n") else ""), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--artifact", required=True)
    ap.add_argument("--decision", required=True, choices=["Approve", "Approve with conditions", "Reject"])
    ap.add_argument("--approver", required=True)
    ap.add_argument("--role", required=True)
    ap.add_argument("--comments", default="")
    ap.add_argument("--conditions", default="")
    ap.add_argument("--sub-id", dest="sub_id",
                    help="section identifier for per-section approval: spike sub-ID (e.g. S-1) for spikes.md, or FEAT-NNN for pr-descriptions.md")
    ap.add_argument("--depth", choices=["Light", "Standard", "Deep"], help="review depth the human confirms they performed (PRs)")
    ap.add_argument("--review-minutes", type=int, help="minutes the reviewer spent on this review (PRs)")
    a = ap.parse_args()

    path = Path(a.artifact)
    if not path.exists():
        print(f"{path} not found", file=sys.stderr)
        return 2
    fm, body, raw = read_artifact(path)
    if not fm:
        print("Artifact has no front matter", file=sys.stderr)
        return 2

    # --- Per-section approval (--sub-id): spike or PR description ---
    if a.sub_id:
        template = fm.get("template")

        if template == "spike":
            sub_id = a.sub_id  # e.g. "S-1"
            existing = _spike_section_meta(raw, sub_id)
            if not existing and f"## Spike {sub_id}:" not in raw and f"## Spike {sub_id.upper()}:" not in raw:
                print(f"Section '## Spike {sub_id}:' not found in {path}", file=sys.stderr)
                return 2
            if a.decision == "Approve with conditions" and not a.conditions:
                print("--conditions is required for 'Approve with conditions'", file=sys.stderr)
                return 2
            new_status = "Rejected" if a.decision == "Reject" else "Approved"
            stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
            _set_spike_meta(path, sub_id, {"status": new_status, "approver": a.approver})
            spike_id = f"SPK {sub_id}"
            LOG.parent.mkdir(parents=True, exist_ok=True)
            if not LOG.exists():
                LOG.write_text(HEADER, encoding="utf-8")
            row = "| " + " | ".join(cell(x) for x in [
                stamp, spike_id, fm.get("version", "-"), a.decision,
                a.approver, a.role, "n/a", a.conditions, a.comments]) + " |\n"
            with LOG.open("a", encoding="utf-8") as fh:
                fh.write(row)
            print(f"{spike_id}: {a.decision} by {a.approver} ({a.role}); status -> {new_status}")
            return 0

        elif template == "pr-description":
            feat_id = a.sub_id  # e.g. "FEAT-001"
            if not re.match(r"FEAT-\d{3}$", feat_id):
                print(f"--sub-id for pr-description must be FEAT-NNN (e.g. FEAT-001), got '{feat_id}'", file=sys.stderr)
                return 2
            if not re.search(rf"^## PR {re.escape(feat_id)}:", raw, re.I | re.M):
                print(f"Section '## PR {feat_id}:' not found in {path}", file=sys.stderr)
                return 2
            if a.review_minutes is None or a.review_minutes < 1:
                print("Refusing: PR approvals need --review-minutes (the reviewer's time spent reviewing, a pilot measure)", file=sys.stderr)
                return 1
            a.comments = f"[review: {a.review_minutes} min] {a.comments}".strip()
            if a.decision != "Reject":
                pr_section = _extract_pr_section(raw, feat_id)
                tier_txt = _pr_subsection(pr_section, "Risk Tier And Review Depth") or _pr_subsection(pr_section, "Risk Level")
                tier = re.search(r"\b(Critical|High|Standard)\b", COMMENT.sub("", tier_txt)) if tier_txt else None
                if not tier:
                    print(f"Refusing to approve: PR section for {feat_id} states no risk tier (Standard, High, Critical)", file=sys.stderr)
                    return 1
                allowed = ["Deep"] if tier.group(1) in ("High", "Critical") else ["Deep", "Standard", "Light"]
                if a.depth not in allowed:
                    print(f"Refusing to approve: a {tier.group(1)} PR needs review depth {' or '.join(allowed)} confirmed by the reviewer "
                          f"(--depth); see .ai/standards/review-and-approval.md", file=sys.stderr)
                    return 1
                a.comments = f"[review depth: {a.depth}, tier {tier.group(1)}] {a.comments}".strip()
            if a.decision == "Approve with conditions" and not a.conditions:
                print("--conditions is required for 'Approve with conditions'", file=sys.stderr)
                return 2
            new_status = "Rejected" if a.decision == "Reject" else "Approved"
            stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
            pr_id = f"PRD {feat_id}"
            _set_pr_meta(path, feat_id, {"status": new_status, "approver": a.approver,
                                          "depth": a.depth or "", "review_minutes": str(a.review_minutes or "")})
            LOG.parent.mkdir(parents=True, exist_ok=True)
            if not LOG.exists():
                LOG.write_text(HEADER, encoding="utf-8")
            row = "| " + " | ".join(cell(x) for x in [
                stamp, pr_id, fm.get("version", "-"), a.decision,
                a.approver, a.role, "n/a", a.conditions, a.comments]) + " |\n"
            with LOG.open("a", encoding="utf-8") as fh:
                fh.write(row)
            print(f"{pr_id}: {a.decision} by {a.approver} ({a.role}); status -> {new_status}")
            return 0

        elif template == "spec-change":
            sub_id = a.sub_id  # e.g. "S-1"
            if not re.match(r"S-\d+$", sub_id):
                print(f"--sub-id for spec-change must be S-N (e.g. S-1), got '{sub_id}'", file=sys.stderr)
                return 2
            if not re.search(rf"^## SCR {re.escape(sub_id)}:", raw, re.M):
                print(f"Section '## SCR {sub_id}:' not found in {path}", file=sys.stderr)
                return 2
            if a.decision == "Approve with conditions" and not a.conditions:
                print("--conditions is required for 'Approve with conditions'", file=sys.stderr)
                return 2
            new_status = "Rejected" if a.decision == "Reject" else "Approved"
            stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
            _set_scr_meta(path, sub_id, {"status": new_status, "approver": a.approver})
            scr_id = f"SCR {sub_id}"
            LOG.parent.mkdir(parents=True, exist_ok=True)
            if not LOG.exists():
                LOG.write_text(HEADER, encoding="utf-8")
            row = "| " + " | ".join(cell(x) for x in [
                stamp, scr_id, fm.get("version", "-"), a.decision,
                a.approver, a.role, "n/a", a.conditions, a.comments]) + " |\n"
            with LOG.open("a", encoding="utf-8") as fh:
                fh.write(row)
            print(f"{scr_id}: {a.decision} by {a.approver} ({a.role}); status -> {new_status}")
            return 0

        elif template == "learned-rule":
            sub_id = a.sub_id  # e.g. "L-1"
            if not re.match(r"L-\d+$", sub_id):
                print(f"--sub-id for learned-rule must be L-N (e.g. L-1), got '{sub_id}'", file=sys.stderr)
                return 2
            if not re.search(rf"^## LRN {re.escape(sub_id)}:", raw, re.M):
                print(f"Section '## LRN {sub_id}:' not found in {path}", file=sys.stderr)
                return 2
            if a.decision == "Approve with conditions" and not a.conditions:
                print("--conditions is required for 'Approve with conditions'", file=sys.stderr)
                return 2
            new_status = "Rejected" if a.decision == "Reject" else "Approved"
            stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
            _set_lrn_meta(path, sub_id, {"status": new_status, "approver": a.approver})
            lrn_id = f"LRN {sub_id}"
            LOG.parent.mkdir(parents=True, exist_ok=True)
            if not LOG.exists():
                LOG.write_text(HEADER, encoding="utf-8")
            row = "| " + " | ".join(cell(x) for x in [
                stamp, lrn_id, fm.get("version", "-"), a.decision,
                a.approver, a.role, "n/a", a.conditions, a.comments]) + " |\n"
            with LOG.open("a", encoding="utf-8") as fh:
                fh.write(row)
            print(f"{lrn_id}: {a.decision} by {a.approver} ({a.role}); status -> {new_status}")
            return 0

        else:
            print(f"--sub-id is only valid for template: spike, pr-description, spec-change, or learned-rule (got '{template}')", file=sys.stderr)
            return 2

    # --- Normal (file-level) approval ---
    validation = fm.get("validation", "Pending")
    if a.decision != "Reject" and validation in ("Pending", "Fail"):
        print(f"Refusing to approve: validation is '{validation}'. Run /validate first; if the user chooses to proceed "
              f"on a Fail, set validation to 'Proceeded on Fail' and log the decision.", file=sys.stderr)
        return 1
    if a.decision == "Approve with conditions" and not a.conditions:
        print("--conditions is required for 'Approve with conditions'", file=sys.stderr)
        return 2

    new_status = "Rejected" if a.decision == "Reject" else "Approved"
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    set_front_matter(path, {"status": new_status, "approver": a.approver})
    filled = fill_record(path, {
        "Decision": cell(a.decision), "Approver": cell(a.approver), "Role": cell(a.role),
        "Version": cell(fm.get("version")), "Conditions": cell(a.conditions or "None"),
        "Comments": cell(a.comments or "None"), "Timestamp": f"{stamp} UTC"})
    if not filled:
        print(f"Note: {path} has no '## Approval Record' section; the decision is in the approval log only", file=sys.stderr)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    if not LOG.exists():
        LOG.write_text(HEADER, encoding="utf-8")
    row = "| " + " | ".join(cell(x) for x in [
        stamp, fm.get("id"), fm.get("version"), a.decision,
        a.approver, a.role, validation, a.conditions, a.comments]) + " |\n"
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(row)
    print(f"{fm.get('id')}: {a.decision} by {a.approver} ({a.role}); status -> {new_status}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
