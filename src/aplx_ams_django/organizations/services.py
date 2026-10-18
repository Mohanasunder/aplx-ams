"""
FEAT-002: organizations service layer.

Thin orchestration layer between views and the data access layer (DAL).
No role-enforcement logic lives here; that is handled by HasRolePermission
in views (PRM-001 v0.1).
"""

from typing import Any

from aplx_ams_django.organizations import dal
from aplx_ams_django.organizations.models import ClientOrg, SAPApplication


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
