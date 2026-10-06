# Patterns
from simplibs.patterns.structured.custom.SEPARATOR import SEPARATOR


DELIMITER = SEPARATOR
"""Regex expression matching a delimiter character.

Init Params:
    (no parameters)

Pattern:
    Same expression as `SEPARATOR`; the separate name states the intended role.

Notes:
    Same set as `SEPARATOR`. Bracket-like delimiters: `OPENING_DELIMITER`, `CLOSING_DELIMITER`.

Example:
    DELIMITER
    # Matches: ",", ";", "|", "\\t"
    # Does not match: "a", "::", ""
"""

