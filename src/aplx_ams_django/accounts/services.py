"""
FEAT-005 accounts service layer — STUB (Mode A: tests first).

create_user and deactivate_user are empty stubs. Business logic, input
validation, and role enforcement are added in Mode B.

Named per STD-001 v0.1 § Naming And Structure.
"""

from __future__ import annotations

from typing import Any


def create_user(data: dict[str, Any]) -> None:
    """Stub: create a new user account and return it.

    Mode B will: validate role enum, enforce client_org_id requirement for
    client_user role (DBD-001 v0.1 constraint), hash the temporary password,
    and persist the user via the DAL.

    Returns None in stub; Mode B returns the created User instance.
    """
    return None


def deactivate_user(user_id: int) -> None:
    """Stub: deactivate the user with the given primary key.

    Mode B will: fetch the user via the DAL, set is_active=False, and save.
    Raises User.DoesNotExist if the user is not found (→ 404 in view).

    Returns None in stub; Mode B returns the updated User instance.
    """
    return None
