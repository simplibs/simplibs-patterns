from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.presets.quantifiers import BETWEEN
from simplibs.regex.presets.character_classes import ALPHANUMERIC
# Patterns
from simplibs.patterns.characters import DASH, SPACE


POSTAL_CODE = ALPHANUMERIC + BETWEEN(CharacterClass(CharacterRange("a", "z"), CharacterRange("A", "Z"), CharacterRange("0", "9"), SPACE, DASH), 1, 8) + ALPHANUMERIC
"""Regex expression matching a postal code in a generic international form.

Init Params:
    (no parameters)

Pattern:
    3–10 characters: letters, digits, spaces or hyphens, starting and ending with a letter or digit.
    Equivalent regex: `[a-zA-Z0-9][a-zA-Z0-9 \\-]{1,8}[a-zA-Z0-9]`

Notes:
    Generic; it cannot reject malformed codes of a particular country.

    Country-specific postal-code formats are not enforced; the pattern is intended as a broad
    international fallback.

Example:
    POSTAL_CODE
    # Matches: "110 00", "SW1A 1AA", "90210", "10115"
    # Does not match: "1", "12", "-1234", "12 "
"""
