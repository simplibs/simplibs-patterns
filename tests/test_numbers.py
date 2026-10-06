from simplibs.regex.testing import assert_pattern

# Pure number patterns
from simplibs.patterns.numbers.pure.INTEGER import INTEGER
from simplibs.patterns.numbers.pure.DECIMAL import DECIMAL
from simplibs.patterns.numbers.pure.INTEGER_PART import INTEGER_PART
from simplibs.patterns.numbers.pure.FRACTIONAL_PART import FRACTIONAL_PART
from simplibs.patterns.numbers.pure.DECIMAL_SEPARATOR import DECIMAL_SEPARATOR
from simplibs.patterns.numbers.pure.ZERO_TO_NINE import ZERO_TO_NINE
from simplibs.patterns.numbers.pure.BINARY import BINARY
from simplibs.patterns.numbers.pure.OCTAL import OCTAL
from simplibs.patterns.numbers.pure.HEX import HEX
from simplibs.patterns.numbers.pure.EXPONENT import EXPONENT
from simplibs.patterns.numbers.pure.FRACTION import FRACTION

# Composed number patterns & factories
from simplibs.patterns.numbers.composed.NUMBER import NUMBER
from simplibs.patterns.numbers.composed.SIGNED import SIGNED
from simplibs.patterns.numbers.composed.SIGNED_INTEGER import SIGNED_INTEGER
from simplibs.patterns.numbers.composed.SIGNED_NUMBER import SIGNED_NUMBER
from simplibs.patterns.numbers.composed.NON_NEGATIVE import NON_NEGATIVE
from simplibs.patterns.numbers.composed.NON_POSITIVE import NON_POSITIVE
from simplibs.patterns.numbers.composed.NON_ZERO import NON_ZERO
from simplibs.patterns.numbers.composed.EXPONENT_PART import EXPONENT_PART
from simplibs.patterns.numbers.composed.SCIENTIFIC import SCIENTIFIC
from simplibs.patterns.numbers.composed.RATIONAL_NUMBER import RATIONAL_NUMBER
from simplibs.patterns.numbers.composed.PERCENTAGE import PERCENTAGE
from simplibs.patterns.numbers.composed.PERMILLE import PERMILLE
from simplibs.patterns.numbers.composed.DIGIT_NUMBER import DIGIT_NUMBER
from simplibs.patterns.numbers.composed.ONE_DIGIT_NUMBER import ONE_DIGIT_NUMBER
from simplibs.patterns.numbers.composed.TWO_DIGIT_NUMBER import TWO_DIGIT_NUMBER
from simplibs.patterns.numbers.composed.THREE_DIGIT_NUMBER import THREE_DIGIT_NUMBER
from simplibs.patterns.numbers.composed.FOUR_DIGIT_NUMBER import FOUR_DIGIT_NUMBER

# Custom number patterns
from simplibs.patterns.numbers.custom.ZERO import ZERO
from simplibs.patterns.numbers.custom.POSITIVE import POSITIVE
from simplibs.patterns.numbers.custom.NEGATIVE import NEGATIVE
from simplibs.patterns.numbers.custom.ZERO_TO_NINETY_NINE import ZERO_TO_NINETY_NINE
from simplibs.patterns.numbers.custom.ZERO_TO_TWO_HUNDRED_FIFTY_FIVE import ZERO_TO_TWO_HUNDRED_FIFTY_FIVE
from simplibs.patterns.numbers.custom.PORT_NUMBER import PORT_NUMBER
from simplibs.patterns.numbers.custom.YEAR_NUMBER import YEAR_NUMBER
from simplibs.patterns.numbers.custom.MONTH_NUMBER import MONTH_NUMBER
from simplibs.patterns.numbers.custom.DAY_NUMBER import DAY_NUMBER
from simplibs.patterns.numbers.custom.HOUR_NUMBER import HOUR_NUMBER
from simplibs.patterns.numbers.custom.MINUTE_NUMBER import MINUTE_NUMBER
from simplibs.patterns.numbers.custom.SECOND_NUMBER import SECOND_NUMBER
from simplibs.patterns.numbers.custom.LATITUDE import LATITUDE
from simplibs.patterns.numbers.custom.LONGITUDE import LONGITUDE


def test_integer(subtests):
    assert_pattern(
        subtests,
        INTEGER,
        r"[0-9]+",
        matches=["0", "42", "007"],
        non_matches=["", "-5", "4.2", "abc"]
    )

def test_decimal(subtests):
    assert_pattern(
        subtests,
        DECIMAL,
        r"[0-9]+\.[0-9]+",
        matches=["3.14", "0.5", "10.000"],
        non_matches=["3", ".5", "3.", "3,14"]
    )

def test_integer_part(subtests):
    assert_pattern(
        subtests,
        INTEGER_PART,
        r"[0-9]+",
        matches=["0", "42", "007"],
        non_matches=["", "-5", "4.2", "abc"]
    )

def test_fractional_part(subtests):
    assert_pattern(
        subtests,
        FRACTIONAL_PART,
        r"[0-9]+",
        matches=["0", "42", "007"],
        non_matches=["", "-5", "4.2", "abc"]
    )

def test_decimal_separator(subtests):
    assert_pattern(
        subtests,
        DECIMAL_SEPARATOR,
        r"\.",
        matches=["."],
        non_matches=["a", ".."]
    )

def test_zero_to_nine(subtests):
    assert_pattern(
        subtests,
        ZERO_TO_NINE,
        r"[0-9]",
        matches=["0", "7", "9"],
        non_matches=["a", "42", "٣"]
    )

def test_binary(subtests):
    assert_pattern(
        subtests,
        BINARY,
        r"0[bB][01]+",
        matches=["0b101", "0B1"],
        non_matches=["0b", "0b2", "101"]
    )

def test_octal(subtests):
    assert_pattern(
        subtests,
        OCTAL,
        r"0[oO][0-7]+",
        matches=["0o17", "0O7"],
        non_matches=["0o", "0o8", "17"]
    )

def test_hex(subtests):
    assert_pattern(
        subtests,
        HEX,
        r"0[xX][0-9a-fA-F]+",
        matches=["0xFF", "0X1a"],
        non_matches=["0x", "0xG", "FF"]
    )

def test_exponent(subtests):
    assert_pattern(
        subtests,
        EXPONENT,
        r"[eE]",
        matches=["e", "E"],
        non_matches=["x", "ee"]
    )

def test_fraction(subtests):
    assert_pattern(
        subtests,
        FRACTION,
        r"[0-9]+/[0-9]+",
        matches=["1/2", "22/7"],
        non_matches=["1/", "/2", "1.5/2"]
    )

def test_number(subtests):
    assert_pattern(
        subtests,
        NUMBER,
        r"[0-9]+\.[0-9]+|[0-9]+",
        matches=["42", "3.14", "0"],
        non_matches=["", "-1", "1.", "abc"]
    )

def test_signed(subtests):
    pattern = SIGNED(INTEGER)
    assert_pattern(
        subtests,
        pattern,
        r"[+\-]?[0-9]+",
        matches=["42", "-42", "+42"],
        non_matches=["--1", "- 1", "", "4-2"]
    )

def test_signed_integer(subtests):
    assert_pattern(
        subtests,
        SIGNED_INTEGER,
        r"[+\-]?[0-9]+",
        matches=["7", "-7", "+7"],
        non_matches=["-", "7-", ""]
    )

def test_signed_number(subtests):
    assert_pattern(
        subtests,
        SIGNED_NUMBER,
        r"[+\-]?(?:[0-9]+\.[0-9]+|[0-9]+)",
        matches=["7", "-7.5", "+0.1"],
        non_matches=["-", "7.", ".5"]
    )

def test_non_negative(subtests):
    assert_pattern(
        subtests,
        NON_NEGATIVE,
        r"[+\-]?0+|\+?0*[1-9][0-9]*",
        matches=["0", "5", "+5"],
        non_matches=["-5", "", "1.5"]
    )

def test_non_positive(subtests):
    assert_pattern(
        subtests,
        NON_POSITIVE,
        r"[+\-]?0+|\-0*[1-9][0-9]*",
        matches=["0", "-5", "-0"],
        non_matches=["5", "+1", ""]
    )

def test_non_zero(subtests):
    assert_pattern(
        subtests,
        NON_ZERO,
        r"\+?0*[1-9][0-9]*|\-0*[1-9][0-9]*",
        matches=["5", "-5", "+3"],
        non_matches=["0", "-0", ""]
    )

def test_exponent_part(subtests):
    assert_pattern(
        subtests,
        EXPONENT_PART,
        r"[eE][+\-]?[0-9]+",
        matches=["e10", "E-3", "e+5"],
        non_matches=["e", "10", "e-"]
    )

def test_scientific(subtests):
    assert_pattern(
        subtests,
        SCIENTIFIC,
        r"(?:[0-9]+\.[0-9]+|[0-9]+)[eE][+\-]?[0-9]+",
        matches=["1e10", "2.5E-3", "0.1e+2"],
        non_matches=["1", "e5", "1e"]
    )

def test_rational_number(subtests):
    assert_pattern(
        subtests,
        RATIONAL_NUMBER,
        r"[+\-]?[0-9]+/[0-9]+",
        matches=["1/2", "-3/4"],
        non_matches=["1/", "-"]
    )

def test_percentage(subtests):
    assert_pattern(
        subtests,
        PERCENTAGE,
        r"(?:[0-9]+\.[0-9]+|[0-9]+)%",
        matches=["50%", "12.5%", "0%"],
        non_matches=["50", "%", "-5%"]
    )

def test_permille(subtests):
    assert_pattern(
        subtests,
        PERMILLE,
        r"(?:[0-9]+\.[0-9]+|[0-9]+)‰",
        matches=["5‰", "0.5‰"],
        non_matches=["5", "‰"]
    )

def test_digit_number(subtests):
    pattern = DIGIT_NUMBER(3)
    assert_pattern(
        subtests,
        pattern,
        r"[0-9]{3}",
        matches=["123", "007"],
        non_matches=["12", "1234", "abc"]
    )

def test_one_digit_number(subtests):
    assert_pattern(
        subtests,
        ONE_DIGIT_NUMBER,
        r"[0-9]{1}",
        matches=["7"],
        non_matches=["12", ""]
    )

def test_two_digit_number(subtests):
    assert_pattern(
        subtests,
        TWO_DIGIT_NUMBER,
        r"[0-9]{2}",
        matches=["12", "07"],
        non_matches=["1", "123"]
    )

def test_three_digit_number(subtests):
    assert_pattern(
        subtests,
        THREE_DIGIT_NUMBER,
        r"[0-9]{3}",
        matches=["123", "007"],
        non_matches=["12", "1234"]
    )

def test_four_digit_number(subtests):
    assert_pattern(
        subtests,
        FOUR_DIGIT_NUMBER,
        r"[0-9]{4}",
        matches=["2026", "0001"],
        non_matches=["202", "20260"]
    )

def test_zero(subtests):
    assert_pattern(
        subtests,
        ZERO,
        r"[+\-]?0+",
        matches=["0", "00", "-0", "+0"],
        non_matches=["1", "", "0.0", "10"]
    )

def test_positive(subtests):
    assert_pattern(
        subtests,
        POSITIVE,
        r"\+?0*[1-9][0-9]*",
        matches=["5", "+5", "007", "100"],
        non_matches=["0", "-5", "00", "5.5"]
    )

def test_negative(subtests):
    assert_pattern(
        subtests,
        NEGATIVE,
        r"\-0*[1-9][0-9]*",
        matches=["-5", "-007", "-100"],
        non_matches=["5", "-0", "0", "-5.5"]
    )

def test_zero_to_ninety_nine(subtests):
    assert_pattern(
        subtests,
        ZERO_TO_NINETY_NINE,
        r"[1-9][0-9]|[0-9]",
        matches=["0", "9", "10", "99"],
        non_matches=["00", "01", "100", ""]
    )

def test_zero_to_two_hundred_fifty_five(subtests):
    assert_pattern(
        subtests,
        ZERO_TO_TWO_HUNDRED_FIFTY_FIVE,
        r"25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9]",
        matches=["0", "9", "10", "199"],
        non_matches=["256", "01", "007", "-1"]
    )

def test_port_number(subtests):
    assert_pattern(
        subtests,
        PORT_NUMBER,
        r"6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{0,3}|0",
        matches=["0", "80", "8080", "65535"],
        non_matches=["65536", "099", "-1", ""]
    )

def test_year_number(subtests):
    assert_pattern(
        subtests,
        YEAR_NUMBER,
        r"[0-9]{4}",
        matches=["2026", "1999"],
        non_matches=["26", "20260"]
    )

def test_month_number(subtests):
    assert_pattern(
        subtests,
        MONTH_NUMBER,
        r"0[1-9]|1[0-2]",
        matches=["01", "09", "10", "12"],
        non_matches=["00", "13", "1", "001"]
    )

def test_day_number(subtests):
    assert_pattern(
        subtests,
        DAY_NUMBER,
        r"0[1-9]|[1-2][0-9]|3[01]",
        matches=["01", "15", "29", "31"],
        non_matches=["00", "32", "1", "40"]
    )

def test_hour_number(subtests):
    assert_pattern(
        subtests,
        HOUR_NUMBER,
        r"[01][0-9]|2[0-3]",
        matches=["00", "09", "19", "23"],
        non_matches=["24", "7", "123"]
    )

def test_minute_number(subtests):
    assert_pattern(
        subtests,
        MINUTE_NUMBER,
        r"[0-5][0-9]",
        matches=["00", "30", "59"],
        non_matches=["60", "5", "123"]
    )

def test_second_number(subtests):
    assert_pattern(
        subtests,
        SECOND_NUMBER,
        r"[0-5][0-9]",
        matches=["00", "30", "59"],
        non_matches=["60", "5", "123"]
    )

def test_latitude(subtests):
    assert_pattern(
        subtests,
        LATITUDE,
        r"\-?(?:90(?:\.0+)?|[1-8]?[0-9](?:\.[0-9]+)?)",
        matches=["0", "45.5", "-33.865", "90"],
        non_matches=["90.5", "91", "-91", "45."]
    )

def test_longitude(subtests):
    assert_pattern(
        subtests,
        LONGITUDE,
        r"\-?(?:180(?:\.0+)?|1[0-7][0-9](?:\.[0-9]+)?|[1-9]?[0-9](?:\.[0-9]+)?)",
        matches=["0", "14.42", "-122.4194", "180"],
        non_matches=["180.5", "181", "-181", "14."]
    )