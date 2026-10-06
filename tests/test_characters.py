from simplibs.regex.testing import assert_pattern

# Pure characters
from simplibs.patterns.characters.pure.DECIMAL_DIGIT import DECIMAL_DIGIT
from simplibs.patterns.characters.pure.NON_ZERO_DIGIT import NON_ZERO_DIGIT
from simplibs.patterns.characters.pure.BINARY_DIGIT import BINARY_DIGIT
from simplibs.patterns.characters.pure.OCTAL_DIGIT import OCTAL_DIGIT
from simplibs.patterns.characters.pure.SPACE import SPACE
from simplibs.patterns.characters.pure.PLUS_SIGN import PLUS_SIGN
from simplibs.patterns.characters.pure.MINUS_SIGN import MINUS_SIGN
from simplibs.patterns.characters.pure.DASH import DASH
from simplibs.patterns.characters.pure.DOT import DOT
from simplibs.patterns.characters.pure.COMMA import COMMA
from simplibs.patterns.characters.pure.COLON import COLON
from simplibs.patterns.characters.pure.SEMICOLON import SEMICOLON
from simplibs.patterns.characters.pure.SLASH import SLASH
from simplibs.patterns.characters.pure.SINGLE_QUOTE import SINGLE_QUOTE
from simplibs.patterns.characters.pure.DOUBLE_QUOTE import DOUBLE_QUOTE
from simplibs.patterns.characters.pure.UNDERSCORE import UNDERSCORE
from simplibs.patterns.characters.pure.AT_SIGN import AT_SIGN
from simplibs.patterns.characters.pure.HASH_SIGN import HASH_SIGN
from simplibs.patterns.characters.pure.DOLLAR import DOLLAR
from simplibs.patterns.characters.pure.PERCENT import PERCENT
from simplibs.patterns.characters.pure.AMPERSAND import AMPERSAND
from simplibs.patterns.characters.pure.ASTERISK import ASTERISK
from simplibs.patterns.characters.pure.EQUALS import EQUALS
from simplibs.patterns.characters.pure.PIPE import PIPE
from simplibs.patterns.characters.pure.CARET import CARET
from simplibs.patterns.characters.pure.TILDE import TILDE
from simplibs.patterns.characters.pure.QUESTION_MARK import QUESTION_MARK
from simplibs.patterns.characters.pure.PARENTHESIS import PARENTHESIS
from simplibs.patterns.characters.pure.BRACKET import BRACKET
from simplibs.patterns.characters.pure.BRACE import BRACE
from simplibs.patterns.characters.pure.PUNCTUATION import PUNCTUATION
from simplibs.patterns.characters.pure.SYMBOL import SYMBOL
from simplibs.patterns.characters.pure.UNICODE_LETTER import UNICODE_LETTER

# Composed characters
from simplibs.patterns.characters.composed.SIGN import SIGN
from simplibs.patterns.characters.composed.QUOTE import QUOTE
from simplibs.patterns.characters.composed.SPECIAL_CHARACTER import SPECIAL_CHARACTER

# Custom characters
from simplibs.patterns.characters.custom.ESCAPED_CHARACTER import ESCAPED_CHARACTER


def test_decimal_digit(subtests):
    assert_pattern(
        subtests,
        DECIMAL_DIGIT,
        r"[0-9]",
        matches=["0", "7", "9"],
        non_matches=["a", "42", "٣"]
    )

def test_non_zero_digit(subtests):
    assert_pattern(
        subtests,
        NON_ZERO_DIGIT,
        r"[1-9]",
        matches=["1", "5", "9"],
        non_matches=["0", "a", "12"]
    )

def test_binary_digit(subtests):
    assert_pattern(
        subtests,
        BINARY_DIGIT,
        r"[01]",
        matches=["0", "1"],
        non_matches=["2", "01"]
    )

def test_octal_digit(subtests):
    assert_pattern(
        subtests,
        OCTAL_DIGIT,
        r"[0-7]",
        matches=["0", "7"],
        non_matches=["8", "a", "07"]
    )

def test_space(subtests):
    assert_pattern(
        subtests,
        SPACE,
        r"\ ",
        matches=[" "],
        non_matches=["a", "  "]
    )

def test_plus_sign(subtests):
    assert_pattern(
        subtests,
        PLUS_SIGN,
        r"\+",
        matches=["+"],
        non_matches=["a", "++"]
    )

def test_minus_sign(subtests):
    assert_pattern(
        subtests,
        MINUS_SIGN,
        r"\-",
        matches=["-"],
        non_matches=["a", "--"]
    )

def test_dash(subtests):
    assert_pattern(
        subtests,
        DASH,
        r"\-",
        matches=["-"],
        non_matches=["a", "--"]
    )

def test_dot(subtests):
    assert_pattern(
        subtests,
        DOT,
        r"\.",
        matches=["."],
        non_matches=["a", ".."]
    )

def test_comma(subtests):
    assert_pattern(
        subtests,
        COMMA,
        r",",
        matches=[","],
        non_matches=["a", ",,"]
    )

def test_colon(subtests):
    assert_pattern(
        subtests,
        COLON,
        r":",
        matches=[":"],
        non_matches=["a", "::"]
    )

def test_semicolon(subtests):
    assert_pattern(
        subtests,
        SEMICOLON,
        r";",
        matches=[";"],
        non_matches=["a", ";;"]
    )

def test_slash(subtests):
    assert_pattern(
        subtests,
        SLASH,
        r"/",
        matches=["/"],
        non_matches=["a", "//"]
    )

def test_single_quote(subtests):
    assert_pattern(
        subtests,
        SINGLE_QUOTE,
        r"'",
        matches=["'"],
        non_matches=["a", "''"]
    )

def test_double_quote(subtests):
    assert_pattern(
        subtests,
        DOUBLE_QUOTE,
        r'"',
        matches=['"'],
        non_matches=["a", '""']
    )

def test_underscore(subtests):
    assert_pattern(
        subtests,
        UNDERSCORE,
        r"_",
        matches=["_"],
        non_matches=["a", "__"]
    )

def test_at_sign(subtests):
    assert_pattern(
        subtests,
        AT_SIGN,
        r"@",
        matches=["@"],
        non_matches=["a", "@@"]
    )

def test_hash_sign(subtests):
    assert_pattern(
        subtests,
        HASH_SIGN,
        r"\#",
        matches=["#"],
        non_matches=["a", "##"]
    )

def test_dollar(subtests):
    assert_pattern(
        subtests,
        DOLLAR,
        r"\$",
        matches=["$"],         non_matches=["a", "$$"]
    )

def test_percent(subtests):
    assert_pattern(
        subtests,
        PERCENT,
        r"%",
        matches=["%"],
        non_matches=["a", "%%"]
    )

def test_ampersand(subtests):
    assert_pattern(
        subtests,
        AMPERSAND,
        r"\&",
        matches=["&"],
        non_matches=["a", "&&"]
    )

def test_asterisk(subtests):
    assert_pattern(
        subtests,
        ASTERISK,
        r"\*",
        matches=["*"],
        non_matches=["a", "**"]
    )

def test_equals(subtests):
    assert_pattern(
        subtests,
        EQUALS,
        r"=",
        matches=["="],
        non_matches=["a", "=="]
    )

def test_pipe(subtests):
    assert_pattern(
        subtests,
        PIPE,
        r"\|",
        matches=["|"],
        non_matches=["a", "||"]
    )

def test_caret(subtests):
    assert_pattern(
        subtests,
        CARET,
        r"\^",
        matches=["^"],
        non_matches=["a", "^^"]
    )

def test_tilde(subtests):
    assert_pattern(
        subtests,
        TILDE,
        r"\~",
        matches=["~"],
        non_matches=["a", "~~"]
    )

def test_question_mark(subtests):
    assert_pattern(
        subtests,
        QUESTION_MARK,
        r"\?",
        matches=["?"],
        non_matches=["a", "??"]
    )

def test_parenthesis(subtests):
    assert_pattern(
        subtests,
        PARENTHESIS,
        r"[()]",
        matches=["(", ")"],
        non_matches=["[", "()"]
    )

def test_bracket(subtests):
    assert_pattern(
        subtests,
        BRACKET,
        r"[\[\]]",
        matches=["[", "]"],
        non_matches=["(", "[]"]
    )

def test_brace(subtests):
    assert_pattern(
        subtests,
        BRACE,
        r"[{}]",
        matches=["{", "}"],
        non_matches=["(", "{}"]
    )

def test_punctuation(subtests):
    assert_pattern(
        subtests,
        PUNCTUATION,
        r'''[!"#%\&'()*,\-./:;?@\[\\\]_{}]''',
        matches=["!", ".", "_"],
        non_matches=["$", "+", "a"]
    )

def test_symbol(subtests):
    assert_pattern(
        subtests,
        SYMBOL,
        r"[$+<=>\^`\|\~]",
        matches=["$", "+", "~"],
        non_matches=["!", "a"]
    )

def test_unicode_letter(subtests):
    assert_pattern(
        subtests,
        UNICODE_LETTER,
        r"[^\W\d_]",
        matches=["a", "é", "ž", "Ω"],
        non_matches=["1", "_", " ", "ab"]
    )

def test_sign(subtests):
    assert_pattern(
        subtests,
        SIGN,
        r"[+\-]",
        matches=["+", "-"],
        non_matches=["a", "+-"]
    )

def test_quote(subtests):
    assert_pattern(
        subtests,
        QUOTE,
        r'''['"]''',
        matches=["'", '"'],
        non_matches=["a", "''"]
    )

def test_special_character(subtests):
    assert_pattern(
        subtests,
        SPECIAL_CHARACTER,
        r'''[!"#%\&'()*,\-./:;?@\[\\\]_{}]|[$+<=>\^`\|\~]''',
        matches=["!", "$", "~"],
        non_matches=["a", "5", " "]
    )

def test_escaped_character(subtests):
    assert_pattern(
        subtests,
        ESCAPED_CHARACTER,
        r"\\(?:x[0-9a-fA-F]{2}|u[0-9a-fA-F]{4}|U[0-9a-fA-F]{8}|.)",
        matches=[r"\.", r"\n", r"\xFF", r"\u1234"],
        non_matches=[r"\x4", "\\", "n"]
    )