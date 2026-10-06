# Patterns
from simplibs.patterns.numbers.pure.FRACTION import FRACTION
from simplibs.patterns.numbers.composed.SIGNED import SIGNED


RATIONAL_NUMBER = SIGNED(FRACTION)
"""Regex expression matching a fraction with an optional sign.

Init Params:
    (no parameters)

Pattern:
    `SIGNED(FRACTION)`.
    Equivalent regex: `[+\\-]?[0-9]+/[0-9]+`

Example:
    RATIONAL_NUMBER
    # Matches: "1/2", "-3/4"
    # Does not match: "1/", "-"
"""

