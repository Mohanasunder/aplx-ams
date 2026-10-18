"""
Pytest configuration for organizations API tests (FEAT-002).

This conftest.py is NOT part of the locked test set (only test_api.py is
locked). The Mode B builder may extend this file to add database fixtures,
test-data factories, and the @pytest.mark.django_db mark once organizations
is registered in INSTALLED_APPS.

Plan gap A-ORG-001: `aplx_ams_django.organizations` is not yet in
settings.INSTALLED_APPS. The Mode B builder must add it to
src/aplx_ams_django/settings/base.py and create proper migrations before
tests that write to the database (AC-1, AC-2) can pass.
"""
