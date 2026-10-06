from simplibs.regex.base_class import Regex
from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.identifiers.pure.IDENTIFIER import IDENTIFIER


def IDENTIFIER_WITH_SUFFIX(suffix: str) -> Regex:
    """Build a regex expression matching an identifier part followed by a fixed suffix.

    Init Params:
        suffix (str): The literal text the name must end with.

    Pattern:
        An `IDENTIFIER`, followed by the literal `suffix`.

    Example:
        pattern = IDENTIFIER_WITH_SUFFIX("_id")
        # Regex: [a-zA-Z_][a-zA-Z0-9_]*_id
        # Matches: "user_id", "order_id"
        # Does not match: "_id", "user"
    """
    return IDENTIFIER + Literal(suffix)

