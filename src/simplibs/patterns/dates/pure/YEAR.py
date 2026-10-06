# Patterns
from simplibs.patterns.numbers import YEAR_NUMBER


YEAR = YEAR_NUMBER
"""Regex expression matching a four-digit year.

Init Params:
    (no parameters)

Pattern:
    Same expression as `YEAR_NUMBER`; the separate name states the intended role.

Example:
    YEAR
    # Matches: "2026", "1999"
    # Does not match: "26", "20260"
"""

