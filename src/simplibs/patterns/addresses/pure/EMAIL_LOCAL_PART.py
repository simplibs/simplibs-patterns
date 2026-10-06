from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.presets.quantifiers import ONE_OR_MORE
# Patterns
from simplibs.patterns.characters import (
    DASH,
    DOT,
    PERCENT,
    PLUS_SIGN,
    UNDERSCORE,
)


EMAIL_LOCAL_PART = ONE_OR_MORE(CharacterClass(CharacterRange("a", "z"), CharacterRange("A", "Z"), CharacterRange("0", "9"), DOT, UNDERSCORE, PERCENT, PLUS_SIGN, DASH))
"""Regex expression matching the part of an email address before the @.

Init Params:
    (no parameters)

Pattern:
    One or more letters, digits or ``. _ % + -``.
    Equivalent regex: `[a-zA-Z0-9._%+\\-]+`

Example:
    EMAIL_LOCAL_PART
    # Matches: "john.doe", "user+tag", "a"
    # Does not match: "a@b", "", "a b"
"""

