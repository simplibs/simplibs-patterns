from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
# Patterns
from simplibs.patterns.identifiers.pure.IDENTIFIER_CHARACTER import IDENTIFIER_CHARACTER
from simplibs.patterns.identifiers.pure.IDENTIFIER_START_CHARACTER import IDENTIFIER_START_CHARACTER


IDENTIFIER = IDENTIFIER_START_CHARACTER + ZERO_OR_MORE(IDENTIFIER_CHARACTER)
"""Regex expression matching a language-neutral identifier.

Init Params:
    (no parameters)

Pattern:
    A letter or underscore, followed by any number of letters, digits or underscores.
    Equivalent regex: `[a-zA-Z_][a-zA-Z0-9_]*`

Notes:
    ASCII only. Naming conventions (snake_case, PascalCase, UPPER_CASE) are not enforced.

Example:
    IDENTIFIER
    # Matches: "name", "_private", "snake_case_2", "X"
    # Does not match: "2fast", "with-dash", "", "a b"
"""

