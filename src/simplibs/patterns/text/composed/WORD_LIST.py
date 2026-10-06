# Patterns
from simplibs.patterns.text.composed.WORDS import WORDS


WORD_LIST = WORDS
"""Regex expression matching a list of words.

Init Params:
    (no parameters)

Pattern:
    Same expression as `WORDS`; the separate name states the intended role.

Notes:
    Separated by whitespace; for comma-separated words see `COMMA_SEPARATED_TEXT`.

Example:
    WORD_LIST
    # Matches: "hello", "hello big   world", "a\\tb"
    # Does not match: "", "hello,world", " hello"
"""

