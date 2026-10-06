# Patterns
from simplibs.patterns.characters import SLASH
from simplibs.patterns.dates.pure.DAY import DAY
from simplibs.patterns.dates.pure.MONTH import MONTH
from simplibs.patterns.dates.pure.YEAR import YEAR


US_DATE = MONTH + SLASH + DAY + SLASH + YEAR
"""Regex expression matching a date in month/day/year form.

Init Params:
    (no parameters)

Pattern:
    `MM/DD/YYYY`: `MONTH`, `DAY` and `YEAR`, joined by slashes.
    Equivalent regex: `(?:0[1-9]|1[0-2])/(?:0[1-9]|[1-2][0-9]|3[01])/[0-9]{4}`

Example:
    US_DATE
    # Matches: "09/30/2026", "01/01/1999"
    # Does not match: "30/09/2026", "9/30/2026", "2026/09/30"
"""

