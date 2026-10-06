# Pure:
from .pure.HOUR import HOUR
from .pure.MINUTE import MINUTE
from .pure.SECOND import SECOND
from .pure.HOUR_12 import HOUR_12
from .pure.AM import AM
from .pure.PM import PM
from .pure.TIME import TIME
from .pure.TIME_WITH_COLONS import TIME_WITH_COLONS
from .pure.TWENTY_FOUR_HOUR_TIME import TWENTY_FOUR_HOUR_TIME
from .pure.COMPACT_TIME import COMPACT_TIME
from .pure.TIME_WITHOUT_COLONS import TIME_WITHOUT_COLONS
# Composed:
from .composed.MILLISECOND import MILLISECOND
from .composed.MICROSECOND import MICROSECOND
from .composed.MERIDIEM import MERIDIEM
from .composed.TIMEZONE_OFFSET import TIMEZONE_OFFSET
from .composed.UTC_OFFSET import UTC_OFFSET
from .composed.TIMEZONE import TIMEZONE
from .composed.TIME_WITH_SECONDS import TIME_WITH_SECONDS
from .composed.TIME_WITH_FRACTION import TIME_WITH_FRACTION
from .composed.ISO_TIME import ISO_TIME
from .composed.TWELVE_HOUR_TIME import TWELVE_HOUR_TIME
from .composed.TIMEZONE_TIME import TIMEZONE_TIME
from .composed.UTC_TIME import UTC_TIME
from .composed.DATE_TIME import DATE_TIME
# Custom:
from .custom.TIMESTAMP import TIMESTAMP
from .custom.UNIX_TIMESTAMP import UNIX_TIMESTAMP


_DESIGN_NOTES = """
# Times Patterns Sub-Package

## Purpose
Times of day and moments in time — hours, minutes, seconds, fractions, AM/PM, time zones, ISO and 12/24-hour times, date-times and timestamps.

## Layout
`pure/` named concepts · `composed/` combinations of other terms and parametrized factories · `custom/` terms that needed a semantic decision

## Internal Components Registry

| Component               | Type             | Description                                |
| :---------------------- | :--------------- | :----------------------------------------- |
| `HOUR`                  | Regex Expression | A two-digit hour (00–23).                  |
| `MINUTE`                | Regex Expression | A two-digit minute (00–59).                |
| `SECOND`                | Regex Expression | A two-digit second (00–59).                |
| `HOUR_12`               | Regex Expression | A two-digit hour in 12-hour form.          |
| `MILLISECOND`           | Regex Expression | Three digits of milliseconds.              |
| `MICROSECOND`           | Regex Expression | Six digits of microseconds.                |
| `AM`                    | Regex Expression | The AM marker.                             |
| `PM`                    | Regex Expression | The PM marker.                             |
| `MERIDIEM`              | Regex Expression | An AM/PM marker.                           |
| `TIMEZONE_OFFSET`       | Regex Expression | A UTC offset such as +02:00.               |
| `UTC_OFFSET`            | Regex Expression | A UTC offset.                              |
| `TIMEZONE`              | Regex Expression | An ISO 8601 time zone designator.          |
| `TIME`                  | Regex Expression | A time in HH:MM form.                      |
| `TIME_WITH_COLONS`      | Regex Expression | A time written with colons.                |
| `TWENTY_FOUR_HOUR_TIME` | Regex Expression | A time in 24-hour form.                    |
| `TIME_WITH_SECONDS`     | Regex Expression | A time in HH:MM:SS form.                   |
| `TIME_WITH_FRACTION`    | Regex Expression | A time with seconds and a fractional part. |
| `ISO_TIME`              | Regex Expression | A time in ISO 8601 form.                   |
| `COMPACT_TIME`          | Regex Expression | A time written without separators.         |
| `TIME_WITHOUT_COLONS`   | Regex Expression | A time written without colons.             |
| `TWELVE_HOUR_TIME`      | Regex Expression | A time in 12-hour form with AM/PM.         |
| `TIMEZONE_TIME`         | Regex Expression | An ISO time with a time zone.              |
| `UTC_TIME`              | Regex Expression | An ISO time in UTC.                        |
| `DATE_TIME`             | Regex Expression | A date and a time together.                |
| `TIMESTAMP`             | Regex Expression | An ISO 8601 timestamp with a time zone.    |
| `UNIX_TIMESTAMP`        | Regex Expression | A Unix timestamp in seconds.               |
"""
