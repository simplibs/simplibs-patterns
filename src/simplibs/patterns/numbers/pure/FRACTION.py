# Patterns
from simplibs.patterns.characters import SLASH
from simplibs.patterns.numbers.pure.INTEGER import INTEGER


FRACTION = INTEGER + SLASH + INTEGER
"""Regex expression matching a fraction written with a slash.

Init Params:
    (no parameters)

Pattern:
    An `INTEGER`, a slash and another `INTEGER`.
    Equivalent regex: `[0-9]+/[0-9]+`

Example:
    FRACTION
    # Matches: "1/2", "22/7"
    # Does not match: "1/", "/2", "1.5/2"
"""

