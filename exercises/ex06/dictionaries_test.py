"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "123456789"


def test_invert_1() -> None:
    """Tests a dictionary with  a duplicat key."""
    dictionary: dict[str, str] = {'a': 'b', 'd': 'c'}
    assert invert(dictionary) == {'b': 'a', 'c': 'd'}


def test_invert_2() -> None:
    """Tests a dictionary with 2 value key-value pairs."""
    dictionary: dict[str, str] = {'a': 'b', 'c': 'd'}
    assert invert(dictionary) == {'b': 'a', 'd': 'c'} 


def test_invert_3() -> None:
    """Tests a dictionary with 3 value key-value pairs."""
    dictionary: dict[str, str] = {'a': 'b', 'c': 'd', 'e': 'f'}
    assert invert(dictionary) == {'b': 'a', 'd': 'c', 'f': 'e'}


def test_favorite_color_none() -> None:
    """Tests a dictionary with no max values."""
    names_and_colors: dict[str, str] = {'marcus': 'blue', 'john': 'red', 'macy': 'purple'}
    assert favorite_color(names_and_colors) == "None"


def test_favorite_color_some() -> None:
    """Tests a dictionary with 2 max values."""
    names_and_colors: dict[str, str] = {'marcus': 'blue', 'john': 'blie', 'macy': 'purple'}
    assert favorite_color(names_and_colors) == "blue"


def test_favorite_color_all() -> None:
    """Tests a dictionary with all max values."""
    names_and_colors: dict[str, str] = {'marcus': 'blue', 'john': 'blue', 'macy': 'blue'}
    assert favorite_color(names_and_colors) == "blue"


def test_count_edge() -> None:
    """Returns the count of an item that is the only component in the list."""
    lst: list = [3, 3, 3, 3, 3]
    assert count(lst) == {'3', 4}


def test_count_use() -> None:
    """Returns the count of items of a list."""
    lst: list = [3, 4, 3, 4, 3]
    assert count(lst) == {'3', 3}


def test_count_use1() -> None:
    """Returns the count of an items of a list."""
    lst: list = [4, 4, 4, 4, 3]
    assert count(lst) == {'4', 3}