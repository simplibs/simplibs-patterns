# Patterns
from simplibs.patterns.web.composed.URL_PATH import URL_PATH


ENDPOINT = URL_PATH
"""Regex expression matching an endpoint path.

Init Params:
    (no parameters)

Pattern:
    Same expression as `URL_PATH`; the separate name states the intended role.

Example:
    ENDPOINT
    # Matches: "/", "/a/b.html", "/path/to/file"
    # Does not match: "a/b", "/a?b", "/a b"
"""

