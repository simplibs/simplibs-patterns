from simplibs.regex.elements.Literal import Literal


COMMA = Literal(",")
"""Regex expression matching the comma character.

Init Params:
    (no parameters)

Pattern:
    Matches exactly one comma character (`,`), taken literally.
    Equivalent regex: `,`

Example:
    COMMA
    # Matches: ","
    # Does not match: "a", ",,"
"""

