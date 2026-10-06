from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.presets.quantifiers import ONE_OR_MORE
from simplibs.regex.presets.literals import TAB
# Patterns
from simplibs.patterns.structured.composed.LIST_OF import LIST_OF


TAB_SEPARATED_LIST = LIST_OF(ONE_OR_MORE(CharacterClass(TAB, negate=True)), TAB)
"""Regex expression matching a list of items separated by a tab.

Init Params:
    (no parameters)

Pattern:
    One or more items, each made of any characters except the tab, separated by a tab.
    Equivalent regex: `[^\\t]+(?:\\t[^\\t]+)*`

Notes:
    Items are not further restricted. For typed items use `LIST_OF(item, separator)`.

Example:
    TAB_SEPARATED_LIST
    # Matches: "a\\tb\\tc", "single"
    # Does not match: "", "a\\t\\tb"
"""

