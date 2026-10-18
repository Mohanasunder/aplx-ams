"""
FEAT-005 accounts serializers — Mode B implementation.

UserCreateSerializer: validates role choices and enforces client_org_id
requirement for client_user role (AC-2, DBD-001 v0.1 chk_client_user_has_org).

UserDetailSerializer: exposes id, role, client_org_id, is_active, and
remaining read-only fields (AC-1, AC-3).

Named per STD-001 v0.1 § Naming And Structure.
"""

from __future__ import annotations

from typing import ClassVar

from rest_framework import serializers

from aplx_ams_django.accounts.models import User, UserRole

_VALID_ROLES = [r.value for r in UserRole]  # type: ignore[attr-defined]


class UserCreateSerializer(serializers.Serializer):
    """Deserializes and validates POST /api/accounts/users/ payloads.

    Enforces:
    - role must be one of the four valid values (AC-1).
    - client_org_id is required when role is client_user (AC-2).
    """

    username = serializers.CharField(max_length=150)
    name = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=254)
    role = serializers.ChoiceField(choices=_VALID_ROLES)
    client_org_id = serializers.IntegerField(required=False, allow_null=True)

    def validate(self, attrs: dict[str, object]) -> dict[str, object]:
        if attrs.get("role") == "client_user" and not attrs.get("client_org_id"):
            raise serializers.ValidationError(
                {"client_org_id": ("Client organization is required for client user accounts.")}
            )
        return attrs


class UserUpdateSerializer(serializers.Serializer):
    """Deserializes and validates PATCH /api/accounts/users/{id}/ payloads.

    All fields are optional (partial update); role and client_org_id may be
    updated when the same cross-field rules apply.
    """

    name = serializers.CharField(max_length=150, required=False)
    email = serializers.EmailField(max_length=254, required=False)
    role = serializers.ChoiceField(choices=_VALID_ROLES, required=False)
    client_org_id = serializers.IntegerField(required=False, allow_null=True)


class UserDetailSerializer(serializers.ModelSerializer):
    """Read-only serializer for User instances returned by the API.

    Exposes id, username, name, email, role, client_org_id (raw FK int or
    null), is_active, and date_joined.
    """

    client_org_id = serializers.IntegerField(read_only=True, allow_null=True)

    class Meta:
        model = User
        fields: ClassVar[list[str]] = [
            "id",
            "username",
            "name",
            "email",
            "role",
            "client_org_id",
            "is_active",
            "date_joined",
        ]
