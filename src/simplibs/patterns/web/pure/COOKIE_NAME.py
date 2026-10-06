# Patterns
from simplibs.patterns.web.pure.HTTP_HEADER_NAME import HTTP_HEADER_NAME


COOKIE_NAME = HTTP_HEADER_NAME
"""Regex expression matching a cookie name.

Init Params:
    (no parameters)

Pattern:
    Same expression as `HTTP_HEADER_NAME`; the separate name states the intended role.

Notes:
    Cookie names are RFC 6265 tokens — the same character set as header names.

Example:
    COOKIE_NAME
    # Matches: "Content-Type", "X-Request-ID", "Host"
    # Does not match: "Content Type", "Name:", ""
"""

