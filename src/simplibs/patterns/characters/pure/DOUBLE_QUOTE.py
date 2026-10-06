from simplibs.regex.elements.Literal import Literal


DOUBLE_QUOTE = Literal("\"")
"""Regex expression matching the double quote character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one double quote character (`"`), taken literally.
    Equivalent regex: `"`

Example:
    DOUBLE_QUOTE
    # Matches: '"'
    # Does not match: "a", '""'
"""

