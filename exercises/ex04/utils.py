"""List utility functions."""

__author__ = "730475029"

# TODO: Implement your functions here.


def all(num_lst: list[int], num: int) -> bool:
    """Takes a list and integer and returns a bool value."""
    i: int = 0
    if len(num_lst) == 0:
        return False
    else:
        while i < len(num_lst):
            if num_lst[i] == num:
                i += 1
            else:
                return False
        return True


def is_equal(lst_1: list[int], lst_2: list[int]) -> bool:
    """Takes 2 lists and integer and returns a bool value if they are equal."""
    i: int = 0
    if len(lst_1) != len(lst_2):
        return False
    else:
        while i < len(lst_1):
            if lst_1[i] == lst_2[i]:
                i += 1
            else:
                return False
        return True


def max(input: list[int]) -> int:
    """Takes a list and returns the largest value."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    largest_value: int = input[0]
    while i < len(input):
        if input[i] > largest_value:
            largest_value = input[i]
        i += 1
    return largest_value