"""
FEAT-005 database-layer tests (Mode A — tests first).

All tests in this file MUST fail on the stub; they assert schema fields and
DB behavior that do not yet exist.  They fail for the right reason (missing
implementation), not because of syntax, import, or test-setup errors.

Criterion -> test function mapping
----------------------------------
REQ-020 AC-1 (all four valid roles can be saved; invalid role rejected):
    test_role_field_exists
    test_role_field_has_all_four_valid_choices
    test_create_user_with_l1_support_engineer_role
    test_create_user_with_l2_l3_support_engineer_role
    test_create_user_with_delivery_manager_role
    test_create_user_with_client_user_role
    test_invalid_role_rejected

REQ-020 AC-2 (client_user with no client_org_id is rejected by DB constraint):
    test_client_user_without_org_raises_integrity_error
    test_client_user_with_valid_org_saved_successfully
    test_internal_role_with_org_raises_integrity_error

REQ-020 AC-3 (is_active field exists; deactivation persists through DB round-trip):
    test_is_active_field_is_booleanfield
    test_is_active_defaults_to_true
    test_deactivate_user_persists_through_db_round_trip

REQ-020 AC-4 (non-DM users cannot create/change/deactivate accounts):
    Not a model-layer concern. Enforced by the API permission layer (DRF
    IsDeliveryManager permission class).  No model test is written here.
    This is noted in the criterion-to-test map returned to the Orchestrator.
"""

from __future__ import annotations

import pytest
from django.db import IntegrityError
from django.db.models import BooleanField

from aplx_ams_django.accounts.models import User
from aplx_ams_django.organizations.models import ClientOrg

# ---------------------------------------------------------------------------
# REQ-020 AC-1: role field metadata (no DB access needed)
# ---------------------------------------------------------------------------


def test_role_field_exists() -> None:
    """AC-1 — User must have a role CharField/TextChoices field named 'role'.

    Fails on stub with FieldDoesNotExist because the stub defines no role field.
    """
    field = User._meta.get_field("role")
    assert field is not None


def test_role_field_has_all_four_valid_choices() -> None:
    """AC-1 — role field must expose choices for all four permitted role values.

    Fails on stub with FieldDoesNotExist (no role field).
    """
    field = User._meta.get_field("role")
    choice_values = {c[0] for c in (field.choices or [])}
    expected = {
        "l1_support_engineer",
        "l2_l3_support_engineer",
        "delivery_manager",
        "client_user",
    }
    assert expected.issubset(choice_values), (
        f"role field is missing choices: {expected - choice_values}"
    )


# ---------------------------------------------------------------------------
# REQ-020 AC-1: role persistence through DB round-trip (requires DB)
# ---------------------------------------------------------------------------


@pytest.mark.django_db
def test_create_user_with_l1_support_engineer_role() -> None:
    """AC-1 — l1_support_engineer role must persist through a DB round-trip.

    Fails on stub with TypeError: 'role' is not a recognized model field.
    """
    user = User.objects.create(
        username="l1_user",
        password="argon2$hashed",
        name="L1 User",
        email="l1@test.example",
        role="l1_support_engineer",
    )
    fetched = User.objects.get(pk=user.pk)
    assert fetched.role == "l1_support_engineer"


@pytest.mark.django_db
def test_create_user_with_l2_l3_support_engineer_role() -> None:
    """AC-1 — l2_l3_support_engineer role must persist through a DB round-trip.

    Fails on stub with TypeError: 'role' is not a recognized model field.
    """
    user = User.objects.create(
        username="l2l3_user",
        password="argon2$hashed",
        name="L2L3 User",
        email="l2l3@test.example",
        role="l2_l3_support_engineer",
    )
    fetched = User.objects.get(pk=user.pk)
    assert fetched.role == "l2_l3_support_engineer"


@pytest.mark.django_db
def test_create_user_with_delivery_manager_role() -> None:
    """AC-1 — delivery_manager role must persist through a DB round-trip.

    Fails on stub with TypeError: 'role' is not a recognized model field.
    """
    user = User.objects.create(
        username="dm_user",
        password="argon2$hashed",
        name="DM User",
        email="dm@test.example",
        role="delivery_manager",
    )
    fetched = User.objects.get(pk=user.pk)
    assert fetched.role == "delivery_manager"


@pytest.mark.django_db
def test_create_user_with_client_user_role() -> None:
    """AC-1 — client_user role with a valid ClientOrg must persist through a DB round-trip.

    Fails on stub with TypeError: 'role' is not a recognized model field.
    """
    org = ClientOrg.objects.create(name="TestCorp")
    user = User.objects.create(
        username="client_user_acc",
        password="argon2$hashed",
        name="Client User",
        email="client@test.example",
        role="client_user",
        client_org=org,
    )
    fetched = User.objects.get(pk=user.pk)
    assert fetched.role == "client_user"
    assert fetched.client_org_id == org.pk


@pytest.mark.django_db
def test_invalid_role_rejected() -> None:
    """AC-1 — An unrecognized role value must be rejected at the DB level.

    Fails on stub: 'role' is not a field, so create() raises TypeError (not
    IntegrityError/DataError); the pytest.raises context sees an unexpected
    exception type and the test is marked FAILED.
    """
    from django.db import DataError

    with pytest.raises((IntegrityError, DataError)):
        User.objects.create(
            username="bad_role_user",
            password="argon2$hashed",
            name="Bad Role",
            email="badrole@test.example",
            role="super_admin",
        )


# ---------------------------------------------------------------------------
# REQ-020 AC-2: client_user <-> client_org constraints (requires DB)
# ---------------------------------------------------------------------------


@pytest.mark.django_db
def test_client_user_without_org_raises_integrity_error() -> None:
    """AC-2 — client_user with client_org=None must be rejected by the DB check constraint.

    Fails on stub: no constraint exists, so no IntegrityError is raised;
    pytest.raises context exits without catching a matching exception -> FAILED.
    (The create itself also raises TypeError for missing 'role' field on the stub,
    which is still a failure caused by missing implementation.)
    """
    with pytest.raises(IntegrityError):
        User.objects.create(
            username="orphan_client",
            password="argon2$hashed",
            name="Orphan Client",
            email="orphan@test.example",
            role="client_user",
            client_org=None,
        )


@pytest.mark.django_db
def test_client_user_with_valid_org_saved_successfully() -> None:
    """AC-2 — client_user with a valid ClientOrg must be accepted (positive path).

    Fails on stub with TypeError: 'role' is not a recognized model field.
    """
    org = ClientOrg.objects.create(name="ValidCorp")
    user = User.objects.create(
        username="valid_client",
        password="argon2$hashed",
        name="Valid Client",
        email="valid@test.example",
        role="client_user",
        client_org=org,
    )
    assert user.pk is not None


@pytest.mark.django_db
def test_internal_role_with_org_raises_integrity_error() -> None:
    """AC-2 (BR B-21) — internal roles must NOT have a client_org (DB check constraint).

    Fails on stub: no constraint exists and no 'role' field -> TypeError.
    """
    org = ClientOrg.objects.create(name="CorpForInternal")
    with pytest.raises(IntegrityError):
        User.objects.create(
            username="dm_with_org",
            password="argon2$hashed",
            name="DM With Org",
            email="dm_org@test.example",
            role="delivery_manager",
            client_org=org,
        )


# ---------------------------------------------------------------------------
# REQ-020 AC-3: is_active field metadata (no DB access needed)
# ---------------------------------------------------------------------------


def test_is_active_field_is_booleanfield() -> None:
    """AC-3 — User.is_active must be a real BooleanField (not a class attribute).

    AbstractBaseUser defines is_active = True as a class attribute only.
    The full implementation must promote it to a proper BooleanField in the
    DB schema.  Fails on stub with FieldDoesNotExist.
    """
    field = User._meta.get_field("is_active")
    assert isinstance(field, BooleanField), (
        f"Expected BooleanField, got {type(field)}"
    )


def test_is_active_defaults_to_true() -> None:
    """AC-3 — is_active BooleanField must default to True per DBD-001 v0.1.

    Fails on stub with FieldDoesNotExist (no is_active field).
    """
    field = User._meta.get_field("is_active")
    assert field.default is True, (
        f"Expected default=True, got {field.default!r}"
    )


# ---------------------------------------------------------------------------
# REQ-020 AC-3: deactivation persistence (requires DB)
# ---------------------------------------------------------------------------


@pytest.mark.django_db
def test_deactivate_user_persists_through_db_round_trip() -> None:
    """AC-3 — Setting is_active=False must survive a DB save and re-fetch.

    Fails on stub for two reasons:
    1. create() raises TypeError because 'role' is not a field (missing implementation).
    2. Even if creation succeeded, is_active is only a class attribute on the stub
       model and would not be persisted to the DB on save(), so the re-fetched
       user would still show is_active=True (the class default).
    """
    user = User.objects.create(
        username="to_deactivate",
        password="argon2$hashed",
        name="Deactivate Me",
        email="deactivate@test.example",
        role="delivery_manager",
    )
    assert user.is_active is True  # default per DBD-001 v0.1
    user.is_active = False
    user.save()
    fetched = User.objects.get(pk=user.pk)
    assert fetched.is_active is False, (
        "is_active=False was not persisted: deactivated user would still appear active"
    )
