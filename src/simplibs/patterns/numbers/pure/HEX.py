from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import ONE_OR_MORE
from simplibs.regex.presets.character_classes import HEX_DIGIT


HEX = Literal("0") + CharacterClass(Literal("x"), Literal("X")) + ONE_OR_MORE(HEX_DIGIT)
"""Regex expression matching a hexadecimal number literal.

Init Params:
    (no parameters)

Pattern:
    `0x` (or `0X`) followed by one or more hexadecimal digits.
    Equivalent regex: `0[xX][0-9a-fA-F]+`

Example:
    HEX
    # Matches: "0xFF", "0X1a"
    # Does not match: "0x", "0xG", "FF"
"""

