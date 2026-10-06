from simplibs.regex.elements.Literal import Literal


SPACE = Literal(" ")
"""Regex expression matching a single space character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one space character, taken literally.
    Equivalent regex: `\\ `

Example:
    SPACE
    # Matches: " "
    # Does not match: "a", "  "
"""

