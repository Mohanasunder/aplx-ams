"""
FEAT-003 backend API tests — Mode A (red run).

Tests assert the contract API behavior as defined in API-001 v0.2 / PRM-001 v0.1.
All tests are RED in Mode A: ContractViewSet is a stub returning 501 with no
permission enforcement, so every assertion fails due to missing behavior, not
due to import, syntax, or setup errors.

Criterion coverage
------------------
AC-1  test_dm_can_create_hours_bank_contract
AC-1  test_hours_bank_contract_balance_shows_100
AC-2  test_second_active_contract_returns_409
AC-3  test_fixed_fee_contract_has_no_contracted_hours
AC-4  test_p1_cannot_create_contract
AC-4  test_p2_cannot_create_contract
AC-4  test_p4_cannot_create_contract

User roles per PRM-001 v0.1:
  P1 = L1 support engineer
  P2 = L2/L3 support engineer
  P3 = Delivery manager (DM)
  P4 = Client user
"""

from __future__ import annotations

from types import SimpleNamespace

from rest_framework.test import APIClient

from aplx_ams_django.organizations.models import ClientOrg


# ---------------------------------------------------------------------------
# Test helpers
# ---------------------------------------------------------------------------


def _make_user(role: str, pk: int = 1) -> SimpleNamespace:
    """Return a lightweight user stub with the given role.

    SimpleNamespace is accepted by DRF force_authenticate; role is the only
    extra attribute HasRolePermission checks (PRM-001 v0.1).
    """
    return SimpleNamespace(is_authenticated=True, role=role, pk=pk)


def _dm_client(pk: int = 100) -> APIClient:
    """Return an APIClient authenticated as a Delivery Manager (P3)."""
    client = APIClient()
    client.force_authenticate(user=_make_user("P3", pk=pk))
    return client


def _create_org(name: str) -> int:
    """Persist a ClientOrg with the given name and return its pk.

    Called inside test functions; the autouse _enable_db_for_all fixture in
    conftest.py provides the DB transaction for every test in this directory.
    """
    org = ClientOrg.objects.create(name=name)
    return org.pk


# ---------------------------------------------------------------------------
# AC-1: DM creates an hours_bank contract of 100 h → HTTP 201, response body
#        contains contract_type=hours_bank and contracted_hours=100.
# ---------------------------------------------------------------------------


def test_dm_can_create_hours_bank_contract() -> None:
    """AC-1 — P3 posts an hours_bank contract with 100 contracted hours.

    Asserts:
    - HTTP status is 201 Created.
    - Response body field contract_type equals "hours_bank".
    - Response body field contracted_hours equals 100.

    Mode A failure: ContractViewSet.create stub returns 501 Not Implemented,
    so the status assertion fails (501 != 201).
    """
    client = _dm_client(pk=100)
    org_id = _create_org("Org Alpha HB")
    response = client.post(
        f"/api/organizations/{org_id}/contracts/",
        {"contract_type": "hours_bank", "contracted_hours": 100, "is_active": True},
        format="json",
    )
    assert response.status_code == 201, (
        f"Expected 201 Created, got {response.status_code}. "
        "ContractViewSet.create not yet implemented (Mode A red)."
    )
    data = response.json()
    assert data["contract_type"] == "hours_bank", (
        f"Expected contract_type='hours_bank', got {data.get('contract_type')}."
    )
    assert int(data["contracted_hours"]) == 100, (
        f"Expected contracted_hours=100, got {data.get('contracted_hours')}."
    )


# ---------------------------------------------------------------------------
# AC-1: GET active contract shows hours_bank_balance = contracted_hours = 100.
# ---------------------------------------------------------------------------


def test_hours_bank_contract_balance_shows_100() -> None:
    """AC-1 — After creating a 100 h hours_bank contract, GET
    /api/organizations/{id}/contracts/active/ returns hours_bank_balance=100.

    Asserts:
    - HTTP status is 200 OK.
    - Response body field hours_bank_balance equals 100.

    Mode A failure: ContractViewSet.get_active stub returns 501, so the
    status assertion fails (501 != 200).
    """
    client = _dm_client(pk=101)
    org_id = _create_org("Org Alpha Balance")
    # Create the contract (also a stub in Mode A, but the GET test must still run)
    client.post(
        f"/api/organizations/{org_id}/contracts/",
        {"contract_type": "hours_bank", "contracted_hours": 100, "is_active": True},
        format="json",
    )
    response = client.get(f"/api/organizations/{org_id}/contracts/active/")
    assert response.status_code == 200, (
        f"Expected 200 OK, got {response.status_code}. "
        "ContractViewSet.get_active not yet implemented (Mode A red)."
    )
    data = response.json()
    assert data.get("hours_bank_balance") == 100, (
        f"Expected hours_bank_balance=100, got {data.get('hours_bank_balance')}."
    )


# ---------------------------------------------------------------------------
# AC-2: Second active contract for same org → HTTP 409.
# ---------------------------------------------------------------------------


def test_second_active_contract_returns_409() -> None:
    """AC-2 — When org A already has one active contract, a second POST with
    is_active=True must return HTTP 409 Conflict.

    Asserts:
    - HTTP status is 409 Conflict on the second create request.
    - The first create was accepted (201) so only the duplicate is refused.

    Mode A failure: ContractViewSet.create stub returns 501 for both requests,
    so the second assertion fails (501 != 409).
    """
    client = _dm_client(pk=102)
    org_id = _create_org("Org Beta")
    # First contract (expected 201 in Mode B; 501 in Mode A — not asserted here)
    client.post(
        f"/api/organizations/{org_id}/contracts/",
        {"contract_type": "hours_bank", "contracted_hours": 100, "is_active": True},
        format="json",
    )
    # Second active contract for the same org — must be refused
    response = client.post(
        f"/api/organizations/{org_id}/contracts/",
        {"contract_type": "fixed_fee", "is_active": True},
        format="json",
    )
    assert response.status_code == 409, (
        f"Expected 409 Conflict for duplicate active contract, got {response.status_code}. "
        "Duplicate active contract guard not yet implemented (Mode A red)."
    )


# ---------------------------------------------------------------------------
# AC-3: fixed_fee contract → HTTP 201, contracted_hours is null.
# ---------------------------------------------------------------------------


def test_fixed_fee_contract_has_no_contracted_hours() -> None:
    """AC-3 — P3 posts a fixed_fee contract without contracted_hours.

    Asserts:
    - HTTP status is 201 Created.
    - Response body field contracted_hours is null (None).

    Mode A failure: ContractViewSet.create stub returns 501, so the status
    assertion fails (501 != 201).
    """
    client = _dm_client(pk=103)
    org_id = _create_org("Org Gamma FF")
    response = client.post(
        f"/api/organizations/{org_id}/contracts/",
        {"contract_type": "fixed_fee", "is_active": True},
        format="json",
    )
    assert response.status_code == 201, (
        f"Expected 201 Created for fixed_fee contract, got {response.status_code}. "
        "ContractViewSet.create not yet implemented (Mode A red)."
    )
    data = response.json()
    assert data.get("contracted_hours") is None, (
        f"Expected contracted_hours=null for fixed_fee, got {data.get('contracted_hours')}."
    )


# ---------------------------------------------------------------------------
# AC-4: non-P3 roles cannot create contracts → HTTP 403.
# ---------------------------------------------------------------------------


def test_p1_cannot_create_contract() -> None:
    """AC-4 — L1 support engineer (P1) cannot create a contract → HTTP 403.

    Asserts:
    - HTTP status is 403 Forbidden when a P1 user POSTs to the contracts endpoint.

    Mode A failure: ContractViewSet.create stub has no permission enforcement
    and returns 501, so the assertion fails (501 != 403).
    """
    client = APIClient()
    client.force_authenticate(user=_make_user("P1", pk=200))
    org_id = _create_org("Org Delta P1")
    response = client.post(
        f"/api/organizations/{org_id}/contracts/",
        {"contract_type": "hours_bank", "contracted_hours": 50, "is_active": True},
        format="json",
    )
    assert response.status_code == 403, (
        f"Expected 403 Forbidden for P1, got {response.status_code}. "
        "Permission enforcement not yet implemented (Mode A red)."
    )


def test_p2_cannot_create_contract() -> None:
    """AC-4 — L2/L3 support engineer (P2) cannot create a contract → HTTP 403.

    Asserts:
    - HTTP status is 403 Forbidden when a P2 user POSTs to the contracts endpoint.

    Mode A failure: ContractViewSet.create stub has no permission enforcement
    and returns 501, so the assertion fails (501 != 403).
    """
    client = APIClient()
    client.force_authenticate(user=_make_user("P2", pk=201))
    org_id = _create_org("Org Delta P2")
    response = client.post(
        f"/api/organizations/{org_id}/contracts/",
        {"contract_type": "hours_bank", "contracted_hours": 50, "is_active": True},
        format="json",
    )
    assert response.status_code == 403, (
        f"Expected 403 Forbidden for P2, got {response.status_code}. "
        "Permission enforcement not yet implemented (Mode A red)."
    )


def test_p4_cannot_create_contract() -> None:
    """AC-4 — Client user (P4) cannot create a contract → HTTP 403.

    Asserts:
    - HTTP status is 403 Forbidden when a P4 user POSTs to the contracts endpoint.

    Mode A failure: ContractViewSet.create stub has no permission enforcement
    and returns 501, so the assertion fails (501 != 403).
    """
    client = APIClient()
    client.force_authenticate(user=_make_user("P4", pk=202))
    org_id = _create_org("Org Delta P4")
    response = client.post(
        f"/api/organizations/{org_id}/contracts/",
        {"contract_type": "hours_bank", "contracted_hours": 50, "is_active": True},
        format="json",
    )
    assert response.status_code == 403, (
        f"Expected 403 Forbidden for P4, got {response.status_code}. "
        "Permission enforcement not yet implemented (Mode A red)."
    )
