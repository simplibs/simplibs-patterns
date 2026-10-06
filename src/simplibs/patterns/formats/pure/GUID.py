# Patterns
from simplibs.patterns.formats.pure.UUID import UUID


GUID = UUID
"""Regex expression matching a GUID.

Init Params:
    (no parameters)

Pattern:
    Same expression as `UUID`; the separate name states the intended role.

Example:
    GUID
    # Matches: "123e4567-e89b-12d3-a456-426614174000", "00000000-0000-0000-0000-000000000000"
    # Does not match: "123e4567e89b12d3a456426614174000", "123e4567-e89b-12d3-a456-42661417400", "g23e4567-e89b-12d3-a456-426614174000"
"""

