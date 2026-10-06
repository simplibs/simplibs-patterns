from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.numbers.composed.NUMBER import NUMBER


PERMILLE = NUMBER + Literal("‰")
"""Regex expression matching a number followed by a per-mille sign.

Init Params:
    (no parameters)

Pattern:
    A `NUMBER` and `‰`.
    Equivalent regex: `(?:[0-9]+\\.[0-9]+|[0-9]+)‰`

Example:
    PERMILLE
    # Matches: "5‰", "0.5‰"
    # Does not match: "5", "‰"
"""

