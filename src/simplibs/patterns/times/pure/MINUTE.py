# Patterns
from simplibs.patterns.numbers import MINUTE_NUMBER


MINUTE = MINUTE_NUMBER
"""Regex expression matching a two-digit minute (00–59).

Init Params:
    (no parameters)

Pattern:
    Same expression as `MINUTE_NUMBER`; the separate name states the intended role.

Example:
    MINUTE
    # Matches: "00", "30", "59"
    # Does not match: "60", "5", "123"
"""

