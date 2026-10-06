from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import (
    DASH,
    DOT,
    SINGLE_QUOTE,
    SPACE,
    UNICODE_LETTER,
)


DISPLAY_NAME = UNICODE_LETTER + ZERO_OR_MORE(UNICODE_LETTER | CharacterClass(SPACE, DOT, SINGLE_QUOTE, DASH))
"""Regex expression matching a person's display name.

Init Params:
    (no parameters)

Pattern:
    A letter, then letters, spaces, dots, apostrophes or hyphens (any language).
    Equivalent regex: `[^\\W\\d_](?:[^\\W\\d_]|[ .'\\-])*`

Notes:
    Does not allow digits or emoji.

Example:
    DISPLAY_NAME
    # Matches: "Jan Novák", "Mary-Jane O'Neil", "J. R. R. Tolkien"
    # Does not match: "", "123", "_x"
"""

