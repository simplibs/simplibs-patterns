from simplibs.regex.presets.quantifiers import ONE_OR_MORE
# Patterns
from simplibs.patterns.characters import DOT
from simplibs.patterns.identifiers.pure.IDENTIFIER import IDENTIFIER


QUALIFIED_IDENTIFIER = IDENTIFIER + ONE_OR_MORE(DOT + IDENTIFIER)
"""Regex expression matching a dotted identifier with at least two parts.

Init Params:
    (no parameters)

Pattern:
    An `IDENTIFIER` followed by one or more (dot, `IDENTIFIER`) pairs.
    Equivalent regex: `[a-zA-Z_][a-zA-Z0-9_]*(?:\\.[a-zA-Z_][a-zA-Z0-9_]*)+`

Notes:
    Needs at least one dot; use `NAMESPACE` when a single part is also fine.

Example:
    QUALIFIED_IDENTIFIER
    # Matches: "os.path", "a.b.c"
    # Does not match: "os", "os.", "a..b", ".a"
"""

