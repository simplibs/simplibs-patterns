from simplibs.regex.elements.Literal import Literal


SEMICOLON = Literal(";")
"""Regex expression matching the semicolon character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one semicolon character (`;`), taken literally.
    Equivalent regex: `;`

Example:
    SEMICOLON
    # Matches: ";"
    # Does not match: "a", ";;"
"""

