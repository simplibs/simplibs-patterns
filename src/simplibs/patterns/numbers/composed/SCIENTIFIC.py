# Patterns
from simplibs.patterns.numbers.composed.EXPONENT_PART import EXPONENT_PART
from simplibs.patterns.numbers.composed.NUMBER import NUMBER


SCIENTIFIC = NUMBER + EXPONENT_PART
"""Regex expression matching an unsigned number in scientific notation.

Init Params:
    (no parameters)

Pattern:
    A `NUMBER` followed by an `EXPONENT_PART`.
    Equivalent regex: `(?:[0-9]+\\.[0-9]+|[0-9]+)[eE][+\\-]?[0-9]+`

Notes:
    Unsigned mantissa; wrap with `SIGNED(SCIENTIFIC)` to allow a leading sign.

Example:
    SCIENTIFIC
    # Matches: "1e10", "2.5E-3", "0.1e+2"
    # Does not match: "1", "e5", "1e"
"""

