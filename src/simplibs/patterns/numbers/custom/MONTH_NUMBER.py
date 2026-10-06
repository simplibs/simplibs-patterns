from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.characters import NON_ZERO_DIGIT


MONTH_NUMBER = Literal("0") + NON_ZERO_DIGIT | Literal("1") + CharacterClass(CharacterRange("0", "2"))
"""Regex expression matching a two-digit month number.

Init Params:
    (no parameters)

Pattern:
    `01`–`12`, always two digits.
    Equivalent regex: `0[1-9]|1[0-2]`

Example:
    MONTH_NUMBER
    # Matches: "01", "09", "10", "12"
    # Does not match: "00", "13", "1", "001"
"""

