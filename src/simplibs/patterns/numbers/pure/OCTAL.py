from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import ONE_OR_MORE
# Patterns
from simplibs.patterns.characters import OCTAL_DIGIT


OCTAL = Literal("0") + CharacterClass(Literal("o"), Literal("O")) + ONE_OR_MORE(OCTAL_DIGIT)
"""Regex expression matching an octal number literal.

Init Params:
    (no parameters)

Pattern:
    `0o` (or `0O`) followed by one or more octal digits.
    Equivalent regex: `0[oO][0-7]+`

Example:
    OCTAL
    # Matches: "0o17", "0O7"
    # Does not match: "0o", "0o8", "17"
"""

