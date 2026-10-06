from simplibs.regex.base_class import Regex
# Patterns
from simplibs.patterns.characters import EQUALS


def PAIR_OF(key: Regex, value: Regex, separator: Regex = EQUALS) -> Regex:
    """Build a regex expression matching a key and a value joined by a separator.

    Init Params:
        key (Regex): The expression for the key.
        value (Regex): The expression for the value.
        separator (Regex): The expression between key and value (default `EQUALS`).

    Pattern:
        `key`, then `separator`, then `value`.

    Example:
        pattern = PAIR_OF(IDENTIFIER, INTEGER)
        # Regex: [a-zA-Z_][a-zA-Z0-9_]*=[0-9]+
        # Matches: "age=42", "x=0"
        # Does not match: "age:42", "age=", "=42"
    """
    return key + separator + value

