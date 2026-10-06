# Patterns
from simplibs.patterns.times.composed.DATE_TIME import DATE_TIME
from simplibs.patterns.times.composed.TIMEZONE import TIMEZONE


TIMESTAMP = DATE_TIME + TIMEZONE
"""Regex expression matching an ISO 8601 timestamp with a time zone.

Init Params:
    (no parameters)

Pattern:
    A `DATE_TIME` followed by a mandatory `TIMEZONE`.

Notes:
Example:
    TIMESTAMP
    # Matches: "2026-09-30T14:30:05Z", "2026-09-30T14:30:05+02:00"
    # Does not match: "2026-09-30T14:30:05", "2026-09-30"
"""

_DESIGN_NOTES = """
Making the time zone optional would make `TIMESTAMP` overlap with `DATE_TIME`. Preserve the
current distinction unless there is a clear API reason to merge them.
"""
