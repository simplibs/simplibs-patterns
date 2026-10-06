from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.presets.character_types import DIGIT, NON_WORD_CHARACTER
# Patterns
from simplibs.patterns.characters.pure.UNDERSCORE import UNDERSCORE


UNICODE_LETTER = CharacterClass(NON_WORD_CHARACTER, DIGIT, UNDERSCORE, negate=True)
"""Regex expression matching a single letter of any language.

Init Params:
    (no parameters)

Pattern:
    Matches one Unicode letter: any word character (`\\w`) that is neither a digit nor an underscore (`[^\\W\\d_]`).
    Equivalent regex: `[^\\W\\d_]`

Notes:
    Use this instead of `LETTER` for names, addresses and other human text.

Example:
    UNICODE_LETTER
    # Matches: "a", "é", "ž", "Ω"
    # Does not match: "1", "_", " ", "ab"
"""

