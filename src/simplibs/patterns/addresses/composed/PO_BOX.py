from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import OPTIONAL
# Patterns
from simplibs.patterns.characters import DOT, SPACE
from simplibs.patterns.numbers import INTEGER


PO_BOX = Literal("P") + OPTIONAL(DOT) + Literal("O") + OPTIONAL(DOT) + SPACE + Literal("Box") + SPACE + INTEGER
"""Regex expression matching a P.O. box line.

Init Params:
    (no parameters)

Pattern:
    `P.O. Box` (dots optional) followed by a number.
    Equivalent regex: `P\\.?O\\.?\\ Box\\ [0-9]+`

Notes:
    Case-sensitive; use the `IGNORECASE` flag to relax it.

Example:
    PO_BOX
    # Matches: "P.O. Box 123", "PO Box 45", "P.O Box 7"
    # Does not match: "Box 123", "P.O. Box", "po box 5"
"""

