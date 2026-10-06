from simplibs.regex.testing import assert_pattern

# Pure communication patterns
from simplibs.patterns.communication.pure.EMAIL import EMAIL
from simplibs.patterns.communication.pure.USER_HANDLE import USER_HANDLE
from simplibs.patterns.communication.pure.MENTION import MENTION
from simplibs.patterns.communication.pure.SOCIAL_HANDLE import SOCIAL_HANDLE
from simplibs.patterns.communication.pure.HASHTAG import HASHTAG
from simplibs.patterns.communication.pure.SUBJECT import SUBJECT
from simplibs.patterns.communication.pure.REPLY_ADDRESS import REPLY_ADDRESS
from simplibs.patterns.communication.pure.SENDER_ADDRESS import SENDER_ADDRESS
from simplibs.patterns.communication.pure.RECIPIENT_ADDRESS import RECIPIENT_ADDRESS
from simplibs.patterns.communication.pure.EMAIL_HEADER_NAME import EMAIL_HEADER_NAME
from simplibs.patterns.communication.pure.EMAIL_HEADER_VALUE import EMAIL_HEADER_VALUE

# Composed communication patterns
from simplibs.patterns.communication.composed.EMAIL_HEADER import EMAIL_HEADER
from simplibs.patterns.communication.composed.EMAIL_SUBJECT import EMAIL_SUBJECT

# Custom communication patterns
from simplibs.patterns.communication.custom.USERNAME import USERNAME
from simplibs.patterns.communication.custom.DISPLAY_NAME import DISPLAY_NAME
from simplibs.patterns.communication.custom.MESSAGE_ID import MESSAGE_ID


def test_email(subtests):
    assert_pattern(
        subtests,
        EMAIL,
        r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+",
        matches=["john.doe@example.com", "a+b@sub.example.co.uk"],
        non_matches=["john@localhost", "@example.com", "john@", "a b@x.com"]
    )

def test_user_handle(subtests):
    assert_pattern(
        subtests,
        USER_HANDLE,
        r"@[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["@john", "@john_doe1"],
        non_matches=["john", "@", "@1abc"]
    )

def test_mention(subtests):
    assert_pattern(
        subtests,
        MENTION,
        r"@[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["@john", "@john_doe1"],
        non_matches=["john", "@", "@1abc"]
    )

def test_social_handle(subtests):
    assert_pattern(
        subtests,
        SOCIAL_HANDLE,
        r"@[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["@john", "@john_doe1"],
        non_matches=["john", "@", "@1abc"]
    )

def test_hashtag(subtests):
    assert_pattern(
        subtests,
        HASHTAG,
        r"\#\w+",
        matches=["#python", "#2026", "#ahoj_světe"],
        non_matches=["python", "#", "# tag"]
    )

def test_subject(subtests):
    assert_pattern(
        subtests,
        SUBJECT,
        r".+",
        matches=["a", "Hello, world!"],
        non_matches=[""]
    )

def test_reply_address(subtests):
    assert_pattern(
        subtests,
        REPLY_ADDRESS,
        r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+",
        matches=["john.doe@example.com", "a+b@sub.example.co.uk"],
        non_matches=["john@localhost", "@example.com", "john@", "a b@x.com"]
    )

def test_sender_address(subtests):
    assert_pattern(
        subtests,
        SENDER_ADDRESS,
        r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+",
        matches=["john.doe@example.com", "a+b@sub.example.co.uk"],
        non_matches=["john@localhost", "@example.com", "john@", "a b@x.com"]
    )

def test_recipient_address(subtests):
    assert_pattern(
        subtests,
        RECIPIENT_ADDRESS,
        r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)+",
        matches=["john.doe@example.com", "a+b@sub.example.co.uk"],
        non_matches=["john@localhost", "@example.com", "john@", "a b@x.com"]
    )

def test_email_header_name(subtests):
    assert_pattern(
        subtests,
        EMAIL_HEADER_NAME,
        r"[!-9;-\~]+",
        matches=["Subject", "X-Mailer", "Content-Type"],
        non_matches=["Sub ject", "Name:", ""]
    )

def test_email_header_value(subtests):
    assert_pattern(
        subtests,
        EMAIL_HEADER_VALUE,
        r".*",
        matches=["", "one line", "a b c"],
        non_matches=["a\nb"]
    )

def test_email_header(subtests):
    assert_pattern(
        subtests,
        EMAIL_HEADER,
        r"[!-9;-\~]+:\ *.*",
        matches=["Subject: Hello", "From:x@y.com", "X-Empty:"],
        non_matches=["no header", "Name value"]
    )

def test_email_subject(subtests):
    assert_pattern(
        subtests,
        EMAIL_SUBJECT,
        r"Subject:\ *.+",
        matches=["Subject: Meeting tomorrow"],
        non_matches=["Subject:", "From: a"]
    )

def test_username(subtests):
    assert_pattern(
        subtests,
        USERNAME,
        r"[a-zA-Z0-9][a-zA-Z0-9._\-]{2,31}",
        matches=["john_doe", "user.name-1", "abc"],
        non_matches=["ab", "_user", "a b", ""]
    )

def test_display_name(subtests):
    assert_pattern(
        subtests,
        DISPLAY_NAME,
        r"[^\W\d_](?:[^\W\d_]|[ .'\-])*",
        matches=["Jan Novák", "Mary-Jane O'Neil", "J. R. R. Tolkien"],
        non_matches=["", "123", "_x"]
    )

def test_message_id(subtests):
    assert_pattern(
        subtests,
        MESSAGE_ID,
        r"<[^@<>\s]+@[^@<>\s]+>",
        matches=["<abc123@mail.example.com>"],
        non_matches=["abc@x", "<abc>", "<a@b@c>"]
    )