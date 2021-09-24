"""Example of a function that process a list"""


def main() -> None:
    names: list[str] = ["Kris", "Kaki"]
    print(contains("Kris", names))


# Define a function named  contains
# We can give two arguments: a needle value we're searching for in a haystack list
def contains(needle: str, haystack: list[str]) -> bool:
    """Return True if needle is found in haystack, False otherwise."""
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return True
        i += 1
    return False
    # Return false after testing each item


# Python idiom for starting main function
if __name__ == "__main__":
    main()