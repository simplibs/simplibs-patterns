from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE


BRACED_TEXT = Literal("{") + ZERO_OR_MORE(CharacterClass(Literal("{"), Literal("}"), negate=True)) + Literal("}")
"""Regex expression matching text in curly braces.

Init Params:
    (no parameters)

Pattern:
    `{`, any characters that are not curly braces, and `}`.
    Equivalent regex: `\\{[^{}]*\\}`

Notes:
    Not nested: curly braces inside are not allowed.

Example:
    BRACED_TEXT
    # Matches: "{abc}", "{}"
    # Does not match: "abc", "{a{b}}", "{open"
"""

