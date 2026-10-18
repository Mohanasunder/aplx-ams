"""Django AppConfig for the organizations app (FEAT-002)."""

from django.apps import AppConfig


class OrganizationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "aplx_ams_django.organizations"
    label = "organizations"
