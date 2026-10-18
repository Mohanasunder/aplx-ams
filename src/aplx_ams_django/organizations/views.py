"""
FEAT-002: organizations views.
FEAT-003: ContractViewSet stub (full implementation in Mode B).

OrgViewSet: CRUD for ClientOrg.
SAPApplicationViewSet: create and list SAP applications scoped to one org.
ContractViewSet: create and retrieve active contract for one org (stub only).

Permission matrix (PRM-001 v0.1):
  POST   /api/organizations/                          — P3
  GET    /api/organizations/                          — P1, P2, P3, P4
  GET    /api/organizations/{id}/                     — P1, P2, P3
  PATCH  /api/organizations/{id}/                     — P3
  POST   /api/organizations/{id}/sap-applications/   — P3
  GET    /api/organizations/{id}/sap-applications/   — P1, P2, P3, P4
  POST   /api/organizations/{id}/contracts/          — P3 (FEAT-003 stub)
  GET    /api/organizations/{id}/contracts/active/   — P3 (FEAT-003 stub)
"""

from typing import ClassVar

from django.db.models import QuerySet
from rest_framework import mixins, status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from aplx_ams_django.organizations import services
from aplx_ams_django.organizations.models import ClientOrg, SAPApplication
from aplx_ams_django.organizations.serializers import (
    ClientOrgSerializer,
    ContractSerializer,
    SAPApplicationSerializer,
)
from aplx_ams_django.permissions import HasRolePermission

_ALL_ROLES = ["P1", "P2", "P3", "P4"]
_STAFF_ROLES = ["P1", "P2", "P3"]
_DM_ONLY = ["P3"]


class OrgViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """ViewSet for client organization CRUD.

    POST /api/organizations/        — P3 only (Delivery Manager)
    GET  /api/organizations/        — P1, P2, P3, P4
    GET  /api/organizations/{id}/   — P1, P2, P3
    PATCH /api/organizations/{id}/  — P3 only
    """

    queryset = ClientOrg.objects.all().order_by("name")
    serializer_class = ClientOrgSerializer
    http_method_names: ClassVar[list[str]] = ["get", "post", "patch", "head", "options"]

    def get_permissions(self) -> list[HasRolePermission]:
        if self.action in ("create", "update", "partial_update"):
            return [HasRolePermission(required_roles=_DM_ONLY)]
        if self.action == "retrieve":
            return [HasRolePermission(required_roles=_STAFF_ROLES)]
        # list and any other read actions
        return [HasRolePermission(required_roles=_ALL_ROLES)]

    def create(self, request: Request, *args: object, **kwargs: object) -> Response:
        """POST /api/organizations/ — create a client org and return 201."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        org = services.create_org(name=serializer.validated_data["name"])
        out = ClientOrgSerializer(org)
        return Response(out.data, status=status.HTTP_201_CREATED)


class SAPApplicationViewSet(viewsets.GenericViewSet):
    """ViewSet for SAP application management, scoped to one client org.

    POST /api/organizations/{org_id}/sap-applications/ — P3
    GET  /api/organizations/{org_id}/sap-applications/ — P1, P2, P3, P4
    """

    serializer_class = SAPApplicationSerializer

    def get_permissions(self) -> list[HasRolePermission]:
        if self.action == "create":
            return [HasRolePermission(required_roles=_DM_ONLY)]
        # list
        return [HasRolePermission(required_roles=_ALL_ROLES)]

    def get_queryset(self) -> QuerySet[SAPApplication]:
        org_id: int = self.kwargs["org_id"]
        return SAPApplication.objects.filter(client_org_id=org_id).order_by("name")

    def list(self, request: Request, org_id: int | None = None) -> Response:
        """GET /api/organizations/{org_id}/sap-applications/ — list SAP apps for org."""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request: Request, org_id: int | None = None) -> Response:
        """POST /api/organizations/{org_id}/sap-applications/ — add SAP app to org."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        org_id = self.kwargs.get("org_id")
        sap_app = services.add_sap_application(org_id=org_id, data=serializer.validated_data)
        return Response(SAPApplicationSerializer(sap_app).data, status=status.HTTP_201_CREATED)


class ContractViewSet(viewsets.GenericViewSet):
    """FEAT-003 stub — ContractViewSet; full implementation added in Mode B.

    POST /api/organizations/{org_id}/contracts/          — P3 (stub)
    GET  /api/organizations/{org_id}/contracts/active/   — P3 (stub)

    Both actions return 501 in Mode A; permission enforcement and business
    logic are wired in Mode B.
    """

    serializer_class = ContractSerializer

    def create(self, request: Request, org_id: int | None = None) -> Response:
        """POST /api/organizations/{org_id}/contracts/ — FEAT-003 stub."""
        return Response({"detail": "not implemented"}, status=status.HTTP_501_NOT_IMPLEMENTED)

    def get_active(self, request: Request, org_id: int | None = None) -> Response:
        """GET /api/organizations/{org_id}/contracts/active/ — FEAT-003 stub."""
        return Response({"detail": "not implemented"}, status=status.HTTP_501_NOT_IMPLEMENTED)
