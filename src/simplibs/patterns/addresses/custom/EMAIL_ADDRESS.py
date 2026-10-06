# Patterns
from simplibs.patterns.characters import AT_SIGN
from simplibs.patterns.web import DOMAIN
from simplibs.patterns.addresses.pure.EMAIL_LOCAL_PART import EMAIL_LOCAL_PART


EMAIL_ADDRESS = EMAIL_LOCAL_PART + AT_SIGN + DOMAIN
"""Regex expression matching an email address.

Init Params:
    (no parameters)

Pattern:
    An `EMAIL_LOCAL_PART`, `@` and a `DOMAIN` (at least two labels).

Notes:
    A practical subset of RFC 5322: no quoted local parts, no comments, no IP-literal domains.

    Unicode local parts and internationalised domain names are not supported; the pattern matches
    ASCII email addresses.

Example:
    EMAIL_ADDRESS
    # Matches: "john.doe@example.com", "a+b@sub.example.co.uk"
    # Does not match: "john@localhost", "@example.com", "john@", "a b@x.com"
"""

