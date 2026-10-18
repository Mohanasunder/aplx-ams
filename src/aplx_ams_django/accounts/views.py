"""
FEAT-005 accounts views — STUB (Mode A: tests first).

UserViewSet is an empty stub. All actions return HTTP 501 (Not Implemented).
Permission enforcement (HasRolePermission), serializers, and service calls
are added in Mode B.

Permission matrix (PRM-001 v0.1 § User account management F-6):
  POST   /api/accounts/users/                  — P3 (delivery_manager)
  GET    /api/accounts/users/                  — P3
  GET    /api/accounts/users/{id}/             — P3
  PATCH  /api/accounts/users/{id}/             — P3
  POST   /api/accounts/users/{id}/deactivate/ — P3
"""

from __future__ import annotations

from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response


class UserViewSet(viewsets.GenericViewSet):
    """ViewSet for user account management (DM-only write) — stub (Mode A).

    All actions return HTTP 501 Not Implemented until Mode B adds logic.
    """

    def list(self, request: Request) -> Response:
        """GET /api/accounts/users/ — stub; returns 501."""
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def create(self, request: Request) -> Response:
        """POST /api/accounts/users/ — stub; returns 501."""
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def retrieve(self, request: Request, pk: int | None = None) -> Response:
        """GET /api/accounts/users/{id}/ — stub; returns 501."""
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def partial_update(self, request: Request, pk: int | None = None) -> Response:
        """PATCH /api/accounts/users/{id}/ — stub; returns 501."""
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    def deactivate(self, request: Request, pk: int | None = None) -> Response:
        """POST /api/accounts/users/{id}/deactivate/ — stub; returns 501."""
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
