from yandex_testing_lesson import reverse
import pytest


def test_empty():
    assert reverse('') == ''


def test_one_char():
    assert reverse('a') == 'a'


def test_palindrome():
    assert reverse('aba') == 'aba'


def test_str():
    assert reverse('ab') == 'ba'


def test_wrong_type1():
    with pytest.raises(TypeError):
        reverse(42)


def test_wrong_type2():
    with pytest.raises(TypeError):
        reverse([',1', '2,', '3'])
