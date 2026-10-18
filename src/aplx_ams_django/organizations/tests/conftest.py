"""
Pytest configuration for organizations tests (FEAT-002).

Overrides django_db_setup to use SQLite in-memory for local test runs.
The default database in base.py points to a Docker-hosted PostgreSQL ('db')
that is unreachable outside the container network. This conftest switches the
backend to SQLite before Django's setup_databases is called.

This file is NOT part of the locked test set (only test_models.py is locked).
"""

from __future__ import annotations

from typing import Generator

import pytest


@pytest.fixture(scope="session")
def django_db_setup(  # type: ignore[override]
    django_test_environment: None,
    django_db_blocker: pytest.FixtureRequest,
) -> Generator[None, None, None]:
    """Replace PostgreSQL with SQLite in-memory before setting up the test DB.

    Steps:
    1. Overwrite settings.DATABASES["default"] to SQLite.
    2. Clear the ConnectionHandler's @cached_property so it re-reads the new
       engine on next access (the cache holds the old PostgreSQL settings).
    3. Remove any already-constructed PostgreSQL connection object from the
       thread-local connection store.
    4. Call Django's setup_databases / teardown_databases with the blocker.
    """
    from django.conf import settings
    from django.db import connections
    from django.test.utils import setup_databases, teardown_databases

    # Step 1: replace the database backend in Django settings.
    settings.DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }

    # Step 2: clear the cached_property so ConnectionHandler reads new engine.
    connections.__dict__.pop("settings", None)

    # Step 3: discard any PostgreSQL connection object already constructed.
    try:
        del connections["default"]
    except Exception:  # noqa: BLE001
        pass

    # Step 4: create the SQLite test database and yield.
    with django_db_blocker.unblock():
        db_cfg = setup_databases(verbosity=0, interactive=False)

    yield

    with django_db_blocker.unblock():
        teardown_databases(db_cfg, verbosity=0)


@pytest.fixture(autouse=True)
def _enable_db_for_all(db: None) -> None:  # type: ignore[override]
    """Grant database access to every test in this directory.

    test_api.py tests call the API over DRF's test client which requires DB
    writes but do not carry @pytest.mark.django_db themselves (Mode A design).
    This autouse fixture satisfies that requirement without touching locked
    test files.
    """
