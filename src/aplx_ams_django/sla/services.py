"""
FEAT-010 sla services — Mode A stubs.

add_holiday: create a new HolidayEntry for a given date.
remove_holiday: soft-remove (set removed_at / removed_by) on an existing entry.

Mode B implementation performs the real DB writes via dal.py.
"""

from __future__ import annotations

from datetime import date

from aplx_ams_django.sla.models import HolidayEntry


def add_holiday(holiday_date: date, added_by: object) -> HolidayEntry:
    """Create a new active HolidayEntry for the given date.

    Args:
        holiday_date: The calendar date to mark as a company holiday.
        added_by: The User instance (delivery_manager) performing the action.

    Returns:
        The newly created HolidayEntry instance.

    Raises:
        NotImplementedError: Mode A stub — not yet implemented.
    """
    raise NotImplementedError("add_holiday is not yet implemented (Mode A stub)")


def remove_holiday(holiday_id: int, removed_by: object) -> HolidayEntry:
    """Soft-remove an existing HolidayEntry by setting removed_at and removed_by.

    Args:
        holiday_id: Primary key of the HolidayEntry to remove.
        removed_by: The User instance (delivery_manager) performing the action.

    Returns:
        The updated HolidayEntry instance with removed_at set.

    Raises:
        HolidayEntry.DoesNotExist: If no active entry with the given id exists.
        NotImplementedError: Mode A stub — not yet implemented.
    """
    raise NotImplementedError("remove_holiday is not yet implemented (Mode A stub)")
