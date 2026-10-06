from simplibs.regex.presets.quantifiers import ONE_OR_MORE
from simplibs.regex.presets.character_types import WHITESPACE


WHITESPACE_TEXT = ONE_OR_MORE(WHITESPACE)
"""Regex expression matching text made only of whitespace.

Init Params:
    (no parameters)

Pattern:
    One or more whitespace characters.
    Equivalent regex: `\\s+`

Example:
    WHITESPACE_TEXT
    # Matches: " ", "\\t\\n "
    # Does not match: "a", "", " a"
"""

