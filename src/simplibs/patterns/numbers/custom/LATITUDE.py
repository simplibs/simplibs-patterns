from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import ONE_OR_MORE, OPTIONAL
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT, DOT, MINUS_SIGN
from simplibs.patterns.numbers.pure.INTEGER import INTEGER


LATITUDE = OPTIONAL(MINUS_SIGN) + (Literal("90") + OPTIONAL(DOT + ONE_OR_MORE(Literal("0"))) | OPTIONAL(CharacterClass(CharacterRange("1", "8"))) + DECIMAL_DIGIT + OPTIONAL(DOT + INTEGER))
"""Regex expression matching a latitude in decimal degrees.

Init Params:
    (no parameters)

Pattern:
    A decimal number from `-90` to `90`; the fractional part is optional.
    Equivalent regex: `\\-?(?:90(?:\\.0+)?|[1-8]?[0-9](?:\\.[0-9]+)?)`

Example:
    LATITUDE
    # Matches: "0", "45.5", "-33.865", "90"
    # Does not match: "90.5", "91", "-91", "45."
"""

