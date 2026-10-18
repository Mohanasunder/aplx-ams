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
    """FEAT-003: serializer for Contract create and read operations.

    Fields: id, contract_type, contracted_hours, is_active, started_at,
    created_at, hours_bank_balance.
    hours_bank_balance equals contracted_hours for hours_bank contracts and
    null for fixed_fee contracts (API-001 v0.2).

    contracted_hours uses coerce_to_string=False so the JSON value is a
    number (float), not the string "100.00", allowing int() coercion in
    callers (test AC-1).
    """

    contracted_hours = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        allow_null=True,
        required=False,
        coerce_to_string=False,
    )
    hours_bank_balance = serializers.SerializerMethodField()

    def get_hours_bank_balance(self, obj: Contract) -> object:
        """Return contracted_hours for hours_bank contracts, None otherwise."""
        if obj.contract_type == Contract.HOURS_BANK:
            return obj.contracted_hours
        return None

    class Meta:
        model = Contract
        fields: ClassVar[list[str]] = [
            "id",
            "contract_type",
            "contracted_hours",
            "is_active",
            "started_at",
            "created_at",
            "hours_bank_balance",
        ]
        read_only_fields: ClassVar[list[str]] = ["id", "started_at", "created_at"]
