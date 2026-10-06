from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT, NON_ZERO_DIGIT


WEEK_NUMBER = Literal("0") + NON_ZERO_DIGIT | CharacterClass(CharacterRange("1", "4")) + DECIMAL_DIGIT | Literal("5") + CharacterClass(CharacterRange("0", "3"))
"""Regex expression matching a two-digit ISO week number.

Init Params:
    (no parameters)

Pattern:
    `01`–`53`, always two digits.
    Equivalent regex: `0[1-9]|[1-4][0-9]|5[0-3]`

Example:
    WEEK_NUMBER
    # Matches: "01", "09", "27", "53"
    # Does not match: "00", "54", "5", "100"
"""

