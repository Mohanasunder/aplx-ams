"""Django AppConfig for the sla app (FEAT-010)."""

from django.apps import AppConfig


class SlaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "aplx_ams_django.sla"
    label = "sla"
