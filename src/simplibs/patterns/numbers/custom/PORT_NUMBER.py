from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import BETWEEN, EXACTLY
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT, NON_ZERO_DIGIT


PORT_NUMBER = Literal("6553") + CharacterClass(CharacterRange("0", "5")) | Literal("655") + CharacterClass(CharacterRange("0", "2")) + DECIMAL_DIGIT | Literal("65") + CharacterClass(CharacterRange("0", "4")) + EXACTLY(DECIMAL_DIGIT, 2) | Literal("6") + CharacterClass(CharacterRange("0", "4")) + EXACTLY(DECIMAL_DIGIT, 3) | CharacterClass(CharacterRange("1", "5")) + EXACTLY(DECIMAL_DIGIT, 4) | NON_ZERO_DIGIT + BETWEEN(DECIMAL_DIGIT, 0, 3) | Literal("0")
"""Regex expression matching a network port number.

Init Params:
    (no parameters)

Pattern:
    Any whole number `0`–`65535` without leading zeros.
    Equivalent regex: `6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{0,3}|0`

Example:
    PORT_NUMBER
    # Matches: "0", "80", "8080", "65535"
    # Does not match: "65536", "099", "-1", ""
"""

