"""
FEAT-002: organizations views.
FEAT-003: ContractViewSet (implemented in Mode B).

OrgViewSet: CRUD for ClientOrg.
SAPApplicationViewSet: create and list SAP applications scoped to one org.
ContractViewSet: create and retrieve active contract for one org.

Permission matrix (PRM-001 v0.1):
  POST   /api/organizations/                          — P3
  GET    /api/organizations/                          — P1, P2, P3, P4
  GET    /api/organizations/{id}/                     — P1, P2, P3
  PATCH  /api/organizations/{id}/                     — P3
  POST   /api/organizations/{id}/sap-applications/   — P3
  GET    /api/organizations/{id}/sap-applications/   — P1, P2, P3, P4
  POST   /api/organizations/{id}/contracts/          — P3
  GET    /api/organizations/{id}/contracts/active/   — P3
"""

from __future__ import annotations

from typing import ClassVar

from django.core.exceptions import ValidationError
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
    """FEAT-003: ContractViewSet for contract creation and active contract retrieval.

    POST /api/organizations/{org_id}/contracts/          — P3 (Delivery Manager)
    GET  /api/organizations/{org_id}/contracts/active/   — P3 (Delivery Manager)

    Permission enforced on every action via HasRolePermission (PRM-001 v0.1).
    """

    serializer_class = ContractSerializer

    def get_permissions(self) -> list[HasRolePermission]:
        return [HasRolePermission(required_roles=_DM_ONLY)]

    def create(self, request: Request, org_id: int | None = None) -> Response:
        """POST /api/organizations/{org_id}/contracts/ — create a contract for the org.

        Returns 201 on success, 409 when an active contract already exists.
        """
        assert org_id is not None
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            contract = services.create_contract(org_id=org_id, data=serializer.validated_data)
        except ValidationError:
            return Response(
                {"detail": "An active contract already exists for this organization."},
                status=status.HTTP_409_CONFLICT,
            )
        return Response(ContractSerializer(contract).data, status=status.HTTP_201_CREATED)

    def get_active(self, request: Request, org_id: int | None = None) -> Response:
        """GET /api/organizations/{org_id}/contracts/active/ — return the active contract.

        Returns 200 with the contract body, or 404 if no active contract exists.
        """
        assert org_id is not None
        contract = services.get_active_contract(org_id=org_id)
        if contract is None:
            return Response(
                {"detail": "No active contract found for this organization."},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(ContractSerializer(contract).data, status=status.HTTP_200_OK)
