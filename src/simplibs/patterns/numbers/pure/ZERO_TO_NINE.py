# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT


ZERO_TO_NINE = DECIMAL_DIGIT
"""Regex expression matching a single digit from 0 to 9.

Init Params:
    (no parameters)

Pattern:
    Same expression as `DECIMAL_DIGIT`; the separate name states the intended role.

Example:
    ZERO_TO_NINE
    # Matches: "0", "7", "9"
    # Does not match: "a", "42", "٣"
"""

