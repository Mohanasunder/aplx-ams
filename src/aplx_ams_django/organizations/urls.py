"""
FEAT-002: organizations URL configuration.

Registers:
  organizations/                             -> OrgViewSet (list, create)
  organizations/{pk}/                        -> OrgViewSet (retrieve, partial_update)
  organizations/{org_id}/sap-applications/  -> SAPApplicationViewSet (list, create)
"""

from django.urls import path
from rest_framework.routers import DefaultRouter

from aplx_ams_django.organizations.views import OrgViewSet, SAPApplicationViewSet

router = DefaultRouter()
router.register("organizations", OrgViewSet, basename="clientorg")

urlpatterns = [
    *router.urls,
    path(
        "organizations/<int:org_id>/sap-applications/",
        SAPApplicationViewSet.as_view({"get": "list", "post": "create"}),
        name="org-sap-applications",
    ),
]
