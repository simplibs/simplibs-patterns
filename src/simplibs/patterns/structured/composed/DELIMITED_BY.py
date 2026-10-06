from simplibs.regex.base_class import Regex
from simplibs.regex.presets.quantifiers import ZERO_OR_MORE


def DELIMITED_BY(item: Regex, delimiter: Regex) -> Regex:
    """Build a regex expression matching one or more items separated by a delimiter.

    Init Params:
        item (Regex): The expression for a single item.
        delimiter (Regex): The expression that separates items.

    Pattern:
        1. One `item`.
        2. Any number of (`delimiter`, `item`) pairs.

    Example:
        pattern = DELIMITED_BY(WORD, Literal("/"))
        # Regex: \\w+(?:/\\w+)*
        # Matches: "usr", "usr/local/bin"
        # Does not match: "/usr", "usr/", "usr//bin", ""
    """
    return item + ZERO_OR_MORE(delimiter + item)

