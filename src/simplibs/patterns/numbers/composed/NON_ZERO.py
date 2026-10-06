# Patterns
from simplibs.patterns.numbers.custom.NEGATIVE import NEGATIVE
from simplibs.patterns.numbers.custom.POSITIVE import POSITIVE


NON_ZERO = POSITIVE | NEGATIVE
"""Regex expression matching an integer different from zero.

Init Params:
    (no parameters)

Pattern:
    `POSITIVE` or `NEGATIVE`.
    Equivalent regex: `\\+?0*[1-9][0-9]*|\\-0*[1-9][0-9]*`

Example:
    NON_ZERO
    # Matches: "5", "-5", "+3"
    # Does not match: "0", "-0", ""
"""

