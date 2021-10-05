"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730475029"


def test_only_evens_odds() -> None:
    """Tests a list with only odd values."""
    lst: list[int] = [3, 5, 7, 9, 11]
    assert only_evens(lst) == []


def test_only_evens_mix() -> None:
    """Tests a list with a mix of even and odd values"""
    lst: list[int] = [2, 9, 13, 56, 87, 100]
    assert only_evens(lst) == [2, 56, 100]


def test_only_evens_mix2() -> None:
    """Tests a list with a mix of even and odd values"""
    lst: list[int] = [4, 10, 26, 112, 93, 2001]
    assert only_evens(lst) == [4, 10, 26, 112]


def test_sub_edge() -> None:
    """Tests a list with start index 0 and end index -1"""
    lst: list[int] = [1, 2, 3, 4]
    first_num: int = 0
    last_num: int = -1
    assert sub(lst, first_num, last_num) == [2, 3, 4]


def test_sub_use() -> None:
    """Tests a list with start index 1 and end index 4"""
    lst: list[int] = [1, 2, 3, 4, 5, 6]
    first_num: int = 1
    last_num: int = 4
    assert sub(lst, first_num, last_num) == [2, 3, 4]


def test_sub_use2() -> None:
    """Tests a list with start index 2 and end index 7"""
    lst: list[int] = [20, 40, 80, 60, 70, 30, 100, 120, 65, 90]
    first_num: int = 2
    last_num: int = 7
    assert sub(lst, first_num, last_num) == [80, 60, 70, 30, 100]


def test_concat_edge() -> None:
    list_1: list[int] = [0]
    list_2: list[int] = [0]
    assert concat(list_1, list_2) == [0, 0]


def test_concat_use() -> None:
    list_1: list[int] = [1, 2, 3, 4]
    list_2: list[int] = [4, 5, 6, 7]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 4, 5, 6, 7]


def test_concat_use2() -> None:
    list_1: list[int] = [100, 200, 400, 800]
    list_2: list[int] = [6000, 300, 600, 300]
    assert concat(list_1, list_2) == [100, 200, 400, 800, 6000, 300, 600, 300]