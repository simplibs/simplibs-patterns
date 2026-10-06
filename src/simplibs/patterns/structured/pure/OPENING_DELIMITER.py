from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal


OPENING_DELIMITER = CharacterClass(Literal("("), Literal("["), Literal("{"), Literal("<"))
"""Regex expression matching an opening bracket.

Init Params:
    (no parameters)

Pattern:
    One of `(`, `[`, `{`, `<`.
    Equivalent regex: `[([{<]`

Example:
    OPENING_DELIMITER
    # Matches: "(", "[", "{", "<"
    # Does not match: ")", "a", "(["
"""

