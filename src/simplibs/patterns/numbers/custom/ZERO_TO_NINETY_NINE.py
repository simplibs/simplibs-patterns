# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT, NON_ZERO_DIGIT


ZERO_TO_NINETY_NINE = NON_ZERO_DIGIT + DECIMAL_DIGIT | DECIMAL_DIGIT
"""Regex expression matching an integer from 0 to 99 without leading zeros.

Init Params:
    (no parameters)

Pattern:
    Two digits starting with 1–9, or a single digit.
    Equivalent regex: `[1-9][0-9]|[0-9]`

Example:
    ZERO_TO_NINETY_NINE
    # Matches: "0", "9", "10", "99"
    # Does not match: "00", "01", "100", ""
"""

