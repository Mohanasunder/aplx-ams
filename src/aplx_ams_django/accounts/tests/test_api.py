"""
FEAT-005 backend API tests — Mode A (tests first / red run).

Criterion -> test function mapping
----------------------------------
REQ-020 AC-1 (DM creates users with all four valid roles -> HTTP 201 and role stored):
    test_dm_creates_user_with_l1_support_engineer_role
    test_dm_creates_user_with_l2_l3_support_engineer_role
    test_dm_creates_user_with_delivery_manager_role
    test_dm_creates_user_with_client_user_role

REQ-020 AC-2 (client_user with no client_org_id -> HTTP 400, account NOT saved):
    test_create_client_user_without_client_org_returns_400

REQ-020 AC-3 (DM deactivates active user -> HTTP 200; is_active=False set):
    test_deactivate_user_returns_200
    test_deactivated_user_has_is_active_false
    # Sign-in refusal (HTTP 401) is deferred to FEAT-006: the sign-in
    # endpoint (/api/auth/login/) is out of scope for FEAT-005 per
    # plan.md section "Out Of Scope".

REQ-020 AC-4 (non-DM roles -> HTTP 403 on create / patch / deactivate):
    test_l1_cannot_create_user
    test_l2_l3_cannot_create_user
    test_client_user_cannot_create_user
    test_l1_cannot_patch_user
    test_l1_cannot_deactivate_user
    test_l2_l3_cannot_patch_user
    test_client_user_cannot_patch_user
    test_l2_l3_cannot_deactivate_user
    test_client_user_cannot_deactivate_user

All tests are RED in Mode A: stub views return HTTP 501 (Not Implemented)
regardless of method, role, or payload. Every assertion fails with an
AssertionError reporting the wrong status code, not because of import or
test-setup errors.

User roles per PRM-001 v0.1:
  delivery_manager (DM) — role stored in User.role
  l1_support_engineer — role stored in User.role
  l2_l3_support_engineer — role stored in User.role
  client_user — role stored in User.role
"""

from __future__ import annotations

from types import SimpleNamespace

from rest_framework.test import APIClient

from aplx_ams_django.organizations.models import ClientOrg

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_BASE_URL = "/api/accounts/users/"


def _make_user(role: str, pk: int = 1) -> SimpleNamespace:
    """Return a lightweight user stub with the given role.

    SimpleNamespace is accepted by DRF force_authenticate; role is the
    only extra attribute HasRolePermission checks (PRM-001 v0.1).
    """
    return SimpleNamespace(is_authenticated=True, role=role, pk=pk)


def _dm_client() -> APIClient:
    """Return an APIClient authenticated as a Delivery Manager (delivery_manager)."""
    client = APIClient()
    client.force_authenticate(user=_make_user("delivery_manager", pk=100))
    return client


# ---------------------------------------------------------------------------
# REQ-020 AC-1: DM creates users with each valid role -> HTTP 201
# ---------------------------------------------------------------------------


def test_dm_creates_user_with_l1_support_engineer_role() -> None:
    """AC-1 — DM creates a user with role l1_support_engineer; account saved (HTTP 201)
    and response body contains role='l1_support_engineer'.

    Mode A failure: stub view returns 501 instead of 201.
    """
    client = _dm_client()
    response = client.post(
        _BASE_URL,
        {
            "username": "l1_test_user",
            "name": "L1 Test User",
            "email": "l1test@test.example",
            "role": "l1_support_engineer",
        },
        format="json",
    )
    assert response.status_code == 201, (
        f"Expected 201 Created for l1_support_engineer role, "
        f"got {response.status_code}. Stub returns 501 (Mode A red)."
    )
    assert response.json()["role"] == "l1_support_engineer", (
        "Response body must contain role='l1_support_engineer'."
    )


def test_dm_creates_user_with_l2_l3_support_engineer_role() -> None:
    """AC-1 — DM creates a user with role l2_l3_support_engineer; account saved (HTTP 201)
    and response body contains role='l2_l3_support_engineer'.

    Mode A failure: stub view returns 501 instead of 201.
    """
    client = _dm_client()
    response = client.post(
        _BASE_URL,
        {
            "username": "l2l3_test_user",
            "name": "L2L3 Test User",
            "email": "l2l3test@test.example",
            "role": "l2_l3_support_engineer",
        },
        format="json",
    )
    assert response.status_code == 201, (
        f"Expected 201 Created for l2_l3_support_engineer role, "
        f"got {response.status_code}. Stub returns 501 (Mode A red)."
    )
    assert response.json()["role"] == "l2_l3_support_engineer", (
        "Response body must contain role='l2_l3_support_engineer'."
    )


def test_dm_creates_user_with_delivery_manager_role() -> None:
    """AC-1 — DM creates a user with role delivery_manager; account saved (HTTP 201)
    and response body contains role='delivery_manager'.

    Mode A failure: stub view returns 501 instead of 201.
    """
    client = _dm_client()
    response = client.post(
        _BASE_URL,
        {
            "username": "dm_test_user",
            "name": "DM Test User",
            "email": "dmtest@test.example",
            "role": "delivery_manager",
        },
        format="json",
    )
    assert response.status_code == 201, (
        f"Expected 201 Created for delivery_manager role, "
        f"got {response.status_code}. Stub returns 501 (Mode A red)."
    )
    assert response.json()["role"] == "delivery_manager", (
        "Response body must contain role='delivery_manager'."
    )


def test_dm_creates_user_with_client_user_role() -> None:
    """AC-1 — DM creates a user with role client_user and a valid client_org_id;
    account saved (HTTP 201) and response body contains role='client_user'
    and the correct client_org_id.

    Mode A failure: stub view returns 501 instead of 201.
    """
    org = ClientOrg.objects.create(name="AC1TestCorp")
    client = _dm_client()
    response = client.post(
        _BASE_URL,
        {
            "username": "client_test_user",
            "name": "Client Test User",
            "email": "clienttest@test.example",
            "role": "client_user",
            "client_org_id": org.pk,
        },
        format="json",
    )
    assert response.status_code == 201, (
        f"Expected 201 Created for client_user role with org, "
        f"got {response.status_code}. Stub returns 501 (Mode A red)."
    )
    assert response.json()["role"] == "client_user", (
        "Response body must contain role='client_user'."
    )
    assert response.json()["client_org_id"] == org.pk, (
        "Response body must contain the correct client_org_id."
    )


# ---------------------------------------------------------------------------
# REQ-020 AC-2: client_user with no client_org_id -> HTTP 400
# ---------------------------------------------------------------------------


def test_create_client_user_without_client_org_returns_400() -> None:
    """AC-2 — DM creates a client_user account with no client_org_id; account NOT saved
    and endpoint returns HTTP 400 Bad Request.

    Mode A failure: stub view returns 501 instead of 400.
    """
    client = _dm_client()
    response = client.post(
        _BASE_URL,
        {
            "username": "orphan_client",
            "name": "Orphan Client",
            "email": "orphan@test.example",
            "role": "client_user",
            # client_org_id intentionally omitted
        },
        format="json",
    )
    assert response.status_code == 400, (
        f"Expected 400 Bad Request for client_user without client_org_id, "
        f"got {response.status_code}. Stub returns 501 (Mode A red)."
    )


# ---------------------------------------------------------------------------
# REQ-020 AC-3: DM deactivates active user -> HTTP 200; is_active=False set
# ---------------------------------------------------------------------------


def test_deactivate_user_returns_200() -> None:
    """AC-3 — DM sends POST /api/accounts/users/{id}/deactivate/ for an active user;
    endpoint returns HTTP 200 OK.

    Mode A failure: create endpoint returns 501, so the first assertion
    fails (mode A red: missing create behavior).

    Note: Sign-in refusal (HTTP 401) for a deactivated user is deferred to
    FEAT-006, which implements the sign-in endpoint. This is explicitly out of
    scope for FEAT-005 per plan.md section 'Out Of Scope'.
    """
    client = _dm_client()
    # Step 1: create user via API (stub returns 501 in Mode A)
    create_resp = client.post(
        _BASE_URL,
        {
            "username": "to_deactivate",
            "name": "To Deactivate",
            "email": "deact@test.example",
            "role": "delivery_manager",
        },
        format="json",
    )
    assert create_resp.status_code == 201, (
        f"Expected 201 for user creation, got {create_resp.status_code} "
        "(Mode A red: stub returns 501)."
    )
    user_id = create_resp.json()["id"]

    # Step 2: deactivate the user
    deact_resp = client.post(f"{_BASE_URL}{user_id}/deactivate/")
    assert deact_resp.status_code == 200, (
        f"Expected 200 OK for deactivation, got {deact_resp.status_code} "
        "(Mode A red: stub returns 501)."
    )


def test_deactivated_user_has_is_active_false() -> None:
    """AC-3 — After DM deactivates a user, the user detail endpoint returns
    is_active=False, confirming the user can no longer sign in.

    Mode A failure: create endpoint returns 501, so the first assertion
    fails (mode A red: missing create behavior).

    Note: Sign-in refusal (HTTP 401) for the deactivated user is deferred to
    FEAT-006 (sign-in endpoint is out of scope for FEAT-005 per plan.md
    section 'Out Of Scope').
    """
    client = _dm_client()
    # Step 1: create an active user
    create_resp = client.post(
        _BASE_URL,
        {
            "username": "is_active_check_user",
            "name": "IsActive Check User",
            "email": "isactive@test.example",
            "role": "delivery_manager",
        },
        format="json",
    )
    assert create_resp.status_code == 201, (
        f"Expected 201 for user creation, got {create_resp.status_code} "
        "(Mode A red: stub returns 501)."
    )
    user_id = create_resp.json()["id"]

    # Step 2: deactivate the user
    deact_resp = client.post(f"{_BASE_URL}{user_id}/deactivate/")
    assert deact_resp.status_code == 200, (
        f"Expected 200 OK for deactivation, got {deact_resp.status_code} "
        "(Mode A red: stub returns 501)."
    )

    # Step 3: fetch the user detail and assert is_active=False
    detail_resp = client.get(f"{_BASE_URL}{user_id}/")
    assert detail_resp.status_code == 200, (
        f"Expected 200 OK for user detail, got {detail_resp.status_code}."
    )
    assert detail_resp.json()["is_active"] is False, (
        "Deactivated user must have is_active=False in the user detail response "
        "so that the sign-in layer (FEAT-006) can reject that user's credentials."
    )


# ---------------------------------------------------------------------------
# REQ-020 AC-4: non-DM roles -> HTTP 403 on create / patch / deactivate
# ---------------------------------------------------------------------------


def test_l1_cannot_create_user() -> None:
    """AC-4 — L1 support engineer (l1_support_engineer) cannot create a user account; refused with HTTP 403.

    Mode A failure: stub view applies no permission check and returns 501 instead of 403.
    """
    client = APIClient()
    client.force_authenticate(user=_make_user("l1_support_engineer"))
    response = client.post(
        _BASE_URL,
        {
            "username": "l1_attempt",
            "name": "L1 Attempt",
            "email": "l1attempt@test.example",
            "role": "l1_support_engineer",
        },
        format="json",
    )
    assert response.status_code == 403, (
        f"Expected 403 Forbidden for l1_support_engineer on create, got {response.status_code}. "
        "Permission check not yet implemented (Mode A red: stub returns 501)."
    )


def test_l2_l3_cannot_create_user() -> None:
    """AC-4 — L2/L3 support engineer (l2_l3_support_engineer) cannot create a user account; refused with HTTP 403.

    Mode A failure: stub view applies no permission check and returns 501 instead of 403.
    """
    client = APIClient()
    client.force_authenticate(user=_make_user("l2_l3_support_engineer"))
    response = client.post(
        _BASE_URL,
        {
            "username": "l2l3_attempt",
            "name": "L2L3 Attempt",
            "email": "l2l3attempt@test.example",
            "role": "l2_l3_support_engineer",
        },
        format="json",
    )
    assert response.status_code == 403, (
        f"Expected 403 Forbidden for l2_l3_support_engineer on create, got {response.status_code}. "
        "Permission check not yet implemented (Mode A red: stub returns 501)."
    )


def test_client_user_cannot_create_user() -> None:
    """AC-4 — Client user (client_user) cannot create a user account; refused with HTTP 403.

    Mode A failure: stub view applies no permission check and returns 501 instead of 403.
    """
    client = APIClient()
    client.force_authenticate(user=_make_user("client_user"))
    response = client.post(
        _BASE_URL,
        {
            "username": "p4_attempt",
            "name": "P4 Attempt",
            "email": "p4attempt@test.example",
            "role": "client_user",
        },
        format="json",
    )
    assert response.status_code == 403, (
        f"Expected 403 Forbidden for client_user on create, got {response.status_code}. "
        "Permission check not yet implemented (Mode A red: stub returns 501)."
    )


def test_l1_cannot_patch_user() -> None:
    """AC-4 — L1 support engineer (l1_support_engineer) cannot update a user account (PATCH); refused with HTTP 403.

    Mode A failure: stub view applies no permission check and returns 501 instead of 403.
    The permission check must run before any DB lookup; a fixed user pk=1 is used.
    """
    client = APIClient()
    client.force_authenticate(user=_make_user("l1_support_engineer"))
    response = client.patch(
        f"{_BASE_URL}1/",
        {"name": "Unauthorized Update"},
        format="json",
    )
    assert response.status_code == 403, (
        f"Expected 403 Forbidden for l1_support_engineer on PATCH, got {response.status_code}. "
        "Permission check not yet implemented (Mode A red: stub returns 501)."
    )


def test_l1_cannot_deactivate_user() -> None:
    """AC-4 — L1 support engineer (l1_support_engineer) cannot deactivate a user account; refused with HTTP 403.

    Mode A failure: stub view applies no permission check and returns 501 instead of 403.
    The permission check must run before any DB lookup; a fixed user pk=1 is used.
    """
    client = APIClient()
    client.force_authenticate(user=_make_user("l1_support_engineer"))
    response = client.post(f"{_BASE_URL}1/deactivate/")
    assert response.status_code == 403, (
        f"Expected 403 Forbidden for l1_support_engineer on deactivate, got {response.status_code}. "
        "Permission check not yet implemented (Mode A red: stub returns 501)."
    )


def test_l2_l3_cannot_patch_user() -> None:
    """AC-4 — L2/L3 support engineer (l2_l3_support_engineer) cannot update a user account (PATCH); refused with HTTP 403.

    Mode A failure: stub view applies no permission check and returns 501 instead of 403.
    The permission check must run before any DB lookup; a fixed user pk=1 is used.
    """
    client = APIClient()
    client.force_authenticate(user=_make_user("l2_l3_support_engineer"))
    response = client.patch(
        f"{_BASE_URL}1/",
        {"name": "Unauthorized Update"},
        format="json",
    )
    assert response.status_code == 403, (
        f"Expected 403 Forbidden for l2_l3_support_engineer on PATCH, got {response.status_code}. "
        "Permission check not yet implemented (Mode A red: stub returns 501)."
    )


def test_client_user_cannot_patch_user() -> None:
    """AC-4 — Client user (client_user) cannot update a user account (PATCH); refused with HTTP 403.

    Mode A failure: stub view applies no permission check and returns 501 instead of 403.
    The permission check must run before any DB lookup; a fixed user pk=1 is used.
    """
    client = APIClient()
    client.force_authenticate(user=_make_user("client_user"))
    response = client.patch(
        f"{_BASE_URL}1/",
        {"name": "Unauthorized Update"},
        format="json",
    )
    assert response.status_code == 403, (
        f"Expected 403 Forbidden for client_user on PATCH, got {response.status_code}. "
        "Permission check not yet implemented (Mode A red: stub returns 501)."
    )


def test_l2_l3_cannot_deactivate_user() -> None:
    """AC-4 — L2/L3 support engineer (l2_l3_support_engineer) cannot deactivate a user account; refused with HTTP 403.

    Mode A failure: stub view applies no permission check and returns 501 instead of 403.
    The permission check must run before any DB lookup; a fixed user pk=1 is used.
    """
    client = APIClient()
    client.force_authenticate(user=_make_user("l2_l3_support_engineer"))
    response = client.post(f"{_BASE_URL}1/deactivate/")
    assert response.status_code == 403, (
        f"Expected 403 Forbidden for l2_l3_support_engineer on deactivate, got {response.status_code}. "
        "Permission check not yet implemented (Mode A red: stub returns 501)."
    )


def test_client_user_cannot_deactivate_user() -> None:
    """AC-4 — Client user (client_user) cannot deactivate a user account; refused with HTTP 403.

    Mode A failure: stub view applies no permission check and returns 501 instead of 403.
    The permission check must run before any DB lookup; a fixed user pk=1 is used.
    """
    client = APIClient()
    client.force_authenticate(user=_make_user("client_user"))
    response = client.post(f"{_BASE_URL}1/deactivate/")
    assert response.status_code == 403, (
        f"Expected 403 Forbidden for client_user on deactivate, got {response.status_code}. "
        "Permission check not yet implemented (Mode A red: stub returns 501)."
    )
