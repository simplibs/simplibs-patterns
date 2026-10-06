# Patterns
from simplibs.patterns.characters import COLON
from simplibs.patterns.text import NON_WHITESPACE_TEXT
from simplibs.patterns.web.pure.URL_SCHEME import URL_SCHEME


URI = URL_SCHEME + COLON + NON_WHITESPACE_TEXT
"""Regex expression matching a URI: a scheme, a colon and non-whitespace text.

Init Params:
    (no parameters)

Pattern:
    A `URL_SCHEME`, `:` and one or more non-whitespace characters.
    Equivalent regex: `[a-zA-Z][a-zA-Z0-9+\\-.]*:\\S+`

Notes:
    Deliberately loose; the part after the colon is not validated.

Example:
    URI
    # Matches: "mailto:a@b.com", "urn:isbn:1", "https://x.org/a"
    # Does not match: "nocolon", "http:", "1http:x"
"""

