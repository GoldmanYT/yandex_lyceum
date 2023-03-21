from yandex_testing_lesson import Rectangle
import pytest


def test_type():
    with pytest.raises(TypeError):
        Rectangle(0, '0')
    with pytest.raises(TypeError):
        Rectangle('0', 0)
    with pytest.raises(TypeError):
        Rectangle('0', '0')


def test_negative():
    with pytest.raises(ValueError):
        Rectangle(-1, 0)
    with pytest.raises(ValueError):
        Rectangle(-1, -1)
    with pytest.raises(ValueError):
        Rectangle(0, -1)


def test():
    rect = Rectangle(5, 5)
    assert rect.get_area() == 25
    assert rect.get_perimeter() == 20
    rect = Rectangle(0, 5)
    assert rect.get_area() == 0
    assert rect.get_perimeter() == 10
    rect = Rectangle(5, 0)
    assert rect.get_area() == 0
    assert rect.get_perimeter() == 10
    rect = Rectangle(2, 7)
    assert rect.get_area() == 14
    assert rect.get_perimeter() == 18
