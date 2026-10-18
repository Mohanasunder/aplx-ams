"""
FEAT-005 accounts models — DBD-001 v0.1 full implementation (Mode B).

Fields: role (TextChoices), name, email, client_org FK, is_active BooleanField,
failed_attempts, locked_until, date_joined.

Constraints:
  chk_role_valid                  — role must be one of the four permitted values
  chk_client_user_has_org         — client_user role must have a client_org
  chk_internal_user_no_org        — non-client_user roles must NOT have a client_org
  chk_failed_attempts_non_negative — failed_attempts >= 0
"""

from __future__ import annotations

import django.db.models as m
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

from aplx_ams_django.organizations.models import ClientOrg


class UserRole(m.TextChoices):
    L1 = "l1_support_engineer", "L1 Support Engineer"
    L2_L3 = "l2_l3_support_engineer", "L2/L3 Support Engineer"
    DM = "delivery_manager", "Delivery Manager"
    CLIENT = "client_user", "Client User"


class UserManager(BaseUserManager):
    def create_user(
        self,
        username: str,
        password: str | None = None,
        **extra_fields: object,
    ) -> "User":
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """Custom user model implementing DBD-001 v0.1 schema for FEAT-005."""

    username = m.CharField(max_length=150, unique=True)
    name = m.CharField(max_length=150)
    email = m.EmailField(max_length=254, unique=True)
    role = m.CharField(max_length=30, choices=UserRole.choices)
    client_org = m.ForeignKey(
        ClientOrg,
        null=True,
        blank=True,
        on_delete=m.SET_NULL,
    )
    is_active = m.BooleanField(default=True)
    failed_attempts = m.SmallIntegerField(default=0)
    locked_until = m.DateTimeField(null=True, blank=True)
    date_joined = m.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS: list[str] = []

    objects = UserManager()

    class Meta:
        db_table = "accounts_user"
        constraints = [
            m.CheckConstraint(
                check=m.Q(role__in=[r.value for r in UserRole]),
                name="chk_role_valid",
            ),
            m.CheckConstraint(
                check=~m.Q(role="client_user") | m.Q(client_org__isnull=False),
                name="chk_client_user_has_org",
            ),
            m.CheckConstraint(
                check=m.Q(role="client_user") | m.Q(client_org__isnull=True),
                name="chk_internal_user_no_org",
            ),
            m.CheckConstraint(
                check=m.Q(failed_attempts__gte=0),
                name="chk_failed_attempts_non_negative",
            ),
        ]
