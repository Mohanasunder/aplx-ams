"""
FEAT-002 stub: organizations views.

OrgViewSet and SAPApplicationViewSet class signatures are in place;
queryset, serializer, and permission logic are added in Mode B (FEAT-002).
"""

from rest_framework import viewsets

from aplx_ams_django.permissions import HasRolePermission


class OrgViewSet(viewsets.GenericViewSet):
    """ViewSet for client organization CRUD — stub, no logic yet.

    POST /api/organizations/  — P3 only (DM)
    GET  /api/organizations/  — P1, P2, P3, P4 (P4 filtered to own org)
    GET  /api/organizations/{id}/  — P1, P2, P3
    PATCH /api/organizations/{id}/ — P3 only (DM)

    Full implementation in Mode B (FEAT-002).
    """

    permission_classes = [HasRolePermission]


class SAPApplicationViewSet(viewsets.GenericViewSet):
    """ViewSet for SAP application management — stub, no logic yet.

    POST /api/organizations/{id}/sap-applications/  — P3 only (DM)
    GET  /api/organizations/{id}/sap-applications/  — P1, P2, P3, P4

    Full implementation in Mode B (FEAT-002).
    """

    permission_classes = [HasRolePermission]
