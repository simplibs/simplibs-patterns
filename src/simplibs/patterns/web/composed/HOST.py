# Patterns
from simplibs.patterns.formats import IPV4_ADDRESS, IPV6_ADDRESS
from simplibs.patterns.web.pure.HOSTNAME import HOSTNAME


HOST = IPV4_ADDRESS | IPV6_ADDRESS | HOSTNAME
"""Regex expression matching a host: IPv4, IPv6 or host name.

Init Params:
    (no parameters)

Pattern:
    `IPV4_ADDRESS`, `IPV6_ADDRESS` or `HOSTNAME`.

Example:
    HOST
    # Matches: "example.com", "localhost", "192.168.0.1", "::1"
    # Does not match: "-x", "a..b", ""
"""

