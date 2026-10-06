from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import DOT
from simplibs.patterns.web.pure.DOMAIN_LABEL import DOMAIN_LABEL


HOSTNAME = DOMAIN_LABEL + ZERO_OR_MORE(DOT + DOMAIN_LABEL)
"""Regex expression matching a host name of one or more labels.

Init Params:
    (no parameters)

Pattern:
    A `DOMAIN_LABEL` followed by any number of (dot, `DOMAIN_LABEL`) pairs.
    Equivalent regex: `[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?)*`

Example:
    HOSTNAME
    # Matches: "localhost", "example.com", "my-server.local"
    # Does not match: "-a", "a..b", ""
"""

