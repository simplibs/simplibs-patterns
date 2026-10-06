from simplibs.regex.presets.quantifiers import EXACTLY
# Patterns
from simplibs.patterns.characters import DOT
from simplibs.patterns.numbers import ZERO_TO_TWO_HUNDRED_FIFTY_FIVE


IPV4_ADDRESS = ZERO_TO_TWO_HUNDRED_FIFTY_FIVE + EXACTLY(DOT + ZERO_TO_TWO_HUNDRED_FIFTY_FIVE, 3)
"""Regex expression matching an IPv4 address.

Init Params:
    (no parameters)

Pattern:
    Four numbers `0`–`255` without leading zeros, separated by dots.

Example:
    IPV4_ADDRESS
    # Matches: "192.168.0.1", "0.0.0.0", "255.255.255.255"
    # Does not match: "256.1.1.1", "1.2.3", "01.2.3.4", "1.2.3.4.5"
"""

