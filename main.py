from yandex_testing_lesson import count_chars
import pytest


def test_empty():
    assert count_chars('') == {}


def test_one_char():
    assert count_chars('a') == {'a': 1}


def test_palindrome():
    assert count_chars('aba') == {'a': 2, 'b': 1}


def test_str():
    assert count_chars('ab') == {'a': 1, 'b': 1}


def test_wrong_type1():
    with pytest.raises(TypeError):
        count_chars(42)


def test_wrong_type2():
    with pytest.raises(TypeError):
        count_chars([',1', '2,', '3'])
