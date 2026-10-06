# Patterns
from simplibs.patterns.identifiers import IDENTIFIER


IDENTIFIER_LIKE_TEXT = IDENTIFIER
"""Regex expression matching text shaped like an identifier.

Init Params:
    (no parameters)

Pattern:
    Same expression as `IDENTIFIER`; the separate name states the intended role.

Example:
    IDENTIFIER_LIKE_TEXT
    # Matches: "name", "_private", "snake_case_2", "X"
    # Does not match: "2fast", "with-dash", "", "a b"
"""

