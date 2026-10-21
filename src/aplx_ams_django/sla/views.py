"""
FEAT-010 sla views — Mode A stubs.

HolidayEntryViewSet: DRF GenericViewSet for /api/holidays/.
Permission matrix (PRM-001 v0.1 § Company holiday list F-2 support):
  GET  /api/holidays/        — all authenticated roles (P1, P2, P3)
  POST /api/holidays/        — P3 (delivery_manager) only
  DELETE /api/holidays/{id}/ — P3 (delivery_manager) only; soft-remove

get_permissions() is implemented so HasRolePermission enforces access control
before any action method is reached. Action methods raise NotImplementedError
(Mode A stubs; Mode B fills in the real logic).
"""

from __future__ import annotations

from typing import ClassVar

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from aplx_ams_django.permissions import HasRolePermission
from aplx_ams_django.sla.serializers import HolidayEntrySerializer

_DM_ONLY = ["delivery_manager"]


class HolidayEntryViewSet(viewsets.GenericViewSet):
    """ViewSet for the company holiday list — Mode A stub.

    get_permissions() enforces the permission matrix before action dispatch:
    - list: any authenticated user (P1, P2, P3)
    - create / destroy: delivery_manager (P3) only
    """

    serializer_class: ClassVar[type] = HolidayEntrySerializer

    def get_permissions(
        self,
    ) -> list[HasRolePermission | IsAuthenticated]:
        """Return the permission objects appropriate for the current action."""
        if self.action in ("create", "destroy"):
            return [HasRolePermission(required_roles=_DM_ONLY)]
        # list and any other action: authenticated users only.
        return [IsAuthenticated()]

    def list(self, request: Request) -> Response:
        """GET /api/holidays/ — return active holiday entries (Mode A stub)."""
        raise NotImplementedError("HolidayEntryViewSet.list is not yet implemented")

    def create(self, request: Request) -> Response:
        """POST /api/holidays/ — create a new holiday entry (Mode A stub).

        AC-1: DM adds a holiday date; future SLA timers exclude that date.
        Returns HTTP 201 on success.
        """
        raise NotImplementedError("HolidayEntryViewSet.create is not yet implemented")

    def destroy(self, request: Request, pk: int | None = None) -> Response:
        """DELETE /api/holidays/{id}/ — soft-remove a holiday entry (Mode A stub).

        AC-2: DM removes a holiday date; that date counts as a normal business day.
        Returns HTTP 204 on success.
        """
        raise NotImplementedError("HolidayEntryViewSet.destroy is not yet implemented")
