from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal


BRACE = CharacterClass(Literal("{"), Literal("}"))
"""Regex expression matching a single curly brace.

Init Params:
    (no parameters)

Pattern:
    Matches `{` or `}`.
    Equivalent regex: `[{}]`

Example:
    BRACE
    # Matches: "{", "}"
    # Does not match: "(", "{}"
"""

