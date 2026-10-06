# Patterns
from simplibs.patterns.addresses import EMAIL_ADDRESS


EMAIL = EMAIL_ADDRESS
"""Regex expression matching an email address.

Init Params:
    (no parameters)

Pattern:
    Same expression as `EMAIL_ADDRESS`; the separate name states the intended role.

Notes:
    `EMAIL_ADDRESS` lives in the `addresses` domain.

Example:
    EMAIL
    # Matches: "john.doe@example.com", "a+b@sub.example.co.uk"
    # Does not match: "john@localhost", "@example.com", "john@", "a b@x.com"
"""

