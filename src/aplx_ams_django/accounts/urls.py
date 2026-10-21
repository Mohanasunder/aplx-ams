"""
FEAT-005 accounts URL configuration (Mode B).
FEAT-006 auth URL configuration (Mode A stubs).

User account endpoints (registered at api/accounts/):
  users/                         -> UserViewSet (list, create)
  users/{pk}/                    -> UserViewSet (retrieve, partial_update)
  users/{pk}/deactivate/         -> UserViewSet.deactivate (custom action)

Auth endpoints (exported as auth_urlpatterns, registered at api/ in root urls.py):
  auth/login/                    -> LoginView (POST)
  auth/logout/                   -> LogoutView (POST)
  auth/me/                       -> MeView (GET)
"""

from django.urls import path
from rest_framework.routers import DefaultRouter

from aplx_ams_django.accounts.views import LoginView, LogoutView, MeView, UserViewSet

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

# Auth URL patterns: mounted at api/ in root urls.py to resolve to /api/auth/...
auth_urlpatterns = [
    path("auth/login/", LoginView.as_view(), name="auth-login"),
    path("auth/logout/", LogoutView.as_view(), name="auth-logout"),
    path("auth/me/", MeView.as_view(), name="auth-me"),
]
