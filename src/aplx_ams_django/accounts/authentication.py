"""
FEAT-006 accounts authentication backend and password validator — Mode B implementation.

SessionAuthBackend:
    Django authentication backend.  Checks is_active flag, Argon2id password
    match, and account lockout state (5 failures within 30 minutes per NFR N-5,
    A-019).

SameSiteSessionAuthentication:
    DRF authentication class used by all API views.  Reads the authenticated
    user from the session (set by AuthenticationMiddleware).  CSRF enforcement
    is skipped because SESSION_COOKIE_SAMESITE='Lax' provides equivalent
    protection in modern browsers (ADR A-17).  Returns "Session" as the
    WWW-Authenticate header so that DRF correctly sends HTTP 401 (not 403)
    when credentials are absent (API-001 v0.2 § F-5).

UppercaseLowercaseDigitValidator:
    Enforces the APLX AMS password policy (NFR N-5, OQ-044): minimum 8 characters,
    at least 1 upper-case letter, 1 lower-case letter, and 1 digit.
"""

from __future__ import annotations

from datetime import timedelta
from typing import Any

from django.core.exceptions import ValidationError
from django.utils import timezone
from rest_framework.authentication import SessionAuthentication

_LOCKOUT_THRESHOLD = 5
_LOCKOUT_MINUTES = 30


class SameSiteSessionAuthentication(SessionAuthentication):
    """DRF authentication class for session-cookie-based auth (API-001 v0.2 § F-5).

    Differences from DRF's built-in SessionAuthentication:
    - CSRF enforcement is disabled: SESSION_COOKIE_SAMESITE='Lax' provides
      equivalent CSRF protection for modern browsers (ADR A-17).
    - Returns "Session" as the WWW-Authenticate header value so that DRF
      returns HTTP 401 (not 403) for unauthenticated requests.
    """

    def enforce_csrf(self, request: Any) -> None:
        """Skip CSRF check; SameSite=Lax cookie provides equivalent protection."""

    def authenticate_header(self, request: Any) -> str:
        """Return a non-empty header value so DRF sends HTTP 401 (not 403)."""
        return "Session"


class UppercaseLowercaseDigitValidator:
    """Password policy validator (NFR N-5, OQ-044).

    Policy: at least 8 characters, at least 1 uppercase letter, 1 lowercase
    letter, and 1 digit.  'Abcdefg1' meets the policy; 'abcdefg1' does not
    (missing uppercase letter).
    """

    def validate(self, password: str, user: object = None) -> None:
        """Raise ValidationError if the password does not meet the policy."""
        errors: list[str] = []
        if len(password) < 8:
            errors.append("This password must be at least 8 characters long.")
        if not any(c.isupper() for c in password):
            errors.append("This password must contain at least one uppercase letter.")
        if not any(c.islower() for c in password):
            errors.append("This password must contain at least one lowercase letter.")
        if not any(c.isdigit() for c in password):
            errors.append("This password must contain at least one digit.")
        if errors:
            raise ValidationError(errors)

    def get_help_text(self) -> str:
        return (
            "Your password must be at least 8 characters long and contain "
            "at least one upper-case letter, one lower-case letter, and one digit."
        )


class SessionAuthBackend:
    """Django authentication backend for APLX AMS (API-001 v0.2 § F-5).

    On authenticate():
      1. Look up the user account by username.
      2. Check is_active (AC-1: deactivated accounts are refused).
      3. Check lockout state: if locked_until is in the future, refuse (AC-4).
      4. Verify Argon2id password hash.
      5. On success: reset failed_attempts and locked_until.
      6. On failure: increment failed_attempts; if count reaches 5, set
         locked_until = now + 30 minutes (AC-4).
      7. Return a generic error for all auth failures (AC-2, A-019).
    """

    def authenticate(
        self,
        request: Any,
        username: str = "",
        password: str = "",
    ) -> Any:
        """Authenticate by username and password; enforce lockout (AC-4)."""
        from aplx_ams_django.accounts.models import User

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        if not user.is_active:
            return None

        # AC-4: refuse immediately if the account is within the lockout window.
        if user.locked_until is not None and user.locked_until > timezone.now():
            return None

        # Verify password.
        if not user.check_password(password):
            user.failed_attempts += 1
            if user.failed_attempts >= _LOCKOUT_THRESHOLD:
                user.locked_until = timezone.now() + timedelta(minutes=_LOCKOUT_MINUTES)
            user.save(update_fields=["failed_attempts", "locked_until"])
            return None

        # Correct password — reset lockout state and return the user.
        user.failed_attempts = 0
        user.locked_until = None
        user.save(update_fields=["failed_attempts", "locked_until"])
        return user

    def get_user(self, user_id: int) -> Any:
        """Fetch a user by primary key; return None if not found."""
        from aplx_ams_django.accounts.models import User

        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
