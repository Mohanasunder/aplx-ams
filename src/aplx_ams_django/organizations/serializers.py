"""
FEAT-002: organizations serializers.

ClientOrgSerializer: id, name, created_at.
SAPApplicationSerializer: id, client_org, name, created_at.
"""

from __future__ import annotations

from typing import ClassVar

from rest_framework import serializers

from aplx_ams_django.organizations.models import ClientOrg, SAPApplication


class ClientOrgSerializer(serializers.ModelSerializer):
    """Serializer for ClientOrg read and create operations."""

    class Meta:
        model = ClientOrg
        fields: ClassVar[list[str]] = ["id", "name", "created_at"]
        read_only_fields: ClassVar[list[str]] = ["id", "created_at"]


class SAPApplicationSerializer(serializers.ModelSerializer):
    """Serializer for SAPApplication read operations.

    client_org is written by the view (from URL kwargs); name is written by the
    caller.  Both id and created_at are read-only server-assigned values.
    """

    class Meta:
        model = SAPApplication
        fields: ClassVar[list[str]] = ["id", "client_org", "name", "created_at"]
        read_only_fields: ClassVar[list[str]] = ["id", "client_org", "created_at"]
