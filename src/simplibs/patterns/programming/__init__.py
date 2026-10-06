# Pure:
from .pure.OPERATOR import OPERATOR
# Composed:
from .composed.NUMBER_LITERAL import NUMBER_LITERAL
# Custom:
from .custom.COMMENT import COMMENT
from .custom.STRING_LITERAL import STRING_LITERAL
from .custom.BOOLEAN_LITERAL import BOOLEAN_LITERAL
from .custom.NULL_LITERAL import NULL_LITERAL
from .custom.KEYWORD import KEYWORD
from .custom.IMPORT import IMPORT
# Enums:
from .enums.Language import Language


_DESIGN_NOTES = """
# Programming Patterns Sub-Package

## Purpose
Source-code constructs that depend on the language — comments, strings, keywords, imports, literals — selected with a `Language` enum, plus a few language-neutral terms.

## Layout
`pure/` named concepts · `composed/` combinations of other terms and parametrized factories · `custom/` terms that needed a semantic decision · `enums/` selector enums

## Internal Components Registry

| Component         | Type             | Description                                         |
| :---------------- | :--------------- | :-------------------------------------------------- |
| `Language`        | Enum             | Programming language selector.                      |
| `OPERATOR`        | Regex Expression | A common operator shared by most languages.         |
| `NUMBER_LITERAL`  | Regex Expression | An unsigned numeric literal.                        |
| `COMMENT`         | Factory          | Builds a single-line comment in the given language. |
| `STRING_LITERAL`  | Factory          | Builds a string literal in the given language.      |
| `BOOLEAN_LITERAL` | Factory          | Builds a boolean literal in the given language.     |
| `NULL_LITERAL`    | Factory          | Builds the null literal of the given language.      |
| `KEYWORD`         | Factory          | Builds a reserved keyword of the given language.    |
| `IMPORT`          | Factory          | Builds an import statement in the given language.   |
"""
