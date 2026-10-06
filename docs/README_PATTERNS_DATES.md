# 📅 `patterns/dates` — Detailed Reference

Calendar dates and their components — year, month, day, week, weekday names, quarter, and the ISO, European, US, ordinal and week date layouts.

Every card below is the term's full docstring. Terms are grouped by how they are defined: **pure** (a named concept), **composed** (built from other terms, or a parametrized factory) and **custom** (needed a semantic decision — read its notes).

All expressions are `simplibs.regex` objects: combine them with `+` (sequence) and `|` (alternation), wrap them with the presets (`ONE_OR_MORE`, `NAMED_GROUP`, …) and compile with `RegexPattern`.

---

## 🧭 Table of Contents

**pure**:

- [`YEAR`](#year)
- [`MONTH`](#month)
- [`DAY`](#day)
- [`DAY_OF_MONTH`](#day_of_month)
- [`WEEKDAY`](#weekday)
- [`QUARTER`](#quarter)
- [`ISO_DATE`](#iso_date)
- [`DATE`](#date)
- [`CALENDAR_DATE`](#calendar_date)
- [`EUROPEAN_DATE`](#european_date)
- [`US_DATE`](#us_date)
- [`ORDINAL_DATE`](#ordinal_date)
- [`WEEK_DATE`](#week_date)

**composed**:

- [`DATE_WITH_SEPARATOR`](#date_with_separator)

**custom**:

- [`DAY_OF_YEAR`](#day_of_year)
- [`WEEK_NUMBER`](#week_number)
- [`MONTH_NAME`](#month_name)
- [`MONTH_ABBREVIATION`](#month_abbreviation)
- [`WEEKDAY_NAME`](#weekday_name)
- [`WEEKDAY_ABBREVIATION`](#weekday_abbreviation)
---

### `YEAR`

Regex expression matching a four-digit year.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `YEAR_NUMBER`; the separate name states the intended role.

**Example usage:**
```python
YEAR
# Matches: "2026", "1999"
# Does not match: "26", "20260"
```

[▲ Back to top](#-table-of-contents)

---

### `MONTH`

Regex expression matching a two-digit month.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `MONTH_NUMBER`; the separate name states the intended role.

**Example usage:**
```python
MONTH
# Matches: "01", "09", "10", "12"
# Does not match: "00", "13", "1", "001"
```

[▲ Back to top](#-table-of-contents)

---

### `DAY`

Regex expression matching a two-digit day.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `DAY_NUMBER`; the separate name states the intended role.

**Example usage:**
```python
DAY
# Matches: "01", "15", "29", "31"
# Does not match: "00", "32", "1", "40"
```

[▲ Back to top](#-table-of-contents)

---

### `DAY_OF_MONTH`

Regex expression matching a two-digit day of the month.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `DAY_NUMBER`; the separate name states the intended role.

**Example usage:**
```python
DAY_OF_MONTH
# Matches: "01", "15", "29", "31"
# Does not match: "00", "32", "1", "40"
```

[▲ Back to top](#-table-of-contents)

---

### `WEEKDAY`

Regex expression matching an ISO weekday number.

**Init Params:**
*(no parameters)*

**Pattern:**
`1` (Monday) to `7` (Sunday).

```regex
[1-7]
```

**Example usage:**
```python
WEEKDAY
# Matches: "1", "7"
# Does not match: "0", "8", "12"
```

[▲ Back to top](#-table-of-contents)

---

### `QUARTER`

Regex expression matching a calendar quarter.

**Init Params:**
*(no parameters)*

**Pattern:**
`Q1`–`Q4`.

```regex
Q[1-4]
```

**Example usage:**
```python
QUARTER
# Matches: "Q1", "Q4"
# Does not match: "Q0", "Q5", "1"
```

[▲ Back to top](#-table-of-contents)

---

### `ISO_DATE`

Regex expression matching a date in ISO 8601 form.

**Init Params:**
*(no parameters)*

**Pattern:**
`YYYY-MM-DD`: `YEAR`, `MONTH` and `DAY`, joined by hyphens.

```regex
[0-9]{4}\-(?:0[1-9]|1[0-2])\-(?:0[1-9]|[1-2][0-9]|3[01])
```

**Notes:**

Checks the shape and the ranges of month (01–12) and day (01–31), not whether the day exists in that month.

**Example usage:**
```python
ISO_DATE
# Matches: "2026-09-30", "1999-01-01"
# Does not match: "2026-9-30", "30.09.2026", "2026-13-01", "2026-00-10"
```

[▲ Back to top](#-table-of-contents)

---

### `DATE`

Regex expression matching a calendar date.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `ISO_DATE`; the separate name states the intended role.

**Notes:**

`DATE` means the ISO form. Other layouts: `EUROPEAN_DATE`, `US_DATE`.

**Example usage:**
```python
DATE
# Matches: "2026-09-30", "1999-01-01"
# Does not match: "2026-9-30", "30.09.2026", "2026-13-01", "2026-00-10"
```

[▲ Back to top](#-table-of-contents)

---

### `CALENDAR_DATE`

Regex expression matching a calendar date.

**Init Params:**
*(no parameters)*

**Pattern:**
Same expression as `ISO_DATE`; the separate name states the intended role.

**Example usage:**
```python
CALENDAR_DATE
# Matches: "2026-09-30", "1999-01-01"
# Does not match: "2026-9-30", "30.09.2026", "2026-13-01", "2026-00-10"
```

[▲ Back to top](#-table-of-contents)

---

### `EUROPEAN_DATE`

Regex expression matching a date in day.month.year form.

**Init Params:**
*(no parameters)*

**Pattern:**
`DD.MM.YYYY`: `DAY`, `MONTH` and `YEAR`, joined by dots.

```regex
(?:0[1-9]|[1-2][0-9]|3[01])\.(?:0[1-9]|1[0-2])\.[0-9]{4}
```

**Notes:**

Zero-padded only (`30. 9. 2026` and `30.9.2026` are not matched).

**Example usage:**
```python
EUROPEAN_DATE
# Matches: "30.09.2026", "01.01.1999"
# Does not match: "30.9.2026", "2026-09-30", "32.01.2026"
```

[▲ Back to top](#-table-of-contents)

---

### `US_DATE`

Regex expression matching a date in month/day/year form.

**Init Params:**
*(no parameters)*

**Pattern:**
`MM/DD/YYYY`: `MONTH`, `DAY` and `YEAR`, joined by slashes.

```regex
(?:0[1-9]|1[0-2])/(?:0[1-9]|[1-2][0-9]|3[01])/[0-9]{4}
```

**Example usage:**
```python
US_DATE
# Matches: "09/30/2026", "01/01/1999"
# Does not match: "30/09/2026", "9/30/2026", "2026/09/30"
```

[▲ Back to top](#-table-of-contents)

---

### `ORDINAL_DATE`

Regex expression matching a year with a day-of-year number.

**Init Params:**
*(no parameters)*

**Pattern:**
`YYYY-DDD`: `YEAR` and `DAY_OF_YEAR`.

```regex
[0-9]{4}\-(?:00[1-9]|0[1-9][0-9]|[1-2][0-9]{2}|3[0-5][0-9]|36[0-6])
```

**Example usage:**
```python
ORDINAL_DATE
# Matches: "2026-273", "1999-001"
# Does not match: "2026-000", "2026-367", "2026-27"
```

[▲ Back to top](#-table-of-contents)

---

### `WEEK_DATE`

Regex expression matching an ISO week date.

**Init Params:**
*(no parameters)*

**Pattern:**
`YYYY-Www-D`: `YEAR`, `W`, `WEEK_NUMBER`, hyphen and `WEEKDAY`.

```regex
[0-9]{4}\-W(?:0[1-9]|[1-4][0-9]|5[0-3])\-[1-7]
```

**Example usage:**
```python
WEEK_DATE
# Matches: "2026-W40-3", "1999-W01-1"
# Does not match: "2026-W54-1", "2026-40-3", "2026-W40-8"
```

[▲ Back to top](#-table-of-contents)

---

### `DATE_WITH_SEPARATOR`

Build a regex expression matching a year-month-day date with a custom separator.

**Init Params:**
* `separator` (*str*): The literal text placed between the three parts.

**Pattern:**
`YEAR`, `separator`, `MONTH`, `separator`, `DAY`.

**Example usage:**
```python
pattern = DATE_WITH_SEPARATOR("/")
# Regex: [0-9]{4}/(?:0[1-9]|1[0-2])/(?:0[1-9]|[1-2][0-9]|3[01])
# Matches: "2026/09/30"
# Does not match: "2026-09-30", "2026/9/30"
```

[▲ Back to top](#-table-of-contents)

---

### `DAY_OF_YEAR`

Regex expression matching a three-digit day of the year.

**Init Params:**
*(no parameters)*

**Pattern:**
`001`–`366`, always three digits.

```regex
00[1-9]|0[1-9][0-9]|[1-2][0-9]{2}|3[0-5][0-9]|36[0-6]
```

**Example usage:**
```python
DAY_OF_YEAR
# Matches: "001", "059", "300", "366"
# Does not match: "000", "367", "1", "0001"
```

[▲ Back to top](#-table-of-contents)

---

### `WEEK_NUMBER`

Regex expression matching a two-digit ISO week number.

**Init Params:**
*(no parameters)*

**Pattern:**
`01`–`53`, always two digits.

```regex
0[1-9]|[1-4][0-9]|5[0-3]
```

**Example usage:**
```python
WEEK_NUMBER
# Matches: "01", "09", "27", "53"
# Does not match: "00", "54", "5", "100"
```

[▲ Back to top](#-table-of-contents)

---

### `MONTH_NAME`

Regex expression matching an English month name.

**Init Params:**
*(no parameters)*

**Pattern:**
A full English month name, capitalised: `January` … `December`.

```regex
January|February|March|April|May|June|July|August|September|October|November|December
```

**Notes:**

English and case-sensitive. Use the `IGNORECASE` flag for case-insensitive matching.

**Example usage:**
```python
MONTH_NAME
# Matches: "January", "May", "December"
# Does not match: "january", "Mar", "Sept"
```

[▲ Back to top](#-table-of-contents)

---

### `MONTH_ABBREVIATION`

Regex expression matching a three-letter English month abbreviation.

**Init Params:**
*(no parameters)*

**Pattern:**
`Jan`, `Feb`, `Mar`, … `Dec`.

```regex
Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec
```

**Notes:**

English, three letters, case-sensitive.

**Example usage:**
```python
MONTH_ABBREVIATION
# Matches: "Jan", "May", "Dec"
# Does not match: "jan", "Sept", "January"
```

[▲ Back to top](#-table-of-contents)

---

### `WEEKDAY_NAME`

Regex expression matching an English weekday name.

**Init Params:**
*(no parameters)*

**Pattern:**
A full English weekday name, capitalised: `Monday` … `Sunday`.

```regex
Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday
```

**Notes:**

English and case-sensitive.

**Example usage:**
```python
WEEKDAY_NAME
# Matches: "Monday", "Sunday"
# Does not match: "monday", "Mon"
```

[▲ Back to top](#-table-of-contents)

---

### `WEEKDAY_ABBREVIATION`

Regex expression matching a three-letter English weekday abbreviation.

**Init Params:**
*(no parameters)*

**Pattern:**
`Mon`, `Tue`, `Wed`, … `Sun`.

```regex
Mon|Tue|Wed|Thu|Fri|Sat|Sun
```

**Notes:**

English, three letters, case-sensitive.

**Example usage:**
```python
WEEKDAY_ABBREVIATION
# Matches: "Mon", "Sun"
# Does not match: "mon", "Monday"
```

[▲ Back to top](#-table-of-contents)

---

[⬅️ Back to main README](../README.md)
