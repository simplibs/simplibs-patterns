# Patterns
from simplibs.patterns.numbers import MONTH_NUMBER


MONTH = MONTH_NUMBER
"""Regex expression matching a two-digit month.

Init Params:
    (no parameters)

Pattern:
    Same expression as `MONTH_NUMBER`; the separate name states the intended role.

Example:
    MONTH
    # Matches: "01", "09", "10", "12"
    # Does not match: "00", "13", "1", "001"
"""

