from simplibs.regex.elements.Literal import Literal


EQUALS = Literal("=")
"""Regex expression matching the equals sign character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one equals sign character (`=`), taken literally.
    Equivalent regex: `=`

Example:
    EQUALS
    # Matches: "="
    # Does not match: "a", "=="
"""

