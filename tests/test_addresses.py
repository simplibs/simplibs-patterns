from simplibs.regex.testing import assert_pattern

# Pure addresses patterns
from simplibs.patterns.addresses.pure.EMAIL_LOCAL_PART import EMAIL_LOCAL_PART

# Composed addresses patterns
from simplibs.patterns.addresses.composed.IP_ADDRESS import IP_ADDRESS
from simplibs.patterns.addresses.composed.PO_BOX import PO_BOX

# Custom addresses patterns
from simplibs.patterns.addresses.custom.EMAIL_ADDRESS import EMAIL_ADDRESS
from simplibs.patterns.addresses.custom.PHONE_NUMBER import PHONE_NUMBER
from simplibs.patterns.addresses.custom.INTERNATIONAL_PHONE_NUMBER import INTERNATIONAL_PHONE_NUMBER
from simplibs.patterns.addresses.custom.POSTAL_CODE import POSTAL_CODE
from simplibs.patterns.addresses.custom.ZIP_CODE import ZIP_CODE
from simplibs.patterns.addresses.custom.STREET_ADDRESS import STREET_ADDRESS


def test_email_local_part(subtests):
    assert_pattern(
        subtests,
        EMAIL_LOCAL_PART,
        r"[a-zA-Z0-9._%+\-]+",
        matches=["john.doe", "user+tag", "a", "test_123%"],
        non_matches=["a@b", "", "a b", "a?b"]
    )

def test_ip_address(subtests):
    assert_pattern(
        subtests,
        IP_ADDRESS,
        '(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(?:\\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])){3}|(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?::[0-9a-fA-F]{1,4}){1,6}|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)',
        matches=["192.168.0.1", "::1", "2001:db8::ff00:42:8329"],
        non_matches=["256.1.1.1", "1.2.3", ""]
    )

def test_po_box(subtests):
    assert_pattern(
        subtests,
        PO_BOX,
        r"P\.?O\.?\ Box\ [0-9]+",
        matches=["P.O. Box 123", "PO Box 45", "P.O Box 7"],
        non_matches=["Box 123", "P.O. Box", "po box 5"]
    )

def test_email_address(subtests):
    assert_pattern(
        subtests,
        EMAIL_ADDRESS,
        r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+",
        matches=["john.doe@example.com", "a+b@sub.example.co.uk"],
        non_matches=["john@localhost", "@example.com", "john@", "a b@x.com"]
    )

def test_phone_number(subtests):
    assert_pattern(
        subtests,
        PHONE_NUMBER,
        r"\+?[0-9(][0-9 \-()]{5,18}[0-9]",
        matches=["+420 123 456 789", "(555) 123-4567", "555-1234"],
        non_matches=["12345", "abc", "+"]
    )

def test_international_phone_number(subtests):
    assert_pattern(
        subtests,
        INTERNATIONAL_PHONE_NUMBER,
        r"\+[1-9][0-9]{6,14}",
        matches=["+420123456789", "+14155552671"],
        non_matches=["420123456789", "+0123456789", "+123", "+420 123 456 789"]
    )

def test_postal_code(subtests):
    assert_pattern(
        subtests,
        POSTAL_CODE,
        r"[a-zA-Z0-9][a-zA-Z0-9 \-]{1,8}[a-zA-Z0-9]",
        matches=["110 00", "SW1A 1AA", "90210", "10115"],
        non_matches=["1", "12", "-1234", "12 "]
    )

def test_zip_code(subtests):
    assert_pattern(
        subtests,
        ZIP_CODE,
        r"[0-9]{5}(?:\-[0-9]{4})?",
        matches=["90210", "90210-1234"],
        non_matches=["9021", "90210-12", "902101234"]
    )

def test_street_address(subtests):
    assert_pattern(
        subtests,
        STREET_ADDRESS,
        r"(?=.*\d)(?=.*[^\W\d_])[\w .,'\-/]+",
        matches=["Václavské náměstí 1", "221B Baker Street", "5 Main St.", "Hlavní 12/3"],
        non_matches=["Main Street", "12345", "", "12 @ home"]
    )