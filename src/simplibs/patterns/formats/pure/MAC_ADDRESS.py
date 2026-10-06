from simplibs.regex.presets.quantifiers import EXACTLY
from simplibs.regex.presets.character_classes import HEX_DIGIT
# Patterns
from simplibs.patterns.characters import COLON


MAC_ADDRESS = EXACTLY(HEX_DIGIT, 2) + EXACTLY(COLON + EXACTLY(HEX_DIGIT, 2), 5)
"""Regex expression matching a MAC address.

Init Params:
    (no parameters)

Pattern:
    Six pairs of hex digits separated by colons.
    Equivalent regex: `[0-9a-fA-F]{2}(?::[0-9a-fA-F]{2}){5}`

Notes:
    Only colon-separated hexadecimal pairs are matched; hyphen-separated and Cisco-style dotted
    notations are not included.

Example:
    MAC_ADDRESS
    # Matches: "00:1A:2B:3C:4D:5E", "ff:ff:ff:ff:ff:ff"
    # Does not match: "00-1A-2B-3C-4D-5E", "00:1A:2B:3C:4D", "00:1A:2B:3C:4D:5G"
"""
