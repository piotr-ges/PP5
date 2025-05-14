"""Convert natural numbers to binary representation."""


def to_binary(n: int) -> str:
    """Convert a natural number (0–100) to binary string."""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")

    if n < 0 or n > 100:
        raise ValueError("Number must be between 0 and 100 (inclusive).")

    return bin(n)[2:]  # remove '0b' prefix
