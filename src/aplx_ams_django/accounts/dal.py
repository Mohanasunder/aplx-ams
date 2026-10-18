"""
FEAT-005 accounts data access layer — Mode B implementation.

get_user_by_id: single-user lookup by primary key.
list_users: all users ordered by username.
get_active_users_by_org: active users filtered by client organization.

Named per STD-001 v0.1 § Naming And Structure.
"""

from __future__ import annotations


def get_user_by_id(user_id: int):
    """Return the User with the given primary key.

    Args:
        user_id: primary key to look up.

    Returns:
        User instance.

    Raises:
        User.DoesNotExist: if no user with that pk exists (→ 404 in view).
    """
    from aplx_ams_django.accounts.models import User

    return User.objects.get(pk=user_id)


def list_users() -> list:
    """Return all user accounts ordered by username.

    Returns:
        List of User instances.
    """
    from aplx_ams_django.accounts.models import User

    return list(User.objects.order_by("username"))


def get_active_users_by_org(org_id: int) -> list:
    """Return all active users belonging to the given client organization.

    Args:
        org_id: primary key of the ClientOrg to filter on.

    Returns:
        List of active User instances for that org.
    """
    from aplx_ams_django.accounts.models import User

    return list(User.objects.filter(client_org_id=org_id, is_active=True))
