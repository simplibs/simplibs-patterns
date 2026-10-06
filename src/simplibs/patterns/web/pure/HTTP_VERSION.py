from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT, DOT


HTTP_VERSION = Literal("HTTP/") + (DECIMAL_DIGIT + DOT + DECIMAL_DIGIT | CharacterClass(Literal("2"), Literal("3")))
"""Regex expression matching an HTTP version.

Init Params:
    (no parameters)

Pattern:
    `HTTP/` followed by `d.d` (e.g. `1.1`) or `2` / `3`.
    Equivalent regex: `HTTP/(?:[0-9]\\.[0-9]|[23])`

Example:
    HTTP_VERSION
    # Matches: "HTTP/1.1", "HTTP/2", "HTTP/3"
    # Does not match: "HTTP/", "HTTP 1.1", "HTTP/1"
"""

