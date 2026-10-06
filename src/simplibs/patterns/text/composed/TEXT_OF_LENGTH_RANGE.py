from simplibs.regex.base_class import Regex
from simplibs.regex.presets.any_character import ANY
from simplibs.regex.presets.quantifiers import BETWEEN


def TEXT_OF_LENGTH_RANGE(min_length: int, max_length: int) -> Regex:
    """Build a regex expression matching text whose length lies in an inclusive range.

    Init Params:
        min_length (int): The minimum number of characters (inclusive).
        max_length (int): The maximum number of characters (inclusive).

    Pattern:
        Between `min_length` and `max_length` characters of any kind.

    Example:
        pattern = TEXT_OF_LENGTH_RANGE(2, 4)
        # Regex: .{2,4}
        # Matches: "ab", "abcd"
        # Does not match: "a", "abcde"
    """
    return BETWEEN(ANY, min_length, max_length)

