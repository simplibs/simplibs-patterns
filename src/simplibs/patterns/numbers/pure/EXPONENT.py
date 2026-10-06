from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal


EXPONENT = CharacterClass(Literal("e"), Literal("E"))
"""Regex expression matching the exponent marker of scientific notation.

Init Params:
    (no parameters)

Pattern:
    Matches `e` or `E`.
    Equivalent regex: `[eE]`

Example:
    EXPONENT
    # Matches: "e", "E"
    # Does not match: "x", "ee"
"""

