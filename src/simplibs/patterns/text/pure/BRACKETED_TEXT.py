from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE


BRACKETED_TEXT = Literal("[") + ZERO_OR_MORE(CharacterClass(Literal("["), Literal("]"), negate=True)) + Literal("]")
"""Regex expression matching text in square brackets.

Init Params:
    (no parameters)

Pattern:
    `[`, any characters that are not square brackets, and `]`.
    Equivalent regex: `\\[[^[\\]]*\\]`

Notes:
    Not nested: square brackets inside are not allowed.

Example:
    BRACKETED_TEXT
    # Matches: "[abc]", "[]"
    # Does not match: "abc", "[a[b]]", "[open"
"""

