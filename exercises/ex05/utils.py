"""List utility functions part 2."""

__author__ = "730475029"

# Define your functions below


def only_evens(lst: list[int]) -> list[int]:
    """Prints only the even numbers from a list."""
    even_list: list[int] = []
    for num in lst:
        if num % 2 == 0:
            even_list.append(num)
    return even_list


def sub(lst: list[int], first_num: int, last_num: int) -> list[int]:
    """Returns the range of values between the defined index."""
    empty_list: list[int] = []
    empty_list = lst[first_num:last_num]
    return empty_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Concatenates two lists together."""
    new_list: list[int] = []
    for x in list_1:
        new_list.append(x)
    for num in list_2:
        new_list.append(num)
    return new_list