"""
FEAT-002: shared DRF permission class.

HasRolePermission enforces role-based access control per PRM-001 v0.1.
Roles: P1 (L1 support), P2 (L2/L3 support), P3 (Delivery manager), P4 (Client user).
"""

from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class HasRolePermission(BasePermission):
    """DRF permission class that checks request.user.role against required_roles.

    Instantiate with a list of allowed roles in get_permissions():
        return [HasRolePermission(required_roles=['P3'])]

    Falls back to view.required_roles class attribute when no list is supplied.
    Returns 403 for authenticated users whose role is not in the allowed list.
    Returns 403 for unauthenticated requests.
    """

    def __init__(self, required_roles: list[str] | None = None) -> None:
        self._required_roles = required_roles

    def has_permission(self, request: Request, view: object) -> bool:
        user = request.user
        if not user or not getattr(user, "is_authenticated", False):
            return False

        required: list[str] | None = self._required_roles
        if required is None:
            required = getattr(view, "required_roles", None)
        if required is None:
            # No restriction configured — any authenticated user passes.
            return True

        return getattr(user, "role", None) in required
