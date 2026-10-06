from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.presets.quantifiers import BETWEEN
from simplibs.regex.presets.character_classes import ALPHANUMERIC
# Patterns
from simplibs.patterns.characters import (
    DASH,
    DOT,
    UNDERSCORE,
)


USERNAME = ALPHANUMERIC + BETWEEN(CharacterClass(CharacterRange("a", "z"), CharacterRange("A", "Z"), CharacterRange("0", "9"), DOT, UNDERSCORE, DASH), 2, 31)
"""Regex expression matching a user name of 3–32 characters.

Init Params:
    (no parameters)

Pattern:
    A letter or digit, then 2–31 letters, digits or ``. _ -``.
    Equivalent regex: `[a-zA-Z0-9][a-zA-Z0-9._\\-]{2,31}`

Notes:
    Username rules vary between services; this pattern therefore uses a generic 3–32 character range
    rather than platform-specific restrictions.

Example:
    USERNAME
    # Matches: "john_doe", "user.name-1", "abc"
    # Does not match: "ab", "_user", "a b", ""
"""

