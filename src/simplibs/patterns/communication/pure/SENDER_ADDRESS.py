# Patterns
from simplibs.patterns.addresses import EMAIL_ADDRESS


SENDER_ADDRESS = EMAIL_ADDRESS
"""Regex expression matching a sender email address.

Init Params:
    (no parameters)

Pattern:
    Same expression as `EMAIL_ADDRESS`; the separate name states the intended role.

Example:
    SENDER_ADDRESS
    # Matches: "john.doe@example.com", "a+b@sub.example.co.uk"
    # Does not match: "john@localhost", "@example.com", "john@", "a b@x.com"
"""

