"""Example of writing a test subject."""


def multiply(xs: list[int]) -> int:
    """Compute the multiplication of a list."""
    product: int = 1
    for num in xs:
        product *= num
    return product
