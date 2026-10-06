# Patterns
from simplibs.patterns.numbers import DAY_NUMBER


DAY_OF_MONTH = DAY_NUMBER
"""Regex expression matching a two-digit day of the month.

Init Params:
    (no parameters)

Pattern:
    Same expression as `DAY_NUMBER`; the separate name states the intended role.

Example:
    DAY_OF_MONTH
    # Matches: "01", "15", "29", "31"
    # Does not match: "00", "32", "1", "40"
"""

