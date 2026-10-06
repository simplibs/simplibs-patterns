# Pure:
from .pure.IDENTIFIER_START_CHARACTER import IDENTIFIER_START_CHARACTER
from .pure.IDENTIFIER_CHARACTER import IDENTIFIER_CHARACTER
from .pure.IDENTIFIER import IDENTIFIER
from .pure.SIMPLE_IDENTIFIER import SIMPLE_IDENTIFIER
from .pure.NAME import NAME
from .pure.QUALIFIED_IDENTIFIER import QUALIFIED_IDENTIFIER
from .pure.QUALIFIED_NAME import QUALIFIED_NAME
from .pure.NAMESPACE import NAMESPACE
from .pure.NAMESPACE_NAME import NAMESPACE_NAME
from .pure.VARIABLE_NAME import VARIABLE_NAME
from .pure.CONSTANT_NAME import CONSTANT_NAME
from .pure.FUNCTION_NAME import FUNCTION_NAME
from .pure.METHOD_NAME import METHOD_NAME
from .pure.CLASS_NAME import CLASS_NAME
from .pure.TYPE_NAME import TYPE_NAME
from .pure.MODULE_NAME import MODULE_NAME
from .pure.PACKAGE_NAME import PACKAGE_NAME
from .pure.ATTRIBUTE_NAME import ATTRIBUTE_NAME
from .pure.PROPERTY_NAME import PROPERTY_NAME
from .pure.PARAMETER_NAME import PARAMETER_NAME
from .pure.ARGUMENT_NAME import ARGUMENT_NAME
from .pure.ENUM_NAME import ENUM_NAME
from .pure.ENUM_MEMBER_NAME import ENUM_MEMBER_NAME
from .pure.KEY import KEY
from .pure.VALUE_NAME import VALUE_NAME
from .pure.LABEL import LABEL
# Composed:
from .composed.QUALIFIED_IDENTIFIER_OF import QUALIFIED_IDENTIFIER_OF
from .composed.IDENTIFIER_WITH_PREFIX import IDENTIFIER_WITH_PREFIX
from .composed.IDENTIFIER_WITH_SUFFIX import IDENTIFIER_WITH_SUFFIX
# Custom:
from .custom.TAG_NAME import TAG_NAME
from .custom.ELEMENT_NAME import ELEMENT_NAME


_DESIGN_NOTES = """
# Identifiers Patterns Sub-Package

## Purpose
Names and identifiers — plain and dotted identifiers, role-specific names (variable, class, module…), markup tag names, and prefix/suffix helpers.

## Layout
`pure/` named concepts · `composed/` combinations of other terms and parametrized factories · `custom/` terms that needed a semantic decision

## Internal Components Registry

| Component                    | Type             | Description                                               |
| :--------------------------- | :--------------- | :-------------------------------------------------------- |
| `IDENTIFIER_START_CHARACTER` | Regex Expression | A character an identifier may start with.                 |
| `IDENTIFIER_CHARACTER`       | Regex Expression | A character that may appear inside an identifier.         |
| `IDENTIFIER`                 | Regex Expression | A language-neutral identifier.                            |
| `SIMPLE_IDENTIFIER`          | Regex Expression | A simple (unqualified) identifier.                        |
| `NAME`                       | Regex Expression | A name.                                                   |
| `QUALIFIED_IDENTIFIER`       | Regex Expression | A dotted identifier with at least two parts.              |
| `QUALIFIED_NAME`             | Regex Expression | A qualified name.                                         |
| `NAMESPACE`                  | Regex Expression | A namespace path of one or more parts.                    |
| `NAMESPACE_NAME`             | Regex Expression | A namespace name.                                         |
| `VARIABLE_NAME`              | Regex Expression | A variable name.                                          |
| `CONSTANT_NAME`              | Regex Expression | A constant name.                                          |
| `FUNCTION_NAME`              | Regex Expression | A function name.                                          |
| `METHOD_NAME`                | Regex Expression | A method name.                                            |
| `CLASS_NAME`                 | Regex Expression | A class name.                                             |
| `TYPE_NAME`                  | Regex Expression | A type name.                                              |
| `MODULE_NAME`                | Regex Expression | A module name.                                            |
| `PACKAGE_NAME`               | Regex Expression | A package name.                                           |
| `ATTRIBUTE_NAME`             | Regex Expression | An attribute name.                                        |
| `PROPERTY_NAME`              | Regex Expression | A property name.                                          |
| `PARAMETER_NAME`             | Regex Expression | A parameter name.                                         |
| `ARGUMENT_NAME`              | Regex Expression | An argument name.                                         |
| `ENUM_NAME`                  | Regex Expression | An enumeration name.                                      |
| `ENUM_MEMBER_NAME`           | Regex Expression | An enumeration member name.                               |
| `KEY`                        | Regex Expression | A key name.                                               |
| `VALUE_NAME`                 | Regex Expression | A value name.                                             |
| `LABEL`                      | Regex Expression | A label name.                                             |
| `TAG_NAME`                   | Regex Expression | A markup tag name.                                        |
| `ELEMENT_NAME`               | Regex Expression | A markup element name.                                    |
| `QUALIFIED_IDENTIFIER_OF`    | Factory          | Builds a dotted identifier with an exact number of parts. |
| `IDENTIFIER_WITH_PREFIX`     | Factory          | Builds an identifier part that follows a fixed prefix.    |
| `IDENTIFIER_WITH_SUFFIX`     | Factory          | Builds an identifier part followed by a fixed suffix.     |
"""
