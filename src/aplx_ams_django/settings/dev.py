"""Dev-only settings: SQLite database so the app runs without Docker."""
from aplx_ams_django.settings.base import *  # noqa: F401, F403

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "dev.sqlite3",  # noqa: F405
    }
}
