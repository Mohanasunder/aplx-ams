"""
FEAT-002 stub: organizations serializers.

ClientOrgSerializer and SAPApplicationSerializer signatures are in place;
all logic is added in Mode B (FEAT-002).
"""

from rest_framework import serializers

from aplx_ams_django.organizations.models import ClientOrg, SAPApplication


class ClientOrgSerializer(serializers.ModelSerializer):
    """Serializer for ClientOrg — stub, no field definitions yet."""

    class Meta:
        model = ClientOrg
        fields: list[str] = []


class SAPApplicationSerializer(serializers.ModelSerializer):
    """Serializer for SAPApplication — stub, no field definitions yet."""

    class Meta:
        model = SAPApplication
        fields: list[str] = []
