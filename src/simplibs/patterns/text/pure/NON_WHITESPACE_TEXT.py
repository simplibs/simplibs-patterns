from simplibs.regex.presets.quantifiers import ONE_OR_MORE
from simplibs.regex.presets.character_types import NON_WHITESPACE


NON_WHITESPACE_TEXT = ONE_OR_MORE(NON_WHITESPACE)
"""Regex expression matching text without any whitespace.

Init Params:
    (no parameters)

Pattern:
    One or more non-whitespace characters.
    Equivalent regex: `\\S+`

Example:
    NON_WHITESPACE_TEXT
    # Matches: "abc", "a-b!"
    # Does not match: "a b", ""
"""

