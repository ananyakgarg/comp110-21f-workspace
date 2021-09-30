def all(haystack: list[int], needle: int) -> bool:
    i: int = 0
    if len(haystack) == 0:
        return False
    else:
        while i < len(haystack):
            if haystack[i] == needle:
                i += 1
            else:
                return False
        return True


def is_equal(list1: list[int], list2: list[int]) -> bool:
    i: int = 0
    if len(list1) != len(list2):
        return False
    else:
        while i < len(list1):
            if list1[i] == list2[i]:
                i += 1
            else:
                return False
        return True


def max(lst: list[int]) -> int:
    i: int = 0
    largest_value: int = lst[0]
    while i < len(lst):
        if lst[i] > largest_value:
            largest_value = lst[i]
        i += 1
    return largest_value       