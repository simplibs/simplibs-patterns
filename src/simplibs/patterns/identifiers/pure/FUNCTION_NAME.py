# Patterns
from simplibs.patterns.identifiers.pure.IDENTIFIER import IDENTIFIER


FUNCTION_NAME = IDENTIFIER
"""Regex expression matching a function name.

Init Params:
    (no parameters)

Pattern:
    Same expression as `IDENTIFIER`; the separate name states the intended role.

Notes:
    Language-neutral: same shape as `IDENTIFIER`. Style rules (e.g. UPPER_CASE for constants) are not enforced.

Example:
    FUNCTION_NAME
    # Matches: "name", "_private", "snake_case_2", "X"
    # Does not match: "2fast", "with-dash", "", "a b"
"""

