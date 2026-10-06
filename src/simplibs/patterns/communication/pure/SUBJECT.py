# Patterns
from simplibs.patterns.text import NON_EMPTY_TEXT


SUBJECT = NON_EMPTY_TEXT
"""Regex expression matching a message subject.

Init Params:
    (no parameters)

Pattern:
    Same expression as `NON_EMPTY_TEXT`; the separate name states the intended role.

Notes:
    One non-empty line of text.

Example:
    SUBJECT
    # Matches: "a", "Hello, world!"
    # Does not match: ""
"""

