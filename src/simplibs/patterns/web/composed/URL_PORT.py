# Patterns
from simplibs.patterns.characters import COLON
from simplibs.patterns.numbers import PORT_NUMBER


URL_PORT = COLON + PORT_NUMBER
"""Regex expression matching the port part of a URL.

Init Params:
    (no parameters)

Pattern:
    A colon followed by a `PORT_NUMBER`.
    Equivalent regex: `:(?:6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{0,3}|0)`

Example:
    URL_PORT
    # Matches: ":80", ":8080", ":65535"
    # Does not match: "80", ":65536", ":"
"""

