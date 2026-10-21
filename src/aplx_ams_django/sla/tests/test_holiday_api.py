"""
FEAT-010 API-layer tests for REQ S-24 (Company Holiday List).

Covers the HTTP endpoint acceptance criteria:
  AC-1: POST /api/holidays/ by delivery_manager → 201 Created.
  AC-2: DELETE /api/holidays/{id}/ by delivery_manager → 204 No Content
        (soft-remove: sets removed_at, not hard delete).
  AC-3: Non-DM roles (L1, L2/L3, client_user) cannot POST → 403 Forbidden.
  AC-3: Non-DM roles cannot DELETE → 403 Forbidden.
  AC-3 (GET): GET /api/holidays/ by all authenticated roles → 200 OK.

Mode A: the sla URL patterns are not yet registered in the root urls.py
(src/aplx_ams_django/urls.py). The backend-builder registers them in Mode B.
Every request therefore returns HTTP 404. This is the accepted red state —
the behavior is missing (URL not registered), not a setup or syntax error.

PLAN GAP: this file (test_holiday_api.py) is not listed in plan.md § Tests
(which names only test_holiday_list.py). An SCR is required to add it to the
plan. Logged as OQ-076 in docs/logs/open-questions-log.md.

AC-3 permission tests are in this file (API layer); the DB-layer test file
(test_holiday_list.py) explicitly defers permission testing here.

Role values from accounts.models.UserRole:
  l1_support_engineer, l2_l3_support_engineer, delivery_manager, client_user
"""

from __future__ import annotations

import pytest
from rest_framework.test import APIClient


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_user(username: str, role: str, client_org: object = None) -> object:
    """Create a User with the specified role for test authentication.

    For client_user role, pass client_org= because chk_client_user_has_org
    requires client_org to be set on insert.
    """
    from django.contrib.auth import get_user_model

    User = get_user_model()
    return User.objects.create_user(
        username=username,
        password="Password1A",
        name=f"Test {role}",
        email=f"{username}@example.com",
        role=role,
        client_org=client_org,
    )


def _authenticated_client(user: object) -> APIClient:
    """Return an APIClient force-logged-in as the given user."""
    client = APIClient()
    client.force_login(user)
    return client


# ---------------------------------------------------------------------------
# AC-1: POST /api/holidays/ by delivery_manager → 201
# ---------------------------------------------------------------------------

@pytest.mark.django_db
def test_ac1_dm_can_add_holiday() -> None:
    """AC-1: A delivery_manager (P3) POST to /api/holidays/ receives 201 Created.

    Mode A red reason: sla URLs are not registered in root urls.py → 404.
    Mode B expected: view creates a HolidayEntry and returns 201.
    """
    dm = _make_user("dm_api_ac1", "delivery_manager")
    client = _authenticated_client(dm)

    response = client.post(
        "/api/holidays/",
        {"holiday_date": "2027-01-26"},
        format="json",
    )

    assert response.status_code == 201, (
        f"DM POST /api/holidays/ expected 201, got {response.status_code}. "
        f"Mode A: 404 expected (URL not registered); Mode B must return 201."
    )


# ---------------------------------------------------------------------------
# AC-2: DELETE /api/holidays/{id}/ by delivery_manager → 204 (soft-remove)
# ---------------------------------------------------------------------------

@pytest.mark.django_db
def test_ac2_dm_can_remove_holiday() -> None:
    """AC-2: A delivery_manager DELETE /api/holidays/{id}/ receives 204 No Content
    and the entry is soft-removed (removed_at set, not hard-deleted).

    Mode A red reason: sla URLs are not registered in root urls.py → 404.
    Mode B expected: service sets removed_at/removed_by and returns 204.
    """
    from datetime import datetime, timezone

    from aplx_ams_django.sla.models import HolidayEntry

    dm = _make_user("dm_api_ac2", "delivery_manager")

    # Pre-create an active holiday entry to delete.
    entry = HolidayEntry.objects.create(
        holiday_date="2027-03-15",
        added_at=datetime(2027, 3, 1, 9, 0, tzinfo=timezone.utc),
        added_by=dm,
    )

    client = _authenticated_client(dm)
    response = client.delete(f"/api/holidays/{entry.pk}/")

    assert response.status_code == 204, (
        f"DM DELETE /api/holidays/{entry.pk}/ expected 204, got {response.status_code}. "
        f"Mode A: 404 expected (URL not registered); Mode B must return 204."
    )

    # In Mode B, also verify the entry is soft-removed (not hard-deleted).
    entry.refresh_from_db()
    assert entry.removed_at is not None, (
        "DELETE must soft-remove (set removed_at), not hard-delete."
    )


# ---------------------------------------------------------------------------
# AC-3: Non-DM cannot POST — each role that must be blocked
# ---------------------------------------------------------------------------

@pytest.mark.django_db
def test_ac3_l1_cannot_add_holiday() -> None:
    """AC-3: An L1 support engineer (P1, role=l1_support_engineer) POST to
    /api/holidays/ must return 403 Forbidden.

    Mode A red reason: sla URLs are not registered → 404 (not 403).
    Mode B expected: HasRolePermission returns 403 before any DB write.
    """
    l1 = _make_user("l1_api_ac3", "l1_support_engineer")
    client = _authenticated_client(l1)

    response = client.post(
        "/api/holidays/",
        {"holiday_date": "2027-06-01"},
        format="json",
    )

    assert response.status_code == 403, (
        f"l1_support_engineer POST /api/holidays/ expected 403 Forbidden, "
        f"got {response.status_code}. "
        f"Mode A: 404 expected (URL not registered); Mode B must return 403."
    )


@pytest.mark.django_db
def test_ac3_l2_l3_cannot_add_holiday() -> None:
    """AC-3: An L2/L3 support engineer (P2, role=l2_l3_support_engineer) POST to
    /api/holidays/ must return 403 Forbidden.

    Mode A red reason: sla URLs are not registered → 404 (not 403).
    Mode B expected: HasRolePermission returns 403.
    """
    l2 = _make_user("l2_api_ac3", "l2_l3_support_engineer")
    client = _authenticated_client(l2)

    response = client.post(
        "/api/holidays/",
        {"holiday_date": "2027-06-02"},
        format="json",
    )

    assert response.status_code == 403, (
        f"l2_l3_support_engineer POST /api/holidays/ expected 403 Forbidden, "
        f"got {response.status_code}. "
        f"Mode A: 404 expected (URL not registered); Mode B must return 403."
    )


@pytest.mark.django_db
def test_ac3_client_user_cannot_add_holiday() -> None:
    """AC-3: A client_user (P4, role=client_user) POST to /api/holidays/ must
    return 403 Forbidden.

    Mode A red reason: sla URLs are not registered → 404 (not 403).
    Mode B expected: HasRolePermission returns 403.
    """
    from aplx_ams_django.organizations.models import ClientOrg

    org = ClientOrg.objects.create(name="TestOrgAC3Post")
    cu = _make_user("cu_api_ac3", "client_user", client_org=org)

    client = _authenticated_client(cu)
    response = client.post(
        "/api/holidays/",
        {"holiday_date": "2027-06-03"},
        format="json",
    )

    assert response.status_code == 403, (
        f"client_user POST /api/holidays/ expected 403 Forbidden, "
        f"got {response.status_code}. "
        f"Mode A: 404 expected (URL not registered); Mode B must return 403."
    )


# ---------------------------------------------------------------------------
# AC-3: Non-DM cannot DELETE
# ---------------------------------------------------------------------------

@pytest.mark.django_db
def test_ac3_l1_cannot_remove_holiday() -> None:
    """AC-3: An L1 support engineer DELETE /api/holidays/{id}/ must return 403.

    Mode A red reason: sla URLs are not registered → 404 (not 403).
    Mode B expected: HasRolePermission returns 403.
    """
    from datetime import datetime, timezone

    from aplx_ams_django.sla.models import HolidayEntry

    dm_owner = _make_user("dm_owner_del_l1", "delivery_manager")
    entry = HolidayEntry.objects.create(
        holiday_date="2027-07-01",
        added_at=datetime(2027, 6, 1, 9, 0, tzinfo=timezone.utc),
        added_by=dm_owner,
    )

    l1 = _make_user("l1_delete_ac3", "l1_support_engineer")
    client = _authenticated_client(l1)
    response = client.delete(f"/api/holidays/{entry.pk}/")

    assert response.status_code == 403, (
        f"l1_support_engineer DELETE /api/holidays/{entry.pk}/ expected 403, "
        f"got {response.status_code}. "
        f"Mode A: 404 expected (URL not registered); Mode B must return 403."
    )


@pytest.mark.django_db
def test_ac3_l2_l3_cannot_remove_holiday() -> None:
    """AC-3: An L2/L3 support engineer DELETE /api/holidays/{id}/ must return 403.

    Mode A red reason: sla URLs are not registered → 404 (not 403).
    Mode B expected: HasRolePermission returns 403.
    """
    from datetime import datetime, timezone

    from aplx_ams_django.sla.models import HolidayEntry

    dm_owner = _make_user("dm_owner_del_l2", "delivery_manager")
    entry = HolidayEntry.objects.create(
        holiday_date="2027-07-02",
        added_at=datetime(2027, 6, 2, 9, 0, tzinfo=timezone.utc),
        added_by=dm_owner,
    )

    l2 = _make_user("l2_delete_ac3", "l2_l3_support_engineer")
    client = _authenticated_client(l2)
    response = client.delete(f"/api/holidays/{entry.pk}/")

    assert response.status_code == 403, (
        f"l2_l3_support_engineer DELETE /api/holidays/{entry.pk}/ expected 403, "
        f"got {response.status_code}. "
        f"Mode A: 404 expected (URL not registered); Mode B must return 403."
    )


# ---------------------------------------------------------------------------
# AC-3 (GET): GET /api/holidays/ is accessible to all authenticated roles
# ---------------------------------------------------------------------------

@pytest.mark.django_db
def test_ac3_all_roles_can_list_holidays_dm() -> None:
    """AC-3 (GET): delivery_manager GET /api/holidays/ must return 200 OK.

    Mode A red reason: sla URLs are not registered → 404 (not 200).
    Mode B expected: list action returns 200 for any authenticated user.
    """
    dm = _make_user("dm_list_ac3", "delivery_manager")
    client = _authenticated_client(dm)
    response = client.get("/api/holidays/")

    assert response.status_code == 200, (
        f"delivery_manager GET /api/holidays/ expected 200, got {response.status_code}. "
        f"Mode A: 404 expected (URL not registered); Mode B must return 200."
    )


@pytest.mark.django_db
def test_ac3_all_roles_can_list_holidays_l1() -> None:
    """AC-3 (GET): l1_support_engineer GET /api/holidays/ must return 200 OK.

    Mode A red reason: sla URLs are not registered → 404 (not 200).
    Mode B expected: list action returns 200 for any authenticated user.
    """
    l1 = _make_user("l1_list_ac3", "l1_support_engineer")
    client = _authenticated_client(l1)
    response = client.get("/api/holidays/")

    assert response.status_code == 200, (
        f"l1_support_engineer GET /api/holidays/ expected 200, got {response.status_code}. "
        f"Mode A: 404 expected (URL not registered); Mode B must return 200."
    )


@pytest.mark.django_db
def test_ac3_unauthenticated_get_is_rejected() -> None:
    """AC-3 (auth): Unauthenticated GET /api/holidays/ must return 401 or 403.

    Mode A red reason: sla URLs are not registered → 404.
    Mode B expected: IsAuthenticated permission returns 401 (DRF default with
    SameSiteSessionAuthentication that sets authenticate_header) for anonymous requests.
    """
    client = APIClient()  # No force_login — anonymous request.
    response = client.get("/api/holidays/")

    assert response.status_code in (401, 403), (
        f"Anonymous GET /api/holidays/ expected 401 or 403, got {response.status_code}. "
        f"Mode A: 404 expected (URL not registered); Mode B must reject unauthenticated."
    )
