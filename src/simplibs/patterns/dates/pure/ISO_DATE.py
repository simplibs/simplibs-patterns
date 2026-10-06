# Patterns
from simplibs.patterns.characters import DASH
from simplibs.patterns.dates.pure.DAY import DAY
from simplibs.patterns.dates.pure.MONTH import MONTH
from simplibs.patterns.dates.pure.YEAR import YEAR


ISO_DATE = YEAR + DASH + MONTH + DASH + DAY
"""Regex expression matching a date in ISO 8601 form.

Init Params:
    (no parameters)

Pattern:
    `YYYY-MM-DD`: `YEAR`, `MONTH` and `DAY`, joined by hyphens.
    Equivalent regex: `[0-9]{4}\\-(?:0[1-9]|1[0-2])\\-(?:0[1-9]|[1-2][0-9]|3[01])`

Notes:
    Checks the shape and the ranges of month (01–12) and day (01–31), not whether the day exists in that month.

Example:
    ISO_DATE
    # Matches: "2026-09-30", "1999-01-01"
    # Does not match: "2026-9-30", "30.09.2026", "2026-13-01", "2026-00-10"
"""

