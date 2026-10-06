from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT, NON_ZERO_DIGIT


ZERO_TO_TWO_HUNDRED_FIFTY_FIVE = Literal("25") + CharacterClass(CharacterRange("0", "5")) | Literal("2") + CharacterClass(CharacterRange("0", "4")) + DECIMAL_DIGIT | Literal("1") + DECIMAL_DIGIT + DECIMAL_DIGIT | NON_ZERO_DIGIT + DECIMAL_DIGIT | DECIMAL_DIGIT
"""Regex expression matching an integer from 0 to 255 without leading zeros.

Init Params:
    (no parameters)

Pattern:
    Any whole number `0`–`255`; `256`, `01` and `007` do not match.
    Equivalent regex: `25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9]`

Example:
    ZERO_TO_TWO_HUNDRED_FIFTY_FIVE
    # Matches: "0", "9", "10", "199"
    # Does not match: "256", "01", "007", "-1"
"""

