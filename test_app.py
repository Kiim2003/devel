from app import add


def test_add():
    assert add(2, 3) == 5

    import pytest


def test_divide():
    assert divide(6, 3) == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
