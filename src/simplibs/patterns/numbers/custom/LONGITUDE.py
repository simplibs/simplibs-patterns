from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import ONE_OR_MORE, OPTIONAL
# Patterns
from simplibs.patterns.characters import (
    DECIMAL_DIGIT,
    DOT,
    MINUS_SIGN,
    NON_ZERO_DIGIT,
)
from simplibs.patterns.numbers.pure.INTEGER import INTEGER


LONGITUDE = OPTIONAL(MINUS_SIGN) + (Literal("180") + OPTIONAL(DOT + ONE_OR_MORE(Literal("0"))) | Literal("1") + CharacterClass(CharacterRange("0", "7")) + DECIMAL_DIGIT + OPTIONAL(DOT + INTEGER) | OPTIONAL(NON_ZERO_DIGIT) + DECIMAL_DIGIT + OPTIONAL(DOT + INTEGER))
"""Regex expression matching a longitude in decimal degrees.

Init Params:
    (no parameters)

Pattern:
    A decimal number from `-180` to `180`; the fractional part is optional.
    Equivalent regex: `\\-?(?:180(?:\\.0+)?|1[0-7][0-9](?:\\.[0-9]+)?|[1-9]?[0-9](?:\\.[0-9]+)?)`

Example:
    LONGITUDE
    # Matches: "0", "14.42", "-122.4194", "180"
    # Does not match: "180.5", "181", "-181", "14."
"""

