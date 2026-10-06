from simplibs.regex.elements.Literal import Literal


UNDERSCORE = Literal("_")
"""Regex expression matching the underscore character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one underscore character (`_`), taken literally.
    Equivalent regex: `_`

Example:
    UNDERSCORE
    # Matches: "_"
    # Does not match: "a", "__"
"""

