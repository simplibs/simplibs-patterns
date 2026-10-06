from simplibs.regex.presets.quantifiers import ONE_OR_MORE
from simplibs.regex.presets.character_classes import HEX_DIGIT


HEX_STRING = ONE_OR_MORE(HEX_DIGIT)
"""Regex expression matching a string of hexadecimal digits.

Init Params:
    (no parameters)

Pattern:
    One or more hex digits.
    Equivalent regex: `[0-9a-fA-F]+`

Example:
    HEX_STRING
    # Matches: "deadBEEF", "00", "1f"
    # Does not match: "xyz", "", "0x1f"
"""

