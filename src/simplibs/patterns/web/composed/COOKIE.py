# Patterns
from simplibs.patterns.characters import EQUALS
from simplibs.patterns.web.pure.COOKIE_NAME import COOKIE_NAME
from simplibs.patterns.web.pure.COOKIE_VALUE import COOKIE_VALUE


COOKIE = COOKIE_NAME + EQUALS + COOKIE_VALUE
"""Regex expression matching a cookie pair.

Init Params:
    (no parameters)

Pattern:
    A `COOKIE_NAME`, `=` and a `COOKIE_VALUE`.
    Equivalent regex: `[a-zA-Z0-9!#$%&'*+\\-.\\^_`|~]+=[\\w\\-.~%+/=:]*`

Example:
    COOKIE
    # Matches: "session=abc123", "flag="
    # Does not match: "=x", "name", "a b=c"
"""

