from simplibs.regex.elements.Literal import Literal


TILDE = Literal("~")
"""Regex expression matching the tilde character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one tilde character (`~`), taken literally.
    Equivalent regex: `\\~`

Example:
    TILDE
    # Matches: "~"
    # Does not match: "a", "~~"
"""

