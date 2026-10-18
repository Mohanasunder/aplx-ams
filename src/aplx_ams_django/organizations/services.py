"""
FEAT-002: organizations service layer.
FEAT-003: contract service (implemented in Mode B).

Thin orchestration layer between views and the data access layer (DAL).
No role-enforcement logic lives here; that is handled by HasRolePermission
in views (PRM-001 v0.1).
"""

from __future__ import annotations

from typing import Any

from django.core.exceptions import ValidationError
from django.db import IntegrityError

from aplx_ams_django.organizations import dal
from aplx_ams_django.organizations.models import ClientOrg, Contract, SAPApplication


def create_org(name: str) -> ClientOrg:
    """Create and return a new client organization.

    Raises django.db.IntegrityError if an org with the same name already exists.
    """
    return ClientOrg.objects.create(name=name)


def add_sap_application(org_id: int, data: dict[str, Any]) -> SAPApplication:
    """Add a SAP application to a client organization and return it.

    Only 'name' is consumed from data; extra keys (e.g. 'sid') are ignored.
    Raises ClientOrg.DoesNotExist if the org is not found.
    Raises django.db.IntegrityError if the same name already exists for that org.
    """
    org = dal.get_org_by_id(org_id)
    name: str = data["name"]
    return SAPApplication.objects.create(client_org=org, name=name)


# ---------------------------------------------------------------------------
# FEAT-003 — contract service
# ---------------------------------------------------------------------------


def create_contract(org_id: int, data: dict[str, Any]) -> Contract:
    """Create a contract for the given org and return it.

    Raises django.core.exceptions.ValidationError when the partial unique
    index rejects a second active contract for the same org (HTTP 409).
    """
    try:
        return dal.create_contract_for_org(org_id=org_id, data=data)
    except IntegrityError as exc:
        raise ValidationError("An active contract already exists for this organization.") from exc


def get_active_contract(org_id: int) -> Contract | None:
    """Return the active contract for the given org, or None if none exists."""
    return dal.get_active_contract_for_org(org_id=org_id)
