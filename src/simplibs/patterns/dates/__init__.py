# Pure:
from .pure.YEAR import YEAR
from .pure.MONTH import MONTH
from .pure.DAY import DAY
from .pure.DAY_OF_MONTH import DAY_OF_MONTH
from .pure.WEEKDAY import WEEKDAY
from .pure.QUARTER import QUARTER
from .pure.ISO_DATE import ISO_DATE
from .pure.DATE import DATE
from .pure.CALENDAR_DATE import CALENDAR_DATE
from .pure.EUROPEAN_DATE import EUROPEAN_DATE
from .pure.US_DATE import US_DATE
from .pure.ORDINAL_DATE import ORDINAL_DATE
from .pure.WEEK_DATE import WEEK_DATE
# Composed:
from .composed.DATE_WITH_SEPARATOR import DATE_WITH_SEPARATOR
# Custom:
from .custom.DAY_OF_YEAR import DAY_OF_YEAR
from .custom.WEEK_NUMBER import WEEK_NUMBER
from .custom.MONTH_NAME import MONTH_NAME
from .custom.MONTH_ABBREVIATION import MONTH_ABBREVIATION
from .custom.WEEKDAY_NAME import WEEKDAY_NAME
from .custom.WEEKDAY_ABBREVIATION import WEEKDAY_ABBREVIATION


_DESIGN_NOTES = """
# Dates Patterns Sub-Package

## Purpose
Calendar dates and their components — year, month, day, week, weekday names, quarter, and the ISO, European, US, ordinal and week date layouts.

## Layout
`pure/` named concepts · `composed/` combinations of other terms and parametrized factories · `custom/` terms that needed a semantic decision

## Internal Components Registry

| Component              | Type             | Description                                           |
| :--------------------- | :--------------- | :---------------------------------------------------- |
| `YEAR`                 | Regex Expression | A four-digit year.                                    |
| `MONTH`                | Regex Expression | A two-digit month.                                    |
| `DAY`                  | Regex Expression | A two-digit day.                                      |
| `DAY_OF_MONTH`         | Regex Expression | A two-digit day of the month.                         |
| `DAY_OF_YEAR`          | Regex Expression | A three-digit day of the year.                        |
| `WEEK_NUMBER`          | Regex Expression | A two-digit ISO week number.                          |
| `WEEKDAY`              | Regex Expression | An ISO weekday number.                                |
| `QUARTER`              | Regex Expression | A calendar quarter.                                   |
| `MONTH_NAME`           | Regex Expression | An English month name.                                |
| `MONTH_ABBREVIATION`   | Regex Expression | A three-letter English month abbreviation.            |
| `WEEKDAY_NAME`         | Regex Expression | An English weekday name.                              |
| `WEEKDAY_ABBREVIATION` | Regex Expression | A three-letter English weekday abbreviation.          |
| `ISO_DATE`             | Regex Expression | A date in ISO 8601 form.                              |
| `DATE`                 | Regex Expression | A calendar date.                                      |
| `CALENDAR_DATE`        | Regex Expression | A calendar date.                                      |
| `EUROPEAN_DATE`        | Regex Expression | A date in day.month.year form.                        |
| `US_DATE`              | Regex Expression | A date in month/day/year form.                        |
| `ORDINAL_DATE`         | Regex Expression | A year with a day-of-year number.                     |
| `WEEK_DATE`            | Regex Expression | An ISO week date.                                     |
| `DATE_WITH_SEPARATOR`  | Factory          | Builds a year-month-day date with a custom separator. |
"""
