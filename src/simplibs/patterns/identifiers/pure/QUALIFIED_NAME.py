# Patterns
from simplibs.patterns.identifiers.pure.QUALIFIED_IDENTIFIER import QUALIFIED_IDENTIFIER


QUALIFIED_NAME = QUALIFIED_IDENTIFIER
"""Regex expression matching a qualified name.

Init Params:
    (no parameters)

Pattern:
    Same expression as `QUALIFIED_IDENTIFIER`; the separate name states the intended role.

Example:
    QUALIFIED_NAME
    # Matches: "os.path", "a.b.c"
    # Does not match: "os", "os.", "a..b", ".a"
"""

