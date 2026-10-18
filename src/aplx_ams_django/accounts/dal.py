"""
FEAT-005 accounts data access layer — STUB (Mode A: tests first).

All DAL functions are empty stubs. Django ORM queries are added in Mode B.

Named per STD-001 v0.1 § Naming And Structure.
"""

from __future__ import annotations


def get_user_by_id(user_id: int) -> None:
    """Stub: return the User with the given primary key.

    Mode B will use User.objects.get(pk=user_id).
    Raises User.DoesNotExist if not found (→ 404 in view).

    Returns None in stub.
    """
    return None


def list_users() -> list:
    """Stub: return all user accounts ordered by username.

    Mode B will use User.objects.order_by('username').

    Returns empty list in stub.
    """
    return []


def get_active_users_by_org(org_id: int) -> list:
    """Stub: return all active users belonging to the given client organization.

    Mode B will use User.objects.filter(client_org_id=org_id, is_active=True).

    Returns empty list in stub.
    """
    return []
