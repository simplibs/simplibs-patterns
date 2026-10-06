from simplibs.regex.elements.Literal import Literal


CARET = Literal("^")
"""Regex expression matching the caret character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one caret character (`^`), taken literally.
    Equivalent regex: `\\^`

Example:
    CARET
    # Matches: "^"
    # Does not match: "a", "^^"
"""

