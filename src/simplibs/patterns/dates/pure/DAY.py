# Patterns
from simplibs.patterns.numbers import DAY_NUMBER


DAY = DAY_NUMBER
"""Regex expression matching a two-digit day.

Init Params:
    (no parameters)

Pattern:
    Same expression as `DAY_NUMBER`; the separate name states the intended role.

Example:
    DAY
    # Matches: "01", "15", "29", "31"
    # Does not match: "00", "32", "1", "40"
"""

