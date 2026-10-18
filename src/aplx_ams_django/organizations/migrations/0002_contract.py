"""
FEAT-003 migration: Contract table (DBD-001 v0.1).

Creates the organizations_contract table with all fields and constraints:
- Two CHECK constraints (hours_bank requires contracted_hours; contracted_hours > 0 when set)
- One partial UNIQUE constraint (at most one active contract per client org, BR B-15)
"""

from __future__ import annotations

from typing import ClassVar

import django.db.models.deletion
from django.db import migrations, models
from django.db.models import Q


class Migration(migrations.Migration):
    dependencies: ClassVar[list[tuple[str, str]]] = [
        ("organizations", "0001_initial"),
    ]

    operations: ClassVar[list] = [
        migrations.CreateModel(
            name="Contract",
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
                    "client_org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts",
                        to="organizations.clientorg",
                    ),
                ),
                (
                    "contract_type",
                    models.CharField(
                        choices=[("hours_bank", "Hours bank"), ("fixed_fee", "Fixed fee")],
                        max_length=20,
                    ),
                ),
                (
                    "contracted_hours",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True),
                ),
                (
                    "monthly_close_at",
                    models.DateTimeField(blank=True, null=True),
                ),
                (
                    "started_at",
                    models.DateTimeField(auto_now_add=True),
                ),
                (
                    "ended_at",
                    models.DateTimeField(blank=True, null=True),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="contract",
            constraint=models.CheckConstraint(
                check=~Q(contract_type="hours_bank") | Q(contracted_hours__isnull=False),
                name="chk_hours_bank_requires_contracted_hours",
            ),
        ),
        migrations.AddConstraint(
            model_name="contract",
            constraint=models.CheckConstraint(
                check=Q(contracted_hours__isnull=True) | Q(contracted_hours__gt=0),
                name="chk_contracted_hours_positive",
            ),
        ),
        migrations.AddConstraint(
            model_name="contract",
            constraint=models.UniqueConstraint(
                fields=["client_org"],
                condition=Q(is_active=True),
                name="organizations_contract_one_active_per_org_idx",
            ),
        ),
    ]
