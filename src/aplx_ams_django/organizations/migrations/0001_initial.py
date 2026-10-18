"""
FEAT-002 initial migration: stub ClientOrg and SAPApplication tables.

The database-builder adds fields in a concurrent session. This migration
creates the tables with only the Django-generated primary key column;
subsequent schema changes will be applied via separate migrations.
"""

from django.db import migrations


class Migration(migrations.Migration):
    initial = True

    dependencies: list[tuple[str, str]] = []

    operations: list[migrations.Operation] = [
        migrations.CreateModel(
            name="ClientOrg",
            fields=[
                (
                    "id",
                    migrations.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "db_table": "organizations_clientorg",
            },
        ),
        migrations.CreateModel(
            name="SAPApplication",
            fields=[
                (
                    "id",
                    migrations.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "db_table": "organizations_sapapplication",
            },
        ),
    ]
