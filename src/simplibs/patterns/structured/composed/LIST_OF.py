from simplibs.regex.base_class import Regex
# Patterns
from simplibs.patterns.characters import COMMA
from simplibs.patterns.structured.composed.DELIMITED_BY import DELIMITED_BY


def LIST_OF(item: Regex, separator: Regex = COMMA) -> Regex:
    """Build a regex expression matching a list of items, comma-separated by default.

    Init Params:
        item (Regex): The expression for a single item.
        separator (Regex): The expression between items (default `COMMA`).

    Pattern:
        One or more `item`s separated by `separator`.

    Example:
        pattern = LIST_OF(INTEGER)
        # Regex: [0-9]+(?:,[0-9]+)*
        # Matches: "1", "1,2,3", "42,7"
        # Does not match: "", "1,", "1,,2", "1 2"
    """
    return DELIMITED_BY(item, separator)

