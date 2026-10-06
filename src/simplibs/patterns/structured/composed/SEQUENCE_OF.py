from simplibs.regex.base_class import Regex
from simplibs.regex.presets.quantifiers import ONE_OR_MORE


def SEQUENCE_OF(item: Regex) -> Regex:
    """Build a regex expression matching one or more consecutive items without separators.

    Init Params:
        item (Regex): The expression to repeat.

    Pattern:
        `item` repeated one or more times.

        Example:
        pattern = SEQUENCE_OF(Literal("ab"))
        # Regex: (?:ab)+
        # Matches: "ab", "ababab"
        # Does not match: "", "aba"
    """
    return ONE_OR_MORE(item)


_DESIGN_NOTES = """
When `item` is already quantified, wrapping behavior matters because directly appending `+` can
change how the underlying regex engine interprets the expression. Preserve this constraint if
`SEQUENCE_OF` is changed.
"""

