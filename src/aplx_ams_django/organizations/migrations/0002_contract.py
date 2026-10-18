"""
FEAT-003 migration stub: Contract table skeleton.

Creates the organizations_contract table with only the auto-generated primary
key so that the Django test runner can serialize the database during Mode A
(tests-first). All schema fields, constraints, and the partial unique index are
added in Mode B when the Contract model is fully implemented.
"""

from __future__ import annotations

from typing import ClassVar

import django.db.models.deletion
from django.db import migrations, models


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
            ],
        ),
    ]
