from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
from simplibs.regex.presets.character_types import WORD_CHARACTER
# Patterns
from simplibs.patterns.characters import (
    COLON,
    DASH,
    DOT,
    EQUALS,
    PERCENT,
    PLUS_SIGN,
    SLASH,
    TILDE,
)


COOKIE_VALUE = ZERO_OR_MORE(CharacterClass(WORD_CHARACTER, DASH, DOT, TILDE, PERCENT, PLUS_SIGN, SLASH, EQUALS, COLON))
"""Regex expression matching a cookie value.

Init Params:
    (no parameters)

Pattern:
    Word characters and ``- . ~ % + / = :``; may be empty.
    Equivalent regex: `[\\w\\-.~%+/=:]*`

Notes:
    The pattern accepts a conservative subset of the RFC 6265 cookie-octet characters.

Example:
    COOKIE_VALUE
    # Matches: "abc123", "a%20b", "dGVzdA==", ""
    # Does not match: "a b", "a;b", "a,b"
"""

