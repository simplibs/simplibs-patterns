# Patterns
from simplibs.patterns.numbers.composed.FOUR_DIGIT_NUMBER import FOUR_DIGIT_NUMBER


YEAR_NUMBER = FOUR_DIGIT_NUMBER
"""Regex expression matching a four-digit year.

Init Params:
    (no parameters)

Pattern:
    Exactly four digits (`0000`–`9999`).
    Equivalent regex: `[0-9]{4}`

Notes:
    The pattern accepts exactly four digits, so two-digit years and years outside the `0000`–`9999`
    range are not represented.

Example:
    YEAR_NUMBER
    # Matches: "2026", "1999"
    # Does not match: "26", "20260"
"""

