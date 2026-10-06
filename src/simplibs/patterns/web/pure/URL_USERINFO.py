from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.presets.quantifiers import ONE_OR_MORE
from simplibs.regex.presets.character_types import WORD_CHARACTER
# Patterns
from simplibs.patterns.characters import (
    COLON,
    DASH,
    DOT,
    PERCENT,
    TILDE,
)


URL_USERINFO = ONE_OR_MORE(CharacterClass(WORD_CHARACTER, DASH, DOT, COLON, TILDE, PERCENT))
"""Regex expression matching the user information part of a URL.

Init Params:
    (no parameters)

Pattern:
    Word characters, `-`, `.`, `:`, `~` or `%`, e.g. `user` or `user:password`.
    Equivalent regex: `[\\w\\-.:~%]+`

Example:
    URL_USERINFO
    # Matches: "user", "user:pass"
    # Does not match: "", "a@b", "a b"
"""

