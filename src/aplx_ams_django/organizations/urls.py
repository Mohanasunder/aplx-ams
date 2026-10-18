"""
FEAT-002: organizations URL configuration.
FEAT-003: contract endpoint stubs registered (full implementation in Mode B).

Registers:
  organizations/                              -> OrgViewSet (list, create)
  organizations/{pk}/                         -> OrgViewSet (retrieve, partial_update)
  organizations/{org_id}/sap-applications/   -> SAPApplicationViewSet (list, create)
  organizations/{org_id}/contracts/          -> ContractViewSet.create   (FEAT-003 stub)
  organizations/{org_id}/contracts/active/   -> ContractViewSet.get_active (FEAT-003 stub)
"""

from django.urls import path
from rest_framework.routers import DefaultRouter

from aplx_ams_django.organizations.views import ContractViewSet, OrgViewSet, SAPApplicationViewSet

router = DefaultRouter()
router.register("organizations", OrgViewSet, basename="clientorg")

urlpatterns = [
    *router.urls,
    path(
        "organizations/<int:org_id>/sap-applications/",
        SAPApplicationViewSet.as_view({"get": "list", "post": "create"}),
        name="org-sap-applications",
    ),
    # FEAT-003 stubs — permission enforcement and logic added in Mode B
    path(
        "organizations/<int:org_id>/contracts/",
        ContractViewSet.as_view({"post": "create"}),
        name="org-contracts",
    ),
    path(
        "organizations/<int:org_id>/contracts/active/",
        ContractViewSet.as_view({"get": "get_active"}),
        name="org-contracts-active",
    ),
]
