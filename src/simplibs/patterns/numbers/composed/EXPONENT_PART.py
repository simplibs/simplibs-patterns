# Patterns
from simplibs.patterns.numbers.pure.EXPONENT import EXPONENT
from simplibs.patterns.numbers.composed.SIGNED_INTEGER import SIGNED_INTEGER


EXPONENT_PART = EXPONENT + SIGNED_INTEGER
"""Regex expression matching the exponent part of a number in scientific notation.

Init Params:
    (no parameters)

Pattern:
    An `EXPONENT` marker followed by a `SIGNED_INTEGER`.
    Equivalent regex: `[eE][+\\-]?[0-9]+`

Example:
    EXPONENT_PART
    # Matches: "e10", "E-3", "e+5"
    # Does not match: "e", "10", "e-"
"""

