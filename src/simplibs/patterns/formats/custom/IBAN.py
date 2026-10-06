from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.presets.quantifiers import BETWEEN, EXACTLY
from simplibs.regex.presets.character_classes import UPPERCASE_LETTER
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT


IBAN = EXACTLY(UPPERCASE_LETTER, 2) + EXACTLY(DECIMAL_DIGIT, 2) + BETWEEN(CharacterClass(CharacterRange("A", "Z"), CharacterRange("0", "9")), 11, 30)
"""Regex expression matching an IBAN without spaces.

Init Params:
    (no parameters)

Pattern:
    Two letters (country), two check digits and 11–30 uppercase letters or digits.
    Equivalent regex: `[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}`

Notes:
    Country-specific lengths and the mod-97 checksum are not verified.

    Country-specific IBAN lengths and the mod-97 checksum are not validated; the pattern uses a
    universal structural form.

Example:
    IBAN
    # Matches: "CZ6508000000192000145399", "GB82WEST12345698765432"
    # Does not match: "cz6508000000192000145399", "CZ65", "CZ65 0800 0000 1920 0014 5399"
"""

