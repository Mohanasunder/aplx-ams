"""
FEAT-010 sla serializers — Mode A stubs.

HolidayEntrySerializer: ModelSerializer for HolidayEntry.
Mode B implementation populates read/write fields per API-001 v0.3 §F-2.
"""

from __future__ import annotations

from typing import ClassVar

from rest_framework import serializers

from aplx_ams_django.sla.models import HolidayEntry


class HolidayEntrySerializer(serializers.ModelSerializer):
    """Serializer for HolidayEntry — stub; action methods not yet implemented."""

    class Meta:
        model = HolidayEntry
        fields: ClassVar[list[str]] = [
            "id",
            "holiday_date",
            "added_at",
            "added_by_id",
            "removed_at",
            "removed_by_id",
        ]
        read_only_fields: ClassVar[list[str]] = [
            "id",
            "added_at",
            "added_by_id",
            "removed_at",
            "removed_by_id",
        ]
