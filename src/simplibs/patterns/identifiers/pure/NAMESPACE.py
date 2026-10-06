from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import DOT
from simplibs.patterns.identifiers.pure.IDENTIFIER import IDENTIFIER


NAMESPACE = IDENTIFIER + ZERO_OR_MORE(DOT + IDENTIFIER)
"""Regex expression matching a namespace path of one or more parts.

Init Params:
    (no parameters)

Pattern:
    An `IDENTIFIER` followed by any number of (dot, `IDENTIFIER`) pairs.
    Equivalent regex: `[a-zA-Z_][a-zA-Z0-9_]*(?:\\.[a-zA-Z_][a-zA-Z0-9_]*)*`

Example:
    NAMESPACE
    # Matches: "std", "std.io", "a.b.c"
    # Does not match: "", "a.", "1a"
"""

