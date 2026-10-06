from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.CharacterRange import CharacterRange
from simplibs.regex.elements.Literal import Literal
from simplibs.regex.presets.quantifiers import ONE_OR_MORE, OPTIONAL, ZERO_OR_MORE
# Patterns
from simplibs.patterns.characters import (
    DASH,
    DECIMAL_DIGIT,
    DOT,
    NON_ZERO_DIGIT,
    PLUS_SIGN,
)


_NUMBER = Literal("0") | NON_ZERO_DIGIT + ZERO_OR_MORE(DECIMAL_DIGIT)
_IDENTIFIER = ONE_OR_MORE(
    CharacterClass(CharacterRange("a", "z"), CharacterRange("A", "Z"), CharacterRange("0", "9"), DASH)
)
_IDENTIFIERS = _IDENTIFIER + ZERO_OR_MORE(DOT + _IDENTIFIER)

SEMVER = _NUMBER + DOT + _NUMBER + DOT + _NUMBER + OPTIONAL(DASH + _IDENTIFIERS) + OPTIONAL(PLUS_SIGN + _IDENTIFIERS)
"""Regex expression matching a semantic version (SemVer 2.0).

Init Params:
    (no parameters)

Pattern:
    `MAJOR.MINOR.PATCH` without leading zeros, optionally followed by `-prerelease` and `+build` parts.

Notes:
    Numeric pre-release identifiers may contain leading zeros, although strict SemVer 2.0 syntax
    does not permit them.

Example:
    SEMVER
    # Matches: "1.2.3", "1.0.0-alpha.1", "1.0.0+build.5", "2.1.0-rc.1+sha.ab12"
    # Does not match: "1.2", "01.2.3", "1.2.3.4", "v1.2.3"
"""

