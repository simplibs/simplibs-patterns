# Pure:
from .pure.INTEGER import INTEGER
from .pure.DECIMAL import DECIMAL
from .pure.INTEGER_PART import INTEGER_PART
from .pure.FRACTIONAL_PART import FRACTIONAL_PART
from .pure.DECIMAL_SEPARATOR import DECIMAL_SEPARATOR
from .pure.ZERO_TO_NINE import ZERO_TO_NINE
from .pure.BINARY import BINARY
from .pure.OCTAL import OCTAL
from .pure.HEX import HEX
from .pure.EXPONENT import EXPONENT
from .pure.FRACTION import FRACTION
# Composed:
from .composed.NUMBER import NUMBER
from .composed.SIGNED import SIGNED
from .composed.SIGNED_INTEGER import SIGNED_INTEGER
from .composed.SIGNED_NUMBER import SIGNED_NUMBER
from .composed.NON_NEGATIVE import NON_NEGATIVE
from .composed.NON_POSITIVE import NON_POSITIVE
from .composed.NON_ZERO import NON_ZERO
from .composed.EXPONENT_PART import EXPONENT_PART
from .composed.SCIENTIFIC import SCIENTIFIC
from .composed.RATIONAL_NUMBER import RATIONAL_NUMBER
from .composed.PERCENTAGE import PERCENTAGE
from .composed.PERMILLE import PERMILLE
from .composed.DIGIT_NUMBER import DIGIT_NUMBER
from .composed.ONE_DIGIT_NUMBER import ONE_DIGIT_NUMBER
from .composed.TWO_DIGIT_NUMBER import TWO_DIGIT_NUMBER
from .composed.THREE_DIGIT_NUMBER import THREE_DIGIT_NUMBER
from .composed.FOUR_DIGIT_NUMBER import FOUR_DIGIT_NUMBER
# Custom:
from .custom.ZERO import ZERO
from .custom.POSITIVE import POSITIVE
from .custom.NEGATIVE import NEGATIVE
from .custom.ZERO_TO_NINETY_NINE import ZERO_TO_NINETY_NINE
from .custom.ZERO_TO_TWO_HUNDRED_FIFTY_FIVE import ZERO_TO_TWO_HUNDRED_FIFTY_FIVE
from .custom.PORT_NUMBER import PORT_NUMBER
from .custom.YEAR_NUMBER import YEAR_NUMBER
from .custom.MONTH_NUMBER import MONTH_NUMBER
from .custom.DAY_NUMBER import DAY_NUMBER
from .custom.HOUR_NUMBER import HOUR_NUMBER
from .custom.MINUTE_NUMBER import MINUTE_NUMBER
from .custom.SECOND_NUMBER import SECOND_NUMBER
from .custom.LATITUDE import LATITUDE
from .custom.LONGITUDE import LONGITUDE


_DESIGN_NOTES = """
# Numbers Patterns Sub-Package

## Purpose
Numbers in text — integers, decimals, signs, bases, scientific notation, fixed-digit numbers, bounded ranges, and the number shapes used by dates, times, ports and coordinates.

## Layout
`pure/` named concepts · `composed/` combinations of other terms and parametrized factories · `custom/` terms that needed a semantic decision

## Internal Components Registry

| Component                        | Type             | Description                                           |
| :------------------------------- | :--------------- | :---------------------------------------------------- |
| `INTEGER`                        | Regex Expression | An unsigned whole number.                             |
| `DECIMAL`                        | Regex Expression | An unsigned decimal number with a dot.                |
| `NUMBER`                         | Regex Expression | An unsigned integer or decimal number.                |
| `INTEGER_PART`                   | Regex Expression | The integer part of a decimal number.                 |
| `FRACTIONAL_PART`                | Regex Expression | The fractional part of a decimal number.              |
| `DECIMAL_SEPARATOR`              | Regex Expression | The decimal separator.                                |
| `ZERO_TO_NINE`                   | Regex Expression | A single digit from 0 to 9.                           |
| `SIGNED`                         | Factory          | Builds the given number preceded by an optional sign. |
| `SIGNED_INTEGER`                 | Regex Expression | An integer with an optional sign.                     |
| `SIGNED_NUMBER`                  | Regex Expression | An integer or decimal number with an optional sign.   |
| `ZERO`                           | Regex Expression | An integer equal to zero.                             |
| `POSITIVE`                       | Regex Expression | An integer greater than zero.                         |
| `NEGATIVE`                       | Regex Expression | An integer less than zero.                            |
| `NON_NEGATIVE`                   | Regex Expression | An integer greater than or equal to zero.             |
| `NON_POSITIVE`                   | Regex Expression | An integer less than or equal to zero.                |
| `NON_ZERO`                       | Regex Expression | An integer different from zero.                       |
| `BINARY`                         | Regex Expression | A binary number literal.                              |
| `OCTAL`                          | Regex Expression | An octal number literal.                              |
| `HEX`                            | Regex Expression | A hexadecimal number literal.                         |
| `EXPONENT`                       | Regex Expression | The exponent marker of scientific notation.           |
| `EXPONENT_PART`                  | Regex Expression | The exponent part of a number in scientific notation. |
| `SCIENTIFIC`                     | Regex Expression | An unsigned number in scientific notation.            |
| `FRACTION`                       | Regex Expression | A fraction written with a slash.                      |
| `RATIONAL_NUMBER`                | Regex Expression | A fraction with an optional sign.                     |
| `PERCENTAGE`                     | Regex Expression | A number followed by a percent sign.                  |
| `PERMILLE`                       | Regex Expression | A number followed by a per-mille sign.                |
| `DIGIT_NUMBER`                   | Factory          | Builds a number made of an exact count of digits.     |
| `ONE_DIGIT_NUMBER`               | Regex Expression | A number of exactly one digit.                        |
| `TWO_DIGIT_NUMBER`               | Regex Expression | A number of exactly two digits.                       |
| `THREE_DIGIT_NUMBER`             | Regex Expression | A number of exactly three digits.                     |
| `FOUR_DIGIT_NUMBER`              | Regex Expression | A number of exactly four digits.                      |
| `ZERO_TO_NINETY_NINE`            | Regex Expression | An integer from 0 to 99 without leading zeros.        |
| `ZERO_TO_TWO_HUNDRED_FIFTY_FIVE` | Regex Expression | An integer from 0 to 255 without leading zeros.       |
| `PORT_NUMBER`                    | Regex Expression | A network port number.                                |
| `YEAR_NUMBER`                    | Regex Expression | A four-digit year.                                    |
| `MONTH_NUMBER`                   | Regex Expression | A two-digit month number.                             |
| `DAY_NUMBER`                     | Regex Expression | A two-digit day-of-month number.                      |
| `HOUR_NUMBER`                    | Regex Expression | A two-digit hour in 24-hour form.                     |
| `MINUTE_NUMBER`                  | Regex Expression | A two-digit minute.                                   |
| `SECOND_NUMBER`                  | Regex Expression | A two-digit second.                                   |
| `LATITUDE`                       | Regex Expression | A latitude in decimal degrees.                        |
| `LONGITUDE`                      | Regex Expression | A longitude in decimal degrees.                       |
"""
