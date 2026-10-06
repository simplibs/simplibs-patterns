from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.elements.Literal import Literal


QUARTER = Literal("Q") + CharacterClass(CharacterRange("1", "4"))
"""Regex expression matching a calendar quarter.

Init Params:
    (no parameters)

Pattern:
    `Q1`–`Q4`.
    Equivalent regex: `Q[1-4]`

Example:
    QUARTER
    # Matches: "Q1", "Q4"
    # Does not match: "Q0", "Q5", "1"
"""

