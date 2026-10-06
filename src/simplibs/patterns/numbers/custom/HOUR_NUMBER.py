from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT


HOUR_NUMBER = CharacterClass(Literal("0"), Literal("1")) + DECIMAL_DIGIT | Literal("2") + CharacterClass(CharacterRange("0", "3"))
"""Regex expression matching a two-digit hour in 24-hour form.

Init Params:
    (no parameters)

Pattern:
    `00`–`23`, always two digits.
    Equivalent regex: `[01][0-9]|2[0-3]`

Example:
    HOUR_NUMBER
    # Matches: "00", "09", "19", "23"
    # Does not match: "24", "7", "123"
"""

