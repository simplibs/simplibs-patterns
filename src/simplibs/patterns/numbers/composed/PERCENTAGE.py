# Patterns
from simplibs.patterns.characters import PERCENT
from simplibs.patterns.numbers.composed.NUMBER import NUMBER


PERCENTAGE = NUMBER + PERCENT
"""Regex expression matching a number followed by a percent sign.

Init Params:
    (no parameters)

Pattern:
    A `NUMBER` and `%`.
    Equivalent regex: `(?:[0-9]+\\.[0-9]+|[0-9]+)%`

Notes:
    Does not check the 0–100 range.

Example:
    PERCENTAGE
    # Matches: "50%", "12.5%", "0%"
    # Does not match: "50", "%", "-5%"
"""

