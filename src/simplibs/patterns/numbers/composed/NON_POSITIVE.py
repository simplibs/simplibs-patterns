# Patterns
from simplibs.patterns.numbers.custom.NEGATIVE import NEGATIVE
from simplibs.patterns.numbers.custom.ZERO import ZERO


NON_POSITIVE = ZERO | NEGATIVE
"""Regex expression matching an integer less than or equal to zero.

Init Params:
    (no parameters)

Pattern:
    `ZERO` or `NEGATIVE`.
    Equivalent regex: `[+\\-]?0+|\\-0*[1-9][0-9]*`

Example:
    NON_POSITIVE
    # Matches: "0", "-5", "-0"
    # Does not match: "5", "+1", ""
"""

