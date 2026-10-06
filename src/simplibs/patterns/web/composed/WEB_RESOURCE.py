# Patterns
from simplibs.patterns.web.composed.URL import URL


WEB_RESOURCE = URL
"""Regex expression matching a web resource.

Init Params:
    (no parameters)

Pattern:
    Same expression as `URL`; the separate name states the intended role.

Notes:
    Any scheme; for http(s) only use `WEB_ADDRESS`.

Example:
    WEB_RESOURCE
    # Matches: "https://example.com/path?q=1#frag", "ftp://files.example.org", "git+ssh://user@host:22/repo.git"
    # Does not match: "example.com", "http:/example.com", "http://"
"""

