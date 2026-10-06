from simplibs.regex.presets.quantifiers import BETWEEN, EXACTLY
from simplibs.regex.presets.character_classes import HEX_DIGIT
# Patterns
from simplibs.patterns.characters import COLON


_HEX = BETWEEN(HEX_DIGIT, 1, 4)
_HEX_COLON = _HEX + COLON
_COLON_HEX = COLON + _HEX

IPV6_ADDRESS = EXACTLY(_HEX_COLON, 7) + _HEX | BETWEEN(_HEX_COLON, 1, 7) + COLON | BETWEEN(_HEX_COLON, 1, 6) + COLON + _HEX | BETWEEN(_HEX_COLON, 1, 5) + BETWEEN(_COLON_HEX, 1, 2) | BETWEEN(_HEX_COLON, 1, 4) + BETWEEN(_COLON_HEX, 1, 3) | BETWEEN(_HEX_COLON, 1, 3) + BETWEEN(_COLON_HEX, 1, 4) | BETWEEN(_HEX_COLON, 1, 2) + BETWEEN(_COLON_HEX, 1, 5) | _HEX_COLON + BETWEEN(_COLON_HEX, 1, 6) | COLON + (BETWEEN(_COLON_HEX, 1, 7) | COLON)
"""Regex expression matching an IPv6 address.

Init Params:
    (no parameters)

Pattern:
    Eight groups of 1–4 hex digits separated by colons, with one run of zero groups optionally compressed to `::`.

Notes:
    Embedded IPv4 tails (::ffff:192.0.2.1) and zone ids (fe80::1%eth0) are not covered.

    IPv4-embedded forms and interface zone identifiers are not supported; the pattern covers
    standard textual IPv6 forms.

Example:
    IPV6_ADDRESS
    # Matches: "2001:db8::ff00:42:8329", "::1", "::", "fe80::1"
    # Does not match: "1:2:3:4:5:6:7", "1::2::3", "12345::1", "g::1"
"""
