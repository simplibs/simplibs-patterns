from simplibs.regex.elements.Literal import Literal


SINGLE_QUOTE = Literal("'")
"""Regex expression matching the single quote character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one single quote character (`'`), taken literally.
    Equivalent regex: `'`

Example:
    SINGLE_QUOTE
    # Matches: "'"
    # Does not match: "a", "''"
"""

