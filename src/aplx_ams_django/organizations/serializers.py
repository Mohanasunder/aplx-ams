"""
FEAT-002: organizations serializers.

ClientOrgSerializer: id, name, created_at.
SAPApplicationSerializer: id, client_org, name, created_at.
"""

from rest_framework import serializers

from aplx_ams_django.organizations.models import ClientOrg, SAPApplication


class ClientOrgSerializer(serializers.ModelSerializer):
    """Serializer for ClientOrg read and create operations."""

    class Meta:
        model = ClientOrg
        fields = ["id", "name", "created_at"]
        read_only_fields = ["id", "created_at"]


class SAPApplicationSerializer(serializers.ModelSerializer):
    """Serializer for SAPApplication read operations.

    client_org is written by the view (from URL kwargs); name is written by the
    caller.  Both id and created_at are read-only server-assigned values.
    """

    class Meta:
        model = SAPApplication
        fields = ["id", "client_org", "name", "created_at"]
        read_only_fields = ["id", "client_org", "created_at"]
