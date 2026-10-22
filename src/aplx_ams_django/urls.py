from django.urls import include, path

from aplx_ams_django.accounts.urls import auth_urlpatterns
from aplx_ams_django.health import health_check

urlpatterns = [
    path("api/health/", health_check, name="health"),
    # FEAT-002: organizations and SAP application endpoints
    path("api/", include("aplx_ams_django.organizations.urls")),
    # FEAT-005: user account endpoints
    path("api/accounts/", include("aplx_ams_django.accounts.urls")),
    # FEAT-006: auth endpoints at /api/auth/login/, /api/auth/logout/, /api/auth/me/
    path("api/", include((auth_urlpatterns, "auth"))),
    # FEAT-010: company holiday list endpoints at /api/holidays/
    path("api/holidays/", include("aplx_ams_django.sla.urls")),
]
