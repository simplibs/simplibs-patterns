# Pure:
from .pure.OPENING_DELIMITER import OPENING_DELIMITER
from .pure.CLOSING_DELIMITER import CLOSING_DELIMITER
# Composed:
from .composed.DELIMITED_BY import DELIMITED_BY
from .composed.LIST_OF import LIST_OF
from .composed.SEQUENCE_OF import SEQUENCE_OF
from .composed.PAIR_OF import PAIR_OF
from .composed.WRAPPED_BY import WRAPPED_BY
from .composed.KEY_VALUE_PAIR import KEY_VALUE_PAIR
from .composed.KEY_VALUE import KEY_VALUE
# Custom:
from .custom.SEPARATOR import SEPARATOR
from .custom.DELIMITER import DELIMITER
from .custom.COMMA_SEPARATED_LIST import COMMA_SEPARATED_LIST
from .custom.SEMICOLON_SEPARATED_LIST import SEMICOLON_SEPARATED_LIST
from .custom.SPACE_SEPARATED_LIST import SPACE_SEPARATED_LIST
from .custom.TAB_SEPARATED_LIST import TAB_SEPARATED_LIST


_DESIGN_NOTES = """
# Structured Patterns Sub-Package

## Purpose
Building blocks for structured text — lists, pairs, delimited and wrapped items — mostly as parametrized factories that take other expressions as arguments.

## Layout
`pure/` named concepts · `composed/` combinations of other terms and parametrized factories · `custom/` terms that needed a semantic decision

## Internal Components Registry

| Component                  | Type             | Description                                                         |
| :------------------------- | :--------------- | :------------------------------------------------------------------ |
| `OPENING_DELIMITER`        | Regex Expression | An opening bracket.                                                 |
| `CLOSING_DELIMITER`        | Regex Expression | A closing bracket.                                                  |
| `SEPARATOR`                | Regex Expression | A common separator character.                                       |
| `DELIMITER`                | Regex Expression | A delimiter character.                                              |
| `DELIMITED_BY`             | Factory          | Builds one or more items separated by a delimiter.                  |
| `LIST_OF`                  | Factory          | Builds a list of items, comma-separated by default.                 |
| `SEQUENCE_OF`              | Factory          | Builds one or more consecutive items without separators.            |
| `PAIR_OF`                  | Factory          | Builds a key and a value joined by a separator.                     |
| `WRAPPED_BY`               | Factory          | Builds an item wrapped between an opening and a closing expression. |
| `KEY_VALUE_PAIR`           | Regex Expression | A key=value pair.                                                   |
| `KEY_VALUE`                | Regex Expression | A key=value pair.                                                   |
| `COMMA_SEPARATED_LIST`     | Regex Expression | A list of items separated by a comma.                               |
| `SEMICOLON_SEPARATED_LIST` | Regex Expression | A list of items separated by a semicolon.                           |
| `SPACE_SEPARATED_LIST`     | Regex Expression | A list of items separated by a space.                               |
| `TAB_SEPARATED_LIST`       | Regex Expression | A list of items separated by a tab.                                 |
"""
