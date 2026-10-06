# Patterns
from simplibs.patterns.text import NON_WHITESPACE_TEXT
from simplibs.patterns.identifiers import IDENTIFIER
from simplibs.patterns.structured.composed.PAIR_OF import PAIR_OF


KEY_VALUE_PAIR = PAIR_OF(IDENTIFIER, NON_WHITESPACE_TEXT)
"""Regex expression matching a key=value pair.

Init Params:
    (no parameters)

Pattern:
    An `IDENTIFIER`, an equals sign and a value without whitespace.
    Equivalent regex: `[a-zA-Z_][a-zA-Z0-9_]*=\\S+`

Example:
    KEY_VALUE_PAIR
    # Matches: "name=value", "a=1", "path=/usr/bin"
    # Does not match: "name", "=value", "a= b"
"""

