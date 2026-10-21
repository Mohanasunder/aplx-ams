"""
FEAT-005 accounts views — Mode B implementation.
FEAT-006 auth views (LoginView, LogoutView, MeView) — Mode B implementation.

UserViewSet enforces delivery_manager role on every action via
HasRolePermission (get_permissions checks before any DB access).

Permission matrix (PRM-001 v0.1 § User account management F-6):
  POST   /api/accounts/users/                  — delivery_manager (AC-4)
  GET    /api/accounts/users/                  — delivery_manager
  GET    /api/accounts/users/{id}/             — delivery_manager
  PATCH  /api/accounts/users/{id}/             — delivery_manager (AC-4)
  POST   /api/accounts/users/{id}/deactivate/ — delivery_manager (AC-4)

Permission matrix (PRM-001 v0.1 § Authentication F-5):
  POST /api/auth/login/  — public (no auth required)
  POST /api/auth/logout/ — all authenticated roles, own session only
  GET  /api/auth/me/     — all authenticated roles, own user record
"""

from __future__ import annotations

from typing import ClassVar

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

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
        serializer = UserUpdateSerializer(instance=user, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        updatable = ("name", "email", "role", "client_org_id")
        for field in updatable:
            if field in serializer.validated_data:
                setattr(user, field, serializer.validated_data[field])
        try:
            user.save()
        except IntegrityError:
            return Response(
                {"non_field_errors": ["A database conflict prevented this update."]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(UserDetailSerializer(user).data)

    def deactivate(self, request: Request, pk: int | None = None) -> Response:
        """POST /api/accounts/users/{pk}/deactivate/ — set is_active=False (AC-3)."""
        assert pk is not None
        try:
            user = services.deactivate_user(pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(UserDetailSerializer(user).data)


# ---------------------------------------------------------------------------
# FEAT-006 auth views — Mode B implementation
# ---------------------------------------------------------------------------

_INVALID_CREDENTIALS = {"detail": "Invalid credentials."}


class LoginView(APIView):
    """POST /api/auth/login/ — authenticate and start a session (AC-1, AC-2, AC-4).

    Public endpoint: no authentication required.
    Permission matrix: AllowAny (PRM-001 v0.1 § Authentication F-5).
    """

    permission_classes: ClassVar[list[type]] = [AllowAny]

    def post(self, request: Request) -> Response:
        """Authenticate with username + password; start a session on success."""
        username = request.data.get("username", "")
        password = request.data.get("password", "")

        user = authenticate(request, username=username, password=password)
        if user is None:
            return Response(_INVALID_CREDENTIALS, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        org_name = user.client_org.name if user.client_org else None
        return Response({"role": user.role, "org": org_name}, status=status.HTTP_200_OK)


class LogoutView(APIView):
    """POST /api/auth/logout/ — invalidate the current session.

    Requires an active authenticated session (own session only per PRM-001 v0.1).
    """

    permission_classes: ClassVar[list[type]] = [IsAuthenticated]

    def post(self, request: Request) -> Response:
        """Invalidate the session and return HTTP 200."""
        logout(request)
        return Response(status=status.HTTP_200_OK)


class MeView(APIView):
    """GET /api/auth/me/ — return the authenticated user's role and org (AC-1).

    Requires authentication; returns the authenticated user's own record.
    """

    permission_classes: ClassVar[list[type]] = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        """Return role and org for the authenticated user."""
        user = request.user
        org_name = user.client_org.name if user.client_org else None
        return Response({"role": user.role, "org": org_name}, status=status.HTTP_200_OK)
