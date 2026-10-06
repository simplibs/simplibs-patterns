# Patterns
from simplibs.patterns.numbers.composed.NUMBER import NUMBER
from simplibs.patterns.numbers.composed.SIGNED import SIGNED


SIGNED_NUMBER = SIGNED(NUMBER)
"""Regex expression matching an integer or decimal number with an optional sign.

Init Params:
    (no parameters)

Pattern:
    `SIGNED(NUMBER)`.
    Equivalent regex: `[+\\-]?(?:[0-9]+\\.[0-9]+|[0-9]+)`

Example:
    SIGNED_NUMBER
    # Matches: "7", "-7.5", "+0.1"
    # Does not match: "-", "7.", ".5"
"""

