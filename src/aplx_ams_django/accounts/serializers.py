"""
FEAT-005 accounts serializers — STUB (Mode A: tests first).

UserCreateSerializer, UserUpdateSerializer, UserDetailSerializer are empty
stubs. Fields and validation logic are added in Mode B.

Named per STD-001 v0.1 § Naming And Structure.
"""

from __future__ import annotations

from rest_framework import serializers


class UserCreateSerializer(serializers.Serializer):
    """Stub: fields and create validation added in Mode B.

    Mode B will add: username, name, email, role, client_org_id (required for
    client_user role per DBD-001 v0.1 constraint chk_client_user_has_org).
    """


class UserUpdateSerializer(serializers.Serializer):
    """Stub: fields and update validation added in Mode B.

    Mode B will add: name, email, role, client_org_id (updatable fields per
    API-001 v0.2 § F-6 endpoint #7).
    """


class UserDetailSerializer(serializers.Serializer):
    """Stub: read fields added in Mode B.

    Mode B will add: id, username, name, email, role, client_org_id,
    is_active, date_joined.
    """
