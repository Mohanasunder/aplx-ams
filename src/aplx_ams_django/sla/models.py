"""
FEAT-010 sla models — DBD-001 v0.1 § Module: sla.

Table: sla_holidayentry
Fields: holiday_date (DATE NOT NULL), added_at (TIMESTAMPTZ NOT NULL DEFAULT NOW()),
        added_by FK → accounts_user (NOT NULL), removed_at (TIMESTAMPTZ nullable),
        removed_by FK → accounts_user (nullable).

Constraint chk_removed_consistent enforces:
    (removed_at IS NULL) = (removed_by_id IS NULL)
    i.e. both set together or both NULL.
"""

from __future__ import annotations

from typing import ClassVar

from django.conf import settings
from django.db import models
from django.utils import timezone


class HolidayEntry(models.Model):
    """One entry in the company holiday calendar (DBD-001 v0.1 § Module: sla)."""

    holiday_date = models.DateField(null=False)
    added_at = models.DateTimeField(null=False, default=timezone.now)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        on_delete=models.PROTECT,
        related_name="holidays_added",
        db_column="added_by_id",
    )
    removed_at = models.DateTimeField(null=True, blank=True)
    removed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="holidays_removed",
        db_column="removed_by_id",
    )

    class Meta:
        db_table = "sla_holidayentry"
        constraints: ClassVar[list[models.BaseConstraint]] = [
            models.CheckConstraint(
                # Both NULL or both set; mirrors SQL:
                # CHECK ((removed_at IS NULL) = (removed_by_id IS NULL))
                check=(
                    models.Q(removed_at__isnull=True, removed_by__isnull=True)
                    | models.Q(removed_at__isnull=False, removed_by__isnull=False)
                ),
                name="chk_removed_consistent",
            ),
        ]

    def __str__(self) -> str:
        status = "removed" if self.removed_at else "active"
        return f"HolidayEntry({self.holiday_date}, {status})"
