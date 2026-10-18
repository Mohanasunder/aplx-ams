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
    "django.contrib.sessions",  # FEAT-006: session framework required for login/logout
    "rest_framework",
    "aplx_ams_django.organizations",
    "aplx_ams_django.accounts",
]

AUTH_USER_MODEL = "accounts.User"

MIDDLEWARE: list[str] = [
    "django.contrib.sessions.middleware.SessionMiddleware",  # FEAT-006: session management
    # FEAT-006: AuthenticationMiddleware reads the session and sets request.user
    # for every request; required for session-based login/logout to work.
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]

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

# FEAT-006: password policy (NFR N-5, OQ-044): >= 8 chars, uppercase, lowercase, digit.
# UppercaseLowercaseDigitValidator enforces the full policy; MinimumLengthValidator
# is kept as a defence-in-depth fallback.
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 8},
    },
    {
        "NAME": (
            "aplx_ams_django.accounts.authentication.UppercaseLowercaseDigitValidator"
        ),
    },
]

# FEAT-006: session cookie security settings (AC-1, NFR N-5).
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_AGE = 28800  # 8 hours in seconds (absolute cap enforced by middleware)

# FEAT-006: use SessionAuthBackend for all authentication (API-001 v0.2 § F-5).
AUTHENTICATION_BACKENDS = [
    "aplx_ams_django.accounts.authentication.SessionAuthBackend",
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
]

# FEAT-006: DRF uses SameSiteSessionAuthentication (no CSRF token required;
# SameSite=Lax cookie provides protection).  The class returns a non-empty
# authenticate_header so DRF sends HTTP 401 (not 403) for unauthenticated requests.
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "aplx_ams_django.accounts.authentication.SameSiteSessionAuthentication",
    ],
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
