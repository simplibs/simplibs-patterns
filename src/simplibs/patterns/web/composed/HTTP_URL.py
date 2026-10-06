from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.web.composed.URL_LOCATION import URL_LOCATION


HTTP_URL = Literal("http://") + URL_LOCATION
"""Regex expression matching an http:// URL.

Init Params:
    (no parameters)

Pattern:
    `http://` followed by a `URL_LOCATION`.

Example:
    HTTP_URL
    # Matches: "http://example.com", "http://localhost:8080/a?b=1"
    # Does not match: "https://example.com", "example.com"
"""

