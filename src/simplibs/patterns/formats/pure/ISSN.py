from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import EXACTLY
# Patterns
from simplibs.patterns.characters import DASH, DECIMAL_DIGIT


ISSN = EXACTLY(DECIMAL_DIGIT, 4) + DASH + EXACTLY(DECIMAL_DIGIT, 3) + CharacterClass(CharacterRange("0", "9"), Literal("X"), Literal("x"))
"""Regex expression matching an ISSN.

Init Params:
    (no parameters)

Pattern:
    `NNNN-NNNX`: four digits, a hyphen, three digits and a digit or `X`.
    Equivalent regex: `[0-9]{4}\\-[0-9]{3}[0-9Xx]`

Notes:
    The check digit is not verified.

Example:
    ISSN
    # Matches: "0317-8471", "2434-561X"
    # Does not match: "03178471", "0317-847", "0317-84711"
"""

