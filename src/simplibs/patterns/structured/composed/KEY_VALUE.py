# Patterns
from simplibs.patterns.structured.composed.KEY_VALUE_PAIR import KEY_VALUE_PAIR


KEY_VALUE = KEY_VALUE_PAIR
"""Regex expression matching a key=value pair.

Init Params:
    (no parameters)

Pattern:
    Same expression as `KEY_VALUE_PAIR`; the separate name states the intended role.

Example:
    KEY_VALUE
    # Matches: "name=value", "a=1", "path=/usr/bin"
    # Does not match: "name", "=value", "a= b"
"""

