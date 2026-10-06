from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.presets.quantifiers import ONE_OR_MORE
# Patterns
from simplibs.patterns.characters import SPACE
from simplibs.patterns.structured.composed.LIST_OF import LIST_OF


SPACE_SEPARATED_LIST = LIST_OF(ONE_OR_MORE(CharacterClass(SPACE, negate=True)), SPACE)
"""Regex expression matching a list of items separated by a space.

Init Params:
    (no parameters)

Pattern:
    One or more items, each made of any characters except the space, separated by a space.
    Equivalent regex: `[^ ]+(?:\\ [^ ]+)*`

Notes:
    Items are not further restricted. For typed items use `LIST_OF(item, separator)`.

Example:
    SPACE_SEPARATED_LIST
    # Matches: "a b c", "single"
    # Does not match: "", "a  b"
"""

