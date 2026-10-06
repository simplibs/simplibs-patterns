from simplibs.regex.presets.quantifiers import EXACTLY
from simplibs.regex.presets.character_classes import HEX_DIGIT


MD5 = EXACTLY(HEX_DIGIT, 32)
"""Regex expression matching an MD5 digest in hex.

Init Params:
    (no parameters)

Pattern:
    Exactly 32 hex digits.
    Equivalent regex: `[0-9a-fA-F]{32}`

Example:
    MD5
    # Matches: "d41d8cd98f00b204e9800998ecf8427e"
    # Does not match: "d41d8cd98f00b204e9800998ecf8427", "d41d8cd98f00b204e9800998ecf8427g"
"""

