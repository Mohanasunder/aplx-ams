#!/usr/bin/env python3
"""Feature sizing and scope checks (principle: small, vertical, reviewable units, one agent session each).

Usage:
  python3 scripts/check_feature_size.py size [FEAT-NNN ...]    # Phase 5: every (or the named) feature fits the limits
  python3 scripts/check_feature_size.py scope [FEAT-NNN] [--base main]
                                                              # Phase 6 / CI: branch changes stay within plan.md files
  python3 scripts/check_feature_size.py task0                 # Phase 5 / CI: Task 0 (FEAT-000, Enabling) exists and every
                                                              # other feature depends on it; once Merged, every gate command is set
  python3 scripts/check_feature_size.py packages [FEAT-NNN] [--base main]
                                                              # Phase 6 / CI: every package added or upgraded in package.json
                                                              # or requirements*.txt is named at that version in New Packages
  python3 scripts/check_feature_size.py waves                 # Phase 5 / CI: every feature in exactly one wave, dependencies in
                                                              # earlier waves, no two features in a wave change the same file, and
                                                              # a feature that changes a shared path is alone in its wave
  python3 scripts/check_feature_size.py start FEAT-NNN        # Phase 6 (create-feature-branch.sh): the feature collides with no
                                                              # open feature (In progress, In review, Blocked) on files or shared paths
Shared paths are the first backticked glob on each bullet line of the 'Shared Paths' section of
.ai/standards/coding-standards.md.
Limits come from project.md: max_acceptance_criteria_per_feature, max_source_files_per_feature, max_test_runtime_minutes.
Feature Type in plan.md is 'Type: Feature' (criteria cite REQ S-N stories), 'Type: Enabling' (criteria cite NFR-, TST-,
or STD- IDs instead; Task 0 is FEAT-000), or 'Type: Fix' (fixes the defect DEF D-N named on the same line; its criteria
are the failed ones, copied unchanged; planned after the wave plan, so 'waves' does not require it in a wave).
'size' counts criteria in acceptance.md (lines with 'ID AC-n') and source files listed under
'Files To Create Or Modify' in plan.md (test files, under tests/ or named *test*/*spec*, are not counted).
It also requires 'Open design decisions: None' and 'Expected test runtime: N minutes' (N within the limit) in the
Size Check section, a 'Tier: Standard|High|Critical' line in the Risk Tier section, and filled Out Of Scope and
New Packages sections, and fails a plan that lists a file matching the 'Production Configuration' globs in
coding-standards.md (features never change production configuration; the devops-engineer drafts it in Phase 8).
'scope' and 'packages' take FEAT-NNN from the branch name (feature/FEAT-NNN-slug, or GITHUB_HEAD_REF in CI) when omitted.
Exit code 1 on any violation.
"""
import json
import os
import re
import subprocess
import sys
from fnmatch import fnmatchcase
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sdlc_lib import ROOT, read_artifact, sections, strip_comments  # noqa: E402

PLAN_DIR = ROOT / "docs" / "05-build-plan"
DEFAULTS = {"max_acceptance_criteria_per_feature": 4, "max_source_files_per_feature": 10, "max_test_runtime_minutes": 10}
AC_LINE = re.compile(r"\b((?!FEAT)[A-Z]{2,5})-\d{3}\s+AC-\d+\b")
ENABLING_SOURCES = {"NFR", "TST", "STD"}
GATES = ROOT / ".ai" / "standards" / "automated-gates.md"
CI = ROOT / ".github" / "workflows" / "ci.yml"
BACKTICK = re.compile(r"`([^`]+)`")
TEST_FILE = re.compile(r"(^|/)(tests?|__tests__|e2e)/|(^|[._/-])(test|spec)s?([._-]|$)", re.I)
# Always allowed on a feature branch besides plan.md files
ALWAYS_IN_SCOPE = re.compile(r"^docs/(06-build|logs|validation)/|^docs/05-build-plan/feature-\d{3}-[^/]+/status\.md$")
PKG_LINE = re.compile(r"^\s*-\s*(npm|pypi):\s*(@?[\w.\-/]+)\s+([^\s|]+)", re.M)
REQ_LINE = re.compile(r"^\s*([A-Za-z0-9][\w.\-]*)(?:\[[^\]]*\])?\s*((?:[=<>!~]=?|===)\s*[^\s;#]+(?:\s*,\s*[=<>!~]=?\s*[^\s;#,]+)*)?")
NPM_KEYS = ("dependencies", "devDependencies", "peerDependencies", "optionalDependencies")
STANDARDS = ROOT / ".ai" / "standards" / "coding-standards.md"
OPEN_STATES = {"In progress", "In review", "Blocked"}
WAVE_ROW = re.compile(r"^\|\s*([^|]+?)\s*\|([^|]*)\|", re.M)
TIER_LINE = re.compile(r"^\s*(?:[-*]\s*)?Tier:\s*(Standard|High|Critical)\b", re.M | re.I)
RUNTIME_LINE = re.compile(r"expected test runtime:\s*(\d+(?:\.\d+)?)\s*min", re.I)


def limits():
    out = dict(DEFAULTS)
    pm = ROOT / "project.md"
    if pm.exists():
        for k in out:
            m = re.search(rf"^{k}:\s*(\d+)", pm.read_text(encoding="utf-8"), re.M)
            if m:
                out[k] = int(m.group(1))
    return out


def feature_dirs(ids):
    dirs = sorted(PLAN_DIR.glob("feature-[0-9][0-9][0-9]-*"))
    if ids:
        wanted = {i.upper().replace("FEAT-", "") for i in ids}
        dirs = [d for d in dirs if d.name.split("-")[1] in wanted]
    return dirs


def section_map(path):
    _, body, _ = read_artifact(path)
    return {h: strip_comments(c) for h, c in sections(body)}


def listed_files(text):
    files = []
    for ln in text.splitlines():
        s = ln.strip().lstrip("-*").strip()
        if not s or s.startswith("#") or s.lower().startswith("not applicable"):
            continue
        files.extend(t.strip() for t in BACKTICK.findall(s) if "/" in t or "." in t)
    return files


def plan_files(d):
    return listed_files(section_map(d / "plan.md").get("Files To Create Or Modify", ""))


def feature_type(plan):
    m = re.search(r"type:\s*(feature|enabling|fix)\b", plan.get("Feature Type", ""), re.I)
    return m.group(1).capitalize() if m else None

def plan_tier(plan):
    """The tier on the Risk Tier section's 'Tier:' line, or None when absent or stated more than once differently."""
    tiers = {t.capitalize() for t in TIER_LINE.findall(plan.get("Risk Tier", ""))}
    return tiers.pop() if len(tiers) == 1 else None

def defect_ids():
    """Return set of defect sub-IDs (DEF D-N) from the defects collection file."""
    out = set()
    p = ROOT / "docs" / "07-testing" / "defects.md"
    if p.exists():
        for m in re.finditer(r"^## Defect (D-\d+):", p.read_text(encoding="utf-8"), re.M):
            out.add(f"DEF {m.group(1)}")
    return out


def depends_on(d):
    m = re.search(r"^- Depends on:(.*)$", (d / "plan.md").read_text(encoding="utf-8"), re.M)
    return set(re.findall(r"FEAT-\d{3}", m.group(1))) if m else set()


def state(d):
    s = d / "status.md"
    m = re.search(r"^- State:\s*(.+)$", s.read_text(encoding="utf-8"), re.M) if s.exists() else None
    return m.group(1).strip() if m else ""


def check_size(ids):
    lim = limits()
    problems, rows = [], []
    dirs = feature_dirs(ids)
    defects = None
    if not dirs:
        print("No feature folders found under docs/05-build-plan/")
        return 1 if ids else 0
    prod_patterns = standards_globs("production configuration")
    for d in dirs:
        fid = "FEAT-" + d.name.split("-")[1]
        if not (d / "plan.md").exists() or not (d / "acceptance.md").exists():
            problems.append(f"{fid}: plan.md or acceptance.md missing")
            continue
        acc = section_map(d / "acceptance.md").get("Acceptance Criteria", "")
        crit = {m.group(0): m.group(1) for m in AC_LINE.finditer(acc)}
        n_ac = len(crit)
        plan = section_map(d / "plan.md")
        ftype = feature_type(plan)
        sources = set(crit.values())
        if ftype is None:
            problems.append(f"{fid}: Feature Type must state 'Type: Feature', 'Type: Enabling', or 'Type: Fix'")
        elif ftype == "Fix":
            # DEF D-N format: 'Type: Fix DEF D-1'
            cited = set(re.findall(r"DEF\s+D-\d+", plan.get("Feature Type", "")))
            defects = defect_ids() if defects is None else defects
            if not cited:
                problems.append(f"{fid}: a Fix must name the defect it fixes on the Feature Type line ('Type: Fix DEF D-N')")
            for dfx in sorted(cited - defects):
                problems.append(f"{fid}: cites {dfx}, but no defect entry with that ID exists")
        elif ftype == "Feature" and "REQ" not in sources:
            problems.append(f"{fid}: a Feature must cover at least one story criterion (REQ S-N AC-n)")
        elif ftype == "Enabling" and not sources <= ENABLING_SOURCES:
            problems.append(f"{fid}: an Enabling feature's criteria cite NFR-, TST-, or STD- IDs only (found {', '.join(sorted(sources - ENABLING_SOURCES))})")
        files = listed_files(plan.get("Files To Create Or Modify", ""))
        src = [f for f in files if not TEST_FILE.search(f)]
        size = plan.get("Size Check", "")
        oos = plan.get("Out Of Scope", "")
        tier = plan_tier(plan)
        runtime = RUNTIME_LINE.search(size)
        rows.append(f"{fid}: {n_ac} criteria, {len(src)} source files ({len(files) - len(src)} test files), "
                    f"tier {tier or '?'}, tests {runtime.group(1) + ' min' if runtime else '?'}")
        if n_ac == 0:
            problems.append(f"{fid}: no criteria found in acceptance.md (write one per line as 'REQ-NNN AC-n: Given ...', or NFR-/TST-/STD- for Enabling)")
        if n_ac > lim["max_acceptance_criteria_per_feature"]:
            problems.append(f"{fid}: {n_ac} acceptance criteria > {lim['max_acceptance_criteria_per_feature']}: split the feature")
        if not files:
            problems.append(f"{fid}: no files listed under 'Files To Create Or Modify' (one path per line, in backticks)")
        if len(src) > lim["max_source_files_per_feature"]:
            problems.append(f"{fid}: {len(src)} source files > {lim['max_source_files_per_feature']}: split the feature")
        if not re.search(r"open design decisions:\s*none\b", size, re.I):
            problems.append(f"{fid}: Size Check must state 'Open design decisions: None' (open decisions go back to Phase 4)")
        if not runtime:
            problems.append(f"{fid}: Size Check must state 'Expected test runtime: N minutes'")
        elif float(runtime.group(1)) > lim["max_test_runtime_minutes"]:
            problems.append(f"{fid}: expected test runtime {runtime.group(1)} min > {lim['max_test_runtime_minutes']}: split the feature")
        if not tier:
            problems.append(f"{fid}: Risk Tier must have one line 'Tier: Standard', 'Tier: High', or 'Tier: Critical'")
        if not oos or "<fill" in oos:
            problems.append(f"{fid}: Out Of Scope section is empty")
        pkgs = plan.get("New Packages", "")
        if not pkgs or "<fill" in pkgs:
            problems.append(f"{fid}: New Packages section is empty (list each package with version, license, and reason, or write 'None')")
        prod = shared_files(files, prod_patterns) if prod_patterns else []
        if prod:
            problems.append(f"{fid}: lists production configuration ({', '.join(prod)}); features never change it: "
                            "the devops-engineer drafts it in Phase 8, reviewed at Critical tier")
    for r in rows:
        print(r)
    for p in problems:
        print(f"FAIL  {p}")
    print(f"Feature size: {len(dirs)} feature(s), {len(problems)} violation(s). Limits: {lim}")
    return 1 if problems else 0


def check_task0():
    dirs = feature_dirs([])
    if not dirs:
        print("task0: no feature folders yet; skipping")
        return 0
    problems = []
    t0 = [d for d in dirs if d.name.startswith("feature-000-")]
    if not t0:
        problems.append("Task 0 missing: create docs/05-build-plan/feature-000-walking-skeleton/ (FEAT-000, Type: Enabling)")
    else:
        d0 = t0[0]
        plan0 = section_map(d0 / "plan.md")
        if feature_type(plan0) != "Enabling":
            problems.append("FEAT-000: Feature Type must be 'Type: Enabling'")
        if depends_on(d0):
            problems.append("FEAT-000: Task 0 must not depend on another feature ('- Depends on: none')")
        if ".github/workflows/ci.yml" not in plan_files(d0):
            problems.append("FEAT-000: Files To Create Or Modify must include `.github/workflows/ci.yml` (Task 0 wires every gate into CI)")
        if state(d0) == "Merged":
            gates = GATES.read_text(encoding="utf-8") if GATES.exists() else ""
            unset = [ln.split("|")[1].strip() for ln in gates.splitlines() if ln.startswith("|") and "<set in" in ln and "(Phase 8)" not in ln]
            for g in unset:
                problems.append(f"FEAT-000 is Merged but automated-gates.md still has no command for: {g}")
            if CI.exists() and "Add the project gate commands here" in CI.read_text(encoding="utf-8"):
                problems.append("FEAT-000 is Merged but ci.yml project-gates job is still the placeholder")
    deps = {"FEAT-" + d.name.split("-")[1]: depends_on(d) for d in dirs}

    def reaches_t0(f, seen=()):
        if f == "FEAT-000":
            return True
        return any(reaches_t0(x, seen + (f,)) for x in deps.get(f, ()) if x not in seen)

    for f in sorted(deps):
        if f != "FEAT-000" and not reaches_t0(f):
            problems.append(f"{f}: must depend on FEAT-000 (directly or through its dependencies) so Task 0 is built first")
    for p_ in problems:
        print(f"FAIL  {p_}")
    print(f"Task 0: {len(dirs)} feature(s) checked, {len(problems)} problem(s).")
    return 1 if problems else 0


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=30)


def test_set_files(fid):
    p = ROOT / "docs" / "06-build" / f"{fid}-TESTS.md"
    return listed_files(section_map(p).get("Test Files", "")) if p.exists() else []


def branch_feature(fid, cmd):
    if fid:
        return fid
    branch = os.environ.get("GITHUB_HEAD_REF") or git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    m = re.match(r"(?:feature|fix|hotfix)/(FEAT-\d{3})", branch)
    if not m:
        print(f"{cmd}: no FEAT-NNN given and the branch is not feature/FEAT-NNN-slug; skipping")
        return None
    return m.group(1)


def check_scope(fid, base):
    fid = branch_feature(fid, "scope")
    if not fid:
        return 0
    dirs = feature_dirs([fid])
    if not dirs:
        print(f"FAIL  {fid}: no plan folder under docs/05-build-plan/")
        return 1
    allowed = {f.replace("\\", "/") for f in plan_files(dirs[0]) + test_set_files(fid)}
    diff = git("diff", "--name-only", f"{base}...HEAD")
    if diff.returncode != 0:
        print(f"FAIL  cannot diff against '{base}': {diff.stderr.strip()}")
        return 1
    outside = [f for f in diff.stdout.split() if f not in allowed and not ALWAYS_IN_SCOPE.search(f)]
    for f in outside:
        print(f"FAIL  {fid}: changed file not in plan.md 'Files To Create Or Modify': {f}")
    print(f"Files in scope: {len(diff.stdout.split())} changed, {len(outside)} outside the plan.")
    return 1 if outside else 0


def ecosystem(path):
    name = Path(path).name
    if name == "package.json":
        return "npm"
    return "pypi" if re.fullmatch(r"requirements.*\.txt", name) else None


def manifest_packages(path, text):
    if not text.strip():
        return {}
    if ecosystem(path) == "npm":
        data = json.loads(text)
        return {n.lower(): v for k in NPM_KEYS for n, v in data.get(k, {}).items()}
    out = {}
    for ln in text.splitlines():
        if ln.lstrip().startswith(("#", "-")):
            continue
        m = REQ_LINE.match(ln)
        if m:
            out[m.group(1).lower().replace("_", "-")] = (m.group(2) or "*").replace(" ", "")
    return out


def check_packages(fid, base):
    fid = branch_feature(fid, "packages")
    if not fid:
        return 0
    dirs = feature_dirs([fid])
    if not dirs:
        print(f"FAIL  {fid}: no plan folder under docs/05-build-plan/")
        return 1
    text = section_map(dirs[0] / "plan.md").get("New Packages", "")
    # DEC-057: plan format uses '@' as separator before version (e.g. 'react @^18.3');
    # strip the leading '@' from npm version specs so they match package.json format.
    approved = {(e, n.lower().replace("_", "-") if e == "pypi" else n.lower()):
                (v.lstrip("@") if e == "npm" else v).replace(" ", "")
                for e, n, v in PKG_LINE.findall(text)}
    diff = git("diff", "--name-only", f"{base}...HEAD")
    if diff.returncode != 0:
        print(f"FAIL  cannot diff against '{base}': {diff.stderr.strip()}")
        return 1
    problems = []
    for f in (x for x in diff.stdout.split() if ecosystem(x)):
        eco = ecosystem(f)
        try:
            old = manifest_packages(f, git("show", f"{base}:{f}").stdout)
            new = manifest_packages(f, git("show", f"HEAD:{f}").stdout)
        except json.JSONDecodeError as e:
            problems.append(f"{fid}: cannot parse {f}: {e}")
            continue
        for name, ver in sorted(new.items()):
            if old.get(name) == ver:
                continue
            want = approved.get((eco, name))
            if want is None:
                problems.append(f"{fid}: {eco} package '{name}' {ver} in {f} is not named in plan.md 'New Packages'")
            elif want != ver.replace(" ", ""):
                problems.append(f"{fid}: {eco} package '{name}' is {ver} in {f}; the plan approved {want}")
    for p in problems:
        print(f"FAIL  {p}")
    print(f"New packages: {len(approved)} approved in the plan, {len(problems)} unapproved change(s).")
    return 1 if problems else 0


def standards_globs(heading):
    if not STANDARDS.exists():
        return []
    _, body, _ = read_artifact(STANDARDS)
    text = next((strip_comments(c) for h, c in sections(body) if h.lower().startswith(heading)), "")
    bullets = (BACKTICK.search(ln) for ln in text.splitlines() if ln.lstrip().startswith(("- ", "* ")))
    return [m.group(1) for m in bullets if m]


def shared_patterns():
    return standards_globs("shared paths")


def shared_files(files, pats):
    return sorted(f for f in files if any(fnmatchcase(f, p) or (p.startswith("**/") and fnmatchcase(f, p[3:])) for p in pats))


def feature_files():
    return {"FEAT-" + d.name.split("-")[1]: {f.replace("\\", "/") for f in plan_files(d)}
            for d in feature_dirs([]) if (d / "plan.md").exists()}


def check_waves():
    plans = sorted(p for p in PLAN_DIR.glob("*.md") if (read_artifact(p)[0] or {}).get("template") == "wave-plan")
    if not plans:
        print("waves: no wave plan under docs/05-build-plan/; skipping")
        return 0
    waves = []
    for name, cell in WAVE_ROW.findall(section_map(plans[-1]).get("Waves", "")):
        ids = re.findall(r"FEAT-\d{3}", cell)
        if ids and not set(name) <= set("-: "):
            waves.append((name, ids))
    files, pats = feature_files(), shared_patterns()
    deps = {"FEAT-" + d.name.split("-")[1]: depends_on(d) for d in feature_dirs([]) if (d / "plan.md").exists()}
    problems, pos = [], {}
    for i, (name, ids) in enumerate(waves):
        for f in ids:
            if f in pos:
                problems.append(f"{f}: in more than one wave")
            elif f not in files:
                problems.append(f"{f}: in wave {name} but has no plan folder")
            pos.setdefault(f, i)
        if len(ids) > 1:
            for f in ids:
                sh = shared_files(files.get(f, ()), pats)
                if sh:
                    problems.append(f"{f}: changes shared paths ({', '.join(sh)}) and must be alone in its wave, not in wave {name}")
            for a in range(len(ids)):
                for b in range(a + 1, len(ids)):
                    both = sorted(files.get(ids[a], set()) & files.get(ids[b], set()))
                    if both:
                        problems.append(f"{ids[a]} and {ids[b]}: both change {', '.join(both)} in wave {name}")
    fixes = {"FEAT-" + d.name.split("-")[1] for d in feature_dirs([])
             if (d / "plan.md").exists() and feature_type(section_map(d / "plan.md")) == "Fix"}
    problems += [f"{f}: in no wave" for f in sorted(files) if f not in pos and f not in fixes]
    for f, ds in sorted(deps.items()):
        for d in sorted(ds):
            if f in pos and d in pos and pos[d] >= pos[f]:
                problems.append(f"{f}: depends on {d}, which is not in an earlier wave")
    for p in problems:
        print(f"FAIL  {p}")
    print(f"Waves ({plans[-1].name}): {len(waves)} wave(s), {len(pos)} feature(s), {len(problems)} problem(s).")
    return 1 if problems else 0


def check_start(fid):
    files, pats = feature_files(), shared_patterns()
    if fid not in files:
        print(f"FAIL  {fid}: no plan folder under docs/05-build-plan/")
        return 1
    mine, my_shared = files[fid], shared_files(files[fid], pats)
    problems = []
    for d in feature_dirs([]):
        other = "FEAT-" + d.name.split("-")[1]
        st = state(d)
        if other == fid or st not in OPEN_STATES:
            continue
        theirs = files.get(other, set())
        both = sorted(mine & theirs)
        if both:
            problems.append(f"{fid} and {other} ({st}) change the same files: {', '.join(both)}")
        elif my_shared:
            problems.append(f"{fid} changes shared paths ({', '.join(my_shared)}) and must run alone; {other} is {st}")
        elif shared_files(theirs, pats):
            problems.append(f"{other} ({st}) changes shared paths and must run alone; start {fid} after it merges")
    for p in problems:
        print(f"FAIL  {p}")
    print(f"Start {fid}: {len(problems)} collision(s) with open features.")
    return 1 if problems else 0


def main():
    args = sys.argv[1:]
    if not args or args[0] not in ("size", "scope", "task0", "packages", "waves", "start"):
        print(__doc__)
        return 2
    cmd, rest = args[0], args[1:]
    base = "main"
    if "--base" in rest:
        i = rest.index("--base")
        base = rest[i + 1]
        rest = rest[:i] + rest[i + 2:]
    if cmd == "size":
        return check_size(rest)
    if cmd == "task0":
        return check_task0()
    if cmd == "packages":
        return check_packages(rest[0] if rest else None, base)
    if cmd == "waves":
        return check_waves()
    if cmd == "start":
        if not rest or not re.fullmatch(r"FEAT-\d{3}", rest[0]):
            print("start needs FEAT-NNN", file=sys.stderr)
            return 2
        return check_start(rest[0])
    return check_scope(rest[0] if rest else None, base)


if __name__ == "__main__":
    sys.exit(main())
