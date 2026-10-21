"""
FEAT-010 sla views — Mode B implementation.

HolidayEntryViewSet: DRF GenericViewSet for /api/holidays/.
Permission matrix (PRM-001 v0.1 § Company holiday list F-2 support):
  GET  /api/holidays/        — all authenticated roles (P1, P2, P3)
  POST /api/holidays/        — P3 (delivery_manager) only
  DELETE /api/holidays/{id}/ — P3 (delivery_manager) only; soft-remove
"""

from __future__ import annotations

from typing import ClassVar

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from aplx_ams_django.permissions import HasRolePermission
from aplx_ams_django.sla.models import HolidayEntry
from aplx_ams_django.sla.serializers import HolidayEntrySerializer
from aplx_ams_django.sla.services import add_holiday, remove_holiday

_DM_ONLY = ["delivery_manager"]


class HolidayEntryViewSet(viewsets.GenericViewSet):
    """ViewSet for the company holiday list.

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
        """GET /api/holidays/ — return active holiday entries ordered by date."""
        queryset = HolidayEntry.objects.filter(removed_at__isnull=True).order_by("holiday_date")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request: Request) -> Response:
        """POST /api/holidays/ — create a new holiday entry.

        AC-1: DM adds a holiday date; future SLA timers exclude that date.
        Returns HTTP 201 on success.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        holiday_date = serializer.validated_data["holiday_date"]

        try:
            entry = add_holiday(holiday_date=holiday_date, added_by=request.user)
        except ValueError as exc:
            return Response({"detail": str(exc)}, status=status.HTTP_409_CONFLICT)

        out_serializer = self.get_serializer(entry)
        return Response(out_serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request: Request, pk: int | None = None) -> Response:
        """DELETE /api/holidays/{id}/ — soft-remove a holiday entry.

        AC-2: DM removes a holiday date; that date counts as a normal business day.
        Returns HTTP 204 on success.
        """
        entry = HolidayEntry.objects.filter(pk=pk, removed_at__isnull=True).first()
        if entry is None:
            return Response(
                {"detail": "Holiday entry not found or already removed."},
                status=status.HTTP_404_NOT_FOUND,
            )

        remove_holiday(entry=entry, removed_by=request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
