from simplibs.regex.testing import assert_pattern

# Pure date patterns
from simplibs.patterns.dates.pure.YEAR import YEAR
from simplibs.patterns.dates.pure.MONTH import MONTH
from simplibs.patterns.dates.pure.DAY import DAY
from simplibs.patterns.dates.pure.DAY_OF_MONTH import DAY_OF_MONTH
from simplibs.patterns.dates.pure.WEEKDAY import WEEKDAY
from simplibs.patterns.dates.pure.QUARTER import QUARTER
from simplibs.patterns.dates.pure.ISO_DATE import ISO_DATE
from simplibs.patterns.dates.pure.DATE import DATE
from simplibs.patterns.dates.pure.CALENDAR_DATE import CALENDAR_DATE
from simplibs.patterns.dates.pure.EUROPEAN_DATE import EUROPEAN_DATE
from simplibs.patterns.dates.pure.US_DATE import US_DATE
from simplibs.patterns.dates.pure.ORDINAL_DATE import ORDINAL_DATE
from simplibs.patterns.dates.pure.WEEK_DATE import WEEK_DATE

# Composed date patterns & factories
from simplibs.patterns.dates.composed.DATE_WITH_SEPARATOR import DATE_WITH_SEPARATOR

# Custom date patterns
from simplibs.patterns.dates.custom.DAY_OF_YEAR import DAY_OF_YEAR
from simplibs.patterns.dates.custom.WEEK_NUMBER import WEEK_NUMBER
from simplibs.patterns.dates.custom.MONTH_NAME import MONTH_NAME
from simplibs.patterns.dates.custom.MONTH_ABBREVIATION import MONTH_ABBREVIATION
from simplibs.patterns.dates.custom.WEEKDAY_NAME import WEEKDAY_NAME
from simplibs.patterns.dates.custom.WEEKDAY_ABBREVIATION import WEEKDAY_ABBREVIATION


def test_year(subtests):
    assert_pattern(
        subtests,
        YEAR,
        r"[0-9]{4}",
        matches=["2026", "1999"],
        non_matches=["26", "20260"]
    )

def test_month(subtests):
    assert_pattern(
        subtests,
        MONTH,
        r"0[1-9]|1[0-2]",
        matches=["01", "09", "10", "12"],
        non_matches=["00", "13", "1", "001"]
    )

def test_day(subtests):
    assert_pattern(
        subtests,
        DAY,
        r"0[1-9]|[1-2][0-9]|3[01]",
        matches=["01", "15", "29", "31"],
        non_matches=["00", "32", "1", "40"]
    )

def test_day_of_month(subtests):
    assert_pattern(
        subtests,
        DAY_OF_MONTH,
        r"0[1-9]|[1-2][0-9]|3[01]",
        matches=["01", "15", "29", "31"],
        non_matches=["00", "32", "1", "40"]
    )

def test_weekday(subtests):
    assert_pattern(
        subtests,
        WEEKDAY,
        r"[1-7]",
        matches=["1", "7"],
        non_matches=["0", "8", "12"]
    )

def test_quarter(subtests):
    assert_pattern(
        subtests,
        QUARTER,
        r"Q[1-4]",
        matches=["Q1", "Q4"],
        non_matches=["Q0", "Q5", "1"]
    )

def test_iso_date(subtests):
    assert_pattern(
        subtests,
        ISO_DATE,
        r"[0-9]{4}\-(?:0[1-9]|1[0-2])\-(?:0[1-9]|[1-2][0-9]|3[01])",
        matches=["2026-09-30", "1999-01-01"],
        non_matches=["2026-9-30", "30.09.2026", "2026-13-01", "2026-00-10"]
    )

def test_date(subtests):
    assert_pattern(
        subtests,
        DATE,
        r"[0-9]{4}\-(?:0[1-9]|1[0-2])\-(?:0[1-9]|[1-2][0-9]|3[01])",
        matches=["2026-09-30", "1999-01-01"],
        non_matches=["2026-9-30", "30.09.2026", "2026-13-01", "2026-00-10"]
    )

def test_calendar_date(subtests):
    assert_pattern(
        subtests,
        CALENDAR_DATE,
        r"[0-9]{4}\-(?:0[1-9]|1[0-2])\-(?:0[1-9]|[1-2][0-9]|3[01])",
        matches=["2026-09-30", "1999-01-01"],
        non_matches=["2026-9-30", "30.09.2026", "2026-13-01", "2026-00-10"]
    )

def test_european_date(subtests):
    assert_pattern(
        subtests,
        EUROPEAN_DATE,
        r"(?:0[1-9]|[1-2][0-9]|3[01])\.(?:0[1-9]|1[0-2])\.[0-9]{4}",
        matches=["30.09.2026", "01.01.1999"],
        non_matches=["30.9.2026", "2026-09-30", "32.01.2026"]
    )

def test_us_date(subtests):
    assert_pattern(
        subtests,
        US_DATE,
        r"(?:0[1-9]|1[0-2])/(?:0[1-9]|[1-2][0-9]|3[01])/[0-9]{4}",
        matches=["09/30/2026", "01/01/1999"],
        non_matches=["30/09/2026", "9/30/2026", "2026/09/30"]
    )

def test_ordinal_date(subtests):
    assert_pattern(
        subtests,
        ORDINAL_DATE,
        r"[0-9]{4}\-(?:00[1-9]|0[1-9][0-9]|[1-2][0-9]{2}|3[0-5][0-9]|36[0-6])",
        matches=["2026-273", "1999-001"],
        non_matches=["2026-000", "2026-367", "2026-27"]
    )

def test_week_date(subtests):
    assert_pattern(
        subtests,
        WEEK_DATE,
        r"[0-9]{4}\-W(?:0[1-9]|[1-4][0-9]|5[0-3])\-[1-7]",
        matches=["2026-W40-3", "1999-W01-1"],
        non_matches=["2026-W54-1", "2026-40-3", "2026-W40-8"]
    )

def test_date_with_separator(subtests):
    pattern = DATE_WITH_SEPARATOR("/")
    assert_pattern(
        subtests,
        pattern,
        r"[0-9]{4}/(?:0[1-9]|1[0-2])/(?:0[1-9]|[1-2][0-9]|3[01])",
        matches=["2026/09/30"],
        non_matches=["2026-09-30", "2026/9/30"]
    )

def test_day_of_year(subtests):
    assert_pattern(
        subtests,
        DAY_OF_YEAR,
        r"00[1-9]|0[1-9][0-9]|[1-2][0-9]{2}|3[0-5][0-9]|36[0-6]",
        matches=["001", "059", "300", "366"],
        non_matches=["000", "367", "1", "0001"]
    )

def test_week_number(subtests):
    assert_pattern(
        subtests,
        WEEK_NUMBER,
        r"0[1-9]|[1-4][0-9]|5[0-3]",
        matches=["01", "09", "27", "53"],
        non_matches=["00", "54", "5", "100"]
    )

def test_month_name(subtests):
    assert_pattern(
        subtests,
        MONTH_NAME,
        r"January|February|March|April|May|June|July|August|September|October|November|December",
        matches=["January", "May", "December"],
        non_matches=["january", "Mar", "Sept"]
    )

def test_month_abbreviation(subtests):
    assert_pattern(
        subtests,
        MONTH_ABBREVIATION,
        r"Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec",
        matches=["Jan", "May", "Dec"],
        non_matches=["jan", "Sept", "January"]
    )

def test_weekday_name(subtests):
    assert_pattern(
        subtests,
        WEEKDAY_NAME,
        r"Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday",
        matches=["Monday", "Sunday"],
        non_matches=["monday", "Mon"]
    )

def test_weekday_abbreviation(subtests):
    assert_pattern(
        subtests,
        WEEKDAY_ABBREVIATION,
        r"Mon|Tue|Wed|Thu|Fri|Sat|Sun",
        matches=["Mon", "Sun"],
        non_matches=["mon", "Monday"]
    )