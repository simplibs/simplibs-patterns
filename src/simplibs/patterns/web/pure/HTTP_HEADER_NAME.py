from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import ONE_OR_MORE
# Patterns
from simplibs.patterns.characters import (
    AMPERSAND,
    ASTERISK,
    CARET,
    DASH,
    DOLLAR,
    DOT,
    HASH_SIGN,
    PERCENT,
    PIPE,
    PLUS_SIGN,
    SINGLE_QUOTE,
    TILDE,
    UNDERSCORE,
)


HTTP_HEADER_NAME = ONE_OR_MORE(CharacterClass(CharacterRange("a", "z"), CharacterRange("A", "Z"), CharacterRange("0", "9"), Literal("!"), HASH_SIGN, DOLLAR, PERCENT, AMPERSAND, SINGLE_QUOTE, ASTERISK, PLUS_SIGN, DASH, DOT, CARET, UNDERSCORE, Literal("`"), PIPE, TILDE))
"""Regex expression matching an HTTP header field name.

Init Params:
    (no parameters)

Pattern:
    One or more token characters (letters, digits and ``! # $ % & ' * + - . ^ _ ` | ~``).
    Equivalent regex: `[a-zA-Z0-9!#$%&'*+\\-.\\^_`|~]+`

Example:
    HTTP_HEADER_NAME
    # Matches: "Content-Type", "X-Request-ID", "Host"
    # Does not match: "Content Type", "Name:", ""
"""

