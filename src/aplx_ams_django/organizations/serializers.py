"""
FEAT-002: organizations serializers.
FEAT-003: ContractSerializer stub (full implementation in Mode B).

ClientOrgSerializer: id, name, created_at.
SAPApplicationSerializer: id, client_org, name, created_at.
ContractSerializer: stub only — fields added in Mode B.
"""

from __future__ import annotations

from typing import ClassVar

from rest_framework import serializers

from aplx_ams_django.organizations.models import ClientOrg, Contract, SAPApplication


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


class ContractSerializer(serializers.ModelSerializer):
    """FEAT-003 stub — full implementation added in Mode B.

    Fields (contract_type, contracted_hours, is_active, hours_bank_balance,
    started_at, created_at) are wired in Mode B once the Contract model has
    all its columns.
    """

    class Meta:
        model = Contract
        fields: ClassVar[list[str]] = ["id"]
