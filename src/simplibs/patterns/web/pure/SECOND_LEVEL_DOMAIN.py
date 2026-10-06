# Patterns
from simplibs.patterns.web.pure.DOMAIN_LABEL import DOMAIN_LABEL


SECOND_LEVEL_DOMAIN = DOMAIN_LABEL
"""Regex expression matching a second-level domain label.

Init Params:
    (no parameters)

Pattern:
    Same expression as `DOMAIN_LABEL`; the separate name states the intended role.

Example:
    SECOND_LEVEL_DOMAIN
    # Matches: "example", "a", "my-site", "a1"
    # Does not match: "-a", "a-", "", "a_b"
"""

