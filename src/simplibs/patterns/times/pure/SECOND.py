# Patterns
from simplibs.patterns.numbers import SECOND_NUMBER


SECOND = SECOND_NUMBER
"""Regex expression matching a two-digit second (00–59).

Init Params:
    (no parameters)

Pattern:
    Same expression as `SECOND_NUMBER`; the separate name states the intended role.

Example:
    SECOND
    # Matches: "00", "30", "59"
    # Does not match: "60", "5", "123"
"""

