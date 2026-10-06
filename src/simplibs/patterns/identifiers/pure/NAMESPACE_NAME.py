# Patterns
from simplibs.patterns.identifiers.pure.NAMESPACE import NAMESPACE


NAMESPACE_NAME = NAMESPACE
"""Regex expression matching a namespace name.

Init Params:
    (no parameters)

Pattern:
    Same expression as `NAMESPACE`; the separate name states the intended role.

Example:
    NAMESPACE_NAME
    # Matches: "std", "std.io", "a.b.c"
    # Does not match: "", "a.", "1a"
"""

