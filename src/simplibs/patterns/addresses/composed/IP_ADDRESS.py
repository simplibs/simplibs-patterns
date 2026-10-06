# Patterns
from simplibs.patterns.formats import IPV4_ADDRESS, IPV6_ADDRESS


IP_ADDRESS = IPV4_ADDRESS | IPV6_ADDRESS
"""Regex expression matching an IPv4 or IPv6 address.

Init Params:
    (no parameters)

Pattern:
    `IPV4_ADDRESS` or `IPV6_ADDRESS`.

Notes:
    `IPV4_ADDRESS`, `IPV6_ADDRESS` and `MAC_ADDRESS` live in the `formats` domain.

Example:
    IP_ADDRESS
    # Matches: "192.168.0.1", "::1", "2001:db8::ff00:42:8329"
    # Does not match: "256.1.1.1", "1.2.3", ""
"""

