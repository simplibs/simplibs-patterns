from simplibs.regex.base_class import Regex
from simplibs.regex.presets.quantifiers import OPTIONAL
# Patterns
from simplibs.patterns.characters import SIGN


def SIGNED(number: Regex) -> Regex:
    """Build a regex expression matching the given number preceded by an optional sign.

    Init Params:
        number (Regex): The unsigned number expression to allow a sign in front of.

    Pattern:
        1. An optional `SIGN` (`+` or `-`).
        2. The `number` expression.

    Example:
        pattern = SIGNED(INTEGER)
        # Regex: [+\\-]?[0-9]+
        # Matches: "42", "-42", "+42"
        # Does not match: "--1", "- 1", "", "4-2"
    """
    return OPTIONAL(SIGN) + number

