# 🔢 `patterns/numbers` — Detailed Reference

Numbers in text — integers, decimals, signs, bases, scientific notation, fixed-digit numbers, bounded ranges, and the number shapes used by dates, times, ports and coordinates.

Every card below is the term's full docstring. Terms are grouped by how they are defined: **pure** (a named concept), **composed** (built from other terms, or a parametrized factory) and **custom** (needed a semantic decision — read its notes).

All expressions are `simplibs.regex` objects: combine them with `+` (sequence) and `|` (alternation), wrap them with the presets (`ONE_OR_MORE`, `NAMED_GROUP`, …) and compile with `RegexPattern`.

---

## 🧭 Table of Contents

**pure**:

- [`INTEGER`](#integer)
- [`DECIMAL`](#decimal)
- [`INTEGER_PART`](#integer_part)
- [`FRACTIONAL_PART`](#fractional_part)
- [`DECIMAL_SEPARATOR`](#decimal_separator)
- [`ZERO_TO_NINE`](#zero_to_nine)
- [`BINARY`](#binary)
- [`OCTAL`](#octal)
- [`HEX`](#hex)
- [`EXPONENT`](#exponent)
- [`FRACTION`](#fraction)

**composed**:

- [`NUMBER`](#number)
- [`SIGNED`](#signed)
- [`SIGNED_INTEGER`](#signed_integer)
- [`SIGNED_NUMBER`](#signed_number)
- [`NON_NEGATIVE`](#non_negative)
- [`NON_POSITIVE`](#non_positive)
- [`NON_ZERO`](#non_zero)
- [`EXPONENT_PART`](#exponent_part)
- [`SCIENTIFIC`](#scientific)
- [`RATIONAL_NUMBER`](#rational_number)
- [`PERCENTAGE`](#percentage)
- [`PERMILLE`](#permille)
- [`DIGIT_NUMBER`](#digit_number)
- [`ONE_DIGIT_NUMBER`](#one_digit_number)
- [`TWO_DIGIT_NUMBER`](#two_digit_number)
- [`THREE_DIGIT_NUMBER`](#three_digit_number)
- [`FOUR_DIGIT_NUMBER`](#four_digit_number)

**custom**:

- [`ZERO`](#zero)
- [`POSITIVE`](#positive)
- [`NEGATIVE`](#negative)
- [`ZERO_TO_NINETY_NINE`](#zero_to_ninety_nine)
- [`ZERO_TO_TWO_HUNDRED_FIFTY_FIVE`](#zero_to_two_hundred_fifty_five)
- [`PORT_NUMBER`](#port_number)
- [`YEAR_NUMBER`](#year_number)
- [`MONTH_NUMBER`](#month_number)
- [`DAY_NUMBER`](#day_number)
- [`HOUR_NUMBER`](#hour_number)
- [`MINUTE_NUMBER`](#minute_number)
- [`SECOND_NUMBER`](#second_number)
- [`LATITUDE`](#latitude)
- [`LONGITUDE`](#longitude)

[⬅️ Back to main README](../README.md#-numbers--42-terms)

---

### `INTEGER`

Regex expression matching an unsigned whole number.

**Init Params:**
*(no parameters)*

**Pattern:**
One or more ASCII digits. Leading zeros are allowed.

```regex
[0-9]+
```

**Notes:**

Unsigned. For a sign use `SIGNED_INTEGER`; for zero / positive / negative checks see `ZERO`, `POSITIVE`, `NEGATIVE`.

**Example usage:**
```python
INTEGER
# Matches: "0", "42", "007"
# Does not match: "", "-5", "4.2", "abc"
```

[▲ Back to top](#-table-of-contents)

---

### `DECIMAL`

Regex expression matching an unsigned decimal number with a dot.

**Init Params:**
*(no parameters)*

**Pattern:**
An `INTEGER`, a dot and another `INTEGER`.

```regex
[0-9]+\.[0-9]+
```

**Example usage:**
```python
DECIMAL
# Matches: "3.14", "0.5", "10.000"
# Does not match: "3", ".5", "3.", "3,14"
```

[▲ Back to top](#-table-of-contents)

---

### `INTEGER_PART`

Regex expression matching the integer part of a decimal number.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `INTEGER`; the separate name states the intended role.

**Example usage:**
```python
INTEGER_PART
# Matches: "0", "42", "007"
# Does not match: "", "-5", "4.2", "abc"
```

[▲ Back to top](#-table-of-contents)

---

### `FRACTIONAL_PART`

Regex expression matching the fractional part of a decimal number.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `INTEGER`; the separate name states the intended role.

**Notes:**

The digits after the decimal separator.

**Example usage:**
```python
FRACTIONAL_PART
# Matches: "0", "42", "007"
# Does not match: "", "-5", "4.2", "abc"
```

[▲ Back to top](#-table-of-contents)

---

### `DECIMAL_SEPARATOR`

Regex expression matching the decimal separator.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `DOT`; the separate name states the intended role.

**Notes:**

Dot only for now.

**Example usage:**
```python
DECIMAL_SEPARATOR
# Matches: "."
# Does not match: "a", ".."
```

[▲ Back to top](#-table-of-contents)

---

### `ZERO_TO_NINE`

Regex expression matching a single digit from 0 to 9.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `DECIMAL_DIGIT`; the separate name states the intended role.

**Example usage:**
```python
ZERO_TO_NINE
# Matches: "0", "7", "9"
# Does not match: "a", "42", "٣"
```

[▲ Back to top](#-table-of-contents)

---

### `BINARY`

Regex expression matching a binary number literal.

**Init Params:**
*(no parameters)*

**Pattern:**
`0b` (or `0B`) followed by one or more binary digits.

```regex
0[bB][01]+
```

**Example usage:**
```python
BINARY
# Matches: "0b101", "0B1"
# Does not match: "0b", "0b2", "101"
```

[▲ Back to top](#-table-of-contents)

---

### `OCTAL`

Regex expression matching an octal number literal.

**Init Params:**
*(no parameters)*

**Pattern:**
`0o` (or `0O`) followed by one or more octal digits.

```regex
0[oO][0-7]+
```

**Example usage:**
```python
OCTAL
# Matches: "0o17", "0O7"
# Does not match: "0o", "0o8", "17"
```

[▲ Back to top](#-table-of-contents)

---

### `HEX`

Regex expression matching a hexadecimal number literal.

**Init Params:**
*(no parameters)*

**Pattern:**
`0x` (or `0X`) followed by one or more hexadecimal digits.

```regex
0[xX][0-9a-fA-F]+
```

**Example usage:**
```python
HEX
# Matches: "0xFF", "0X1a"
# Does not match: "0x", "0xG", "FF"
```

[▲ Back to top](#-table-of-contents)

---

### `EXPONENT`

Regex expression matching the exponent marker of scientific notation.

**Init Params:**
*(no parameters)*

**Pattern:**
Matches `e` or `E`.

```regex
[eE]
```

**Example usage:**
```python
EXPONENT
# Matches: "e", "E"
# Does not match: "x", "ee"
```

[▲ Back to top](#-table-of-contents)

---

### `FRACTION`

Regex expression matching a fraction written with a slash.

**Init Params:**
*(no parameters)*

**Pattern:**
An `INTEGER`, a slash and another `INTEGER`.

```regex
[0-9]+/[0-9]+
```

**Example usage:**
```python
FRACTION
# Matches: "1/2", "22/7"
# Does not match: "1/", "/2", "1.5/2"
```

[▲ Back to top](#-table-of-contents)

---

### `NUMBER`

Regex expression matching an unsigned integer or decimal number.

**Init Params:**
*(no parameters)*

**Pattern:**
A `DECIMAL` or an `INTEGER` (decimal is tried first so `3.14` is matched as a whole).

```regex
[0-9]+\.[0-9]+|[0-9]+
```

**Example usage:**
```python
NUMBER
# Matches: "42", "3.14", "0"
# Does not match: "", "-1", "1.", "abc"
```

[▲ Back to top](#-table-of-contents)

---

### `SIGNED`

Build a regex expression matching the given number preceded by an optional sign.

**Init Params:**
* `number` (*Regex*): The unsigned number expression to allow a sign in front of.

**Pattern:**
1. An optional `SIGN` (`+` or `-`).
2. The `number` expression.

**Example usage:**
```python
pattern = SIGNED(INTEGER)
# Regex: [+\-]?[0-9]+
# Matches: "42", "-42", "+42"
# Does not match: "--1", "- 1", "", "4-2"
```

[▲ Back to top](#-table-of-contents)

---

### `SIGNED_INTEGER`

Regex expression matching an integer with an optional sign.

**Init Params:**
*(no parameters)*

**Pattern:**
`SIGNED(INTEGER)`.

```regex
[+\-]?[0-9]+
```

**Example usage:**
```python
SIGNED_INTEGER
# Matches: "7", "-7", "+7"
# Does not match: "-", "7-", ""
```

[▲ Back to top](#-table-of-contents)

---

### `SIGNED_NUMBER`

Regex expression matching an integer or decimal number with an optional sign.

**Init Params:**
*(no parameters)*

**Pattern:**
`SIGNED(NUMBER)`.

```regex
[+\-]?(?:[0-9]+\.[0-9]+|[0-9]+)
```

**Example usage:**
```python
SIGNED_NUMBER
# Matches: "7", "-7.5", "+0.1"
# Does not match: "-", "7.", ".5"
```

[▲ Back to top](#-table-of-contents)

---

### `NON_NEGATIVE`

Regex expression matching an integer greater than or equal to zero.

**Init Params:**
*(no parameters)*

**Pattern:**
`ZERO` or `POSITIVE`.

```regex
[+\-]?0+|\+?0*[1-9][0-9]*
```

**Example usage:**
```python
NON_NEGATIVE
# Matches: "0", "5", "+5"
# Does not match: "-5", "", "1.5"
```

[▲ Back to top](#-table-of-contents)

---

### `NON_POSITIVE`

Regex expression matching an integer less than or equal to zero.

**Init Params:**
*(no parameters)*

**Pattern:**
`ZERO` or `NEGATIVE`.

```regex
[+\-]?0+|\-0*[1-9][0-9]*
```

**Example usage:**
```python
NON_POSITIVE
# Matches: "0", "-5", "-0"
# Does not match: "5", "+1", ""
```

[▲ Back to top](#-table-of-contents)

---

### `NON_ZERO`

Regex expression matching an integer different from zero.

**Init Params:**
*(no parameters)*

**Pattern:**
`POSITIVE` or `NEGATIVE`.

```regex
\+?0*[1-9][0-9]*|\-0*[1-9][0-9]*
```

**Example usage:**
```python
NON_ZERO
# Matches: "5", "-5", "+3"
# Does not match: "0", "-0", ""
```

[▲ Back to top](#-table-of-contents)

---

### `EXPONENT_PART`

Regex expression matching the exponent part of a number in scientific notation.

**Init Params:**
*(no parameters)*

**Pattern:**
An `EXPONENT` marker followed by a `SIGNED_INTEGER`.

```regex
[eE][+\-]?[0-9]+
```

**Example usage:**
```python
EXPONENT_PART
# Matches: "e10", "E-3", "e+5"
# Does not match: "e", "10", "e-"
```

[▲ Back to top](#-table-of-contents)

---

### `SCIENTIFIC`

Regex expression matching an unsigned number in scientific notation.

**Init Params:**
*(no parameters)*

**Pattern:**
A `NUMBER` followed by an `EXPONENT_PART`.

```regex
(?:[0-9]+\.[0-9]+|[0-9]+)[eE][+\-]?[0-9]+
```

**Notes:**

Unsigned mantissa; wrap with `SIGNED(SCIENTIFIC)` to allow a leading sign.

**Example usage:**
```python
SCIENTIFIC
# Matches: "1e10", "2.5E-3", "0.1e+2"
# Does not match: "1", "e5", "1e"
```

[▲ Back to top](#-table-of-contents)

---

### `RATIONAL_NUMBER`

Regex expression matching a fraction with an optional sign.

**Init Params:**
*(no parameters)*

**Pattern:**
`SIGNED(FRACTION)`.

```regex
[+\-]?[0-9]+/[0-9]+
```

**Example usage:**
```python
RATIONAL_NUMBER
# Matches: "1/2", "-3/4"
# Does not match: "1/", "-"
```

[▲ Back to top](#-table-of-contents)

---

### `PERCENTAGE`

Regex expression matching a number followed by a percent sign.

**Init Params:**
*(no parameters)*

**Pattern:**
A `NUMBER` and `%`.

```regex
(?:[0-9]+\.[0-9]+|[0-9]+)%
```

**Notes:**

Does not check the 0–100 range.

**Example usage:**
```python
PERCENTAGE
# Matches: "50%", "12.5%", "0%"
# Does not match: "50", "%", "-5%"
```

[▲ Back to top](#-table-of-contents)

---

### `PERMILLE`

Regex expression matching a number followed by a per-mille sign.

**Init Params:**
*(no parameters)*

**Pattern:**
A `NUMBER` and `‰`.

```regex
(?:[0-9]+\.[0-9]+|[0-9]+)‰
```

**Example usage:**
```python
PERMILLE
# Matches: "5‰", "0.5‰"
# Does not match: "5", "‰"
```

[▲ Back to top](#-table-of-contents)

---

### `DIGIT_NUMBER`

Build a regex expression matching a number made of an exact count of digits.

**Init Params:**
* `count` (*int*): The exact number of digits.

**Pattern:**
Exactly `count` ASCII digits (leading zeros allowed).

**Example usage:**
```python
pattern = DIGIT_NUMBER(3)
# Regex: [0-9]{3}
# Matches: "123", "007"
# Does not match: "12", "1234", "abc"
```

[▲ Back to top](#-table-of-contents)

---

### `ONE_DIGIT_NUMBER`

Regex expression matching a number of exactly one digit.

**Init Params:**
*(no parameters)*

**Pattern:**
`DIGIT_NUMBER(1)`.

```regex
[0-9]{1}
```

**Example usage:**
```python
ONE_DIGIT_NUMBER
# Matches: "7"
# Does not match: "12", ""
```

[▲ Back to top](#-table-of-contents)

---

### `TWO_DIGIT_NUMBER`

Regex expression matching a number of exactly two digits.

**Init Params:**
*(no parameters)*

**Pattern:**
`DIGIT_NUMBER(2)`.

```regex
[0-9]{2}
```

**Example usage:**
```python
TWO_DIGIT_NUMBER
# Matches: "12", "07"
# Does not match: "1", "123"
```

[▲ Back to top](#-table-of-contents)

---

### `THREE_DIGIT_NUMBER`

Regex expression matching a number of exactly three digits.

**Init Params:**
*(no parameters)*

**Pattern:**
`DIGIT_NUMBER(3)`.

```regex
[0-9]{3}
```

**Example usage:**
```python
THREE_DIGIT_NUMBER
# Matches: "123", "007"
# Does not match: "12", "1234"
```

[▲ Back to top](#-table-of-contents)

---

### `FOUR_DIGIT_NUMBER`

Regex expression matching a number of exactly four digits.

**Init Params:**
*(no parameters)*

**Pattern:**
`DIGIT_NUMBER(4)`.

```regex
[0-9]{4}
```

**Example usage:**
```python
FOUR_DIGIT_NUMBER
# Matches: "2026", "0001"
# Does not match: "202", "20260"
```

[▲ Back to top](#-table-of-contents)

---

### `ZERO`

Regex expression matching an integer equal to zero.

**Init Params:**
*(no parameters)*

**Pattern:**
An optional sign and one or more zeros.

```regex
[+\-]?0+
```

**Example usage:**
```python
ZERO
# Matches: "0", "00", "-0", "+0"
# Does not match: "1", "", "0.0", "10"
```

[▲ Back to top](#-table-of-contents)

---

### `POSITIVE`

Regex expression matching an integer greater than zero.

**Init Params:**
*(no parameters)*

**Pattern:**
An optional `+`, optional leading zeros, then a digit 1–9 and any further digits.

```regex
\+?0*[1-9][0-9]*
```

**Example usage:**
```python
POSITIVE
# Matches: "5", "+5", "007", "100"
# Does not match: "0", "-5", "00", "5.5"
```

[▲ Back to top](#-table-of-contents)

---

### `NEGATIVE`

Regex expression matching an integer less than zero.

**Init Params:**
*(no parameters)*

**Pattern:**
A `-`, optional leading zeros, then a digit 1–9 and any further digits.

```regex
\-0*[1-9][0-9]*
```

**Example usage:**
```python
NEGATIVE
# Matches: "-5", "-007", "-100"
# Does not match: "5", "-0", "0", "-5.5"
```

[▲ Back to top](#-table-of-contents)

---

### `ZERO_TO_NINETY_NINE`

Regex expression matching an integer from 0 to 99 without leading zeros.

**Init Params:**
*(no parameters)*

**Pattern:**
Two digits starting with 1–9, or a single digit.

```regex
[1-9][0-9]|[0-9]
```

**Example usage:**
```python
ZERO_TO_NINETY_NINE
# Matches: "0", "9", "10", "99"
# Does not match: "00", "01", "100", ""
```

[▲ Back to top](#-table-of-contents)

---

### `ZERO_TO_TWO_HUNDRED_FIFTY_FIVE`

Regex expression matching an integer from 0 to 255 without leading zeros.

**Init Params:**
*(no parameters)*

**Pattern:**
Any whole number `0`–`255`; `256`, `01` and `007` do not match.

```regex
25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9]
```

**Example usage:**
```python
ZERO_TO_TWO_HUNDRED_FIFTY_FIVE
# Matches: "0", "9", "10", "199"
# Does not match: "256", "01", "007", "-1"
```

[▲ Back to top](#-table-of-contents)

---

### `PORT_NUMBER`

Regex expression matching a network port number.

**Init Params:**
*(no parameters)*

**Pattern:**
Any whole number `0`–`65535` without leading zeros.

```regex
6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{0,3}|0
```

**Example usage:**
```python
PORT_NUMBER
# Matches: "0", "80", "8080", "65535"
# Does not match: "65536", "099", "-1", ""
```

[▲ Back to top](#-table-of-contents)

---

### `YEAR_NUMBER`

Regex expression matching a four-digit year.

**Init Params:**
*(no parameters)*

**Pattern:**
Exactly four digits (`0000`–`9999`).

```regex
[0-9]{4}
```

**Example usage:**
```python
YEAR_NUMBER
# Matches: "2026", "1999"
# Does not match: "26", "20260"
```

[▲ Back to top](#-table-of-contents)

---

### `MONTH_NUMBER`

Regex expression matching a two-digit month number.

**Init Params:**
*(no parameters)*

**Pattern:**
`01`–`12`, always two digits.

```regex
0[1-9]|1[0-2]
```

**Example usage:**
```python
MONTH_NUMBER
# Matches: "01", "09", "10", "12"
# Does not match: "00", "13", "1", "001"
```

[▲ Back to top](#-table-of-contents)

---

### `DAY_NUMBER`

Regex expression matching a two-digit day-of-month number.

**Init Params:**
*(no parameters)*

**Pattern:**
`01`–`31`, always two digits. Whether the day exists in a given month is not checked.

```regex
0[1-9]|[1-2][0-9]|3[01]
```

**Example usage:**
```python
DAY_NUMBER
# Matches: "01", "15", "29", "31"
# Does not match: "00", "32", "1", "40"
```

[▲ Back to top](#-table-of-contents)

---

### `HOUR_NUMBER`

Regex expression matching a two-digit hour in 24-hour form.

**Init Params:**
*(no parameters)*

**Pattern:**
`00`–`23`, always two digits.

```regex
[01][0-9]|2[0-3]
```

**Example usage:**
```python
HOUR_NUMBER
# Matches: "00", "09", "19", "23"
# Does not match: "24", "7", "123"
```

[▲ Back to top](#-table-of-contents)

---

### `MINUTE_NUMBER`

Regex expression matching a two-digit minute.

**Init Params:**
*(no parameters)*

**Pattern:**
`00`–`59`, always two digits.

```regex
[0-5][0-9]
```

**Example usage:**
```python
MINUTE_NUMBER
# Matches: "00", "30", "59"
# Does not match: "60", "5", "123"
```

[▲ Back to top](#-table-of-contents)

---

### `SECOND_NUMBER`

Regex expression matching a two-digit second.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `MINUTE_NUMBER`; the separate name states the intended role.

**Notes:**

`00`–`59`; leap seconds (`60`) are not accepted.

**Example usage:**
```python
SECOND_NUMBER
# Matches: "00", "30", "59"
# Does not match: "60", "5", "123"
```

[▲ Back to top](#-table-of-contents)

---

### `LATITUDE`

Regex expression matching a latitude in decimal degrees.

**Init Params:**
*(no parameters)*

**Pattern:**
A decimal number from `-90` to `90`; the fractional part is optional.

```regex
\-?(?:90(?:\.0+)?|[1-8]?[0-9](?:\.[0-9]+)?)
```

**Example usage:**
```python
LATITUDE
# Matches: "0", "45.5", "-33.865", "90"
# Does not match: "90.5", "91", "-91", "45."
```

[▲ Back to top](#-table-of-contents)

---

### `LONGITUDE`

Regex expression matching a longitude in decimal degrees.

**Init Params:**
*(no parameters)*

**Pattern:**
A decimal number from `-180` to `180`; the fractional part is optional.

```regex
\-?(?:180(?:\.0+)?|1[0-7][0-9](?:\.[0-9]+)?|[1-9]?[0-9](?:\.[0-9]+)?)
```

**Example usage:**
```python
LONGITUDE
# Matches: "0", "14.42", "-122.4194", "180"
# Does not match: "180.5", "181", "-181", "14."
```

[▲ Back to top](#-table-of-contents)

---

[⬅️ Back to main README](../README.md#-numbers--42-terms)
