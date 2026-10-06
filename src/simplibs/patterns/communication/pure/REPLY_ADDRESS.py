# Patterns
from simplibs.patterns.addresses import EMAIL_ADDRESS


REPLY_ADDRESS = EMAIL_ADDRESS
"""Regex expression matching a reply-to email address.

Init Params:
    (no parameters)

Pattern:
    Same expression as `EMAIL_ADDRESS`; the separate name states the intended role.

Example:
    REPLY_ADDRESS
    # Matches: "john.doe@example.com", "a+b@sub.example.co.uk"
    # Does not match: "john@localhost", "@example.com", "john@", "a b@x.com"
"""

