from simplibs.regex.base_class import Regex
from simplibs.regex.presets.quantifiers import EXACTLY
# Patterns
from simplibs.patterns.characters import DECIMAL_DIGIT


def DIGIT_NUMBER(count: int) -> Regex:
    """Build a regex expression matching a number made of an exact count of digits.

    Init Params:
        count (int): The exact number of digits.

    Pattern:
        Exactly `count` ASCII digits (leading zeros allowed).

    Example:
        pattern = DIGIT_NUMBER(3)
        # Regex: [0-9]{3}
        # Matches: "123", "007"
        # Does not match: "12", "1234", "abc"
    """
    return EXACTLY(DECIMAL_DIGIT, count)

