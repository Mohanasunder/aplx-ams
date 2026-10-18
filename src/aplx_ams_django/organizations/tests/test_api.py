"""
FEAT-002 backend API tests — Mode A (red run).

Criterion coverage:
  REQ-018 AC-1  test_dm_can_create_org_and_sap_app
  REQ-018 AC-2  test_sap_app_isolated_to_org
  REQ-018 AC-3  test_p1_cannot_create_org
  REQ-018 AC-3  test_p2_cannot_create_org
  REQ-018 AC-3  test_p4_cannot_create_org
  REQ-018 AC-3  test_p1_cannot_add_sap_app

All tests are RED in Mode A: organizations/urls.py has empty urlpatterns so
every endpoint returns 404. Tests assert 201, 200, or 403 — all fail with
AssertionError because the behavior is missing, not because of import or
setup errors.

User roles per PRM-001 v0.1:
  P1 = L1 support engineer
  P2 = L2/L3 support engineer
  P3 = Delivery manager (DM)
  P4 = Client user
"""

from types import SimpleNamespace

from rest_framework.test import APIClient


# ---------------------------------------------------------------------------
# Test helpers
# ---------------------------------------------------------------------------

def _make_user(role: str, pk: int = 1) -> SimpleNamespace:
    """Return a lightweight user stub with the given role.

    SimpleNamespace is accepted by DRF force_authenticate; role is the
    only extra attribute HasRolePermission checks (PRM-001 v0.1).
    """
    return SimpleNamespace(is_authenticated=True, role=role, pk=pk)


def _dm_client() -> APIClient:
    """Return an APIClient authenticated as a Delivery Manager (P3)."""
    client = APIClient()
    client.force_authenticate(user=_make_user("P3", pk=100))
    return client


# ---------------------------------------------------------------------------
# REQ-018 AC-1
# ---------------------------------------------------------------------------

def test_dm_can_create_org_and_sap_app() -> None:
    """REQ-018 AC-1 — DM creates a client org, adds a SAP app; the SAP app
    then appears in that org's SAP application list (so client users of
    that org can choose it when raising a ticket).

    Mode A failure: POST /api/organizations/ returns 404 (endpoint not
    registered) instead of 201.
    """
    client = _dm_client()

    # Step 1: create client organization
    org_response = client.post(
        "/api/organizations/",
        {"name": "Applexus"},
        format="json",
    )
    assert org_response.status_code == 201, (
        f"Expected 201 Created, got {org_response.status_code}. "
        "Endpoint not yet implemented (Mode A red)."
    )
    org_id = org_response.json()["id"]

    # Step 2: add a SAP application to the org
    sap_response = client.post(
        f"/api/organizations/{org_id}/sap-applications/",
        {"name": "SAP S/4HANA", "sid": "S4H"},
        format="json",
    )
    assert sap_response.status_code == 201, (
        f"Expected 201 Created, got {sap_response.status_code}."
    )
    sap_app_id = sap_response.json()["id"]

    # Step 3: verify SAP app is visible in the org's list
    list_response = client.get(f"/api/organizations/{org_id}/sap-applications/")
    assert list_response.status_code == 200
    sap_ids = [app["id"] for app in list_response.json()]
    assert sap_app_id in sap_ids, (
        "SAP application must appear in the org's SAP application list "
        "so that client users of that org can choose it when raising a ticket."
    )


# ---------------------------------------------------------------------------
# REQ-018 AC-2
# ---------------------------------------------------------------------------

def test_sap_app_isolated_to_org() -> None:
    """REQ-018 AC-2 — SAP application added to org A is NOT visible in org
    B's SAP application list.

    Mode A failure: POST /api/organizations/ returns 404 (endpoint not
    registered) instead of 201.
    """
    client = _dm_client()

    # Create org A
    resp_a = client.post(
        "/api/organizations/",
        {"name": "Org A"},
        format="json",
    )
    assert resp_a.status_code == 201, (
        f"Expected 201 Created for org A, got {resp_a.status_code}."
    )
    org_a_id = resp_a.json()["id"]

    # Create org B (use a different DM user pk to avoid caching effects)
    resp_b = client.post(
        "/api/organizations/",
        {"name": "Org B"},
        format="json",
    )
    assert resp_b.status_code == 201, (
        f"Expected 201 Created for org B, got {resp_b.status_code}."
    )
    org_b_id = resp_b.json()["id"]

    # Add SAP app to org A only
    sap_resp = client.post(
        f"/api/organizations/{org_a_id}/sap-applications/",
        {"name": "SAP ECC", "sid": "ECC"},
        format="json",
    )
    assert sap_resp.status_code == 201
    sap_app_id = sap_resp.json()["id"]

    # Verify org B's SAP app list does NOT contain org A's SAP app
    list_resp = client.get(f"/api/organizations/{org_b_id}/sap-applications/")
    assert list_resp.status_code == 200
    b_sap_ids = [app["id"] for app in list_resp.json()]
    assert sap_app_id not in b_sap_ids, (
        "SAP application from org A must NOT appear in org B's list."
    )


# ---------------------------------------------------------------------------
# REQ-018 AC-3  — unauthorized roles cannot create orgs or add SAP apps
# ---------------------------------------------------------------------------

def test_p1_cannot_create_org() -> None:
    """REQ-018 AC-3 — L1 support engineer (P1) cannot create a client org;
    the request must be refused with HTTP 403.

    Mode A failure: endpoint returns 404 (not registered) instead of 403.
    """
    client = APIClient()
    client.force_authenticate(user=_make_user("P1"))
    response = client.post(
        "/api/organizations/",
        {"name": "Unauthorized Org"},
        format="json",
    )
    assert response.status_code == 403, (
        f"Expected 403 Forbidden for P1, got {response.status_code}. "
        "Permission check not yet implemented (Mode A red)."
    )


def test_p2_cannot_create_org() -> None:
    """REQ-018 AC-3 — L2/L3 support engineer (P2) cannot create a client
    org; the request must be refused with HTTP 403.

    Mode A failure: endpoint returns 404 (not registered) instead of 403.
    """
    client = APIClient()
    client.force_authenticate(user=_make_user("P2"))
    response = client.post(
        "/api/organizations/",
        {"name": "Unauthorized Org"},
        format="json",
    )
    assert response.status_code == 403, (
        f"Expected 403 Forbidden for P2, got {response.status_code}."
    )


def test_p4_cannot_create_org() -> None:
    """REQ-018 AC-3 — Client user (P4) cannot create a client org; the
    request must be refused with HTTP 403.

    Mode A failure: endpoint returns 404 (not registered) instead of 403.
    """
    client = APIClient()
    client.force_authenticate(user=_make_user("P4"))
    response = client.post(
        "/api/organizations/",
        {"name": "Unauthorized Org"},
        format="json",
    )
    assert response.status_code == 403, (
        f"Expected 403 Forbidden for P4, got {response.status_code}."
    )


def test_p1_cannot_add_sap_app() -> None:
    """REQ-018 AC-3 — L1 support engineer (P1) cannot add a SAP application
    to a client org; the request must be refused with HTTP 403.

    Mode A failure: endpoint returns 404 (not registered) instead of 403.
    """
    client = APIClient()
    client.force_authenticate(user=_make_user("P1"))
    # Use a fixed org id; the permission check should run before any DB lookup.
    response = client.post(
        "/api/organizations/1/sap-applications/",
        {"name": "SAP BTP", "sid": "BTP"},
        format="json",
    )
    assert response.status_code == 403, (
        f"Expected 403 Forbidden for P1 on SAP app endpoint, got {response.status_code}."
    )
