from simplibs.regex.presets.quantifiers import EXACTLY
from simplibs.regex.presets.character_classes import HEX_DIGIT


SHA1 = EXACTLY(HEX_DIGIT, 40)
"""Regex expression matching a SHA-1 digest in hex.

Init Params:
    (no parameters)

Pattern:
    Exactly 40 hex digits.
    Equivalent regex: `[0-9a-fA-F]{40}`

Example:
    SHA1
    # Matches: "da39a3ee5e6b4b0d3255bfef95601890afd80709"
    # Does not match: "da39a3ee5e6b4b0d3255bfef95601890afd8070"
"""

