# Patterns
from simplibs.patterns.identifiers.pure.IDENTIFIER import IDENTIFIER


MODULE_NAME = IDENTIFIER
"""Regex expression matching a module name.

Init Params:
    (no parameters)

Pattern:
    Same expression as `IDENTIFIER`; the separate name states the intended role.

Notes:
    Language-neutral: same shape as `IDENTIFIER`. Style rules (e.g. UPPER_CASE for constants) are not enforced.

Example:
    MODULE_NAME
    # Matches: "name", "_private", "snake_case_2", "X"
    # Does not match: "2fast", "with-dash", "", "a b"
"""

