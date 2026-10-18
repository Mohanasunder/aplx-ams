"""
FEAT-006 accounts authentication backend and password validator — Mode A stubs.

SessionAuthBackend:
    Checks is_active flag, Argon2id password match, and account lockout state
    (5 failures within 30 minutes per NFR N-5, A-019).
    Mode A stub: authenticate() returns None; get_user() returns None.

UppercaseLowercaseDigitValidator:
    Enforces the APLX AMS password policy (NFR N-5, OQ-044): minimum 8 characters,
    at least 1 upper-case letter, 1 lower-case letter, and 1 digit.
    Mode A stub: validate() performs no checks and returns without raising.

Logic is added in Mode B.
"""

from __future__ import annotations

from typing import Any


class UppercaseLowercaseDigitValidator:
    """Password policy validator (NFR N-5, OQ-044).

    Policy: at least 8 characters, at least 1 uppercase letter, 1 lowercase
    letter, and 1 digit.  'Abcdefg1' meets the policy; 'abcdefg1' does not
    (missing uppercase letter).

    Mode A stub — validate() performs no checks and returns None.
    Logic is added in Mode B.
    """

    def validate(self, password: str, user: object = None) -> None:
        """Stub: performs no validation. Will raise ValidationError in Mode B."""

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

    Mode A stub — all methods return None (no logic). Logic is added in Mode B.
    """

    def authenticate(
        self,
        request: Any,
        username: str = "",
        password: str = "",
    ) -> None:
        """Stub: returns None for all inputs. Implemented in Mode B."""
        return None

    def get_user(self, user_id: int) -> None:
        """Stub: returns None. Implemented in Mode B."""
        return None
