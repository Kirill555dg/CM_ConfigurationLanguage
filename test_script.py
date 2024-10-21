import pytest
from script import parse_config, pretty_print_xml


def test_output_xml():
    input_text = """
    var base 100
    var aye [1,4,3]
    cool {
       who : [54, 13, 12];
       smth : |base|;
       users : {
           kirill : |aye|;
           misha : 123
       }
    }
    """

    expected_output = (
'''<?xml version="1.0" ?>
<cool>
\t<who type="array">
\t\t<element type="int">54</element>
\t\t<element type="int">13</element>
\t\t<element type="int">12</element>
\t</who>
\t<smth type="int">100</smth>
\t<users type="dict">
\t\t<kirill type="array">
\t\t\t<element type="int">1</element>
\t\t\t<element type="int">4</element>
\t\t\t<element type="int">3</element>
\t\t</kirill>
\t\t<misha type="int">123</misha>
\t</users>
</cool>
'''
    )

    assert(pretty_print_xml(parse_config(input_text))) == expected_output


def test_simple_config():
    input_text = """
    config {
        who : [54, 13, 12];
        smth : 100
    }
    """
    expected_output = (
        "<config>"
            "<who type=\"array\">"
                "<element type=\"int\">54</element>"
                "<element type=\"int\">13</element>"
                "<element type=\"int\">12</element>"
            "</who>"
            "<smth type=\"int\">100</smth>"
        "</config>"
    )
    assert parse_config(input_text) == expected_output


def test_nested_dict():
    input_text = """
    config {
        users : {
            kirill : 123;
            misha : 456
        }
    }
    """
    expected_output = (
        "<config>"
            "<users type=\"dict\">"
                "<kirill type=\"int\">123</kirill>"
                "<misha type=\"int\">456</misha>"
            "</users>"
        "</config>"
    )
    assert parse_config(input_text) == expected_output


def test_constant_substitution():
    input_text = """
    var base 100
    config {
        smth : |base|
    }
    """
    expected_output = (
        "<config>"
            "<smth type=\"int\">100</smth>"
        "</config>"
    )
    assert parse_config(input_text) == expected_output


def test_array_with_constants():
    input_text = """
    var item 5
    config {
        array : [|item|, 10, 15]
    }
    """
    expected_output = (
        "<config>"
            "<array type=\"array\">"
                "<element type=\"int\">5</element>"
                "<element type=\"int\">10</element>"
                "<element type=\"int\">15</element>"
            "</array>"
        "</config>"
    )
    assert parse_config(input_text) == expected_output


# Тесты на ошибки

def test_syntax_error():
    input_text = """
    config {
        who : [54, 13, 12;
        smth : 100
    """
    result = parse_config(input_text)
    assert "Синтаксическая ошибка" in result or "Unexpected Characters" in result


def test_undefined_constant_error():
    input_text = """
    config {
        smth : |undefined_constant|
    }
    """
    result = parse_config(input_text)
    assert "В конфигурации использована неизвестная константа по имени undefined_constant" in result


def test_duplicate_constant_error():
    input_text = """
    var base 100
    var base 200
    config {
        smth : |base|
    }
    """
    result = parse_config(input_text)
    assert "Ошибка" in result and "Константа base уже объявлена" in result