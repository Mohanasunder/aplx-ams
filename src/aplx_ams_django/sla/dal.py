"""
FEAT-010 sla data access layer — stub (Mode A).

get_holidays_in_range: returns HolidayEntry rows active in [start, end].

Stub raises NotImplementedError; Mode B will replace with the real query.
Named per STD-001 v0.1 § Naming And Structure.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aplx_ams_django.sla.models import HolidayEntry


def get_holidays_in_range(
    start: date,
    end: date,
    as_of: datetime | None = None,
) -> list["HolidayEntry"]:
    """Return active HolidayEntry rows whose holiday_date falls in [start, end].

    An entry is "active" when:
      - removed_at is NULL (not yet removed), AND
      - added_at <= as_of (the entry existed at the queried point in time).

    Args:
        start: First date of the inclusive range.
        end: Last date of the inclusive range.
        as_of: Point-in-time filter (datetime, timezone-aware). When None,
               the current timestamp is used. Supports AC-4 (holiday added
               mid-day only counts from the moment of addition onward).

    Returns:
        List of HolidayEntry instances whose holiday_date is in [start, end]
        and that are active at the given as_of time.

    Raises:
        NotImplementedError: until Mode B implementation is complete.
    """
    raise NotImplementedError
