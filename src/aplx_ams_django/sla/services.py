"""
FEAT-010 sla services — Mode B implementation.

add_holiday: create a new HolidayEntry for a given date.
remove_holiday: soft-remove (set removed_at / removed_by) on an existing entry.
is_holiday: check whether a date is an active company holiday.
"""

from __future__ import annotations

from datetime import date

from django.utils import timezone

from aplx_ams_django.sla.models import HolidayEntry


def add_holiday(holiday_date: date, added_by: object) -> HolidayEntry:
    """Create a new active HolidayEntry for the given date.

    Args:
        holiday_date: The calendar date to mark as a company holiday.
        added_by: The User instance (delivery_manager) performing the action.

    Returns:
        The newly created HolidayEntry instance.

    Raises:
        ValueError: If a non-removed entry for holiday_date already exists.
    """
    if HolidayEntry.objects.filter(holiday_date=holiday_date, removed_at__isnull=True).exists():
        raise ValueError(f"An active holiday already exists for {holiday_date}")

    return HolidayEntry.objects.create(
        holiday_date=holiday_date,
        added_by=added_by,
    )


def remove_holiday(entry: HolidayEntry, removed_by: object) -> HolidayEntry:
    """Soft-remove an existing HolidayEntry by setting removed_at and removed_by.

    Args:
        entry: The HolidayEntry instance to soft-remove.
        removed_by: The User instance (delivery_manager) performing the action.

    Returns:
        The updated HolidayEntry instance with removed_at set.
    """
    entry.removed_at = timezone.now()
    entry.removed_by = removed_by
    entry.save(update_fields=["removed_at", "removed_by"])
    return entry


def is_holiday(holiday_date: date) -> bool:
    """Return True if an active (removed_at IS NULL) HolidayEntry exists for the date.

    Args:
        holiday_date: The calendar date to check.

    Returns:
        True if the date is an active company holiday, False otherwise.
    """
    return HolidayEntry.objects.filter(
        holiday_date=holiday_date,
        removed_at__isnull=True,
    ).exists()
