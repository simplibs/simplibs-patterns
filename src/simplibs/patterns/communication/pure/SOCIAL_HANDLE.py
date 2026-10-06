# Patterns
from simplibs.patterns.communication.pure.USER_HANDLE import USER_HANDLE


SOCIAL_HANDLE = USER_HANDLE
"""Regex expression matching a social media handle.

Init Params:
    (no parameters)

Pattern:
    Same expression as `USER_HANDLE`; the separate name states the intended role.

Example:
    SOCIAL_HANDLE
    # Matches: "@john", "@john_doe1"
    # Does not match: "john", "@", "@1abc"
"""

