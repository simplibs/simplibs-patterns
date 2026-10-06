from simplibs.regex.elements.CharacterClass import CharacterClass
from simplibs.regex.elements.Literal import Literal


PUNCTUATION = CharacterClass(Literal("!"), Literal("\""), Literal("#"), Literal("%"), Literal("&"), Literal("'"), Literal("("), Literal(")"), Literal("*"), Literal(","), Literal("-"), Literal("."), Literal("/"), Literal(":"), Literal(";"), Literal("?"), Literal("@"), Literal("["), Literal("\\"), Literal("]"), Literal("_"), Literal("{"), Literal("}"),)
"""Regex expression matching a single punctuation character.

Init Params:
    (no parameters)

Pattern:
    Matches one of `! " # % & ' ( ) * , - . / : ; ? @ [ \\ ] _ { }`.
    Equivalent regex: `[!"#%&'()*,\\-./:;?@[\\\\\\]_{}]`

Notes:
    Follows the Unicode split of ASCII punctuation: characters like `$`, `+`, `<` are symbols (see `SYMBOL`).

Example:
    PUNCTUATION
    # Matches: "!", ".", "_"
    # Does not match: "$", "+", "a"
"""

