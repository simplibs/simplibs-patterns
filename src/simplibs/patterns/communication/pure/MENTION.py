# Patterns
from simplibs.patterns.communication.pure.USER_HANDLE import USER_HANDLE


MENTION = USER_HANDLE
"""Regex expression matching a mention.

Init Params:
    (no parameters)

Pattern:
    Same expression as `USER_HANDLE`; the separate name states the intended role.

Example:
    MENTION
    # Matches: "@john", "@john_doe1"
    # Does not match: "john", "@", "@1abc"
"""

