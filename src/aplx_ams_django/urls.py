from django.urls import path

from aplx_ams_django.health import health_check

urlpatterns = [
    path("api/health/", health_check, name="health"),
]
