# Patterns
from simplibs.patterns.text.pure.WORD import WORD


SINGLE_WORD = WORD
"""Regex expression matching a single word.

Init Params:
    (no parameters)

Pattern:
    Same expression as `WORD`; the separate name states the intended role.

Example:
    SINGLE_WORD
    # Matches: "Python", "snake_case", "abc123"
    # Does not match: "two words", "", "a-b"
"""

