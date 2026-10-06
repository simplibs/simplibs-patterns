# Patterns
from simplibs.patterns.characters.pure.PUNCTUATION import PUNCTUATION
from simplibs.patterns.characters.pure.SYMBOL import SYMBOL


SPECIAL_CHARACTER = PUNCTUATION | SYMBOL
"""Regex expression matching a single punctuation or symbol character.

Init Params:
    (no parameters)

Pattern:
    `PUNCTUATION` or `SYMBOL` — any printable ASCII character that is neither a letter, a digit nor a space.
    Equivalent regex: `[!"#%&'()*,\\-./:;?@[\\\\\\]_{}]|[$+<=>\\^`|~]`

Example:
    SPECIAL_CHARACTER
    # Matches: "!", "$", "~"
    # Does not match: "a", "5", " "
"""

