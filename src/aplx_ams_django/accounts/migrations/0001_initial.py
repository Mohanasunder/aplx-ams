"""
FEAT-005 full migration — creates accounts_user (DBD-001 v0.1).

Depends on organizations 0002_contract (latest organizations migration).
Creates the accounts_user table with all fields and four check constraints:
  chk_role_valid
  chk_client_user_has_org
  chk_internal_user_no_org
  chk_failed_attempts_non_negative
"""

from __future__ import annotations

from typing import ClassVar

import django.db.models.deletion
from django.db import migrations, models
from django.db.models import Q


class Migration(migrations.Migration):
    initial = True

    dependencies: ClassVar[list[tuple[str, str]]] = [
        ("organizations", "0002_contract"),
    ]

    operations: ClassVar[list[migrations.Operation]] = [
        migrations.CreateModel(
            name="User",
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
                    "password",
                    models.CharField(max_length=128, verbose_name="password"),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="last login",
                    ),
                ),
                (
                    "username",
                    models.CharField(max_length=150, unique=True),
                ),
                (
                    "name",
                    models.CharField(max_length=150),
                ),
                (
                    "email",
                    models.EmailField(max_length=254, unique=True),
                ),
                (
                    "role",
                    models.CharField(
                        max_length=30,
                        choices=[
                            ("l1_support_engineer", "L1 Support Engineer"),
                            ("l2_l3_support_engineer", "L2/L3 Support Engineer"),
                            ("delivery_manager", "Delivery Manager"),
                            ("client_user", "Client User"),
                        ],
                    ),
                ),
                (
                    "client_org",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="organizations.clientorg",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True),
                ),
                (
                    "failed_attempts",
                    models.SmallIntegerField(default=0),
                ),
                (
                    "locked_until",
                    models.DateTimeField(blank=True, null=True),
                ),
                (
                    "date_joined",
                    models.DateTimeField(auto_now_add=True),
                ),
            ],
            options={
                "db_table": "accounts_user",
            },
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.CheckConstraint(
                check=Q(
                    role__in=[
                        "l1_support_engineer",
                        "l2_l3_support_engineer",
                        "delivery_manager",
                        "client_user",
                    ]
                ),
                name="chk_role_valid",
            ),
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.CheckConstraint(
                check=~Q(role="client_user") | Q(client_org__isnull=False),
                name="chk_client_user_has_org",
            ),
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.CheckConstraint(
                check=Q(role="client_user") | Q(client_org__isnull=True),
                name="chk_internal_user_no_org",
            ),
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.CheckConstraint(
                check=Q(failed_attempts__gte=0),
                name="chk_failed_attempts_non_negative",
            ),
        ),
    ]
