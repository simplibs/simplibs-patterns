from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT, NON_ZERO_DIGIT


DAY_NUMBER = Literal("0") + NON_ZERO_DIGIT | CharacterClass(CharacterRange("1", "2")) + DECIMAL_DIGIT | Literal("3") + CharacterClass(Literal("0"), Literal("1"))
"""Regex expression matching a two-digit day-of-month number.

Init Params:
    (no parameters)

Pattern:
    `01`–`31`, always two digits. Whether the day exists in a given month is not checked.
    Equivalent regex: `0[1-9]|[1-2][0-9]|3[01]`

Example:
    DAY_NUMBER
    # Matches: "01", "15", "29", "31"
    # Does not match: "00", "32", "1", "40"
"""

