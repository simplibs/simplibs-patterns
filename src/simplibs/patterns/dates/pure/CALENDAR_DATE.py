# Patterns
from simplibs.patterns.dates.pure.ISO_DATE import ISO_DATE


CALENDAR_DATE = ISO_DATE
"""Regex expression matching a calendar date.

Init Params:
    (no parameters)

Pattern:
    Same expression as `ISO_DATE`; the separate name states the intended role.

Example:
    CALENDAR_DATE
    # Matches: "2026-09-30", "1999-01-01"
    # Does not match: "2026-9-30", "30.09.2026", "2026-13-01", "2026-00-10"
"""

