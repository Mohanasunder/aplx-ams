"""
FEAT-003 database-layer tests (Mode A — tests first).

Tests assert the schema design for the Contract model as defined in DBD-001 v0.1.
All tests must fail on the stub because implementation is missing.

Criterion -> test function mapping
----------------------------------
AC-1 (hours_bank contract of 100 h sets contracted_hours to 100):
    test_create_hours_bank_contract_sets_contracted_hours

AC-2 (second active contract for same org is refused — BR B-15):
    test_second_active_contract_same_org_raises_integrity_error
    test_second_inactive_contract_same_org_succeeds

AC-3 (fixed_fee contract holds no contracted hours):
    test_create_fixed_fee_contract_without_contracted_hours_succeeds

AC-4 DB layer (model field constraints):
    test_contract_has_client_org_fk
    test_contract_has_contract_type_field
    test_contract_has_contracted_hours_field_nullable
    test_contract_has_is_active_field_with_default_true
    test_contract_has_started_at_field
    test_contract_has_created_at_field
    test_hours_bank_without_contracted_hours_raises_integrity_error
"""

from __future__ import annotations

import pytest
from django.db import IntegrityError
from django.db.models import BooleanField, CharField, DateTimeField, DecimalField, ForeignKey

from aplx_ams_django.organizations.models import ClientOrg, Contract

# ---------------------------------------------------------------------------
# AC-4 DB layer: Contract field structure (no DB access needed)
# ---------------------------------------------------------------------------


def test_contract_has_client_org_fk() -> None:
    """AC-4 — Contract.client_org must be a ForeignKey to ClientOrg."""
    field = Contract._meta.get_field("client_org")
    assert isinstance(field, ForeignKey)
    assert field.related_model is ClientOrg


def test_contract_has_contract_type_field() -> None:
    """AC-4 — Contract.contract_type must be a CharField with choices hours_bank and fixed_fee."""
    field = Contract._meta.get_field("contract_type")
    assert isinstance(field, CharField)
    choice_values = {v for v, _ in (field.choices or [])}
    assert "hours_bank" in choice_values
    assert "fixed_fee" in choice_values


def test_contract_has_contracted_hours_field_nullable() -> None:
    """AC-3 / AC-4 — Contract.contracted_hours must be a nullable DecimalField."""
    field = Contract._meta.get_field("contracted_hours")
    assert isinstance(field, DecimalField)
    assert field.null is True


def test_contract_has_is_active_field_with_default_true() -> None:
    """AC-4 — Contract.is_active must be a BooleanField defaulting to True."""
    field = Contract._meta.get_field("is_active")
    assert isinstance(field, BooleanField)
    assert field.default is True


def test_contract_has_started_at_field() -> None:
    """AC-4 — Contract.started_at must be a DateTimeField."""
    field = Contract._meta.get_field("started_at")
    assert isinstance(field, DateTimeField)


def test_contract_has_created_at_field() -> None:
    """AC-4 — Contract.created_at must be a DateTimeField(auto_now_add=True)."""
    field = Contract._meta.get_field("created_at")
    assert isinstance(field, DateTimeField)
    assert field.auto_now_add is True


# ---------------------------------------------------------------------------
# AC-1: hours_bank contract sets contracted_hours (requires DB)
# ---------------------------------------------------------------------------


@pytest.mark.django_db
def test_create_hours_bank_contract_sets_contracted_hours() -> None:
    """AC-1 — Creating an hours_bank contract with 100 contracted hours persists 100."""
    org = ClientOrg.objects.create(name="OrgA")
    contract = Contract.objects.create(
        client_org=org,
        contract_type="hours_bank",
        contracted_hours=100,
        is_active=True,
    )
    contract.refresh_from_db()
    assert contract.contracted_hours == 100


# ---------------------------------------------------------------------------
# AC-2: at most one active contract per org — BR B-15 (requires DB)
# ---------------------------------------------------------------------------


@pytest.mark.django_db
def test_second_active_contract_same_org_raises_integrity_error() -> None:
    """AC-2 — A second active contract for the same org must raise IntegrityError (BR B-15)."""
    org = ClientOrg.objects.create(name="OrgB")
    Contract.objects.create(
        client_org=org,
        contract_type="hours_bank",
        contracted_hours=100,
        is_active=True,
    )
    with pytest.raises(IntegrityError):
        Contract.objects.create(
            client_org=org,
            contract_type="fixed_fee",
            contracted_hours=None,
            is_active=True,
        )


@pytest.mark.django_db
def test_second_inactive_contract_same_org_succeeds() -> None:
    """AC-2 — A second contract with is_active=False for the same org must NOT raise."""
    org = ClientOrg.objects.create(name="OrgC")
    Contract.objects.create(
        client_org=org,
        contract_type="hours_bank",
        contracted_hours=100,
        is_active=True,
    )
    second = Contract.objects.create(
        client_org=org,
        contract_type="fixed_fee",
        contracted_hours=None,
        is_active=False,
    )
    assert second.pk is not None


# ---------------------------------------------------------------------------
# AC-3: fixed_fee contract holds no contracted hours (requires DB)
# ---------------------------------------------------------------------------


@pytest.mark.django_db
def test_create_fixed_fee_contract_without_contracted_hours_succeeds() -> None:
    """AC-3 — A fixed_fee contract with contracted_hours=None must save without error."""
    org = ClientOrg.objects.create(name="OrgD")
    contract = Contract.objects.create(
        client_org=org,
        contract_type="fixed_fee",
        contracted_hours=None,
        is_active=True,
    )
    contract.refresh_from_db()
    assert contract.contracted_hours is None


# ---------------------------------------------------------------------------
# AC-4 DB layer: check constraint — hours_bank requires contracted_hours (requires DB)
# ---------------------------------------------------------------------------


@pytest.mark.django_db
def test_hours_bank_without_contracted_hours_raises_integrity_error() -> None:
    """AC-4 — An hours_bank contract without contracted_hours must raise IntegrityError.

    Asserts the DB-level check constraint chk_hours_bank_requires_contracted_hours.
    """
    org = ClientOrg.objects.create(name="OrgE")
    with pytest.raises(IntegrityError):
        Contract.objects.create(
            client_org=org,
            contract_type="hours_bank",
            contracted_hours=None,
            is_active=True,
        )
