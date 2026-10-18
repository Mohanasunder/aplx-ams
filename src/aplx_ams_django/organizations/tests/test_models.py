"""
FEAT-002 database-layer tests (Mode A — tests first).

All tests in this file MUST fail on the stubs; they assert schema fields and
DB behavior that do not yet exist.  They fail for the right reason (missing
implementation), not because of syntax, import, or test-setup errors.

Criterion → test function mapping
----------------------------------
REQ-018 AC-1 (ClientOrg/SAPApplication exist with correct fields):
    test_client_org_has_name_field
    test_client_org_has_created_at_field
    test_sap_application_has_client_org_fk
    test_sap_application_has_name_field
    test_sap_application_has_created_at_field
    test_client_org_name_unique_in_db

REQ-018 AC-2 (SAP apps are scoped to one org; same name OK in different org):
    test_sap_application_has_unique_name_per_org_constraint
    test_sap_app_unique_per_org
    test_same_sap_app_name_different_org_allowed
"""

import pytest
from django.db import IntegrityError
from django.db.models import DateTimeField, ForeignKey

from aplx_ams_django.organizations.models import ClientOrg, SAPApplication

# ---------------------------------------------------------------------------
# REQ-018 AC-1: ClientOrg field structure (no DB access needed)
# ---------------------------------------------------------------------------


def test_client_org_has_name_field() -> None:
    """REQ-018 AC-1 — ClientOrg.name must be a CharField(max_length=255, unique=True)."""
    field = ClientOrg._meta.get_field("name")
    assert field.max_length == 255
    assert field.unique is True


def test_client_org_has_created_at_field() -> None:
    """REQ-018 AC-1 — ClientOrg.created_at must be a DateTimeField(auto_now_add=True)."""
    field = ClientOrg._meta.get_field("created_at")
    assert isinstance(field, DateTimeField)
    assert field.auto_now_add is True


# ---------------------------------------------------------------------------
# REQ-018 AC-1 / AC-2: SAPApplication field structure (no DB access needed)
# ---------------------------------------------------------------------------


def test_sap_application_has_client_org_fk() -> None:
    """REQ-018 AC-1 AC-2 — SAPApplication.client_org must be a FK to ClientOrg."""
    field = SAPApplication._meta.get_field("client_org")
    assert isinstance(field, ForeignKey)
    assert field.related_model is ClientOrg


def test_sap_application_has_name_field() -> None:
    """REQ-018 AC-1 — SAPApplication.name must be a CharField(max_length=255)."""
    field = SAPApplication._meta.get_field("name")
    assert field.max_length == 255


def test_sap_application_has_created_at_field() -> None:
    """REQ-018 AC-1 — SAPApplication.created_at must be a DateTimeField(auto_now_add=True)."""
    field = SAPApplication._meta.get_field("created_at")
    assert isinstance(field, DateTimeField)
    assert field.auto_now_add is True


def test_sap_application_has_unique_name_per_org_constraint() -> None:
    """REQ-018 AC-2 — SAPApplication must enforce uniqueness on (client_org, name).

    Accepted implementations: unique_together OR a named UniqueConstraint.
    """
    meta = SAPApplication._meta
    has_unique_together = ("client_org", "name") in (meta.unique_together or ())
    has_unique_constraint = any(
        hasattr(c, "fields") and set(c.fields) == {"client_org", "name"}
        for c in (meta.constraints or ())
    )
    assert has_unique_together or has_unique_constraint, (
        "SAPApplication must define a unique constraint on (client_org, name)"
    )


# ---------------------------------------------------------------------------
# REQ-018 AC-1: ClientOrg DB uniqueness (requires DB)
# ---------------------------------------------------------------------------


@pytest.mark.django_db
def test_client_org_name_unique_in_db() -> None:
    """REQ-018 AC-1 — Duplicate ClientOrg.name must raise IntegrityError at the DB level."""
    ClientOrg.objects.create(name="Applexus")
    with pytest.raises(IntegrityError):
        ClientOrg.objects.create(name="Applexus")


# ---------------------------------------------------------------------------
# REQ-018 AC-2: SAPApplication uniqueness per org (requires DB)
# ---------------------------------------------------------------------------


@pytest.mark.django_db
def test_sap_app_unique_per_org() -> None:
    """REQ-018 AC-2 — Same SAP app name within the same org must raise IntegrityError."""
    org = ClientOrg.objects.create(name="Applexus")
    SAPApplication.objects.create(client_org=org, name="S4HANA")
    with pytest.raises(IntegrityError):
        SAPApplication.objects.create(client_org=org, name="S4HANA")


@pytest.mark.django_db
def test_same_sap_app_name_different_org_allowed() -> None:
    """REQ-018 AC-2 — Same SAP app name on a different org must NOT raise IntegrityError."""
    org_a = ClientOrg.objects.create(name="OrgA")
    org_b = ClientOrg.objects.create(name="OrgB")
    SAPApplication.objects.create(client_org=org_a, name="S4HANA")
    app_b = SAPApplication.objects.create(client_org=org_b, name="S4HANA")
    assert app_b.pk is not None
