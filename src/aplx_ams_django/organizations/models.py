"""
FEAT-002: organizations models.

Implements ClientOrg and SAPApplication as defined in DBD-001 v0.1.
FEAT-003: Contract model (DBD-001 v0.1).
"""

from __future__ import annotations

from typing import ClassVar

from django.db import models
from django.db.models import Q


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


class Contract(models.Model):
    """Represents a support contract between APLX and a client organization (DBD-001 v0.1)."""

    HOURS_BANK = "hours_bank"
    FIXED_FEE = "fixed_fee"
    CONTRACT_TYPE_CHOICES: ClassVar[list[tuple[str, str]]] = [
        (HOURS_BANK, "Hours bank"),
        (FIXED_FEE, "Fixed fee"),
    ]

    client_org = models.ForeignKey(ClientOrg, on_delete=models.CASCADE, related_name="contracts")
    contract_type = models.CharField(max_length=20, choices=CONTRACT_TYPE_CHOICES)
    contracted_hours = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    monthly_close_at = models.DateTimeField(null=True, blank=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints: ClassVar[list[models.BaseConstraint]] = [
            models.CheckConstraint(
                check=~Q(contract_type="hours_bank") | Q(contracted_hours__isnull=False),
                name="chk_hours_bank_requires_contracted_hours",
            ),
            models.CheckConstraint(
                check=Q(contracted_hours__isnull=True) | Q(contracted_hours__gt=0),
                name="chk_contracted_hours_positive",
            ),
            models.UniqueConstraint(
                fields=["client_org"],
                condition=Q(is_active=True),
                name="organizations_contract_one_active_per_org_idx",
            ),
        ]
