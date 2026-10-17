#!/usr/bin/env python3
"""Traceability: find orphans from the artifacts themselves, not from the hand-kept matrix.

Usage:
  python3 scripts/traceability.py check [--phase 2|5|7] # default 7; exit 1 on any orphan
  python3 scripts/traceability.py report                # one row per criterion: feature, state, tests, result

Sources:
  Goals            rows whose first cell is G-n (goal not marked 'Removed') in Business Goals And KPIs of Approved
                        business briefs in docs/01-discovery (BRF G-n)
  Epics            'BRF G-n' in Business Value and 'REQ S-N' in Stories of docs/02-requirements/epics.md;
                   a goal is out of scope only when a decision log row's Context names it (DEC-NNN)
  Story criteria   numbered items ('1. Given ...') under ### Acceptance Criteria within each ## Story S-N:
                   section in docs/02-requirements/user-stories.md, skipping Won't priority and items marked
                   'Removed'; item n is REQ S-N AC-n
  Feature criteria 'ID AC-n' lines under Acceptance Criteria in docs/05-build-plan/feature-NNN-*/acceptance.md
  Feature type     'Type: Feature | Enabling | Fix' in plan.md Feature Type; a Fix names its DEF D-N on that
                   line and does not own criteria (it re-proves criteria another feature owns)
  Feature state    the '- State:' line in the feature's status.md
  Feature tests    'ID AC-n' in the Criteria To Tests Map of an Approved docs/06-build/FEAT-NNN-TESTS.md
  Test cases       'REQ S-N AC-n' in ### Linked Criteria within ## Test Case TC-N: sections of
                   docs/07-testing/test-cases.md
  Failures         'TC TC-N' IDs in the Failures section of docs/07-testing/test-execution-report.md
  Matrix           docs/logs/traceability-matrix.md has a row for every in-scope story
  Defects          '- Class:', '- Route:', '- Status:' lines in ### Classification And Route within each
                   ## Defect D-N: section of docs/07-testing/defects.md (<!-- def_status: Rejected --> ignored)
  Threats          rows whose first cell is T-n (not marked 'Removed') in the Threats table of Approved threat
                   models (THR T-n), and rows citing THR T-n in Threat Model Coverage of
                   docs/07-testing/nfr-test-report.md
  Risks            ID, Mitigation, and Status columns of docs/logs/risk-register.md (RSK R-N IDs)

--phase 2: every goal of an Approved brief is cited by an epic whose Stories lists an in-scope user story
(priority not Won't), or a decision (DEC-NNN) puts it out of scope; every epic cites at least one goal, cites
only existing goals, and lists at least one in-scope story. The goal checks also run at --phase 5 and 7.
--phase 5: every story criterion is in exactly one feature, every feature criterion citing a story exists in an
in-scope story, and the matrix has a row per story.
--phase 7: also every feature is Merged, every feature criterion has a test in its Approved test set, every story
criterion is linked to a test case, a test execution report exists, and no linked test case failed in it; every
defect has a Class (Code, Spec, Test, Environment); a Code defect routes to a Fix feature that names it, Merged
once the defect is Fixed or Closed; a Spec defect routes to an existing SCR S-N; no Blocker defect is open;
Won't fix cites DEC-NNN; every threat has a Threat Model Coverage row with a result: Verified, Failed (the row
cites an existing DEF D-N), or Not testable (the row cites an RSK R-N that the risk register marks Accepted with
the tech lead's decision (DEC-NNN)).
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sdlc_lib import DOCS, read_artifact, sections, strip_comments  # noqa: E402

# REQ S-N AC-n format (collection sub-ID)
CRIT = re.compile(r"\b(REQ\s+S-\d+)\s+AC-(\d+)\b")
STORY_ITEM = re.compile(r"^\s*(\d+)[.)]\s+(\S.*)$", re.M)
# TC TC-N format (collection sub-ID)
TC_ID = re.compile(r"\bTC\s+TC-\d+\b")
CLASSES = ("code", "spec", "test", "environment")
WONT_FIX = re.compile(r"won'?t\s+fix", re.I)
THREAT_REF = re.compile(r"\b(THR(?:-\d{3})?(?:\s+\S+)?)\s+T-(\d+)\b")
RESULT = re.compile(r"\b(verified|failed|not testable)\b", re.I)
# BRF is a fixed single-instance ID; goals are cited as 'BRF G-n'
GOAL_REF = re.compile(r"\b(BRF(?:-\d{3})?)\s+G-(\d+)\b")
# REQ S-N format (also accepts legacy REQ-NNN for robustness)
REQ_ID = re.compile(r"\bREQ(?:\s+S-\d+|-\d{3})\b")
DEF_META_RE = re.compile(r"<!--\s*def_(\w+):\s*(.*?)\s*-->")
SCR_SECTION_RE = re.compile(r"^## SCR (S-\d+):\s*", re.M)
SCR_META_RE = re.compile(r"<!--\s*scr_status:\s*(.*?)\s*-->")


def sub_sections(text):
    """Split text into {heading: content} on '### ' headings."""
    out, current, buf = {}, None, []
    for ln in text.splitlines():
        if ln.startswith("### "):
            if current is not None:
                out[current] = "\n".join(buf)
            current, buf = ln[4:].strip(), []
        elif current is not None:
            buf.append(ln)
    if current is not None:
        out[current] = "\n".join(buf)
    return out


def load(path):
    fm, body, _ = read_artifact(path)
    return fm or {}, {h: strip_comments(c) for h, c in sections(body)}


def artifacts(folder, template):
    for p in sorted(folder.rglob("*.md")):
        fm, sec = load(p)
        if fm.get("template") == template and fm.get("id"):
            yield p, fm, sec


def criteria(text):
    return {f"{a} AC-{n}" for a, n in CRIT.findall(text)}


def stories():
    """Read user stories from collection file docs/02-requirements/user-stories.md."""
    out = {}
    p = DOCS / "02-requirements" / "user-stories.md"
    if not p.exists():
        return out
    fm, body, _ = read_artifact(p)
    if not fm:
        return out
    for heading, content in sections(body):
        m = re.match(r"Story (S-\d+):", heading)
        if not m:
            continue
        sub_id = m.group(1)
        story_id = f"REQ {sub_id}"
        sub = sub_sections(content)
        priority = strip_comments(sub.get("Priority", ""))
        if re.match(r"\s*won'?t\b", priority, re.I):
            continue
        ac_text = strip_comments(sub.get("Acceptance Criteria", ""))
        items = STORY_ITEM.findall(ac_text)
        out[story_id] = [f"{story_id} AC-{n}" for n, t in items if not re.match(r"removed\b", t, re.I)]
    return out


def features():
    out = {}
    for d in sorted((DOCS / "05-build-plan").glob("feature-[0-9][0-9][0-9]-*")):
        fid = "FEAT-" + d.name.split("-")[1]
        acc, st, plan = d / "acceptance.md", d / "status.md", d / "plan.md"
        crit = sorted(criteria(load(acc)[1].get("Acceptance Criteria", ""))) if acc.exists() else []
        m = re.search(r"^- State:\s*(.+)$", st.read_text(encoding="utf-8"), re.M) if st.exists() else None
        ftype = load(plan)[1].get("Feature Type", "") if plan.exists() else ""
        t = re.search(r"type:\s*(feature|enabling|fix)\b", ftype, re.I)
        # DEF D-N format for defect references in plan.md
        out[fid] = {"criteria": crit, "state": m.group(1).strip() if m else "",
                    "type": t.group(1).capitalize() if t else "",
                    "defects": set(re.findall(r"DEF\s+D-\d+", ftype))}
    return out


def _field_in(text, key):
    """Extract '- Key: value' from text."""
    m = re.search(rf"^\s*-\s*{key}:\s*(.+)$", text, re.M | re.I)
    return m.group(1).strip() if m else ""


def defects():
    """Read defects from collection file docs/07-testing/defects.md."""
    out = {}
    p = DOCS / "07-testing" / "defects.md"
    if not p.exists():
        return out
    fm, body, _ = read_artifact(p)
    for heading, content in sections(body):
        m = re.match(r"Defect (D-\d+):", heading)
        if not m:
            continue
        sub_id = m.group(1)
        did = f"DEF {sub_id}"
        meta = dict(DEF_META_RE.findall(content))
        if meta.get("status", "").lower() == "rejected":
            continue
        sub = sub_sections(strip_comments(content))
        route_text = sub.get("Classification And Route", "")
        cls_raw = _field_in(route_text, "Class").split()
        sev_raw = meta.get("severity", "").split()
        out[did] = {
            "class": cls_raw[0].lower() if cls_raw else meta.get("class", "").lower(),
            "route": _field_in(route_text, "Route"),
            "status": _field_in(route_text, "Status") or meta.get("status", ""),
            "severity": sev_raw[0].strip(":.,").lower() if sev_raw else "",
        }
    return out


def check_defects(ft):
    problems = []
    # SCRs from collection file docs/logs/spec-changes.md
    scr_file = DOCS / "logs" / "spec-changes.md"
    if scr_file.exists():
        scrs = {m.group(1) for m in SCR_SECTION_RE.finditer(scr_file.read_text(encoding="utf-8"))}
    else:
        scrs = set()
    for did, d in sorted(defects().items()):
        status = d["status"].lower()
        if d["class"] not in CLASSES:
            problems.append(f"{did}: Class must be Code, Spec, Test, or Environment")
        elif d["class"] == "code":
            fixes = [f for f in re.findall(r"FEAT-\d{3}", d["route"])
                     if f in ft and ft[f]["type"] == "Fix" and did in ft[f]["defects"]]
            if not fixes:
                problems.append(f"{did}: a Code defect routes to a Fix feature ('Type: Fix {did}') named in Route")
            elif status.startswith(("fixed", "closed")):
                problems += [f"{did}: marked {d['status']} but {f} is {ft[f]['state'] or 'not started'}, not Merged"
                             for f in fixes if ft[f]["state"] != "Merged"]
        elif d["class"] == "spec":
            # Route should cite SCR S-N format
            cited_scrs = set(re.findall(r"S-\d+", d["route"]))
            if not cited_scrs & scrs:
                problems.append(f"{did}: a Spec defect routes to an existing spec change record (SCR S-N) named in Route")
        if WONT_FIX.search(status) and not re.search(r"DEC-\d{3}", d["status"]):
            problems.append(f"{did}: Won't fix needs the human decision (DEC-NNN) on the Status line")
        if d["severity"] == "blocker" and not (status.startswith("closed") or WONT_FIX.search(status)):
            problems.append(f"{did}: Blocker defect is {d['status'] or 'Open'}, not Closed")
    return problems


def table_cells(ln):
    return [x.strip() for x in ln.strip().strip("|").split("|")] if ln.strip().startswith("|") else []


def threats():
    out = set()
    for _, fm, sec in artifacts(DOCS / "03-architecture", "threat-model"):
        if fm.get("status") == "Approved":
            for ln in sec.get("Threats", "").splitlines():
                c = table_cells(ln)
                m = re.fullmatch(r"(?:THR(?:-\d{3})?\s+)?T-(\d+)", c[0]) if c else None
                if m and not (len(c) > 1 and re.match(r"removed\b", c[1], re.I)):
                    out.add(f"{fm['id']} T-{m.group(1)}")
    return out


def risk_rows():
    p = DOCS / "logs" / "risk-register.md"
    rows = [table_cells(ln) for ln in p.read_text(encoding="utf-8").splitlines()] if p.exists() else []
    # RSK R-N format (collection sub-ID)
    return {c[0]: {"mitigation": c[6], "status": c[7]}
            for c in rows if len(c) >= 8 and re.fullmatch(r"RSK\s+R-\d+", c[0])}


def check_threats():
    th = threats()
    if not th:
        return []
    # TER is a single-instance file
    ter = DOCS / "07-testing" / "test-execution-report.md"
    reports = []
    if ter.exists():
        fm, sec = load(ter)
        if fm.get("status") != "Rejected":
            reports.append((fm.get("date", ""), fm.get("id", "TER"), sec))
    if not reports:
        # fallback: search for any nfr-test-report artifact
        reports = [(fm.get("date", ""), fm["id"], sec)
                   for _, fm, sec in artifacts(DOCS / "07-testing", "nfr-test-report")
                   if fm.get("status") != "Rejected"]
    if not reports:
        return ["no NFR test report under docs/07-testing covers the threat model"]
    _, nid, sec = max(reports)
    rows = {}
    for ln in sec.get("Threat Model Coverage", "").splitlines():
        m, r = THREAT_REF.search(ln), RESULT.search(ln)
        if m and table_cells(ln):
            rows[f"{m.group(1)} T-{m.group(2)}"] = (r.group(1).lower() if r else "", ln)
    known_defects, risks = set(defects()), risk_rows()
    problems = []
    for t in sorted(th):
        if t not in rows:
            problems.append(f"{t}: threat has no row in {nid} Threat Model Coverage")
            continue
        result, ln = rows[t]
        if not result:
            problems.append(f"{t}: result in {nid} must be Verified, Failed, or Not testable")
        elif result == "failed" and not set(re.findall(r"DEF\s+D-\d+", ln)) & known_defects:
            problems.append(f"{t}: control Failed, but its row cites no existing defect (DEF D-N)")
        elif result == "not testable":
            # RSK R-N format
            accepted = [r for r in re.findall(r"RSK\s+R-\d+", ln) if r in risks
                        and risks[r]["status"].lower().startswith("accepted")
                        and re.search(r"DEC-\d{3}", risks[r]["mitigation"] + " " + risks[r]["status"])]
            if not accepted:
                problems.append(f"{t}: Not testable needs a risk (RSK R-N) cited in its row and marked Accepted in "
                                "docs/logs/risk-register.md with the tech lead's decision (DEC-NNN)")
    return problems


def test_set(fid):
    p = DOCS / "06-build" / f"{fid}-TESTS.md"
    if not p.exists():
        return None
    fm, sec = load(p)
    return criteria(sec.get("Criteria To Tests Map", "")) if fm.get("status") == "Approved" else None


def test_cases():
    """Read test cases from collection file docs/07-testing/test-cases.md."""
    out = {}
    p = DOCS / "07-testing" / "test-cases.md"
    if not p.exists():
        return out
    fm, body, _ = read_artifact(p)
    for heading, content in sections(body):
        if not re.match(r"Test Case TC-\d+:", heading):
            continue
        tc_id = "TC " + re.match(r"Test Case (TC-\d+):", heading).group(1)
        sub = sub_sections(strip_comments(content))
        for c in criteria(sub.get("Linked Criteria", "")):
            out.setdefault(c, set()).add(tc_id)
    return out


def failing():
    """Read failures from single-instance test-execution-report.md."""
    ter = DOCS / "07-testing" / "test-execution-report.md"
    if ter.exists():
        fm, sec = load(ter)
        if fm.get("status") != "Rejected":
            return fm.get("id", "TER"), set(TC_ID.findall(sec.get("Failures", "")))
    # fallback: find any test-execution-report artifact
    reports = [(fm.get("date", ""), fm["id"], sec) for _, fm, sec in artifacts(DOCS / "07-testing", "test-execution-report")
               if fm.get("status") != "Rejected"]
    if not reports:
        return None, set()
    _, rid, sec = max(reports)
    return rid, set(TC_ID.findall(sec.get("Failures", "")))


def matrix_rows():
    m = DOCS / "logs" / "traceability-matrix.md"
    if not m.exists():
        return set()
    text = m.read_text(encoding="utf-8")
    # Match 'REQ S-N' format in first column
    return set(re.findall(r"^\|\s*(REQ\s+S-\d+)\s*\|", text, re.M))


def goals():
    """(Approved brief IDs, {'BRF G-n'}) from Business Goals And KPIs; rows marked Removed skipped."""
    briefs, out = [], set()
    for _, fm, sec in artifacts(DOCS / "01-discovery", "business-brief"):
        if fm.get("status") != "Approved":
            continue
        briefs.append(fm["id"])
        for ln in sec.get("Business Goals And KPIs", "").splitlines():
            c = table_cells(ln)
            m = re.fullmatch(r"G-(\d+)", c[0]) if c else None
            if m and not (len(c) > 1 and re.match(r"removed\b", c[1], re.I)):
                out.add(f"{fm['id']} G-{m.group(1)}")
    return briefs, out


def epics():
    """EPC E-N -> (goals cited in Business Value, REQ S-N IDs in Stories); from epics.md collection."""
    p = DOCS / "02-requirements" / "epics.md"
    if not p.exists():
        return {}
    fm, body, _ = read_artifact(p)
    out = {}
    for heading, content in sections(body):
        m = re.match(r"EPC (E-\d+):", heading)
        if not m:
            continue
        eid = f"EPC {m.group(1)}"
        sub = sub_sections(strip_comments(content))
        bv = sub.get("Business Value", "")
        stories_text = sub.get("Stories", "")
        cited_goals = {f"{b} G-{n}" for b, n in GOAL_REF.findall(bv)}
        cited_reqs = set(REQ_ID.findall(stories_text))
        out[eid] = (cited_goals, cited_reqs)
    return out


def scoped_stories():
    """User stories in any status but Won't priority."""
    return set(stories().keys())


def excluded_goals():
    """'BRF G-n' -> DEC-NNN for decision log rows whose Context names the goal."""
    p = DOCS / "logs" / "decision-log.md"
    out = {}
    for ln in p.read_text(encoding="utf-8").splitlines() if p.exists() else []:
        c = table_cells(ln)
        if len(c) >= 7 and re.fullmatch(r"DEC-\d{3}", c[0]):
            for b, n in GOAL_REF.findall(c[6]):
                out[f"{b} G-{n}"] = c[0]
    return out


def check_goals():
    briefs, gs = goals()
    if not briefs:
        return ["no Approved business brief under docs/01-discovery"]
    problems = [f"{b}: no goal IDs (G-n in the first column of Business Goals And KPIs)" for b in briefs
                if not any(g.startswith(f"{b} ") for g in gs)]
    ep, st, out = epics(), scoped_stories(), excluded_goals()
    covered = set()
    for eid, (cited, reqs) in sorted(ep.items()):
        if not cited:
            problems.append(f"{eid}: Business Value cites no brief goal (BRF G-n)")
        problems += [f"{eid}: cites {g}, which is not a goal of an Approved brief" for g in sorted(cited - gs)]
        if reqs & st:
            covered |= cited
        else:
            problems.append(f"{eid}: Stories lists no in-scope user story (REQ S-N)")
    problems += [f"{g}: no epic with an in-scope story covers this goal, and no decision (DEC-NNN) puts it out of scope"
                for g in sorted(gs - covered) if g not in out]
    return problems


def check(phase):
    if phase == 2:
        problems = check_goals()
        for p in problems:
            print(f"FAIL  {p}")
        print(f"Traceability (phase 2 gate): {len(goals()[1])} goals, {len(epics())} epics, {len(problems)} gap(s).")
        return 1 if problems else 0
    st, ft = stories(), features()
    owners, cited = {}, {}
    for fid, f in ft.items():
        for c in f["criteria"]:
            cited.setdefault(c, []).append(fid)
            if f["type"] != "Fix":
                owners.setdefault(c, []).append(fid)
    story_crit = {c for cs in st.values() for c in cs}
    problems = [f"{sid}: no numbered acceptance criteria ('1. Given ...')" for sid, cs in sorted(st.items()) if not cs]
    problems += check_goals()
    for c in sorted(story_crit):
        if c not in owners:
            problems.append(f"{c}: story criterion in no feature")
        elif len(owners[c]) > 1:
            problems.append(f"{c}: in more than one feature ({', '.join(owners[c])})")
    for c, fids in sorted(cited.items()):
        if c.startswith("REQ ") and c not in story_crit:
            problems.append(f"{c}: in {', '.join(fids)} but not a criterion of an Approved, in-scope story")
    rows = matrix_rows()
    problems += [f"{sid}: no row in docs/logs/traceability-matrix.md" for sid in sorted(st) if sid not in rows]
    if phase >= 7:
        for fid, f in sorted(ft.items()):
            if f["state"] != "Merged":
                problems.append(f"{fid}: state is '{f['state'] or 'unknown'}', not Merged")
            ts = test_set(fid)
            if ts is None:
                problems.append(f"{fid}: no Approved test set (docs/06-build/{fid}-TESTS.md)")
                continue
            problems += [f"{c}: no test in {fid}-TESTS Criteria To Tests Map" for c in f["criteria"] if c not in ts]
        tcs = test_cases()
        rid, fails = failing()
        if rid is None:
            problems.append("no test execution report under docs/07-testing")
        for c in sorted(story_crit):
            linked = tcs.get(c, set())
            if not linked:
                problems.append(f"{c}: no test case links it (Linked Criteria)")
            elif linked & fails:
                problems.append(f"{c}: linked test case(s) failed in {rid}: {', '.join(sorted(linked & fails))}")
        problems += check_defects(ft)
        problems += check_threats()
    for p in problems:
        print(f"FAIL  {p}")
    print(f"Traceability (phase {phase} gate): {len(st)} stories, {len(story_crit)} story criteria, "
          f"{len(ft)} features, {len(problems)} orphan(s).")
    return 1 if problems else 0


def report():
    st, ft = stories(), features()
    tcs = test_cases()
    rid, fails = failing()
    owner = {c: fid for fid, f in ft.items() if f["type"] != "Fix" for c in f["criteria"]}
    fixes = {}
    for fid, f in ft.items():
        if f["type"] == "Fix":
            for c in f["criteria"]:
                fixes.setdefault(c, []).append(f"{fid} ({', '.join(sorted(f['defects'])) or 'no DEF'}, {f['state'] or '-'})")
    print("| Criterion | Feature | State | In test set | Test cases | Result | Fixes |")
    print("| --- | --- | --- | --- | --- | --- | --- |")
    for c in sorted({c for cs in st.values() for c in cs} | set(owner) | set(fixes)):
        fid = owner.get(c, "")
        ts = test_set(fid) if fid else None
        linked = sorted(tcs.get(c, set()))
        result = "-" if not linked or rid is None else ("Fail" if set(linked) & fails else "Pass")
        print(f"| {c} | {fid or 'none'} | {ft.get(fid, {}).get('state') or '-'} | {'yes' if ts and c in ts else 'no'} "
              f"| {', '.join(linked) or 'none'} | {result} | {'; '.join(fixes.get(c, [])) or '-'} |")
    return 0


def main():
    args = sys.argv[1:]
    if not args or args[0] not in ("check", "report"):
        print(__doc__)
        return 2
    if args[0] == "report":
        return report()
    phase = 7
    if "--phase" in args:
        i = args.index("--phase")
        phase = int(args[i + 1]) if i + 1 < len(args) and args[i + 1] in ("2", "5", "7") else 0
        if phase == 0:
            print("--phase must be 2, 5, or 7", file=sys.stderr)
            return 2
    return check(phase)


if __name__ == "__main__":
    sys.exit(main())
