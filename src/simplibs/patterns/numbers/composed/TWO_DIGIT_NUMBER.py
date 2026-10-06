# Patterns
from simplibs.patterns.numbers.composed.DIGIT_NUMBER import DIGIT_NUMBER


TWO_DIGIT_NUMBER = DIGIT_NUMBER(2)
"""Regex expression matching a number of exactly two digits.

Init Params:
    (no parameters)

Pattern:
    `DIGIT_NUMBER(2)`.
    Equivalent regex: `[0-9]{2}`

Example:
    TWO_DIGIT_NUMBER
    # Matches: "12", "07"
    # Does not match: "1", "123"
"""

