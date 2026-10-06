from simplibs.regex.base_class import Regex
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.any_character import ANY
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE


def PREFIXED_TEXT(prefix: str) -> Regex:
    """Build a regex expression matching text that starts with the given prefix.

    Init Params:
        prefix (str): The literal text the match must start with.

    Pattern:
        The literal `prefix`, followed by any number of characters.

    Example:
        pattern = PREFIXED_TEXT("log:")
        # Regex: log:.*
        # Matches: "log: started", "log:"
        # Does not match: "info: started"
    """
    return Literal(prefix) + ZERO_OR_MORE(ANY)

