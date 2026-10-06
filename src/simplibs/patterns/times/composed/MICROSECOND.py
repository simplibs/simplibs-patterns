# Patterns
from simplibs.patterns.numbers import DIGIT_NUMBER


MICROSECOND = DIGIT_NUMBER(6)
"""Regex expression matching six digits of microseconds.

Init Params:
    (no parameters)

Pattern:
    Exactly six digits (`000000`–`999999`).
    Equivalent regex: `[0-9]{6}`

Example:
    MICROSECOND
    # Matches: "000123", "999999"
    # Does not match: "123", "1234567"
"""

