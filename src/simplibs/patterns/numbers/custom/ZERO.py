from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import ONE_OR_MORE, OPTIONAL
# Patterns
from simplibs.patterns.characters import SIGN


ZERO = OPTIONAL(SIGN) + ONE_OR_MORE(Literal("0"))
"""Regex expression matching an integer equal to zero.

Init Params:
    (no parameters)

Pattern:
    An optional sign and one or more zeros.
    Equivalent regex: `[+\\-]?0+`

Notes:
Example:
    ZERO
    # Matches: "0", "00", "-0", "+0"
    # Does not match: "1", "", "0.0", "10"
"""

_DESIGN_NOTES = """
If numeric sign/zero presets are later extended to decimals, define their numeric semantics
consistently across `POSITIVE`, `NEGATIVE` and `ZERO` rather than extending only `ZERO`.
"""

