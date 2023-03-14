from yandex_testing_lesson import is_under_queen_attack
import pytest


def test_type1():
    for pos in (1, 1., [1, 2], ('1', '2'), {}, set()):
        with pytest.raises(TypeError):
            is_under_queen_attack(pos, '')


def test_value1():
    for pos in ('a0', 'b9', 'abc', 'j5', 'A1', '28'):
        with pytest.raises(ValueError):
            is_under_queen_attack(pos, '')


def test_type2():
    for pos in (1, 1., [1, 2], ('1', '2'), {}, set()):
        with pytest.raises(TypeError):
            is_under_queen_attack('a1', pos)


def test_value2():
    for pos in ('a0', 'b9', 'abc', 'j5', 'A1', '28'):
        with pytest.raises(ValueError):
            is_under_queen_attack('a1', pos)


def test_same():
    assert is_under_queen_attack('a1', 'a1') is True


def test_horizontal_vertical():
    for x, y in zip('12345678', 'abcdefgh'):
        pos = y + x
        if any(i in 'h1' for i in pos):
            assert is_under_queen_attack(pos, 'h1') is True
        else:
            assert is_under_queen_attack(pos, 'h1') is False


def test_diagonal():
    assert is_under_queen_attack('a1', 'h8') is True
    assert is_under_queen_attack('a2', 'h8') is False
    assert is_under_queen_attack('a1', 'h7') is False
    assert is_under_queen_attack('b1', 'a2') is True
    assert is_under_queen_attack('c2', 'a3') is False
    assert is_under_queen_attack('c1', 'a3') is True
    assert is_under_queen_attack('a7', 'b6') is True
