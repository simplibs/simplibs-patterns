from simplibs.regex.presets.quantifiers import ONE_OR_MORE
# Patterns
from simplibs.patterns.characters import DOT
from simplibs.patterns.numbers import INTEGER


VERSION = INTEGER + ONE_OR_MORE(DOT + INTEGER)
"""Regex expression matching a dotted version number.

Init Params:
    (no parameters)

Pattern:
    An `INTEGER` followed by one or more (dot, `INTEGER`) pairs.
    Equivalent regex: `[0-9]+(?:\\.[0-9]+)+`

Example:
    VERSION
    # Matches: "1.2", "10.0.3", "2026.9.30"
    # Does not match: "1", "1.", "v1.2", "1.a"
"""

