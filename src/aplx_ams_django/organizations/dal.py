"""
FEAT-002: organizations data access layer.

All queries use the Django ORM. No raw SQL.
"""

from aplx_ams_django.organizations.models import ClientOrg, SAPApplication


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
