"""
FEAT-005 accounts views — Mode B implementation.

UserViewSet enforces delivery_manager role on every action via
HasRolePermission (get_permissions checks before any DB access).

Permission matrix (PRM-001 v0.1 § User account management F-6):
  POST   /api/accounts/users/                  — delivery_manager (AC-4)
  GET    /api/accounts/users/                  — delivery_manager
  GET    /api/accounts/users/{id}/             — delivery_manager
  PATCH  /api/accounts/users/{id}/             — delivery_manager (AC-4)
  POST   /api/accounts/users/{id}/deactivate/ — delivery_manager (AC-4)
"""

from __future__ import annotations

from django.db import IntegrityError
from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from aplx_ams_django.accounts import dal, services
from aplx_ams_django.accounts.models import User
from aplx_ams_django.accounts.serializers import (
    UserCreateSerializer,
    UserDetailSerializer,
    UserUpdateSerializer,
)
from aplx_ams_django.permissions import HasRolePermission

_DM_ONLY = ["delivery_manager"]


class UserViewSet(viewsets.GenericViewSet):
    """ViewSet for user account management — delivery_manager role required.

    get_permissions() is called by DRF before dispatching to any action,
    so authorization is checked before any database lookup (AC-4).
    """

    def get_permissions(self) -> list[HasRolePermission]:
        """Return HasRolePermission restricted to delivery_manager for all actions."""
        return [HasRolePermission(required_roles=_DM_ONLY)]

    def list(self, request: Request) -> Response:
        """GET /api/accounts/users/ — list all users ordered by username."""
        users = dal.list_users()
        return Response(UserDetailSerializer(users, many=True).data)

    def create(self, request: Request) -> Response:
        """POST /api/accounts/users/ — create a new user account (AC-1, AC-2)."""
        serializer = UserCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = services.create_user(serializer.validated_data)
        return Response(UserDetailSerializer(user).data, status=status.HTTP_201_CREATED)

    def retrieve(self, request: Request, pk: int | None = None) -> Response:
        """GET /api/accounts/users/{pk}/ — return a single user detail."""
        assert pk is not None
        try:
            user = dal.get_user_by_id(pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(UserDetailSerializer(user).data)

    def partial_update(self, request: Request, pk: int | None = None) -> Response:
        """PATCH /api/accounts/users/{pk}/ — partial update of updatable fields."""
        assert pk is not None
        try:
            user = dal.get_user_by_id(pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        updatable = ("name", "email", "role", "client_org_id")
        for field in updatable:
            if field in serializer.validated_data:
                setattr(user, field, serializer.validated_data[field])
        try:
            user.save()
        except IntegrityError as exc:
            return Response({"detail": str(exc)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(UserDetailSerializer(user).data)

    def deactivate(self, request: Request, pk: int | None = None) -> Response:
        """POST /api/accounts/users/{pk}/deactivate/ — set is_active=False (AC-3)."""
        assert pk is not None
        try:
            user = services.deactivate_user(pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(UserDetailSerializer(user).data)
