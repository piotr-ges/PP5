"""Module providing basic calculator functions."""


def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference between a and b."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of a and b."""
    return a * b


def divide(a: int, b: int) -> float:
    """Return the result of dividing a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
