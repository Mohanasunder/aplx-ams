"""
FEAT-005 accounts models — STUB (Mode A: tests first).

Contains only the class signature and the USERNAME_FIELD stub.  Mode B will
add all DBD-001 v0.1 columns: role (role_enum), name, email, client_org_id FK
to organizations_clientorg, is_active BooleanField, failed_attempts, locked_until,
date_joined, and last_login, together with the two check constraints:
  chk_client_user_has_org  — client_user role must have a client_org
  chk_internal_user_no_org — non-client_user roles must NOT have a client_org
"""

from __future__ import annotations

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    """Custom user model (stub).  Real fields are added in Mode B."""

    username = models.CharField(max_length=150, unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS: list[str] = []

    class Meta:
        db_table = "accounts_user"
