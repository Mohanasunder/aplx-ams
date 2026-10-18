"""
FEAT-002 stub: organizations service layer.

create_org() and add_sap_application() are stubs; DM role enforcement
and all business logic are added in Mode B (FEAT-002).
"""

from typing import Any

from aplx_ams_django.organizations.models import ClientOrg, SAPApplication


def create_org(name: str) -> ClientOrg:
    """Create and return a new client organization.

    DM role check and full implementation added in Mode B (FEAT-002).
    """
    raise NotImplementedError


def add_sap_application(org_id: int, data: dict[str, Any]) -> SAPApplication:
    """Add a SAP application to a client organization and return it.

    DM role check and full implementation added in Mode B (FEAT-002).
    """
    raise NotImplementedError
