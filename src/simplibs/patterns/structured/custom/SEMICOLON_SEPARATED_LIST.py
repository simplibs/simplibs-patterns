from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.presets.quantifiers import ONE_OR_MORE
# Patterns
from simplibs.patterns.characters import SEMICOLON
from simplibs.patterns.structured.composed.LIST_OF import LIST_OF


SEMICOLON_SEPARATED_LIST = LIST_OF(ONE_OR_MORE(CharacterClass(SEMICOLON, negate=True)), SEMICOLON)
"""Regex expression matching a list of items separated by a semicolon.

Init Params:
    (no parameters)

Pattern:
    One or more items, each made of any characters except the semicolon, separated by a semicolon.
    Equivalent regex: `[^;]+(?:;[^;]+)*`

Notes:
    Items are not further restricted. For typed items use `LIST_OF(item, separator)`.

Example:
    SEMICOLON_SEPARATED_LIST
    # Matches: "a;b;c", "single"
    # Does not match: "", "a;;b"
"""

