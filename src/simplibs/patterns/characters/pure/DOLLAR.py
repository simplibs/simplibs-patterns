from simplibs.regex.elements.Literal import Literal


DOLLAR = Literal("$")
"""Regex expression matching the dollar sign character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one dollar sign character (`$`), taken literally.
    Equivalent regex: `\\$`

Example:
    DOLLAR
    # Matches: "$"
    # Does not match: "a", "$$"
"""

