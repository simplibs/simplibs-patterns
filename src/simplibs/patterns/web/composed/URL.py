from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.web.pure.URL_SCHEME import URL_SCHEME
from simplibs.patterns.web.composed.URL_LOCATION import URL_LOCATION


URL = URL_SCHEME + Literal("://") + URL_LOCATION
"""Regex expression matching a URL with a scheme and ://.

Init Params:
    (no parameters)

Pattern:
    A `URL_SCHEME`, `://` and a `URL_LOCATION`.

Notes:
    URLs without `//` (mailto:, urn:) are `URI`s, not `URL`s.

Example:
    URL
    # Matches: "https://example.com/path?q=1#frag", "ftp://files.example.org", "git+ssh://user@host:22/repo.git"
    # Does not match: "example.com", "http:/example.com", "http://"
"""

