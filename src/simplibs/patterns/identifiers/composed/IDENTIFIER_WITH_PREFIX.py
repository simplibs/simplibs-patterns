from simplibs.regex.base_class import Regex
from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.identifiers.pure.IDENTIFIER import IDENTIFIER


def IDENTIFIER_WITH_PREFIX(prefix: str) -> Regex:
    """Build a regex expression matching an identifier part that follows a fixed prefix.

    Init Params:
        prefix (str): The literal text the name must start with.

    Pattern:
        The literal `prefix`, followed by an `IDENTIFIER`.

    Notes:
        The part after the prefix must itself be a valid identifier, so `get_1` is rejected.

    Example:
        pattern = IDENTIFIER_WITH_PREFIX("get_")
        # Regex: get_[a-zA-Z_][a-zA-Z0-9_]*
        # Matches: "get_value", "get_x1"
        # Does not match: "get_", "value"
    """
    return Literal(prefix) + IDENTIFIER

