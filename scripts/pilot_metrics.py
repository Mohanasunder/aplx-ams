#!/usr/bin/env python3
"""Pilot measures, computed from the project's own logs (no manual tallying).

  1. First-pass acceptance: share of feature PRs approved with no human change request and no earlier rejection
     (review-feedback-log.md human rows, approval-log.md PR decisions)
  2. Spec-gap rework: spec change records triggered during build, test, or operation (Trigger cites FEAT-,
     DEF D-N, or INC I-N), and the features their Impact names
  3. Learned rules added per week (learned-rule approvals)
  4. Human review time per feature: minutes the reviewer reports in /approve ('[review: N min]' in approval-log.md)

PR approval log rows use artifact ID 'PRD FEAT-NNN' (e.g. 'PRD FEAT-001'); the approval log is the source of truth.

Targets are set in project.md after two weeks of baseline (pilot_target_* keys).

Usage:
  python3 scripts/pilot_metrics.py show      # print the weekly table
  python3 scripts/pilot_metrics.py report    # also write docs/logs/pilot-metrics.md
"""
import re
import statistics
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sdlc_lib import DOCS, ROOT, read_artifact, sections, strip_comments  # noqa: E402

APPROVAL_LOG = DOCS / "logs" / "approval-log.md"
FEEDBACK_LOG = DOCS / "logs" / "review-feedback-log.md"
OUT = DOCS / "logs" / "pilot-metrics.md"
TARGET_KEYS = ["pilot_target_first_pass_pct", "pilot_target_review_minutes",
               "pilot_target_spec_gap_scrs_per_week", "pilot_target_rules_per_week"]


def rows(path):
    if not path.exists():
        return []
    out = []
    for ln in path.read_text(encoding="utf-8").splitlines():
        if ln.strip().startswith("|"):
            c = [x.strip() for x in ln.strip().strip("|").split("|")]
            if not all(re.fullmatch(r":?-{3,}:?", x) for x in c if x):
                out.append(c)
    return out[1:]


def week(d):
    try:
        y, m, dd = (int(x) for x in d[:10].split("-"))
        iso = date(y, m, dd).isocalendar()
        return f"{iso[0]}-W{iso[1]:02d}"
    except ValueError:
        return None


def artifacts(template):
    out = {}
    for p in DOCS.rglob("*.md"):
        try:
            fm, body, _ = read_artifact(p)
        except Exception:
            continue
        if fm and fm.get("template") == template:
            out[fm["id"]] = (fm, {h: strip_comments(c) for h, c in sections(body)}, body)
    return out


def targets():
    pm = ROOT / "project.md"
    txt = pm.read_text(encoding="utf-8") if pm.exists() else ""
    out = {}
    for k in TARGET_KEYS:
        m = re.search(rf"^{k}:\s*([0-9.]+)\s*$", txt, re.M)
        if m:
            out[k] = float(m.group(1))
    return out


def _pr_feat_map():
    """Build {approval-log-id: FEAT-NNN} from pr-descriptions.md sections.

    Approval log rows for PR approvals carry artifact ID 'PRD FEAT-NNN'.
    """
    prd_file = DOCS / "06-build" / "pr-descriptions.md"
    out = {}
    if not prd_file.exists():
        return out
    try:
        fm_file, body, _ = read_artifact(prd_file)
    except Exception:
        return out
    if not fm_file or fm_file.get("template") != "pr-description":
        return out
    for heading, _ in sections(body):
        m = re.match(r"^PR (FEAT-\d{3}):", heading)
        if m:
            feat = m.group(1)
            out[f"PRD {feat}"] = feat
    return out


def compute():
    appr = rows(APPROVAL_LOG)  # ts, id, version, decision, approver, role, validation, conditions, comments
    pr_feat = _pr_feat_map()  # {"PRD FEAT-001": "FEAT-001", ...}
    human_cr = defaultdict(int)
    for c in rows(FEEDBACK_LOG):
        if len(c) >= 3 and c[2].lower() == "human":
            human_cr[c[1]] += 1
    W = defaultdict(lambda: {"prs": 0, "first": 0, "minutes": [], "scrs": 0, "feats": set(), "rules": 0})
    rejected_feats, minutes_by_feat, feat_week = set(), defaultdict(int), {}
    for c in appr:
        if len(c) < 9:
            continue
        ts, aid, decision, comments = c[0], c[1], c[3], c[8]
        if aid in pr_feat:
            feat = pr_feat[aid]
            m = re.search(r"\[review:\s*(\d+)\s*min\]", comments)
            if m:
                minutes_by_feat[feat] += int(m.group(1))
            if decision == "Reject":
                rejected_feats.add(feat)
            elif decision.startswith("Approve") and week(ts):
                w = week(ts)
                feat_week[feat] = w
                W[w]["prs"] += 1
                if feat not in rejected_feats and human_cr.get(feat, 0) == 0:
                    W[w]["first"] += 1
    for feat, w in feat_week.items():
        if minutes_by_feat.get(feat):
            W[w]["minutes"].append(minutes_by_feat[feat])
    # SCR sections from collection file docs/logs/spec-changes.md
    scr_file = DOCS / "logs" / "spec-changes.md"
    if scr_file.exists():
        try:
            scr_fm, scr_body, _ = read_artifact(scr_file)
            scr_date_re = re.compile(r"<!--\s*scr_date:\s*(\d{4}-\d{2}-\d{2})\s*-->")
            trig_re = re.compile(r"###\s+Trigger\s*\n(.*?)(?=\n###|\Z)", re.S)
            for heading, content in sections(scr_body):
                if not re.match(r"SCR S-\d+:", heading):
                    continue
                trig_m = trig_re.search(content)
                trig = trig_m.group(1) if trig_m else ""
                date_m = scr_date_re.search(content)
                d_str = date_m.group(1) if date_m else (scr_fm or {}).get("date", "")
                if re.search(r"\b(FEAT-\d{3}|DEF\s+D-\d+|PRD|INC\s+I-\d+)", trig) and week(d_str):
                    w = week(d_str)
                    W[w]["scrs"] += 1
                    W[w]["feats"].update(re.findall(r"\bFEAT-\d{3}\b", content))
        except Exception:
            pass
    # Learned rules: approval log rows with 'LRN L-N' artifact IDs
    for c in appr:
        if len(c) >= 4 and re.fullmatch(r"LRN\s+L-\d+", c[1]) and c[3].startswith("Approve") and week(c[0]):
            W[week(c[0])]["rules"] += 1
    return W


def render(W):
    t = targets()
    lines = ["# Pilot Metrics", "",
             "Generated by `python3 scripts/pilot_metrics.py report` from the approval log, review feedback log, spec change records, and learned rules. Do not edit by hand.", "",
             "| Week | PRs approved | First-pass acceptance | Avg review min per feature | Spec-gap SCRs | Features reworked | Learned rules added |",
             "| --- | --- | --- | --- | --- | --- | --- |"]
    for w in sorted(W):
        d = W[w]
        fp = f"{100 * d['first'] / d['prs']:.0f}% ({d['first']}/{d['prs']})" if d["prs"] else "-"
        mins = f"{statistics.mean(d['minutes']):.0f}" if d["minutes"] else "-"
        lines.append(f"| {w} | {d['prs']} | {fp} | {mins} | {d['scrs']} | {len(d['feats'])} | {d['rules']} |")
    if not W:
        lines.append("| - | 0 | - | - | 0 | 0 | 0 |")
    lines += ["", "## Targets", ""]
    if t:
        last = W[sorted(W)[-1]] if W else None
        for k in TARGET_KEYS:
            if k not in t:
                continue
            actual = "-"
            if last:
                actual = {"pilot_target_first_pass_pct": f"{100 * last['first'] / last['prs']:.0f}" if last["prs"] else "-",
                          "pilot_target_review_minutes": f"{statistics.mean(last['minutes']):.0f}" if last["minutes"] else "-",
                          "pilot_target_spec_gap_scrs_per_week": str(last["scrs"]),
                          "pilot_target_rules_per_week": str(last["rules"])}[k]
            lines.append(f"- {k}: target {t[k]:g}, latest week {actual}")
    elif len([w for w in W if W[w]["prs"]]) >= 2:
        lines.append("Baseline ready (two or more weeks with approved PRs): the human sets pilot_target_* values in project.md.")
    else:
        lines.append("Collecting baseline: targets are set after two weeks with approved PRs.")
    return "\n".join(lines) + "\n"


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("show", "report"):
        print(__doc__)
        return 2
    text = render(compute())
    print(text)
    if sys.argv[1] == "report":
        OUT.write_text(text, encoding="utf-8")
        print(f"Wrote {OUT.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
