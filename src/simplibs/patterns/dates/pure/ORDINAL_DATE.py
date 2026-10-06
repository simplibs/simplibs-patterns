# Patterns
from simplibs.patterns.characters import DASH
from simplibs.patterns.dates.pure.YEAR import YEAR
from simplibs.patterns.dates.custom.DAY_OF_YEAR import DAY_OF_YEAR


ORDINAL_DATE = YEAR + DASH + DAY_OF_YEAR
"""Regex expression matching a year with a day-of-year number.

Init Params:
    (no parameters)

Pattern:
    `YYYY-DDD`: `YEAR` and `DAY_OF_YEAR`.
    Equivalent regex: `[0-9]{4}\\-(?:00[1-9]|0[1-9][0-9]|[1-2][0-9]{2}|3[0-5][0-9]|36[0-6])`

Example:
    ORDINAL_DATE
    # Matches: "2026-273", "1999-001"
    # Does not match: "2026-000", "2026-367", "2026-27"
"""

