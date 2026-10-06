# Patterns
from simplibs.patterns.text.pure.NON_EMPTY_TEXT import NON_EMPTY_TEXT


CHARACTERS = NON_EMPTY_TEXT
"""Regex expression matching one or more characters.

Init Params:
    (no parameters)

Pattern:
    Same expression as `NON_EMPTY_TEXT`; the separate name states the intended role.

Example:
    CHARACTERS
    # Matches: "a", "Hello, world!"
    # Does not match: ""
"""

