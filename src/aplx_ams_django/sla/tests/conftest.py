"""
Pytest configuration for sla tests (FEAT-010).

Overrides django_db_setup to use SQLite in-memory for local test runs.
The default database in base.py points to a Docker-hosted PostgreSQL ('db')
that is unreachable outside the container network. This conftest switches the
backend to SQLite before Django's setup_databases is called.

Also registers aplx_ams_django.sla in Django's app registry. Because this
conftest lives in a sub-directory, pytest discovers it after django.setup() has
already been called (with the base INSTALLED_APPS that lacks sla). The fixture
therefore re-populates the Django app registry to include sla before creating
the test database. The backend-builder adds sla to settings/base.py in Mode B;
this fixture covers Mode A without touching settings/base.py.

This file is NOT part of the locked test set.
"""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

import pytest


@pytest.fixture(scope="session")
def django_db_setup(
    django_test_environment: None,
    django_db_blocker: Any,
) -> Generator[None, None, None]:
    """Replace PostgreSQL with SQLite in-memory and register the sla app.

    Steps:
    1. Add 'aplx_ams_django.sla' to settings.INSTALLED_APPS.
    2. Re-populate Django's app registry so HolidayEntry can be imported and
       its migration is discovered by setup_databases.
    3. Overwrite settings.DATABASES["default"] to SQLite.
    4. Clear the ConnectionHandler's @cached_property.
    5. Remove any already-constructed PostgreSQL connection object.
    6. Call Django's setup_databases / teardown_databases with the blocker.
    """
    from django.apps import apps
    from django.conf import settings
    from django.db import connections
    from django.test.utils import setup_databases, teardown_databases

    # Step 1: add sla to settings.INSTALLED_APPS if absent.
    # settings/base.py is modified by the backend-builder in Mode B.
    if "aplx_ams_django.sla" not in settings.INSTALLED_APPS:
        settings.INSTALLED_APPS = [*settings.INSTALLED_APPS, "aplx_ams_django.sla"]

    # Step 2: register the sla app and its models in Django's app registry.
    # django.setup() was called before pytest discovered this nested conftest,
    # so the registry lacks sla. We add only sla — without disturbing existing
    # app registrations — so HolidayEntry can be imported and its migration is
    # discovered by setup_databases.
    if not apps.app_configs.get("sla"):
        import importlib

        from aplx_ams_django.sla.apps import SlaConfig

        sla_module = importlib.import_module("aplx_ams_django.sla")
        sla_config = SlaConfig("aplx_ams_django.sla", sla_module)
        sla_config.apps = apps  # type: ignore[attr-defined]
        apps.app_configs["sla"] = sla_config
        apps.all_models.setdefault("sla", {})  # type: ignore[attr-defined]
        # Import models so HolidayEntry is registered in all_models["sla"].
        sla_config.import_models()
        sla_config.ready = True  # type: ignore[attr-defined]

    # Step 3: replace the database backend in Django settings.
    settings.DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }

    # Step 4: clear the cached_property so ConnectionHandler reads new engine.
    connections.__dict__.pop("settings", None)

    # Step 5: discard any PostgreSQL connection object already constructed.
    try:
        del connections["default"]
    except Exception:  # noqa: S110
        pass

    # Step 6: create the SQLite test database and yield.
    with django_db_blocker.unblock():
        db_cfg = setup_databases(verbosity=0, interactive=False)

    yield

    with django_db_blocker.unblock():
        teardown_databases(db_cfg, verbosity=0)


@pytest.fixture(autouse=True)
def _enable_db_for_all(db: None) -> None:
    """Grant database access to every test in this directory."""
