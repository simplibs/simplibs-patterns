from simplibs.regex.elements.Literal import Literal


ASTERISK = Literal("*")
"""Regex expression matching the asterisk character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one asterisk character (`*`), taken literally.
    Equivalent regex: `\\*`

Example:
    ASTERISK
    # Matches: "*"
    # Does not match: "a", "**"
"""

