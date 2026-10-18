"""
FEAT-005 accounts service layer — Mode B implementation.

create_user: persists a new User with an unusable password placeholder (AC-1).
deactivate_user: sets is_active=False on an existing user (AC-3).

Named per STD-001 v0.1 § Naming And Structure.
"""

from __future__ import annotations

from typing import Any


def create_user(data: dict[str, Any]):
    """Create and persist a new user account.

    Sets an unusable password (the password is managed by a separate
    credential flow; see FEAT-006).

    Args:
        data: validated fields from UserCreateSerializer — username, name,
              email, role, and optionally client_org_id.

    Returns:
        The saved User instance.
    """
    from aplx_ams_django.accounts.models import User

    user = User(
        username=data["username"],
        name=data["name"],
        email=data["email"],
        role=data["role"],
        client_org_id=data.get("client_org_id"),
    )
    user.set_unusable_password()
    user.save()
    return user


def deactivate_user(user_id: int):
    """Set is_active=False on the user identified by user_id.

    Args:
        user_id: primary key of the target User.

    Returns:
        The updated User instance.

    Raises:
        User.DoesNotExist: if no user with that pk exists (→ 404 in view).
    """
    from aplx_ams_django.accounts.models import User

    user = User.objects.get(pk=user_id)
    user.is_active = False
    user.save()
    return user
