from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import SINGLE_QUOTE


SINGLE_QUOTED_TEXT = SINGLE_QUOTE + ZERO_OR_MORE(CharacterClass(SINGLE_QUOTE, negate=True)) + SINGLE_QUOTE
"""Regex expression matching text in single quotes.

Init Params:
    (no parameters)

Pattern:
    A `'`, any characters that are not `'`, and a closing `'`.
    Equivalent regex: `'[^']*'`

Notes:
    No escape handling: a quote inside the text always ends it.

Example:
    SINGLE_QUOTED_TEXT
    # Matches: "'hello'", "''"
    # Does not match: "hello", "'a'b'", "'open"
"""

