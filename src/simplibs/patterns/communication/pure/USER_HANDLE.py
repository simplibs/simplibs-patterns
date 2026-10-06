# Patterns
from simplibs.patterns.characters import AT_SIGN
from simplibs.patterns.identifiers import IDENTIFIER


USER_HANDLE = AT_SIGN + IDENTIFIER
"""Regex expression matching a user handle such as @name.

Init Params:
    (no parameters)

Pattern:
    `@` followed by an `IDENTIFIER`.
    Equivalent regex: `@[a-zA-Z_][a-zA-Z0-9_]*`

Notes:
    The handle syntax is based on a standard programming identifier, so dots and hyphens are not
    accepted.

Example:
    USER_HANDLE
    # Matches: "@john", "@john_doe1"
    # Does not match: "john", "@", "@1abc"
"""
