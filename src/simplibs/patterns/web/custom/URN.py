from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
from simplibs.regex.presets.character_classes import ALPHANUMERIC
# Patterns
from simplibs.patterns.characters import COLON, DASH
from simplibs.patterns.text import NON_WHITESPACE_TEXT


URN = Literal("urn:") + ALPHANUMERIC + ZERO_OR_MORE(CharacterClass(CharacterRange("a", "z"), CharacterRange("A", "Z"), CharacterRange("0", "9"), DASH)) + COLON + NON_WHITESPACE_TEXT
"""Regex expression matching a URN.

Init Params:
    (no parameters)

Pattern:
    `urn:`, a namespace identifier, a colon and a non-whitespace specific part.
    Equivalent regex: `urn:[a-zA-Z0-9][a-zA-Z0-9\\-]*:\\S+`

Example:
    URN
    # Matches: "urn:isbn:0451450523", "urn:uuid:6e8bc430-9c3a-11d9-9669-0800200c9a66"
    # Does not match: "urn:", "isbn:123", "urn:x"
"""

