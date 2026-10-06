from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.characters import DASH
from simplibs.patterns.dates.pure.WEEKDAY import WEEKDAY
from simplibs.patterns.dates.pure.YEAR import YEAR
from simplibs.patterns.dates.custom.WEEK_NUMBER import WEEK_NUMBER


WEEK_DATE = YEAR + Literal("-W") + WEEK_NUMBER + DASH + WEEKDAY
"""Regex expression matching an ISO week date.

Init Params:
    (no parameters)

Pattern:
    `YYYY-Www-D`: `YEAR`, `W`, `WEEK_NUMBER`, hyphen and `WEEKDAY`.
    Equivalent regex: `[0-9]{4}\\-W(?:0[1-9]|[1-4][0-9]|5[0-3])\\-[1-7]`

Example:
    WEEK_DATE
    # Matches: "2026-W40-3", "1999-W01-1"
    # Does not match: "2026-W54-1", "2026-40-3", "2026-W40-8"
"""

