# Patterns
from simplibs.patterns.addresses import EMAIL_ADDRESS


RECIPIENT_ADDRESS = EMAIL_ADDRESS
"""Regex expression matching a recipient email address.

Init Params:
    (no parameters)

Pattern:
    Same expression as `EMAIL_ADDRESS`; the separate name states the intended role.

Example:
    RECIPIENT_ADDRESS
    # Matches: "john.doe@example.com", "a+b@sub.example.co.uk"
    # Does not match: "john@localhost", "@example.com", "john@", "a b@x.com"
"""

