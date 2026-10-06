from simplibs.regex.testing import assert_pattern

# Pure formats patterns
from simplibs.patterns.formats.pure.UUID import UUID
from simplibs.patterns.formats.pure.GUID import GUID
from simplibs.patterns.formats.pure.HEX_COLOR import HEX_COLOR
from simplibs.patterns.formats.pure.VERSION import VERSION
from simplibs.patterns.formats.pure.MAC_ADDRESS import MAC_ADDRESS
from simplibs.patterns.formats.pure.IPV4_ADDRESS import IPV4_ADDRESS
from simplibs.patterns.formats.pure.ISBN10 import ISBN10
from simplibs.patterns.formats.pure.ISBN13 import ISBN13
from simplibs.patterns.formats.pure.ISSN import ISSN
from simplibs.patterns.formats.pure.BASE64_CHARACTER import BASE64_CHARACTER
from simplibs.patterns.formats.pure.BASE64_URL_CHARACTER import BASE64_URL_CHARACTER
from simplibs.patterns.formats.pure.HEX_STRING import HEX_STRING
from simplibs.patterns.formats.pure.MD5 import MD5
from simplibs.patterns.formats.pure.SHA1 import SHA1
from simplibs.patterns.formats.pure.SHA256 import SHA256

# Composed formats patterns
from simplibs.patterns.formats.composed.RGB_COLOR import RGB_COLOR
from simplibs.patterns.formats.composed.RGBA_COLOR import RGBA_COLOR
from simplibs.patterns.formats.composed.ISBN import ISBN
from simplibs.patterns.formats.composed.HASH import HASH

# Custom formats patterns
from simplibs.patterns.formats.custom.SEMVER import SEMVER
from simplibs.patterns.formats.custom.IPV6_ADDRESS import IPV6_ADDRESS
from simplibs.patterns.formats.custom.CREDIT_CARD_NUMBER import CREDIT_CARD_NUMBER
from simplibs.patterns.formats.custom.IBAN import IBAN
from simplibs.patterns.formats.custom.BASE64 import BASE64
from simplibs.patterns.formats.custom.BASE64_URL import BASE64_URL
from simplibs.patterns.formats.custom.ULID import ULID
from simplibs.patterns.formats.custom.JWT import JWT


def test_uuid(subtests):
    assert_pattern(
        subtests,
        UUID,
        r"[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}",
        matches=["123e4567-e89b-12d3-a456-426614174000", "00000000-0000-0000-0000-000000000000"],
        non_matches=["123e4567e89b12d3a456426614174000", "123e4567-e89b-12d3-a456-42661417400", "g23e4567-e89b-12d3-a456-426614174000"]
    )

def test_guid(subtests):
    assert_pattern(
        subtests,
        GUID,
        r"[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}",
        matches=["123e4567-e89b-12d3-a456-426614174000", "00000000-0000-0000-0000-000000000000"],
        non_matches=["123e4567e89b12d3a456426614174000", "123e4567-e89b-12d3-a456-42661417400", "g23e4567-e89b-12d3-a456-426614174000"]
    )

def test_hex_color(subtests):
    assert_pattern(
        subtests,
        HEX_COLOR,
        r"\#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})",
        matches=["#fff", "#1A2B3C"],
        non_matches=["#ffff", "fff", "#ggg"]
    )

def test_version(subtests):
    assert_pattern(
        subtests,
        VERSION,
        r"[0-9]+(?:\.[0-9]+)+",
        matches=["1.2", "10.0.3", "2026.9.30"],
        non_matches=["1", "1.", "v1.2", "1.a"]
    )

def test_mac_address(subtests):
    assert_pattern(
        subtests,
        MAC_ADDRESS,
        r"[0-9a-fA-F]{2}(?::[0-9a-fA-F]{2}){5}",
        matches=["00:1A:2B:3C:4D:5E", "ff:ff:ff:ff:ff:ff"],
        non_matches=["00-1A-2B-3C-4D-5E", "00:1A:2B:3C:4D", "00:1A:2B:3C:4D:5G"]
    )

def test_ipv4_address(subtests):
    assert_pattern(
        subtests,
        IPV4_ADDRESS,
        r"(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){3}",
        matches=["192.168.0.1", "0.0.0.0", "255.255.255.255"],
        non_matches=["256.1.1.1", "1.2.3", "01.2.3.4", "1.2.3.4.5"]
    )

def test_isbn10(subtests):
    assert_pattern(
        subtests,
        ISBN10,
        r"[0-9]{9}[0-9Xx]",
        matches=["0306406152", "080442957X"],
        non_matches=["030640615", "03064061523", "0306-406152"]
    )

def test_isbn13(subtests):
    assert_pattern(
        subtests,
        ISBN13,
        r"97[89][0-9]{10}",
        matches=["9780306406157", "9791234567896"],
        non_matches=["9770306406157", "978030640615", "978-0306406157"]
    )

def test_issn(subtests):
    assert_pattern(
        subtests,
        ISSN,
        r"[0-9]{4}\-[0-9]{3}[0-9Xx]",
        matches=["0317-8471", "2434-561X"],
        non_matches=["03178471", "0317-847", "0317-84711"]
    )

def test_base64_character(subtests):
    assert_pattern(
        subtests,
        BASE64_CHARACTER,
        r"[A-Za-z0-9+/]",
        matches=["A", "z", "5", "+"],
        non_matches=["-", "_", "="]
    )

def test_base64_url_character(subtests):
    assert_pattern(
        subtests,
        BASE64_URL_CHARACTER,
        r"[A-Za-z0-9\-_]",
        matches=["A", "z", "5", "-"],
        non_matches=["+", "/", "="]
    )

def test_hex_string(subtests):
    assert_pattern(
        subtests,
        HEX_STRING,
        r"[0-9a-fA-F]+",
        matches=["deadBEEF", "00", "1f"],
        non_matches=["xyz", "", "0x1f"]
    )

def test_md5(subtests):
    assert_pattern(
        subtests,
        MD5,
        r"[0-9a-fA-F]{32}",
        matches=["d41d8cd98f00b204e9800998ecf8427e"],
        non_matches=["d41d8cd98f00b204e9800998ecf8427", "d41d8cd98f00b204e9800998ecf8427g"]
    )

def test_sha1(subtests):
    assert_pattern(
        subtests,
        SHA1,
        r"[0-9a-fA-F]{40}",
        matches=["da39a3ee5e6b4b0d3255bfef95601890afd80709"],
        non_matches=["da39a3ee5e6b4b0d3255bfef95601890afd8070"]
    )

def test_sha256(subtests):
    assert_pattern(
        subtests,
        SHA256,
        r"[0-9a-fA-F]{64}",
        matches=["e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"],
        non_matches=["e3b0c44298fc1c14"]
    )

def test_rgb_color(subtests):
    assert_pattern(
        subtests,
        RGB_COLOR,
        r"rgb\((?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(?:,\ *(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){2}\)",
        matches=["rgb(255, 0, 0)", "rgb(0,0,0)"],
        non_matches=["rgb(256,0,0)", "rgb(1,2)", "rgba(0,0,0,1)"]
    )

def test_rgba_color(subtests):
    assert_pattern(
        subtests,
        RGBA_COLOR,
        r"rgba\((?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(?:,\ *(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){2},\ *(?:0(?:\.[0-9]+)?|1(?:\.0+)?|\.[0-9]+)\)",
        matches=["rgba(255, 0, 0, 0.5)", "rgba(0,0,0,1)", "rgba(0,0,0,.25)"],
        non_matches=["rgba(0,0,0)", "rgba(0,0,0,2)", "rgba(0,0,0,1.5)"]
    )

def test_isbn(subtests):
    assert_pattern(
        subtests,
        ISBN,
        r"97[89][0-9]{10}|[0-9]{9}[0-9Xx]",
        matches=["9780306406157", "0306406152"],
        non_matches=["12345", ""]
    )

def test_hash(subtests):
    assert_pattern(
        subtests,
        HASH,
        r"[0-9a-fA-F]{64}|[0-9a-fA-F]{40}|[0-9a-fA-F]{32}",
        matches=["d41d8cd98f00b204e9800998ecf8427e", "da39a3ee5e6b4b0d3255bfef95601890afd80709"],
        non_matches=["abc", "d41d8cd98f00b204e9800998ecf8427"]
    )

def test_semver(subtests):
    assert_pattern(
        subtests,
        SEMVER,
        r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)(?:\-[a-zA-Z0-9\-]+(?:\.[a-zA-Z0-9\-]+)*)?(?:\+[a-zA-Z0-9\-]+(?:\.[a-zA-Z0-9\-]+)*)?",
        matches=["1.2.3", "1.0.0-alpha.1", "1.0.0+build.5", "2.1.0-rc.1+sha.ab12"],
        non_matches=["1.2", "01.2.3", "1.2.3.4", "v1.2.3"]
    )

def test_ipv6_address(subtests):
    assert_pattern(
        subtests,
        IPV6_ADDRESS,
        r"(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?::[0-9a-fA-F]{1,4}){1,6}|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)",
        matches=["2001:db8::ff00:42:8329", "::1", "::", "fe80::1"],
        non_matches=["1:2:3:4:5:6:7", "1::2::3", "12345::1", "g::1"]
    )

def test_credit_card_number(subtests):
    assert_pattern(
        subtests,
        CREDIT_CARD_NUMBER,
        r"[0-9]{13,19}",
        matches=["4111111111111111", "378282246310005"],
        non_matches=["411111111111", "41111 1111 1111 1111", "41111111111111111111"]
    )

def test_iban(subtests):
    assert_pattern(
        subtests,
        IBAN,
        r"[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}",
        matches=["CZ6508000000192000145399", "GB82WEST12345698765432"],
        non_matches=["cz6508000000192000145399", "CZ65", "CZ65 0800 0000 1920 0014 5399"]
    )

def test_base64(subtests):
    assert_pattern(
        subtests,
        BASE64,
        r"(?:[A-Za-z0-9+/]{4})+(?:[A-Za-z0-9+/]{2}={2}|[A-Za-z0-9+/]{3}=)?|[A-Za-z0-9+/]{2}={2}|[A-Za-z0-9+/]{3}=",
        matches=["aGVsbG8=", "aGVsbG8gd29ybGQ=", "QUJD", "YQ=="],
        non_matches=["aGVsbG8", "a", "not base64!", ""]
    )

def test_base64_url(subtests):
    assert_pattern(
        subtests,
        BASE64_URL,
        r"[A-Za-z0-9\-_]+={0,2}",
        matches=["aGVsbG8", "a-b_c", "aGVsbG8="],
        non_matches=["a+b", "a/b", ""]
    )

def test_ulid(subtests):
    assert_pattern(
        subtests,
        ULID,
        r"[0-7][0-9A-HJKMNP-TV-Z]{25}",
        matches=["01ARZ3NDEKTSV4RRFFQ69G5FAV", "7ZZZZZZZZZZZZZZZZZZZZZZZZZ"],
        non_matches=["81ARZ3NDEKTSV4RRFFQ69G5FAV", "01ARZ3NDEKTSV4RRFFQ69G5FAI", "01arz3ndektsv4rrffq69g5fav", "01ARZ3NDEKTSV4RRFFQ69G5FA"]
    )

def test_jwt(subtests):
    assert_pattern(
        subtests,
        JWT,
        r"[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+",
        matches=["eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk"],
        non_matches=["a.b", "a.b.c.d", "abc"]
    )