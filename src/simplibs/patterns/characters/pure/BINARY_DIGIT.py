from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal


BINARY_DIGIT = CharacterClass(Literal("0"), Literal("1"))
"""Regex expression matching a single binary digit.

Init Params:
    (no parameters)

Pattern:
    Matches `0` or `1`.
    Equivalent regex: `[01]`

Example:
    BINARY_DIGIT
    # Matches: "0", "1"
    # Does not match: "2", "01"
"""

