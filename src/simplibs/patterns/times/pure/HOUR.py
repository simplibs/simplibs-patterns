# Patterns
from simplibs.patterns.numbers import HOUR_NUMBER


HOUR = HOUR_NUMBER
"""Regex expression matching a two-digit hour (00–23).

Init Params:
    (no parameters)

Pattern:
    Same expression as `HOUR_NUMBER`; the separate name states the intended role.

Example:
    HOUR
    # Matches: "00", "09", "19", "23"
    # Does not match: "24", "7", "123"
"""

