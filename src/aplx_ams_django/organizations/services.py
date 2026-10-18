"""
FEAT-002: organizations service layer.
FEAT-003: contract service stubs (full implementation in Mode B).

Thin orchestration layer between views and the data access layer (DAL).
No role-enforcement logic lives here; that is handled by HasRolePermission
in views (PRM-001 v0.1).
"""

from typing import Any

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
# FEAT-003 stubs — full implementation in Mode B
# ---------------------------------------------------------------------------


def create_contract(org_id: int, data: dict[str, Any]) -> Contract:
    """FEAT-003 stub — create a contract for the given org.

    Full implementation (validation, 409 guard, DAL call) added in Mode B.
    """
    raise NotImplementedError("FEAT-003: create_contract not yet implemented")


def get_active_contract(org_id: int) -> Contract:
    """FEAT-003 stub — return the active contract for the given org.

    Full implementation (DAL delegation, hours_bank_balance computation)
    added in Mode B.
    """
    raise NotImplementedError("FEAT-003: get_active_contract not yet implemented")
