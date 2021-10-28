"""Practice with dictionaries."""

__author__ = "123456789"

# Define your functions below


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Returns an inverted version of the input dictionary."""
    inverted_dict: dict[str, str] = {}
    for key in dictionary:
        if dictionary[key] in inverted_dict:
            raise KeyError("Duplicate Key Detected.")
        inverted_dict = {dictionary[key]: key}
    return inverted_dict
    

def favorite_color(names_and_colors: dict[str, str]) -> str:
    """Returns the color that appears most."""
    dict_values: dict[str, int] = {}
    for key in names_and_colors:
        if names_and_colors[key] not in dict_values:
            dict_values[names_and_colors[key]] = 1
        else:
            dict_values[names_and_colors[key]] += 1
    highest: int = 0
    occurrence: str = ""
    for key in dict_values:
        if dict_values[key] > highest:
            highest = dict_values[key]
            occurrence = key
    return occurrence


def count(lst: list[str]) -> dict[str, int]:
    """Returns a dictionary with the counts of the highest counted value."""
    result: dict = {}
    for item in lst:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result