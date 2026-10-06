from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import OPTIONAL, ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT, NON_ZERO_DIGIT, PLUS_SIGN


POSITIVE = OPTIONAL(PLUS_SIGN) + ZERO_OR_MORE(Literal("0")) + NON_ZERO_DIGIT + ZERO_OR_MORE(DECIMAL_DIGIT)
"""Regex expression matching an integer greater than zero.

Init Params:
    (no parameters)

Pattern:
    An optional `+`, optional leading zeros, then a digit 1–9 and any further digits.
    Equivalent regex: `\\+?0*[1-9][0-9]*`

Example:
    POSITIVE
    # Matches: "5", "+5", "007", "100"
    # Does not match: "0", "-5", "00", "5.5"
"""

