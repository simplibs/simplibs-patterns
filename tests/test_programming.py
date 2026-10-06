from simplibs.regex.testing import assert_pattern

# Programming patterns and enums
from simplibs.patterns.programming.enums.Language import Language
from simplibs.patterns.programming.pure.OPERATOR import OPERATOR
from simplibs.patterns.programming.composed.NUMBER_LITERAL import NUMBER_LITERAL
from simplibs.patterns.programming.custom.COMMENT import COMMENT
from simplibs.patterns.programming.custom.STRING_LITERAL import STRING_LITERAL
from simplibs.patterns.programming.custom.BOOLEAN_LITERAL import BOOLEAN_LITERAL
from simplibs.patterns.programming.custom.NULL_LITERAL import NULL_LITERAL
from simplibs.patterns.programming.custom.KEYWORD import KEYWORD
from simplibs.patterns.programming.custom.IMPORT import IMPORT


def test_operator(subtests):
    assert_pattern(
        subtests,
        OPERATOR,
        r"==|!=|<=|>=|[+\-*/=<>]",
        matches=["==", "!=", "<=", "+"],
        non_matches=["=>", "a", "!", ""]
    )

def test_number_literal(subtests):
    assert_pattern(
        subtests,
        NUMBER_LITERAL,
        r"(?:[0-9]+\.[0-9]+|[0-9]+)[eE][+\-]?[0-9]+|[0-9]+\.[0-9]+|[0-9]+",
        matches=["42", "3.14", "1e10", "2.5E-3"],
        non_matches=["", "abc", "1.", "-5"]
    )

def test_comment_python(subtests):
    assert_pattern(
        subtests,
        COMMENT(Language.PYTHON),
        r"\#.*",
        matches=["# set x"],
        non_matches=["x = 1"]
    )

def test_comment_javascript(subtests):
    assert_pattern(
        subtests,
        COMMENT(Language.JAVASCRIPT),
        r"//.*",
        matches=["// set x"],
        non_matches=["x = 1"]
    )

def test_string_literal_python(subtests):
    assert_pattern(
        subtests,
        STRING_LITERAL(Language.PYTHON),
        r''''(?:[^'\\\n]|\\.)*'|"(?:[^"\\\n]|\\.)*"''',
        matches=["'hi'", '"a \\" b"'],
        non_matches=["x = 1", "'open"]
    )

def test_string_literal_javascript(subtests):
    assert_pattern(
        subtests,
        STRING_LITERAL(Language.JAVASCRIPT),
        r''''(?:[^'\\\n]|\\.)*'|"(?:[^"\\\n]|\\.)*"|`(?:[^`\\]|\\.)*`''',
        matches=["'hi'", '"a \\" b"', "`template`"],
        non_matches=["x = 1", "'open"]
    )

def test_boolean_literal_python(subtests):
    assert_pattern(
        subtests,
        BOOLEAN_LITERAL(Language.PYTHON),
        r"\bTrue\b|\bFalse\b",
        matches=["True", "False"],
        non_matches=["true", "false", "Truely"]
    )

def test_boolean_literal_javascript(subtests):
    assert_pattern(
        subtests,
        BOOLEAN_LITERAL(Language.JAVASCRIPT),
        r"\btrue\b|\bfalse\b",
        matches=["true", "false"],
        non_matches=["True", "False"]
    )

def test_null_literal_python(subtests):
    assert_pattern(
        subtests,
        NULL_LITERAL(Language.PYTHON),
        r"\bNone\b",
        matches=["None"],
        non_matches=["null", "nullable"]
    )

def test_null_literal_javascript(subtests):
    assert_pattern(
        subtests,
        NULL_LITERAL(Language.JAVASCRIPT),
        r"\bnull\b",
        matches=["null"],
        non_matches=["None", "nullable"]
    )

def test_keyword_python(subtests):
    assert_pattern(
        subtests,
        KEYWORD(Language.PYTHON),
        r"\b(?:False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)\b",
        matches=["def", "lambda", "return"],
        non_matches=["define", "x = 1"]
    )

def test_keyword_javascript(subtests):
    assert_pattern(
        subtests,
        KEYWORD(Language.JAVASCRIPT),
        r"\b(?:async|await|break|case|catch|class|const|continue|debugger|default|delete|do|else|export|extends|finally|for|function|if|import|in|instanceof|let|new|return|static|super|switch|this|throw|try|typeof|var|void|while|with|yield)\b",
        matches=["function", "const", "return"],
        non_matches=["functional", "x = 1"]
    )

def test_import_python(subtests):
    assert_pattern(
        subtests,
        IMPORT(Language.PYTHON),
        'import\\ +[a-zA-Z_][a-zA-Z0-9_]*(?:\\.[a-zA-Z_][a-zA-Z0-9_]*)*(?:\\ +as\\ +[a-zA-Z_][a-zA-Z0-9_]*)?|from\\ +(?:\\.*[a-zA-Z_][a-zA-Z0-9_]*(?:\\.[a-zA-Z_][a-zA-Z0-9_]*)*|\\.+)\\ +import\\ +(?:\\*|[a-zA-Z_][a-zA-Z0-9_]*(?:\\ +as\\ +[a-zA-Z_][a-zA-Z0-9_]*)?(?:,\\ *[a-zA-Z_][a-zA-Z0-9_]*(?:\\ +as\\ +[a-zA-Z_][a-zA-Z0-9_]*)?)*)',
        matches=["import os", "import os.path as p", "from os import path", "from . import x"],
        non_matches=["import", "from os", "importos", "import os as"]
    )

def test_import_javascript(subtests):
    assert_pattern(
        subtests,
        IMPORT(Language.JAVASCRIPT),
        'import\\ +(?:[a-zA-Z_][a-zA-Z0-9_]*|\\{\\ *[a-zA-Z_][a-zA-Z0-9_]*(?:\\ +as\\ +[a-zA-Z_][a-zA-Z0-9_]*)?(?:,\\ *[a-zA-Z_][a-zA-Z0-9_]*(?:\\ +as\\ +[a-zA-Z_][a-zA-Z0-9_]*)?)*\\ *\\}|\\*\\ +as\\ +[a-zA-Z_][a-zA-Z0-9_]*)\\ +from\\ +(?:\'(?:[^\'\\\\\\n]|\\\\.)*\'|"(?:[^"\\\\\\n]|\\\\.)*"|`(?:[^`\\\\]|\\\\.)*`)|import\\ +(?:\'(?:[^\'\\\\\\n]|\\\\.)*\'|"(?:[^"\\\\\\n]|\\\\.)*"|`(?:[^`\\\\]|\\\\.)*`)',
        matches=['import React from "react"', 'import { useState } from "react"', 'import "styles.css"'],
        non_matches=["import", "from \"react\"", "import React"]
    )