"""
FEAT-002: organizations data access layer.
FEAT-003: contract DAL stubs (full implementation in Mode B).

All queries use the Django ORM. No raw SQL.
"""

from typing import Any

from aplx_ams_django.organizations.models import ClientOrg, Contract, SAPApplication


def get_org_by_id(org_id: int) -> ClientOrg:
    """Return the ClientOrg with the given primary key.

    Raises ClientOrg.DoesNotExist if not found.
    """
    return ClientOrg.objects.get(pk=org_id)


def list_orgs() -> list[ClientOrg]:
    """Return all client organizations ordered by name."""
    return list(ClientOrg.objects.order_by("name"))


def get_sap_apps_for_org(org_id: int) -> list[SAPApplication]:
    """Return all SAP applications belonging to the given client organization."""
    return list(SAPApplication.objects.filter(client_org_id=org_id).order_by("name"))


# ---------------------------------------------------------------------------
# FEAT-003 stubs — full implementation in Mode B
# ---------------------------------------------------------------------------


def create_contract_for_org(org_id: int, data: dict[str, Any]) -> Contract:
    """FEAT-003 stub — persist a new Contract for the given org.

    Full implementation (field mapping, uniqueness guard, DB write) is added
    in Mode B after the Contract model columns exist.
    """
    raise NotImplementedError("FEAT-003: create_contract_for_org not yet implemented")


def get_active_contract_for_org(org_id: int) -> Contract:
    """FEAT-003 stub — return the single active Contract for the given org.

    Full implementation (query, DoesNotExist handling) added in Mode B.
    """
    raise NotImplementedError("FEAT-003: get_active_contract_for_org not yet implemented")
