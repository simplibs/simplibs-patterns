from simplibs.regex.presets.quantifiers import ONE_OR_MORE
from simplibs.regex.presets.character_types import WORD_CHARACTER


WORD = ONE_OR_MORE(WORD_CHARACTER)
"""Regex expression matching a single word.

Init Params:
    (no parameters)

Pattern:
    One or more word characters (letters, digits, underscore) without any separator.
    Equivalent regex: `\\w+`

Notes:
    A whole word, unlike `WORD_CHARACTER` (one character) and unlike `simplibs.regex` `WORD` (`\\w`, one character).

Example:
    WORD
    # Matches: "Python", "snake_case", "abc123"
    # Does not match: "two words", "", "a-b"
"""

