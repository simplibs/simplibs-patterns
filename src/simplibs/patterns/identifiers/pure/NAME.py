# Patterns
from simplibs.patterns.identifiers.pure.IDENTIFIER import IDENTIFIER


NAME = IDENTIFIER
"""Regex expression matching a name.

Init Params:
    (no parameters)

Pattern:
    Same expression as `IDENTIFIER`; the separate name states the intended role.

Example:
    NAME
    # Matches: "name", "_private", "snake_case_2", "X"
    # Does not match: "2fast", "with-dash", "", "a b"
"""

