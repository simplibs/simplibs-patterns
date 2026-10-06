from simplibs.regex.presets.quantifiers import EXACTLY
from simplibs.regex.presets.character_classes import HEX_DIGIT


SHA256 = EXACTLY(HEX_DIGIT, 64)
"""Regex expression matching a SHA-256 digest in hex.

Init Params:
    (no parameters)

Pattern:
    Exactly 64 hex digits.
    Equivalent regex: `[0-9a-fA-F]{64}`

Example:
    SHA256
    # Matches: "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    # Does not match: "e3b0c44298fc1c14"
"""

