# Patterns
from simplibs.patterns.numbers.custom.POSITIVE import POSITIVE
from simplibs.patterns.numbers.custom.ZERO import ZERO


NON_NEGATIVE = ZERO | POSITIVE
"""Regex expression matching an integer greater than or equal to zero.

Init Params:
    (no parameters)

Pattern:
    `ZERO` or `POSITIVE`.
    Equivalent regex: `[+\\-]?0+|\\+?0*[1-9][0-9]*`

Example:
    NON_NEGATIVE
    # Matches: "0", "5", "+5"
    # Does not match: "-5", "", "1.5"
"""

