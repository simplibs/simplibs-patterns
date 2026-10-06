from simplibs.regex.presets.quantifiers import ONE_OR_MORE
# Patterns
from simplibs.patterns.characters import DOT
from simplibs.patterns.web.pure.DOMAIN_LABEL import DOMAIN_LABEL


DOMAIN = DOMAIN_LABEL + ONE_OR_MORE(DOT + DOMAIN_LABEL)
"""Regex expression matching a domain name with at least two labels.

Init Params:
    (no parameters)

Pattern:
    A `DOMAIN_LABEL` followed by one or more (dot, `DOMAIN_LABEL`) pairs.
    Equivalent regex: `[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9\\-]{0,61}[a-zA-Z0-9])?)+`

Example:
    DOMAIN
    # Matches: "example.com", "sub.example.co.uk"
    # Does not match: "localhost", "example.", "-a.com", ".com"
"""

