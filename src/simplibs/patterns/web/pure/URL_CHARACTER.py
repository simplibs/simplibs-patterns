from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.characters import (
    AMPERSAND,
    ASTERISK,
    AT_SIGN,
    COLON,
    COMMA,
    DASH,
    DOLLAR,
    DOT,
    EQUALS,
    PERCENT,
    PLUS_SIGN,
    SEMICOLON,
    SINGLE_QUOTE,
    SLASH,
    TILDE,
    UNDERSCORE,
)


URL_CHARACTER = CharacterClass(CharacterRange("a", "z"), CharacterRange("A", "Z"), CharacterRange("0", "9"), DASH, DOT, UNDERSCORE, TILDE, PERCENT, SLASH, COLON, AT_SIGN, EQUALS, Literal("!"), DOLLAR, AMPERSAND, SINGLE_QUOTE, Literal("("), Literal(")"), ASTERISK, PLUS_SIGN, COMMA, SEMICOLON,)
"""Regex expression matching a character allowed in a URL path, query or fragment.

Init Params:
    (no parameters)

Pattern:
    Letters, digits and ``- . _ ~ % / : @ = ! $ & ' ( ) * + , ;``. Excludes `?`, `#` and whitespace.
    Equivalent regex: `[a-zA-Z0-9\\-._~%/:@=!$&'()*+,;]`

Example:
    URL_CHARACTER
    # Matches: "a", "/", "%", "~"
    # Does not match: "?", "#", " ", "ab"
"""

