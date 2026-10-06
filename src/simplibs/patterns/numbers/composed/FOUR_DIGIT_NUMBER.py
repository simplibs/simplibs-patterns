# Patterns
from simplibs.patterns.numbers.composed.DIGIT_NUMBER import DIGIT_NUMBER


FOUR_DIGIT_NUMBER = DIGIT_NUMBER(4)
"""Regex expression matching a number of exactly four digits.

Init Params:
    (no parameters)

Pattern:
    `DIGIT_NUMBER(4)`.
    Equivalent regex: `[0-9]{4}`

Example:
    FOUR_DIGIT_NUMBER
    # Matches: "2026", "0001"
    # Does not match: "202", "20260"
"""

