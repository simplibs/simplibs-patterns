# Patterns
from simplibs.patterns.numbers.composed.DIGIT_NUMBER import DIGIT_NUMBER


THREE_DIGIT_NUMBER = DIGIT_NUMBER(3)
"""Regex expression matching a number of exactly three digits.

Init Params:
    (no parameters)

Pattern:
    `DIGIT_NUMBER(3)`.
    Equivalent regex: `[0-9]{3}`

Example:
    THREE_DIGIT_NUMBER
    # Matches: "123", "007"
    # Does not match: "12", "1234"
"""

