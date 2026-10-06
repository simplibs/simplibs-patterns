from simplibs.regex.testing import assert_pattern

# Pure time patterns
from simplibs.patterns.times.pure.HOUR import HOUR
from simplibs.patterns.times.pure.MINUTE import MINUTE
from simplibs.patterns.times.pure.SECOND import SECOND
from simplibs.patterns.times.pure.HOUR_12 import HOUR_12
from simplibs.patterns.times.pure.AM import AM
from simplibs.patterns.times.pure.PM import PM
from simplibs.patterns.times.pure.TIME import TIME
from simplibs.patterns.times.pure.TIME_WITH_COLONS import TIME_WITH_COLONS
from simplibs.patterns.times.pure.TWENTY_FOUR_HOUR_TIME import TWENTY_FOUR_HOUR_TIME
from simplibs.patterns.times.pure.COMPACT_TIME import COMPACT_TIME
from simplibs.patterns.times.pure.TIME_WITHOUT_COLONS import TIME_WITHOUT_COLONS

# Composed time patterns
from simplibs.patterns.times.composed.MILLISECOND import MILLISECOND
from simplibs.patterns.times.composed.MICROSECOND import MICROSECOND
from simplibs.patterns.times.composed.MERIDIEM import MERIDIEM
from simplibs.patterns.times.composed.TIMEZONE_OFFSET import TIMEZONE_OFFSET
from simplibs.patterns.times.composed.UTC_OFFSET import UTC_OFFSET
from simplibs.patterns.times.composed.TIMEZONE import TIMEZONE
from simplibs.patterns.times.composed.TIME_WITH_SECONDS import TIME_WITH_SECONDS
from simplibs.patterns.times.composed.TIME_WITH_FRACTION import TIME_WITH_FRACTION
from simplibs.patterns.times.composed.ISO_TIME import ISO_TIME
from simplibs.patterns.times.composed.TWELVE_HOUR_TIME import TWELVE_HOUR_TIME
from simplibs.patterns.times.composed.TIMEZONE_TIME import TIMEZONE_TIME
from simplibs.patterns.times.composed.UTC_TIME import UTC_TIME
from simplibs.patterns.times.composed.DATE_TIME import DATE_TIME

# Custom time patterns
from simplibs.patterns.times.custom.TIMESTAMP import TIMESTAMP
from simplibs.patterns.times.custom.UNIX_TIMESTAMP import UNIX_TIMESTAMP


def test_hour(subtests):
    assert_pattern(
        subtests,
        HOUR,
        r"[01][0-9]|2[0-3]",
        matches=["00", "09", "19", "23"],
        non_matches=["24", "7", "123"]
    )

def test_minute(subtests):
    assert_pattern(
        subtests,
        MINUTE,
        r"[0-5][0-9]",
        matches=["00", "30", "59"],
        non_matches=["60", "5", "123"]
    )

def test_second(subtests):
    assert_pattern(
        subtests,
        SECOND,
        r"[0-5][0-9]",
        matches=["00", "30", "59"],
        non_matches=["60", "5", "123"]
    )

def test_hour_12(subtests):
    assert_pattern(
        subtests,
        HOUR_12,
        r"0[1-9]|1[0-2]",
        matches=["01", "09", "12"],
        non_matches=["00", "13", "1"]
    )

def test_am(subtests):
    assert_pattern(
        subtests,
        AM,
        r"AM",
        matches=["AM"],
        non_matches=["PM", "am"]
    )

def test_pm(subtests):
    assert_pattern(
        subtests,
        PM,
        r"PM",
        matches=["PM"],
        non_matches=["AM", "pm"]
    )

def test_time(subtests):
    assert_pattern(
        subtests,
        TIME,
        r"(?:[01][0-9]|2[0-3]):[0-5][0-9]",
        matches=["00:00", "14:30", "23:59"],
        non_matches=["24:00", "7:30", "14:60", "1430"]
    )

def test_time_with_colons(subtests):
    assert_pattern(
        subtests,
        TIME_WITH_COLONS,
        r"(?:[01][0-9]|2[0-3]):[0-5][0-9]",
        matches=["00:00", "14:30", "23:59"],
        non_matches=["24:00", "7:30", "14:60", "1430"]
    )

def test_twenty_four_hour_time(subtests):
    assert_pattern(
        subtests,
        TWENTY_FOUR_HOUR_TIME,
        r"(?:[01][0-9]|2[0-3]):[0-5][0-9]",
        matches=["00:00", "14:30", "23:59"],
        non_matches=["24:00", "7:30", "14:60", "1430"]
    )

def test_compact_time(subtests):
    assert_pattern(
        subtests,
        COMPACT_TIME,
        r"(?:[01][0-9]|2[0-3])[0-5][0-9]",
        matches=["1430", "0000", "2359"],
        non_matches=["14:30", "2400", "143"]
    )

def test_time_without_colons(subtests):
    assert_pattern(
        subtests,
        TIME_WITHOUT_COLONS,
        r"(?:[01][0-9]|2[0-3])[0-5][0-9]",
        matches=["1430", "0000", "2359"],
        non_matches=["14:30", "2400", "143"]
    )

def test_millisecond(subtests):
    assert_pattern(
        subtests,
        MILLISECOND,
        r"[0-9]{3}",
        matches=["000", "123"],
        non_matches=["12", "1234"]
    )

def test_microsecond(subtests):
    assert_pattern(
        subtests,
        MICROSECOND,
        r"[0-9]{6}",
        matches=["000123", "999999"],
        non_matches=["123", "1234567"]
    )

def test_meridiem(subtests):
    assert_pattern(
        subtests,
        MERIDIEM,
        r"AM|PM",
        matches=["AM", "PM"],
        non_matches=["am", "A.M.", ""]
    )

def test_timezone_offset(subtests):
    assert_pattern(
        subtests,
        TIMEZONE_OFFSET,
        r"[+\-](?:[01][0-9]|2[0-3]):[0-5][0-9]",
        matches=["+02:00", "-05:30", "+00:00"],
        non_matches=["02:00", "+2:00", "+24:00", "+0200"]
    )

def test_utc_offset(subtests):
    assert_pattern(
        subtests,
        UTC_OFFSET,
        r"[+\-](?:[01][0-9]|2[0-3]):[0-5][0-9]",
        matches=["+02:00", "-05:30", "+00:00"],
        non_matches=["02:00", "+2:00", "+24:00", "+0200"]
    )

def test_timezone(subtests):
    assert_pattern(
        subtests,
        TIMEZONE,
        r"Z|[+\-](?:[01][0-9]|2[0-3]):[0-5][0-9]",
        matches=["Z", "+02:00", "-05:00"],
        non_matches=["z", "UTC", "+2"]
    )

def test_time_with_seconds(subtests):
    assert_pattern(
        subtests,
        TIME_WITH_SECONDS,
        r"(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]",
        matches=["00:00:00", "14:30:05"],
        non_matches=["14:30", "14:30:60"]
    )

def test_time_with_fraction(subtests):
    assert_pattern(
        subtests,
        TIME_WITH_FRACTION,
        r"(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]\.[0-9]+",
        matches=["14:30:05.123", "00:00:00.5"],
        non_matches=["14:30:05", "14:30:05."]
    )

def test_iso_time(subtests):
    assert_pattern(
        subtests,
        ISO_TIME,
        r"(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](?:\.[0-9]+)?",
        matches=["14:30:05", "14:30:05.123"],
        non_matches=["14:30", "14:30:05."]
    )

def test_twelve_hour_time(subtests):
    assert_pattern(
        subtests,
        TWELVE_HOUR_TIME,
        r"(?:0[1-9]|1[0-2]):[0-5][0-9]\ ?(?:AM|PM)",
        matches=["09:30 AM", "12:00PM"],
        non_matches=["13:00 PM", "09:30", "9:30 AM"]
    )

def test_timezone_time(subtests):
    assert_pattern(
        subtests,
        TIMEZONE_TIME,
        r"(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](?:\.[0-9]+)?(?:Z|[+\-](?:[01][0-9]|2[0-3]):[0-5][0-9])",
        matches=["14:30:05Z", "14:30:05+02:00"],
        non_matches=["14:30:05", "14:30Z"]
    )

def test_utc_time(subtests):
    assert_pattern(
        subtests,
        UTC_TIME,
        r"(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](?:\.[0-9]+)?Z",
        matches=["14:30:05Z", "14:30:05.123Z"],
        non_matches=["14:30:05", "14:30:05+00:00"]
    )

def test_date_time(subtests):
    assert_pattern(
        subtests,
        DATE_TIME,
        r"[0-9]{4}\-(?:0[1-9]|1[0-2])\-(?:0[1-9]|[1-2][0-9]|3[01])[T ](?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](?:\.[0-9]+)?",
        matches=["2026-09-30T14:30:05", "2026-09-30 14:30:05.5"],
        non_matches=["2026-09-30", "14:30:05", "2026-09-30T14:30"]
    )

def test_timestamp(subtests):
    assert_pattern(
        subtests,
        TIMESTAMP,
        r"[0-9]{4}\-(?:0[1-9]|1[0-2])\-(?:0[1-9]|[1-2][0-9]|3[01])[T ](?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](?:\.[0-9]+)?(?:Z|[+\-](?:[01][0-9]|2[0-3]):[0-5][0-9])",
        matches=["2026-09-30T14:30:05Z", "2026-09-30T14:30:05+02:00"],
        non_matches=["2026-09-30T14:30:05", "2026-09-30"]
    )

def test_unix_timestamp(subtests):
    assert_pattern(
        subtests,
        UNIX_TIMESTAMP,
        r"[0-9]{1,10}",
        matches=["0", "1790000000", "86400"],
        non_matches=["", "-1", "17900000000", "1.5"]
    )