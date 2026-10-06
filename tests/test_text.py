from simplibs.regex.testing import assert_pattern

# Pure text patterns
from simplibs.patterns.text.pure.EMPTY_TEXT import EMPTY_TEXT
from simplibs.patterns.text.pure.NON_EMPTY_TEXT import NON_EMPTY_TEXT
from simplibs.patterns.text.pure.CHARACTER import CHARACTER
from simplibs.patterns.text.pure.CHARACTERS import CHARACTERS
from simplibs.patterns.text.pure.WORD import WORD
from simplibs.patterns.text.pure.SINGLE_WORD import SINGLE_WORD
from simplibs.patterns.text.pure.LINE import LINE
from simplibs.patterns.text.pure.SINGLE_LINE import SINGLE_LINE
from simplibs.patterns.text.pure.WHITESPACE_TEXT import WHITESPACE_TEXT
from simplibs.patterns.text.pure.NON_WHITESPACE_TEXT import NON_WHITESPACE_TEXT
from simplibs.patterns.text.pure.ALPHANUMERIC_TEXT import ALPHANUMERIC_TEXT
from simplibs.patterns.text.pure.ALPHA_TEXT import ALPHA_TEXT
from simplibs.patterns.text.pure.DIGIT_TEXT import DIGIT_TEXT
from simplibs.patterns.text.pure.LOWERCASE_TEXT import LOWERCASE_TEXT
from simplibs.patterns.text.pure.UPPERCASE_TEXT import UPPERCASE_TEXT
from simplibs.patterns.text.pure.IDENTIFIER_LIKE_TEXT import IDENTIFIER_LIKE_TEXT
from simplibs.patterns.text.pure.SINGLE_QUOTED_TEXT import SINGLE_QUOTED_TEXT
from simplibs.patterns.text.pure.DOUBLE_QUOTED_TEXT import DOUBLE_QUOTED_TEXT
from simplibs.patterns.text.pure.PARENTHESIZED_TEXT import PARENTHESIZED_TEXT
from simplibs.patterns.text.pure.BRACKETED_TEXT import BRACKETED_TEXT
from simplibs.patterns.text.pure.BRACED_TEXT import BRACED_TEXT

# Composed text patterns & factories
from simplibs.patterns.text.composed.QUOTED_TEXT import QUOTED_TEXT
from simplibs.patterns.text.composed.WORDS import WORDS
from simplibs.patterns.text.composed.SPACE_SEPARATED_WORDS import SPACE_SEPARATED_WORDS
from simplibs.patterns.text.composed.WORD_LIST import WORD_LIST
from simplibs.patterns.text.composed.COMMA_SEPARATED_TEXT import COMMA_SEPARATED_TEXT
from simplibs.patterns.text.composed.MULTILINE_TEXT import MULTILINE_TEXT
from simplibs.patterns.text.composed.WHOLE_WORD import WHOLE_WORD
from simplibs.patterns.text.composed.TEXT_BETWEEN import TEXT_BETWEEN
from simplibs.patterns.text.composed.PREFIXED_TEXT import PREFIXED_TEXT
from simplibs.patterns.text.composed.SUFFIXED_TEXT import SUFFIXED_TEXT
from simplibs.patterns.text.composed.TEXT_OF_LENGTH import TEXT_OF_LENGTH
from simplibs.patterns.text.composed.TEXT_OF_LENGTH_RANGE import TEXT_OF_LENGTH_RANGE

# Custom text patterns & factories
from simplibs.patterns.text.custom.MIXED_CASE_TEXT import MIXED_CASE_TEXT
from simplibs.patterns.text.custom.CSV_LINE import CSV_LINE
from simplibs.patterns.text.custom.TEXT_UNTIL import TEXT_UNTIL
from simplibs.patterns.text.custom.TEXT_AFTER import TEXT_AFTER
from simplibs.patterns.text.custom.TEXT_BEFORE import TEXT_BEFORE


def test_empty_text(subtests):
    assert_pattern(
        subtests,
        EMPTY_TEXT,
        r".{0}",
        matches=[""],
        non_matches=["a", " "]
    )

def test_non_empty_text(subtests):
    assert_pattern(
        subtests,
        NON_EMPTY_TEXT,
        r".+",
        matches=["a", "Hello, world!"],
        non_matches=[""]
    )

def test_character(subtests):
    assert_pattern(
        subtests,
        CHARACTER,
        r".",
        matches=["a", "!", " "],
        non_matches=["", "ab"]
    )

def test_characters(subtests):
    assert_pattern(
        subtests,
        CHARACTERS,
        r".+",
        matches=["a", "Hello, world!"],
        non_matches=[""]
    )

def test_word(subtests):
    assert_pattern(
        subtests,
        WORD,
        r"\w+",
        matches=["Python", "snake_case", "abc123"],
        non_matches=["two words", "", "a-b"]
    )

def test_single_word(subtests):
    assert_pattern(
        subtests,
        SINGLE_WORD,
        r"\w+",
        matches=["Python", "snake_case", "abc123"],
        non_matches=["two words", "", "a-b"]
    )

def test_line(subtests):
    assert_pattern(
        subtests,
        LINE,
        r".*",
        matches=["", "one line", "a b c"],
        non_matches=["a\nb"]
    )

def test_single_line(subtests):
    assert_pattern(
        subtests,
        SINGLE_LINE,
        r".*",
        matches=["", "one line", "a b c"],
        non_matches=["a\nb"]
    )

def test_whitespace_text(subtests):
    assert_pattern(
        subtests,
        WHITESPACE_TEXT,
        r"\s+",
        matches=[" ", "\t\n "],
        non_matches=["a", "", " a"]
    )

def test_non_whitespace_text(subtests):
    assert_pattern(
        subtests,
        NON_WHITESPACE_TEXT,
        r"\S+",
        matches=["abc", "a-b!"],
        non_matches=["a b", ""]
    )

def test_alphanumeric_text(subtests):
    assert_pattern(
        subtests,
        ALPHANUMERIC_TEXT,
        r"[a-zA-Z0-9]+",
        matches=["abc123", "X"],
        non_matches=["a b", "a_b", ""]
    )

def test_alpha_text(subtests):
    assert_pattern(
        subtests,
        ALPHA_TEXT,
        r"[a-zA-Z]+",
        matches=["abc", "Hello"],
        non_matches=["abc1", "a b", ""]
    )

def test_digit_text(subtests):
    assert_pattern(
        subtests,
        DIGIT_TEXT,
        r"[0-9]+",
        matches=["0", "2026", "007"],
        non_matches=["1.5", "-1", "", "a1"]
    )

def test_lowercase_text(subtests):
    assert_pattern(
        subtests,
        LOWERCASE_TEXT,
        r"[a-z]+",
        matches=["abc", "x"],
        non_matches=["Abc", "abc1", ""]
    )

def test_uppercase_text(subtests):
    assert_pattern(
        subtests,
        UPPERCASE_TEXT,
        r"[A-Z]+",
        matches=["ABC", "X"],
        non_matches=["aBC", "ABC1", ""]
    )

def test_identifier_like_text(subtests):
    assert_pattern(
        subtests,
        IDENTIFIER_LIKE_TEXT,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_single_quoted_text(subtests):
    assert_pattern(
        subtests,
        SINGLE_QUOTED_TEXT,
        r"'[^']*'",
        matches=["'hello'", "''"],
        non_matches=["hello", "'a'b'", "'open"]
    )

def test_double_quoted_text(subtests):
    assert_pattern(
        subtests,
        DOUBLE_QUOTED_TEXT,
        r'"[^"]*"',
        matches=['"hello"', '""'],
        non_matches=["hello", '"a"b"', '"open']
    )

def test_parenthesized_text(subtests):
    assert_pattern(
        subtests,
        PARENTHESIZED_TEXT,
        r"\([^()]*\)",
        matches=["(abc)", "()"],
        non_matches=["abc", "(a(b))", "(open"]
    )

def test_bracketed_text(subtests):
    assert_pattern(
        subtests,
        BRACKETED_TEXT,
        r"\[[^\[\]]*\]",
        matches=["[abc]", "[]"],
        non_matches=["abc", "[a[b]]", "[open"]
    )

def test_braced_text(subtests):
    assert_pattern(
        subtests,
        BRACED_TEXT,
        r"\{[^{}]*\}",
        matches=["{abc}", "{}"],
        non_matches=["abc", "{a{b}}", "{open"]
    )

def test_quoted_text(subtests):
    assert_pattern(
        subtests,
        QUOTED_TEXT,
        r''''[^']*'|"[^"]*"''',
        matches=["'hi'", '"hi"'],
        non_matches=["hi", "'hi\""]
    )

def test_words(subtests):
    assert_pattern(
        subtests,
        WORDS,
        r"\w+(?:\s+\w+)*",
        matches=["hello", "hello big   world", "a\tb"],
        non_matches=["", "hello,world", " hello"]
    )

def test_space_separated_words(subtests):
    assert_pattern(
        subtests,
        SPACE_SEPARATED_WORDS,
        r"\w+(?:\ \w+)*",
        matches=["hello", "a b c"],
        non_matches=["a  b", "a\tb", ""]
    )

def test_word_list(subtests):
    assert_pattern(
        subtests,
        WORD_LIST,
        r"\w+(?:\s+\w+)*",
        matches=["hello", "hello big   world", "a\tb"],
        non_matches=["", "hello,world", " hello"]
    )

def test_comma_separated_text(subtests):
    assert_pattern(
        subtests,
        COMMA_SEPARATED_TEXT,
        r"\w+(?:,\w+)*",
        matches=["a", "a,b,c", "one,two"],
        non_matches=["a, b", "a,,b", "a,", ""]
    )

def test_multiline_text(subtests):
    assert_pattern(
        subtests,
        MULTILINE_TEXT,
        r".*(?:\n.*)+",
        matches=["a\nb", "a\n\nb", "x\ny\nz"],
        non_matches=["single line", ""]
    )

def test_whole_word(subtests):
    pattern = WHOLE_WORD("Python")
    assert_pattern(
        subtests,
        pattern,
        r"\bPython\b",
        matches=["Python"],
        non_matches=["CPython", "Pythonic", "python"]
    )

def test_text_between(subtests):
    pattern = TEXT_BETWEEN("<", ">")
    assert_pattern(
        subtests,
        pattern,
        r"<.*?>",
        matches=["<b>"],
        non_matches=["no brackets"]
    )

def test_prefixed_text(subtests):
    pattern = PREFIXED_TEXT("log:")
    assert_pattern(
        subtests,
        pattern,
        r"log:.*",
        matches=["log: started", "log:"],
        non_matches=["info: started"]
    )

def test_suffixed_text(subtests):
    pattern = SUFFIXED_TEXT(".py")
    assert_pattern(
        subtests,
        pattern,
        r".*\.py",
        matches=["main.py", ".py"],
        non_matches=["main.txt"]
    )

def test_text_of_length(subtests):
    pattern = TEXT_OF_LENGTH(3)
    assert_pattern(
        subtests,
        pattern,
        r".{3}",
        matches=["abc", "123"],
        non_matches=["ab", "abcd"]
    )

def test_text_of_length_range(subtests):
    pattern = TEXT_OF_LENGTH_RANGE(2, 4)
    assert_pattern(
        subtests,
        pattern,
        r".{2,4}",
        matches=["ab", "abcd"],
        non_matches=["a", "abcde"]
    )

def test_mixed_case_text(subtests):
    assert_pattern(
        subtests,
        MIXED_CASE_TEXT,
        r"(?=.*[a-z])(?=.*[A-Z]).+",
        matches=["Hello", "aB", "fooBar!"],
        non_matches=["hello", "HELLO", "123", ""]
    )

def test_csv_line(subtests):
    assert_pattern(
        subtests,
        CSV_LINE,
        r"[^,\r\n]*(?:,[^,\r\n]*)*",
        matches=["a,b,c", "a,,c", "single", ""],
        non_matches=["a\nb"]
    )

def test_text_until(subtests):
    pattern = TEXT_UNTIL("=")
    assert_pattern(
        subtests,
        pattern,
        r"(?:(?!=).)*",
        matches=["key", "abc"],
        non_matches=[]
    )

def test_text_after(subtests):
    pattern = TEXT_AFTER("key=")
    assert_pattern(
        subtests,
        pattern,
        r"(?<=key=).+",
        finds={"key=value": "value", "value": None},
    )

def test_text_before(subtests):
    pattern = TEXT_BEFORE("=")
    assert_pattern(
        subtests,
        pattern,
        r".+?(?==)",
        finds={"key=value": "key", "value": None},
    )