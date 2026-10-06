from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.web.composed.URL_LOCATION import URL_LOCATION


HTTPS_URL = Literal("https://") + URL_LOCATION
"""Regex expression matching an https:// URL.

Init Params:
    (no parameters)

Pattern:
    `https://` followed by a `URL_LOCATION`.

Example:
    HTTPS_URL
    # Matches: "https://example.com", "https://example.com/a/b?c=d#e"
    # Does not match: "http://example.com", "example.com"
"""

