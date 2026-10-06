# 🕒 `patterns/times` — Detailed Reference

Times of day and moments in time — hours, minutes, seconds, fractions, AM/PM, time zones, ISO and 12/24-hour times, date-times and timestamps.

Every card below is the term's full docstring. Terms are grouped by how they are defined: **pure** (a named concept), **composed** (built from other terms, or a parametrized factory) and **custom** (needed a semantic decision — read its notes).

All expressions are `simplibs.regex` objects: combine them with `+` (sequence) and `|` (alternation), wrap them with the presets (`ONE_OR_MORE`, `NAMED_GROUP`, …) and compile with `RegexPattern`.

---

## 🧭 Table of Contents

**pure**:

- [`HOUR`](#hour)
- [`MINUTE`](#minute)
- [`SECOND`](#second)
- [`HOUR_12`](#hour_12)
- [`AM`](#am)
- [`PM`](#pm)
- [`TIME`](#time)
- [`TIME_WITH_COLONS`](#time_with_colons)
- [`TWENTY_FOUR_HOUR_TIME`](#twenty_four_hour_time)
- [`COMPACT_TIME`](#compact_time)
- [`TIME_WITHOUT_COLONS`](#time_without_colons)

**composed**:

- [`MILLISECOND`](#millisecond)
- [`MICROSECOND`](#microsecond)
- [`MERIDIEM`](#meridiem)
- [`TIMEZONE_OFFSET`](#timezone_offset)
- [`UTC_OFFSET`](#utc_offset)
- [`TIMEZONE`](#timezone)
- [`TIME_WITH_SECONDS`](#time_with_seconds)
- [`TIME_WITH_FRACTION`](#time_with_fraction)
- [`ISO_TIME`](#iso_time)
- [`TWELVE_HOUR_TIME`](#twelve_hour_time)
- [`TIMEZONE_TIME`](#timezone_time)
- [`UTC_TIME`](#utc_time)
- [`DATE_TIME`](#date_time)

**custom**:

- [`TIMESTAMP`](#timestamp)
- [`UNIX_TIMESTAMP`](#unix_timestamp)

[⬅️ Back to main README](../README.md#-times--26-terms)

---

### `HOUR`

Regex expression matching a two-digit hour (00–23).

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `HOUR_NUMBER`; the separate name states the intended role.

**Example usage:**
```python
HOUR
# Matches: "00", "09", "19", "23"
# Does not match: "24", "7", "123"
```

[▲ Back to top](#-table-of-contents)

---

### `MINUTE`

Regex expression matching a two-digit minute (00–59).

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `MINUTE_NUMBER`; the separate name states the intended role.

**Example usage:**
```python
MINUTE
# Matches: "00", "30", "59"
# Does not match: "60", "5", "123"
```

[▲ Back to top](#-table-of-contents)

---

### `SECOND`

Regex expression matching a two-digit second (00–59).

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `SECOND_NUMBER`; the separate name states the intended role.

**Example usage:**
```python
SECOND
# Matches: "00", "30", "59"
# Does not match: "60", "5", "123"
```

[▲ Back to top](#-table-of-contents)

---

### `HOUR_12`

Regex expression matching a two-digit hour in 12-hour form.

**Init Params:**
*(no parameters)*

**Pattern:**
`01`–`12`, always two digits.

```regex
0[1-9]|1[0-2]
```

**Example usage:**
```python
HOUR_12
# Matches: "01", "09", "12"
# Does not match: "00", "13", "1"
```

[▲ Back to top](#-table-of-contents)

---

### `AM`

Regex expression matching the AM marker.

**Init Params:**
*(no parameters)*

**Pattern:**
The text `AM`.

```regex
AM
```

**Example usage:**
```python
AM
# Matches: "AM"
# Does not match: "PM", "am"
```

[▲ Back to top](#-table-of-contents)

---

### `PM`

Regex expression matching the PM marker.

**Init Params:**
*(no parameters)*

**Pattern:**
The text `PM`.

```regex
PM
```

**Example usage:**
```python
PM
# Matches: "PM"
# Does not match: "AM", "pm"
```

[▲ Back to top](#-table-of-contents)

---

### `TIME`

Regex expression matching a time in HH:MM form.

**Init Params:**
*(no parameters)*

**Pattern:**
`HOUR`, colon, `MINUTE` (24-hour).

```regex
(?:[01][0-9]|2[0-3]):[0-5][0-9]
```

**Example usage:**
```python
TIME
# Matches: "00:00", "14:30", "23:59"
# Does not match: "24:00", "7:30", "14:60", "1430"
```

[▲ Back to top](#-table-of-contents)

---

### `TIME_WITH_COLONS`

Regex expression matching a time written with colons.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `TIME`; the separate name states the intended role.

**Example usage:**
```python
TIME_WITH_COLONS
# Matches: "00:00", "14:30", "23:59"
# Does not match: "24:00", "7:30", "14:60", "1430"
```

[▲ Back to top](#-table-of-contents)

---

### `TWENTY_FOUR_HOUR_TIME`

Regex expression matching a time in 24-hour form.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `TIME`; the separate name states the intended role.

**Example usage:**
```python
TWENTY_FOUR_HOUR_TIME
# Matches: "00:00", "14:30", "23:59"
# Does not match: "24:00", "7:30", "14:60", "1430"
```

[▲ Back to top](#-table-of-contents)

---

### `COMPACT_TIME`

Regex expression matching a time written without separators.

**Init Params:**
*(no parameters)*

**Pattern:**
`HOUR` immediately followed by `MINUTE` (`HHMM`).

```regex
(?:[01][0-9]|2[0-3])[0-5][0-9]
```

**Example usage:**
```python
COMPACT_TIME
# Matches: "1430", "0000", "2359"
# Does not match: "14:30", "2400", "143"
```

[▲ Back to top](#-table-of-contents)

---

### `TIME_WITHOUT_COLONS`

Regex expression matching a time written without colons.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `COMPACT_TIME`; the separate name states the intended role.

**Example usage:**
```python
TIME_WITHOUT_COLONS
# Matches: "1430", "0000", "2359"
# Does not match: "14:30", "2400", "143"
```

[▲ Back to top](#-table-of-contents)

---

### `MILLISECOND`

Regex expression matching three digits of milliseconds.

**Init Params:**
*(no parameters)*

**Pattern:**
Exactly three digits (`000`–`999`).

```regex
[0-9]{3}
```

**Example usage:**
```python
MILLISECOND
# Matches: "000", "123"
# Does not match: "12", "1234"
```

[▲ Back to top](#-table-of-contents)

---

### `MICROSECOND`

Regex expression matching six digits of microseconds.

**Init Params:**
*(no parameters)*

**Pattern:**
Exactly six digits (`000000`–`999999`).

```regex
[0-9]{6}
```

**Example usage:**
```python
MICROSECOND
# Matches: "000123", "999999"
# Does not match: "123", "1234567"
```

[▲ Back to top](#-table-of-contents)

---

### `MERIDIEM`

Regex expression matching an AM/PM marker.

**Init Params:**
*(no parameters)*

**Pattern:**
`AM` or `PM` (uppercase).

```regex
AM|PM
```

**Example usage:**
```python
MERIDIEM
# Matches: "AM", "PM"
# Does not match: "am", "A.M.", ""
```

[▲ Back to top](#-table-of-contents)

---

### `TIMEZONE_OFFSET`

Regex expression matching a UTC offset such as +02:00.

**Init Params:**
*(no parameters)*

**Pattern:**
`SIGN`, `HOUR`, colon, `MINUTE`.

```regex
[+\-](?:[01][0-9]|2[0-3]):[0-5][0-9]
```

**Example usage:**
```python
TIMEZONE_OFFSET
# Matches: "+02:00", "-05:30", "+00:00"
# Does not match: "02:00", "+2:00", "+24:00", "+0200"
```

[▲ Back to top](#-table-of-contents)

---

### `UTC_OFFSET`

Regex expression matching a UTC offset.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `TIMEZONE_OFFSET`; the separate name states the intended role.

**Example usage:**
```python
UTC_OFFSET
# Matches: "+02:00", "-05:30", "+00:00"
# Does not match: "02:00", "+2:00", "+24:00", "+0200"
```

[▲ Back to top](#-table-of-contents)

---

### `TIMEZONE`

Regex expression matching an ISO 8601 time zone designator.

**Init Params:**
*(no parameters)*

**Pattern:**
`Z` (UTC) or a `TIMEZONE_OFFSET`.

```regex
Z|[+\-](?:[01][0-9]|2[0-3]):[0-5][0-9]
```

**Example usage:**
```python
TIMEZONE
# Matches: "Z", "+02:00", "-05:00"
# Does not match: "z", "UTC", "+2"
```

[▲ Back to top](#-table-of-contents)

---

### `TIME_WITH_SECONDS`

Regex expression matching a time in HH:MM:SS form.

**Init Params:**
*(no parameters)*

**Pattern:**
A `TIME`, colon, `SECOND`.

```regex
(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]
```

**Example usage:**
```python
TIME_WITH_SECONDS
# Matches: "00:00:00", "14:30:05"
# Does not match: "14:30", "14:30:60"
```

[▲ Back to top](#-table-of-contents)

---

### `TIME_WITH_FRACTION`

Regex expression matching a time with seconds and a fractional part.

**Init Params:**
*(no parameters)*

**Pattern:**
A `TIME_WITH_SECONDS`, a dot and one or more digits.

```regex
(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]\.[0-9]+
```

**Example usage:**
```python
TIME_WITH_FRACTION
# Matches: "14:30:05.123", "00:00:00.5"
# Does not match: "14:30:05", "14:30:05."
```

[▲ Back to top](#-table-of-contents)

---

### `ISO_TIME`

Regex expression matching a time in ISO 8601 form.

**Init Params:**
*(no parameters)*

**Pattern:**
A `TIME_WITH_SECONDS`, optionally followed by a dot and fraction digits.

```regex
(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](?:\.[0-9]+)?
```

**Example usage:**
```python
ISO_TIME
# Matches: "14:30:05", "14:30:05.123"
# Does not match: "14:30", "14:30:05."
```

[▲ Back to top](#-table-of-contents)

---

### `TWELVE_HOUR_TIME`

Regex expression matching a time in 12-hour form with AM/PM.

**Init Params:**
*(no parameters)*

**Pattern:**
`HOUR_12`, colon, `MINUTE`, an optional space and `MERIDIEM`.

```regex
(?:0[1-9]|1[0-2]):[0-5][0-9]\ ?(?:AM|PM)
```

**Example usage:**
```python
TWELVE_HOUR_TIME
# Matches: "09:30 AM", "12:00PM"
# Does not match: "13:00 PM", "09:30", "9:30 AM"
```

[▲ Back to top](#-table-of-contents)

---

### `TIMEZONE_TIME`

Regex expression matching an ISO time with a time zone.

**Init Params:**
*(no parameters)*

**Pattern:**
An `ISO_TIME` followed by a `TIMEZONE`.

```regex
(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](?:\.[0-9]+)?(?:Z|[+\-](?:[01][0-9]|2[0-3]):[0-5][0-9])
```

**Example usage:**
```python
TIMEZONE_TIME
# Matches: "14:30:05Z", "14:30:05+02:00"
# Does not match: "14:30:05", "14:30Z"
```

[▲ Back to top](#-table-of-contents)

---

### `UTC_TIME`

Regex expression matching an ISO time in UTC.

**Init Params:**
*(no parameters)*

**Pattern:**
An `ISO_TIME` followed by `Z`.

```regex
(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](?:\.[0-9]+)?Z
```

**Example usage:**
```python
UTC_TIME
# Matches: "14:30:05Z", "14:30:05.123Z"
# Does not match: "14:30:05", "14:30:05+00:00"
```

[▲ Back to top](#-table-of-contents)

---

### `DATE_TIME`

Regex expression matching a date and a time together.

**Init Params:**
*(no parameters)*

**Pattern:**
An `ISO_DATE`, a `T` or a space, and an `ISO_TIME`.

```regex
[0-9]{4}\-(?:0[1-9]|1[0-2])\-(?:0[1-9]|[1-2][0-9]|3[01])[T ](?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](?:\.[0-9]+)?
```

**Example usage:**
```python
DATE_TIME
# Matches: "2026-09-30T14:30:05", "2026-09-30 14:30:05.5"
# Does not match: "2026-09-30", "14:30:05", "2026-09-30T14:30"
```

[▲ Back to top](#-table-of-contents)

---

### `TIMESTAMP`

Regex expression matching an ISO 8601 timestamp with a time zone.

**Init Params:**
*(no parameters)*

**Pattern:**
A `DATE_TIME` followed by a mandatory `TIMEZONE`.

```regex
[0-9]{4}\-(?:0[1-9]|1[0-2])\-(?:0[1-9]|[1-2][0-9]|3[01])[T ](?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](?:\.[0-9]+)?(?:Z|[+\-](?:[01][0-9]|2[0-3]):[0-5][0-9])
```

**Example usage:**
```python
TIMESTAMP
# Matches: "2026-09-30T14:30:05Z", "2026-09-30T14:30:05+02:00"
# Does not match: "2026-09-30T14:30:05", "2026-09-30"
```

[▲ Back to top](#-table-of-contents)

---

### `UNIX_TIMESTAMP`

Regex expression matching a Unix timestamp in seconds.

**Init Params:**
*(no parameters)*

**Pattern:**
One to ten digits (up to the year 2286).

```regex
[0-9]{1,10}
```

**Example usage:**
```python
UNIX_TIMESTAMP
# Matches: "0", "1790000000", "86400"
# Does not match: "", "-1", "17900000000", "1.5"
```

[▲ Back to top](#-table-of-contents)

---

[⬅️ Back to main README](../README.md#-times--26-terms)
