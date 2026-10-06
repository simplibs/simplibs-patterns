# Patterns
from simplibs.patterns.numbers.pure.INTEGER import INTEGER
from simplibs.patterns.numbers.composed.SIGNED import SIGNED


SIGNED_INTEGER = SIGNED(INTEGER)
"""Regex expression matching an integer with an optional sign.

Init Params:
    (no parameters)

Pattern:
    `SIGNED(INTEGER)`.
    Equivalent regex: `[+\\-]?[0-9]+`

Example:
    SIGNED_INTEGER
    # Matches: "7", "-7", "+7"
    # Does not match: "-", "7-", ""
"""

