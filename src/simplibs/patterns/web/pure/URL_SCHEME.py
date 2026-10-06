from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
from simplibs.regex.presets.character_classes import LETTER
# Patterns
from simplibs.patterns.characters import (
    DASH,
    DOT,
    PLUS_SIGN,
)


URL_SCHEME = LETTER + ZERO_OR_MORE(CharacterClass(CharacterRange("a", "z"), CharacterRange("A", "Z"), CharacterRange("0", "9"), PLUS_SIGN, DASH, DOT))
"""Regex expression matching a URL scheme.

Init Params:
    (no parameters)

Pattern:
    A letter followed by letters, digits, `+`, `-` or `.`.
    Equivalent regex: `[a-zA-Z][a-zA-Z0-9+\\-.]*`

Example:
    URL_SCHEME
    # Matches: "http", "git+ssh", "a1"
    # Does not match: "1http", "-x", ""
"""

