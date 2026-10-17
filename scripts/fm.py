#!/usr/bin/env python3
"""Get or set front matter fields on an artifact.

  python3 scripts/fm.py get docs/02-requirements/REQ-001.md validation
  python3 scripts/fm.py set docs/02-requirements/REQ-001.md validation "Pass" status "In review"

Agents may set 'validation' and 'status' to 'Draft' or 'In review' only. Setting status to Approved
or Rejected is done solely by scripts/log_approval.py on behalf of a named human.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sdlc_lib import STATUS_VALUES, VALIDATION_VALUES, read_artifact, set_front_matter  # noqa: E402


def main(argv):
    if len(argv) < 3 or argv[0] not in ("get", "set"):
        print(__doc__)
        return 2
    cmd, path, rest = argv[0], argv[1], argv[2:]
    if cmd == "get":
        fm, _, _ = read_artifact(path)
        for k in rest:
            print(f"{k}: {fm.get(k, '')}")
        return 0
    if len(rest) % 2:
        print("set needs key value pairs", file=sys.stderr)
        return 2
    updates = dict(zip(rest[0::2], rest[1::2]))
    if "status" in updates:
        if updates["status"] not in STATUS_VALUES:
            print(f"status must be one of {STATUS_VALUES}", file=sys.stderr)
            return 2
        if updates["status"] in ("Approved", "Rejected"):
            print("Refusing: only scripts/log_approval.py (a named human) may set Approved/Rejected", file=sys.stderr)
            return 1
    if "validation" in updates and updates["validation"] not in VALIDATION_VALUES:
        print(f"validation must be one of {VALIDATION_VALUES}", file=sys.stderr)
        return 2
    if "approver" in updates:
        print("Refusing: 'approver' is set by scripts/log_approval.py", file=sys.stderr)
        return 1
    set_front_matter(path, updates)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
