from simplibs.regex.base_class import Regex
from simplibs.regex.elements.Literal import Literal
# Patterns
from simplibs.patterns.dates.pure.DAY import DAY
from simplibs.patterns.dates.pure.MONTH import MONTH
from simplibs.patterns.dates.pure.YEAR import YEAR


def DATE_WITH_SEPARATOR(separator: str) -> Regex:
    """Build a regex expression matching a year-month-day date with a custom separator.

    Init Params:
        separator (str): The literal text placed between the three parts.

    Pattern:
        `YEAR`, `separator`, `MONTH`, `separator`, `DAY`.

    Example:
        pattern = DATE_WITH_SEPARATOR("/")
        # Regex: [0-9]{4}/(?:0[1-9]|1[0-2])/(?:0[1-9]|[1-2][0-9]|3[01])
        # Matches: "2026/09/30"
        # Does not match: "2026-09-30", "2026/9/30"
    """
    return YEAR + Literal(separator) + MONTH + Literal(separator) + DAY

