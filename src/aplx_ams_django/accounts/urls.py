"""
FEAT-005 accounts URL configuration — STUB (Mode A: tests first).

Registers user account endpoints at:
  users/                         -> UserViewSet (list, create)
  users/{pk}/                    -> UserViewSet (retrieve, partial_update)
  users/{pk}/deactivate/         -> UserViewSet.deactivate (custom action)

All views return 501 in Mode A; logic added in Mode B.
"""

from django.urls import path
from rest_framework.routers import DefaultRouter

from aplx_ams_django.accounts.views import UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet, basename="user")

urlpatterns = [
    *router.urls,
    path(
        "users/<int:pk>/deactivate/",
        UserViewSet.as_view({"post": "deactivate"}),
        name="user-deactivate",
    ),
]
