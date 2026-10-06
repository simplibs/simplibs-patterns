from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.presets.any_character import ANY
from simplibs.regex.presets.lookaround import LOOKAHEAD
from simplibs.regex.presets.quantifiers import ONE_OR_MORE, ZERO_OR_MORE
from simplibs.regex.presets.character_types import DIGIT
from simplibs.regex.presets.character_types import WORD_CHARACTER
# Patterns
from simplibs.patterns.characters import (
    COMMA,
    DASH,
    DOT,
    SINGLE_QUOTE,
    SLASH,
    SPACE,
    UNICODE_LETTER,
)


STREET_ADDRESS = LOOKAHEAD(ZERO_OR_MORE(ANY) + DIGIT) + LOOKAHEAD(ZERO_OR_MORE(ANY) + UNICODE_LETTER) + ONE_OR_MORE(CharacterClass(WORD_CHARACTER, SPACE, DOT, COMMA, SINGLE_QUOTE, DASH, SLASH))
"""Regex expression matching a street address line in a lenient form.

Init Params:
    (no parameters)

Pattern:
    Text of word characters, spaces and ``. , ' - /`` that contains at least one letter (any language) and at least one digit.
    Equivalent regex: `(?=.*\\d)(?=.*[^\\W\\d_])[\\w .,'\\-/]+`

Notes:
    Locale-independent heuristic: it recognises the shape 'letters + a number', not a real address grammar.

    The pattern recognises the general shape of an address line rather than a locale-specific
    address grammar.

Example:
    STREET_ADDRESS
    # Matches: "Václavské náměstí 1", "221B Baker Street", "5 Main St.", "Hlavní 12/3"
    # Does not match: "Main Street", "12345", "", "12 @ home"
"""
