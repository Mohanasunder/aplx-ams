"""Django AppConfig for the accounts app (FEAT-005)."""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "aplx_ams_django.accounts"
    label = "accounts"
