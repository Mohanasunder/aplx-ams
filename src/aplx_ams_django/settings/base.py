"""
Shared Django settings. Reads secrets from /run/secrets/ (A-038, ADR A-17).
"""

import os
from pathlib import Path


def read_secret(name: str, default: str = "") -> str:
    """Read a Docker Compose file secret from /run/secrets/<name>."""
    path = Path(f"/run/secrets/{name}")
    if path.exists():
        return path.read_text().strip()
    return os.environ.get(name.upper(), default)


BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = read_secret("django_secret_key", "insecure-dev-key-replace-in-production")

DEBUG = True

ALLOWED_HOSTS: list[str] = ["*"]

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "rest_framework",
]

MIDDLEWARE: list[str] = []

ROOT_URLCONF = "aplx_ams_django.urls"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "aplx_ams"),
        "USER": os.environ.get("POSTGRES_USER", "aplx_ams_owner"),
        "PASSWORD": read_secret("db_password", os.environ.get("POSTGRES_PASSWORD", "")),
        "HOST": os.environ.get("POSTGRES_HOST", "db"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
