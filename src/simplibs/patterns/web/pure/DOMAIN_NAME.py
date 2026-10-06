# Patterns
from simplibs.patterns.web.pure.DOMAIN import DOMAIN


DOMAIN_NAME = DOMAIN
"""Regex expression matching a domain name.

Init Params:
    (no parameters)

Pattern:
    Same expression as `DOMAIN`; the separate name states the intended role.

Example:
    DOMAIN_NAME
    # Matches: "example.com", "sub.example.co.uk"
    # Does not match: "localhost", "example.", "-a.com", ".com"
"""

