# Patterns
from simplibs.patterns.characters import DOT


DECIMAL_SEPARATOR = DOT
"""Regex expression matching the decimal separator.

Init Params:
    (no parameters)

Pattern:
    Same expression as `DOT`; the separate name states the intended role.

Notes:
    Dot only for now.

Example:
    DECIMAL_SEPARATOR
    # Matches: "."
    # Does not match: "a", ".."
"""

