# Patterns
from simplibs.patterns.identifiers.custom.TAG_NAME import TAG_NAME


ELEMENT_NAME = TAG_NAME
"""Regex expression matching a markup element name.

Init Params:
    (no parameters)

Pattern:
    Same expression as `TAG_NAME`; the separate name states the intended role.

Example:
    ELEMENT_NAME
    # Matches: "div", "h1", "my-element"
    # Does not match: "1div", "-x", "", "a_b"
"""

