from simplibs.regex.presets.quantifiers import ONE_OR_MORE, ZERO_OR_MORE
from simplibs.regex.presets.character_types import WHITESPACE
# Patterns
from simplibs.patterns.text.pure.WORD import WORD


WORDS = WORD + ZERO_OR_MORE(ONE_OR_MORE(WHITESPACE) + WORD)
"""Regex expression matching one or more words separated by whitespace.

Init Params:
    (no parameters)

Pattern:
    A `WORD`, then any number of (whitespace, `WORD`) pairs.
    Equivalent regex: `\\w+(?:\\s+\\w+)*`

Example:
    WORDS
    # Matches: "hello", "hello big   world", "a\\tb"
    # Does not match: "", "hello,world", " hello"
"""

