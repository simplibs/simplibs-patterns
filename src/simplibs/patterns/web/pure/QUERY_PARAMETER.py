from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.presets.quantifiers import ONE_OR_MORE, ZERO_OR_MORE
from simplibs.regex.presets.character_types import WORD_CHARACTER
# Patterns
from simplibs.patterns.characters import (
    AT_SIGN,
    COLON,
    COMMA,
    DASH,
    DOT,
    EQUALS,
    PERCENT,
    PLUS_SIGN,
    SLASH,
    TILDE,
)


QUERY_PARAMETER = ONE_OR_MORE(CharacterClass(WORD_CHARACTER, DASH, DOT, TILDE, PERCENT, PLUS_SIGN)) + EQUALS + ZERO_OR_MORE(CharacterClass(WORD_CHARACTER, DASH, DOT, TILDE, PERCENT, PLUS_SIGN, COMMA, COLON, AT_SIGN, SLASH))
"""Regex expression matching a single key=value query parameter.

Init Params:
    (no parameters)

Pattern:
    A key, `=` and a (possibly empty) value; neither contains `&` or `=`.
    Equivalent regex: `[\\w\\-.~%+]+=[\\w\\-.~%+,:@/]*`

Example:
    QUERY_PARAMETER
    # Matches: "page=2", "q=hello+world", "flag="
    # Does not match: "=x", "a b=1", "a=b&c=d"
"""

