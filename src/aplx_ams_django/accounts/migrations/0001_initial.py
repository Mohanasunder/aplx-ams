"""
FEAT-005 stub migration — creates accounts_user with id, password, last_login,
and username only.

Mode B will replace this with the full DBD-001 v0.1 schema:
  role            role_enum        NOT NULL
  name            VARCHAR(150)     NOT NULL
  email           VARCHAR(254)     NOT NULL UNIQUE
  client_org_id   BIGINT FK        (nullable — allowed for non-client-user roles)
  is_active       BOOLEAN          NOT NULL DEFAULT TRUE
  failed_attempts SMALLINT         NOT NULL DEFAULT 0
  locked_until    TIMESTAMPTZ      (nullable)
  date_joined     TIMESTAMPTZ      NOT NULL DEFAULT NOW()
  last_login      TIMESTAMPTZ      (nullable)
plus:
  chk_client_user_has_org
  chk_internal_user_no_org
  chk_failed_attempts_non_negative
"""

from __future__ import annotations

from typing import ClassVar

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies: ClassVar[list[tuple[str, str]]] = []

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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("username", models.CharField(max_length=150, unique=True)),
            ],
            options={
                "db_table": "accounts_user",
            },
        ),
    ]
