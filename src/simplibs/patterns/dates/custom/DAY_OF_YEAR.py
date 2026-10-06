from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import EXACTLY
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT, NON_ZERO_DIGIT


DAY_OF_YEAR = Literal("00") + NON_ZERO_DIGIT | Literal("0") + NON_ZERO_DIGIT + DECIMAL_DIGIT | CharacterClass(CharacterRange("1", "2")) + EXACTLY(DECIMAL_DIGIT, 2) | Literal("3") + CharacterClass(CharacterRange("0", "5")) + DECIMAL_DIGIT | Literal("36") + CharacterClass(CharacterRange("0", "6"))
"""Regex expression matching a three-digit day of the year.

Init Params:
    (no parameters)

Pattern:
    `001`–`366`, always three digits.
    Equivalent regex: `00[1-9]|0[1-9][0-9]|[1-2][0-9]{2}|3[0-5][0-9]|36[0-6]`

Example:
    DAY_OF_YEAR
    # Matches: "001", "059", "300", "366"
    # Does not match: "000", "367", "1", "0001"
"""

