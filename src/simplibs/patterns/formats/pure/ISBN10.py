from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import EXACTLY
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT


ISBN10 = EXACTLY(DECIMAL_DIGIT, 9) + CharacterClass(CharacterRange("0", "9"), Literal("X"), Literal("x"))
"""Regex expression matching an ISBN-10 without hyphens.

Init Params:
    (no parameters)

Pattern:
    Nine digits followed by a digit or `X`.
    Equivalent regex: `[0-9]{9}[0-9Xx]`

Notes:
    The check digit is not verified (a regex cannot compute it).

Example:
    ISBN10
    # Matches: "0306406152", "080442957X"
    # Does not match: "030640615", "03064061523", "0306-406152"
"""

