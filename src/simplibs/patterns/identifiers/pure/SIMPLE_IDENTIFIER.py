# Patterns
from simplibs.patterns.identifiers.pure.IDENTIFIER import IDENTIFIER


SIMPLE_IDENTIFIER = IDENTIFIER
"""Regex expression matching a simple (unqualified) identifier.

Init Params:
    (no parameters)

Pattern:
    Same expression as `IDENTIFIER`; the separate name states the intended role.

Example:
    SIMPLE_IDENTIFIER
    # Matches: "name", "_private", "snake_case_2", "X"
    # Does not match: "2fast", "with-dash", "", "a b"
"""

