"""
FEAT-002: organizations models.

Implements ClientOrg and SAPApplication as defined in DBD-001 v0.1.
"""

from typing import ClassVar

from django.db import models


class ClientOrg(models.Model):
    """Represents a client organization whose SAP applications AMS supports."""

    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass


class SAPApplication(models.Model):
    """Represents an SAP application belonging to one client organization."""

    client_org = models.ForeignKey(
        ClientOrg, on_delete=models.CASCADE, related_name="sap_applications"
    )
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together: ClassVar[list[tuple[str, str]]] = [("client_org", "name")]
