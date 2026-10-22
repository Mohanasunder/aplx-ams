"""
FEAT-010 initial migration — creates sla_holidayentry (DBD-001 v0.1 § Module: sla).

Depends on accounts 0001_initial for the FKs to accounts_user.

Creates:
  sla_holidayentry table with all fields and the chk_removed_consistent CHECK constraint.
"""

from __future__ import annotations

from typing import ClassVar

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
from django.db.models import Q
from django.utils import timezone


class Migration(migrations.Migration):
    initial = True

    dependencies: ClassVar[list[tuple[str, str]]] = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0001_initial"),
    ]

    operations: ClassVar[list[migrations.Operation]] = [
        migrations.CreateModel(
            name="HolidayEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "holiday_date",
                    models.DateField(),
                ),
                (
                    "added_at",
                    models.DateTimeField(default=timezone.now),
                ),
                (
                    "added_by",
                    models.ForeignKey(
                        db_column="added_by_id",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="holidays_added",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "removed_at",
                    models.DateTimeField(blank=True, null=True),
                ),
                (
                    "removed_by",
                    models.ForeignKey(
                        blank=True,
                        db_column="removed_by_id",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="holidays_removed",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "sla_holidayentry",
            },
        ),
        migrations.AddConstraint(
            model_name="holidayentry",
            constraint=models.CheckConstraint(
                check=(
                    Q(removed_at__isnull=True, removed_by__isnull=True)
                    | Q(removed_at__isnull=False, removed_by__isnull=False)
                ),
                name="chk_removed_consistent",
            ),
        ),
    ]
