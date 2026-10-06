# Patterns
from simplibs.patterns.web.composed.HTTPS_URL import HTTPS_URL
from simplibs.patterns.web.composed.HTTP_URL import HTTP_URL


WEB_ADDRESS = HTTPS_URL | HTTP_URL
"""Regex expression matching a web address (http or https).

Init Params:
    (no parameters)

Pattern:
    `HTTPS_URL` or `HTTP_URL`.

Example:
    WEB_ADDRESS
    # Matches: "https://example.com", "http://example.com/a"
    # Does not match: "ftp://example.com", "example.com"
"""

