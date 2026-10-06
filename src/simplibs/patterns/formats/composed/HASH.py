# Patterns
from simplibs.patterns.formats.pure.MD5 import MD5
from simplibs.patterns.formats.pure.SHA1 import SHA1
from simplibs.patterns.formats.pure.SHA256 import SHA256


HASH = SHA256 | SHA1 | MD5
"""Regex expression matching a common hash digest in hex.

Init Params:
    (no parameters)

Pattern:
    A `SHA256`, `SHA1` or `MD5` digest (64, 40 or 32 hex digits).
    Equivalent regex: `[0-9a-fA-F]{64}|[0-9a-fA-F]{40}|[0-9a-fA-F]{32}`

Notes:
    The pattern is limited to the common SHA-256, SHA-1 and MD5 hexadecimal digest lengths.

Example:
    HASH
    # Matches: "d41d8cd98f00b204e9800998ecf8427e", "da39a3ee5e6b4b0d3255bfef95601890afd80709"
    # Does not match: "abc", "d41d8cd98f00b204e9800998ecf8427"
"""

