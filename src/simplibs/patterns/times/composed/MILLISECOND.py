# Patterns
from simplibs.patterns.numbers import DIGIT_NUMBER


MILLISECOND = DIGIT_NUMBER(3)
"""Regex expression matching three digits of milliseconds.

Init Params:
    (no parameters)

Pattern:
    Exactly three digits (`000`–`999`).
    Equivalent regex: `[0-9]{3}`

Example:
    MILLISECOND
    # Matches: "000", "123"
    # Does not match: "12", "1234"
"""

