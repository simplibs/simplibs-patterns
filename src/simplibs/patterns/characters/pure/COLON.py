from simplibs.regex.elements.Literal import Literal


COLON = Literal(":")
"""Regex expression matching the colon character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one colon character (`:`), taken literally.
    Equivalent regex: `:`

Example:
    COLON
    # Matches: ":"
    # Does not match: "a", "::"
"""

