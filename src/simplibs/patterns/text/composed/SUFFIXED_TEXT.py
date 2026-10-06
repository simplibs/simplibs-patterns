from simplibs.regex.base_class import Regex
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.any_character import ANY
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE


def SUFFIXED_TEXT(suffix: str) -> Regex:
    """Build a regex expression matching text that ends with the given suffix.

    Init Params:
        suffix (str): The literal text the match must end with.

    Pattern:
        Any number of characters, followed by the literal `suffix`.

    Example:
        pattern = SUFFIXED_TEXT(".py")
        # Regex: .*\\.py
        # Matches: "main.py", ".py"
        # Does not match: "main.txt"
    """
    return ZERO_OR_MORE(ANY) + Literal(suffix)

