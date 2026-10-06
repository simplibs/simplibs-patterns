from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import DOUBLE_QUOTE


DOUBLE_QUOTED_TEXT = DOUBLE_QUOTE + ZERO_OR_MORE(CharacterClass(DOUBLE_QUOTE, negate=True)) + DOUBLE_QUOTE
"""Regex expression matching text in double quotes.

Init Params:
    (no parameters)

Pattern:
    A `"`, any characters that are not `"`, and a closing `"`.
    Equivalent regex: `"[^"]*"`

Notes:
    No escape handling: a quote inside the text always ends it.

Example:
    DOUBLE_QUOTED_TEXT
    # Matches: '"hello"', '""'
    # Does not match: "hello", '"a"b"', '"open'
"""

