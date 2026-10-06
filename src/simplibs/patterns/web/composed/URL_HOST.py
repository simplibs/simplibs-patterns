from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.formats import IPV4_ADDRESS, IPV6_ADDRESS
from simplibs.patterns.web.pure.HOSTNAME import HOSTNAME


URL_HOST = IPV4_ADDRESS | Literal("[") + IPV6_ADDRESS + Literal("]") | HOSTNAME
"""Regex expression matching the host part of a URL.

Init Params:
    (no parameters)

Pattern:
    `IPV4_ADDRESS`, an IPv6 address in square brackets, or a `HOSTNAME`.

Example:
    URL_HOST
    # Matches: "example.com", "localhost", "192.168.0.1", "[::1]"
    # Does not match: "::1", "[::1", "a..b"
"""

