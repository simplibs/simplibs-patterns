from simplibs.regex.testing import assert_pattern
from simplibs.regex.elements.Literal import Literal
from simplibs.patterns.identifiers import IDENTIFIER
from simplibs.patterns.numbers import INTEGER

# Pure structured patterns
from simplibs.patterns.structured.pure.OPENING_DELIMITER import OPENING_DELIMITER
from simplibs.patterns.structured.pure.CLOSING_DELIMITER import CLOSING_DELIMITER

# Composed structured patterns & factories
from simplibs.patterns.structured.composed.DELIMITED_BY import DELIMITED_BY
from simplibs.patterns.structured.composed.LIST_OF import LIST_OF
from simplibs.patterns.structured.composed.SEQUENCE_OF import SEQUENCE_OF
from simplibs.patterns.structured.composed.PAIR_OF import PAIR_OF
from simplibs.patterns.structured.composed.WRAPPED_BY import WRAPPED_BY
from simplibs.patterns.structured.composed.KEY_VALUE_PAIR import KEY_VALUE_PAIR
from simplibs.patterns.structured.composed.KEY_VALUE import KEY_VALUE

# Custom structured patterns
from simplibs.patterns.structured.custom.SEPARATOR import SEPARATOR
from simplibs.patterns.structured.custom.DELIMITER import DELIMITER
from simplibs.patterns.structured.custom.COMMA_SEPARATED_LIST import COMMA_SEPARATED_LIST
from simplibs.patterns.structured.custom.SEMICOLON_SEPARATED_LIST import SEMICOLON_SEPARATED_LIST
from simplibs.patterns.structured.custom.SPACE_SEPARATED_LIST import SPACE_SEPARATED_LIST
from simplibs.patterns.structured.custom.TAB_SEPARATED_LIST import TAB_SEPARATED_LIST


def test_opening_delimiter(subtests):
    assert_pattern(
        subtests,
        OPENING_DELIMITER,
        r"[(\[{<]",
        matches=["(", "[", "{", "<"],
        non_matches=[")", "a", "(["]
    )

def test_closing_delimiter(subtests):
    assert_pattern(
        subtests,
        CLOSING_DELIMITER,
        r"[)\]}>]",
        matches=[")", "]", "}", ">"],
        non_matches=["(", "a", "])"]
    )

def test_delimited_by(subtests):
    pattern = DELIMITED_BY(IDENTIFIER, Literal("/"))
    assert_pattern(
        subtests,
        pattern,
        r"[a-zA-Z_][a-zA-Z0-9_]*(?:/[a-zA-Z_][a-zA-Z0-9_]*)*",
        matches=["usr", "usr/local/bin"],
        non_matches=["/usr", "usr/", "usr//bin", ""]
    )

def test_list_of(subtests):
    pattern = LIST_OF(INTEGER)
    assert_pattern(
        subtests,
        pattern,
        r"[0-9]+(?:,[0-9]+)*",
        matches=["1", "1,2,3", "42,7"],
        non_matches=["", "1,", "1,,2", "1 2"]
    )

def test_sequence_of(subtests):
    pattern = SEQUENCE_OF(Literal("ab"))
    assert_pattern(
        subtests,
        pattern, r"(?:ab)+",
        matches=["ab", "ababab"],
        non_matches=["", "aba"]
    )

def test_pair_of(subtests):
    pattern = PAIR_OF(IDENTIFIER, INTEGER)
    assert_pattern(
        subtests,
        pattern,
        r"[a-zA-Z_][a-zA-Z0-9_]*=[0-9]+",
        matches=["age=42", "x=0"],
        non_matches=["age:42", "age=", "=42"]
    )

def test_wrapped_by(subtests):
    pattern = WRAPPED_BY(INTEGER, Literal("<"), Literal(">"))
    assert_pattern(
        subtests,
        pattern,
        r"<[0-9]+>",
        matches=["<42>"],
        non_matches=["42", "<>", "<42"]
    )

def test_key_value_pair(subtests):
    assert_pattern(
        subtests,
        KEY_VALUE_PAIR,
        r"[a-zA-Z_][a-zA-Z0-9_]*=\S+",
        matches=["name=value", "a=1", "path=/usr/bin"],
        non_matches=["name", "=value", "a= b"]
    )

def test_key_value(subtests):
    assert_pattern(
        subtests,
        KEY_VALUE,
        r"[a-zA-Z_][a-zA-Z0-9_]*=\S+",
        matches=["name=value", "a=1", "path=/usr/bin"],
        non_matches=["name", "=value", "a= b"]
    )

def test_separator(subtests):
    assert_pattern(
        subtests,
        SEPARATOR,
        r"[,;\|\t ]",
        matches=[",", ";", "|", "\t", " "],
        non_matches=["a", "::", ""]
    )

def test_delimiter(subtests):
    assert_pattern(
        subtests,
        DELIMITER,
        r"[,;\|\t ]",
        matches=[",", ";", "|", "\t", " "],
        non_matches=["a", "::", ""]
    )

def test_comma_separated_list(subtests):
    assert_pattern(
        subtests,
        COMMA_SEPARATED_LIST,
        r"[^,]+(?:,[^,]+)*",
        matches=["a,b,c", "single"],
        non_matches=["", "a,,b", "a,"]
    )

def test_semicolon_separated_list(subtests):
    assert_pattern(
        subtests,
        SEMICOLON_SEPARATED_LIST,
        r"[^;]+(?:;[^;]+)*",
        matches=["a;b;c", "single"],
        non_matches=["", "a;;b"]
    )

def test_space_separated_list(subtests):
    assert_pattern(
        subtests,
        SPACE_SEPARATED_LIST,
        r"[^ ]+(?:\ [^ ]+)*",
        matches=["a b c", "single"],
        non_matches=["", "a  b"]
    )

def test_tab_separated_list(subtests):
    assert_pattern(
        subtests,
        TAB_SEPARATED_LIST,
        r"[^\t]+(?:\t[^\t]+)*",
        matches=["a\tb\tc", "single"],
        non_matches=["", "a\t\tb"]
    )