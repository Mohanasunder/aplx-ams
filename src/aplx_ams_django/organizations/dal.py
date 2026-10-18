"""
FEAT-002 stub: organizations data access layer.

Query functions are stubs; implementation and RLS filtering are added in
Mode B (FEAT-002).
"""

from aplx_ams_django.organizations.models import ClientOrg, SAPApplication


def get_org_by_id(org_id: int) -> ClientOrg:
    """Return the ClientOrg with the given primary key.

    Raises ClientOrg.DoesNotExist if not found.
    Implementation added in Mode B (FEAT-002).
    """
    raise NotImplementedError


def list_orgs() -> list[ClientOrg]:
    """Return all client organizations.

    RLS filtering (P4 sees only own org) added in Mode B (FEAT-002).
    """
    raise NotImplementedError


def get_sap_apps_for_org(org_id: int) -> list[SAPApplication]:
    """Return all SAP applications belonging to the given client organization.

    Implementation added in Mode B (FEAT-002).
    """
    raise NotImplementedError
