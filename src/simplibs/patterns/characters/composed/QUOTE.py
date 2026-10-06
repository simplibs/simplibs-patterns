from simplibs.regex.elements.CharacterClass import CharacterClass
# Patterns
from simplibs.patterns.characters.pure.DOUBLE_QUOTE import DOUBLE_QUOTE
from simplibs.patterns.characters.pure.SINGLE_QUOTE import SINGLE_QUOTE


QUOTE = CharacterClass(SINGLE_QUOTE, DOUBLE_QUOTE)
"""Regex expression matching a single quote character of either kind.

Init Params:
    (no parameters)

Pattern:
    `SINGLE_QUOTE` or `DOUBLE_QUOTE` — one of `'` and `"`.
    Equivalent regex: `['"]`

Example:
    QUOTE
    # Matches: "'", '"'
    # Does not match: "a", "''"
"""

