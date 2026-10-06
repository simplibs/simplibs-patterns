from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT, MINUS_SIGN, NON_ZERO_DIGIT


NEGATIVE = MINUS_SIGN + ZERO_OR_MORE(Literal("0")) + NON_ZERO_DIGIT + ZERO_OR_MORE(DECIMAL_DIGIT)
"""Regex expression matching an integer less than zero.

Init Params:
    (no parameters)

Pattern:
    A `-`, optional leading zeros, then a digit 1–9 and any further digits.
    Equivalent regex: `\\-0*[1-9][0-9]*`

Example:
    NEGATIVE
    # Matches: "-5", "-007", "-100"
    # Does not match: "5", "-0", "0", "-5.5"
"""

