from simplibs.regex.presets.quantifiers import EXACTLY
from simplibs.regex.presets.character_classes import HEX_DIGIT
# Patterns
from simplibs.patterns.characters import DASH


UUID = EXACTLY(HEX_DIGIT, 8) + DASH + EXACTLY(HEX_DIGIT, 4) + DASH + EXACTLY(HEX_DIGIT, 4) + DASH + EXACTLY(HEX_DIGIT, 4) + DASH + EXACTLY(HEX_DIGIT, 12)
"""Regex expression matching a UUID in canonical form.

Init Params:
    (no parameters)

Pattern:
    Hex groups of 8-4-4-4-12 digits separated by hyphens.
    Equivalent regex: `[0-9a-fA-F]{8}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{12}`

Notes:
    Version and variant bits are not checked.

Example:
    UUID
    # Matches: "123e4567-e89b-12d3-a456-426614174000", "00000000-0000-0000-0000-000000000000"
    # Does not match: "123e4567e89b12d3a456426614174000", "123e4567-e89b-12d3-a456-42661417400", "g23e4567-e89b-12d3-a456-426614174000"
"""

