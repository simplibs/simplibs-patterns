# Patterns
from simplibs.patterns.characters import DOT
from simplibs.patterns.dates.pure.DAY import DAY
from simplibs.patterns.dates.pure.MONTH import MONTH
from simplibs.patterns.dates.pure.YEAR import YEAR


EUROPEAN_DATE = DAY + DOT + MONTH + DOT + YEAR
"""Regex expression matching a date in day.month.year form.

Init Params:
    (no parameters)

Pattern:
    `DD.MM.YYYY`: `DAY`, `MONTH` and `YEAR`, joined by dots.
    Equivalent regex: `(?:0[1-9]|[1-2][0-9]|3[01])\\.(?:0[1-9]|1[0-2])\\.[0-9]{4}`

Notes:
    Zero-padded only (`30. 9. 2026` and `30.9.2026` are not matched).

Example:
    EUROPEAN_DATE
    # Matches: "30.09.2026", "01.01.1999"
    # Does not match: "30.9.2026", "2026-09-30", "32.01.2026"
"""

_DESIGN_NOTES = """
A separate pattern could represent unpadded European date forms if that syntax is needed.
Keeping `EUROPEAN_DATE` zero-padded preserves its current unambiguous `DD.MM.YYYY` definition.
"""

