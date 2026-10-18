"""
FEAT-002: organizations data access layer.
FEAT-003: contract DAL (implemented in Mode B).

All queries use the Django ORM. No raw SQL.
"""

from __future__ import annotations

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
# FEAT-003 — contract DAL
# ---------------------------------------------------------------------------


def create_contract_for_org(org_id: int, data: dict[str, Any]) -> Contract:
    """Persist a new Contract for the given org and return it.

    Raises django.db.IntegrityError when the partial unique index
    (one active contract per org) would be violated.
    """
    return Contract.objects.create(client_org_id=org_id, **data)


def get_active_contract_for_org(org_id: int) -> Contract | None:
    """Return the single active Contract for the given org, or None."""
    return Contract.objects.filter(client_org_id=org_id, is_active=True).first()
