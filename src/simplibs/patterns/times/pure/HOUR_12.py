from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.characters import NON_ZERO_DIGIT


HOUR_12 = Literal("0") + NON_ZERO_DIGIT | Literal("1") + CharacterClass(CharacterRange("0", "2"))
"""Regex expression matching a two-digit hour in 12-hour form.

Init Params:
    (no parameters)

Pattern:
    `01`–`12`, always two digits.
    Equivalent regex: `0[1-9]|1[0-2]`

Example:
    HOUR_12
    # Matches: "01", "09", "12"
    # Does not match: "00", "13", "1"
"""

