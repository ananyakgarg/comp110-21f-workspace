"""Tests for the multiply function."""


from lessons.multiply import multiply


def test_multiply_empty() -> None:
    xs: list[int] = []
    assert multiply(xs) == 1


def test_multiply_one() -> None:
    xs: list[int] = [1, 2, 3, 4]
    assert multiply(xs) == 24


def test_multiply_more() -> None:
    xs: list[int] = [3, 4, 5, 6, 7]
    assert multiply(xs) == 2520
