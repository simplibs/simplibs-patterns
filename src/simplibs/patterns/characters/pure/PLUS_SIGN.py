from simplibs.regex.elements.Literal import Literal


PLUS_SIGN = Literal("+")
"""Regex expression matching the plus sign character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one plus sign character (`+`), taken literally.
    Equivalent regex: `\\+`

Example:
    PLUS_SIGN
    # Matches: "+"
    # Does not match: "a", "++"
"""

