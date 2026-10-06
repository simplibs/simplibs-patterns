# Patterns
from simplibs.patterns.numbers.composed.DIGIT_NUMBER import DIGIT_NUMBER


ONE_DIGIT_NUMBER = DIGIT_NUMBER(1)
"""Regex expression matching a number of exactly one digit.

Init Params:
    (no parameters)

Pattern:
    `DIGIT_NUMBER(1)`.
    Equivalent regex: `[0-9]{1}`

Example:
    ONE_DIGIT_NUMBER
    # Matches: "7"
    # Does not match: "12", ""
"""

