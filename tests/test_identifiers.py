from simplibs.regex.testing import assert_pattern

# Pure identifier patterns
from simplibs.patterns.identifiers.pure.IDENTIFIER_START_CHARACTER import IDENTIFIER_START_CHARACTER
from simplibs.patterns.identifiers.pure.IDENTIFIER_CHARACTER import IDENTIFIER_CHARACTER
from simplibs.patterns.identifiers.pure.IDENTIFIER import IDENTIFIER
from simplibs.patterns.identifiers.pure.SIMPLE_IDENTIFIER import SIMPLE_IDENTIFIER
from simplibs.patterns.identifiers.pure.NAME import NAME
from simplibs.patterns.identifiers.pure.QUALIFIED_IDENTIFIER import QUALIFIED_IDENTIFIER
from simplibs.patterns.identifiers.pure.QUALIFIED_NAME import QUALIFIED_NAME
from simplibs.patterns.identifiers.pure.NAMESPACE import NAMESPACE
from simplibs.patterns.identifiers.pure.NAMESPACE_NAME import NAMESPACE_NAME
from simplibs.patterns.identifiers.pure.VARIABLE_NAME import VARIABLE_NAME
from simplibs.patterns.identifiers.pure.CONSTANT_NAME import CONSTANT_NAME
from simplibs.patterns.identifiers.pure.FUNCTION_NAME import FUNCTION_NAME
from simplibs.patterns.identifiers.pure.METHOD_NAME import METHOD_NAME
from simplibs.patterns.identifiers.pure.CLASS_NAME import CLASS_NAME
from simplibs.patterns.identifiers.pure.TYPE_NAME import TYPE_NAME
from simplibs.patterns.identifiers.pure.MODULE_NAME import MODULE_NAME
from simplibs.patterns.identifiers.pure.PACKAGE_NAME import PACKAGE_NAME
from simplibs.patterns.identifiers.pure.ATTRIBUTE_NAME import ATTRIBUTE_NAME
from simplibs.patterns.identifiers.pure.PROPERTY_NAME import PROPERTY_NAME
from simplibs.patterns.identifiers.pure.PARAMETER_NAME import PARAMETER_NAME
from simplibs.patterns.identifiers.pure.ARGUMENT_NAME import ARGUMENT_NAME
from simplibs.patterns.identifiers.pure.ENUM_NAME import ENUM_NAME
from simplibs.patterns.identifiers.pure.ENUM_MEMBER_NAME import ENUM_MEMBER_NAME
from simplibs.patterns.identifiers.pure.KEY import KEY
from simplibs.patterns.identifiers.pure.VALUE_NAME import VALUE_NAME
from simplibs.patterns.identifiers.pure.LABEL import LABEL

# Composed identifier patterns & factories
from simplibs.patterns.identifiers.composed.QUALIFIED_IDENTIFIER_OF import QUALIFIED_IDENTIFIER_OF
from simplibs.patterns.identifiers.composed.IDENTIFIER_WITH_PREFIX import IDENTIFIER_WITH_PREFIX
from simplibs.patterns.identifiers.composed.IDENTIFIER_WITH_SUFFIX import IDENTIFIER_WITH_SUFFIX

# Custom identifier patterns
from simplibs.patterns.identifiers.custom.TAG_NAME import TAG_NAME
from simplibs.patterns.identifiers.custom.ELEMENT_NAME import ELEMENT_NAME


def test_identifier_start_character(subtests):
    assert_pattern(
        subtests,
        IDENTIFIER_START_CHARACTER,
        r"[a-zA-Z_]",
        matches=["a", "Z", "_"],
        non_matches=["1", "-", "ab"]
    )

def test_identifier_character(subtests):
    assert_pattern(
        subtests,
        IDENTIFIER_CHARACTER,
        r"[a-zA-Z0-9_]",
        matches=["a", "Z", "5", "_"],
        non_matches=["-", "ab", " "]
    )

def test_identifier(subtests):
    assert_pattern(
        subtests,
        IDENTIFIER,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_simple_identifier(subtests):
    assert_pattern(
        subtests,
        SIMPLE_IDENTIFIER,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_name(subtests):
    assert_pattern(
        subtests,
        NAME,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_qualified_identifier(subtests):
    assert_pattern(
        subtests,
        QUALIFIED_IDENTIFIER,
        r"[a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)+",
        matches=["os.path", "a.b.c"],
        non_matches=["os", "os.", "a..b", ".a"]
    )

def test_qualified_name(subtests):
    assert_pattern(
        subtests,
        QUALIFIED_NAME,
        r"[a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)+",
        matches=["os.path", "a.b.c"],
        non_matches=["os", "os.", "a..b", ".a"]
    )

def test_namespace(subtests):
    assert_pattern(
        subtests,
        NAMESPACE,
        r"[a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)*",
        matches=["std", "std.io", "a.b.c"],
        non_matches=["", "a.", "1a"]
    )

def test_namespace_name(subtests):
    assert_pattern(
        subtests,
        NAMESPACE_NAME,
        r"[a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)*",
        matches=["std", "std.io", "a.b.c"],
        non_matches=["", "a.", "1a"]
    )

def test_variable_name(subtests):
    assert_pattern(
        subtests,
        VARIABLE_NAME,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_constant_name(subtests):
    assert_pattern(
        subtests,
        CONSTANT_NAME,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_function_name(subtests):
    assert_pattern(
        subtests,
        FUNCTION_NAME,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_method_name(subtests):
    assert_pattern(
        subtests,
        METHOD_NAME,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_class_name(subtests):
    assert_pattern(
        subtests,
        CLASS_NAME,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_type_name(subtests):
    assert_pattern(
        subtests,
        TYPE_NAME,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_module_name(subtests):
    assert_pattern(
        subtests,
        MODULE_NAME,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_package_name(subtests):
    assert_pattern(
        subtests,
        PACKAGE_NAME,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_attribute_name(subtests):
    assert_pattern(
        subtests,
        ATTRIBUTE_NAME,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_property_name(subtests):
    assert_pattern(
        subtests,
        PROPERTY_NAME,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_parameter_name(subtests):
    assert_pattern(
        subtests,
        PARAMETER_NAME,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_argument_name(subtests):
    assert_pattern(
        subtests,
        ARGUMENT_NAME,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_enum_name(subtests):
    assert_pattern(
        subtests,
        ENUM_NAME,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_enum_member_name(subtests):
    assert_pattern(
        subtests,
        ENUM_MEMBER_NAME,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_key(subtests):
    assert_pattern(
        subtests,
        KEY,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_value_name(subtests):
    assert_pattern(
        subtests,
        VALUE_NAME,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_label(subtests):
    assert_pattern(
        subtests,
        LABEL,
        r"[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["name", "_private", "snake_case_2", "X"],
        non_matches=["2fast", "with-dash", "", "a b"]
    )

def test_qualified_identifier_of(subtests):
    pattern = QUALIFIED_IDENTIFIER_OF(3)
    assert_pattern(
        subtests,
        pattern,
        r"[a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*){2}",
        matches=["a.b.c", "os.path.join"],
        non_matches=["a.b", "a.b.c.d", "abc"]
    )

def test_identifier_with_prefix(subtests):
    pattern = IDENTIFIER_WITH_PREFIX("get_")
    assert_pattern(
        subtests,
        pattern,
        r"get_[a-zA-Z_][a-zA-Z0-9_]*",
        matches=["get_value", "get_x1"],
        non_matches=["get_", "value"]
    )

def test_identifier_with_suffix(subtests):
    pattern = IDENTIFIER_WITH_SUFFIX("_id")
    assert_pattern(
        subtests,
        pattern,
        r"[a-zA-Z_][a-zA-Z0-9_]*_id",
        matches=["user_id", "order_id"],
        non_matches=["_id", "user"]
    )

def test_tag_name(subtests):
    assert_pattern(
        subtests,
        TAG_NAME,
        r"[a-zA-Z][a-zA-Z0-9\-]*",
        matches=["div", "h1", "my-element"],
        non_matches=["1div", "-x", "", "a_b"]
    )

def test_element_name(subtests):
    assert_pattern(
        subtests,
        ELEMENT_NAME,
        r"[a-zA-Z][a-zA-Z0-9\-]*",
        matches=["div", "h1", "my-element"],
        non_matches=["1div", "-x", "", "a_b"]
    )