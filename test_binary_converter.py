import pytest
from binary_converter import to_binary

@pytest.mark.parametrize("n, expected", [
    (0, "0"),
    (1, "1"),
    (2, "10"),
    (10, "1010"),
    (100, "1100100"),
])
def test_valid_conversion(n, expected):
    assert to_binary(n) == expected


@pytest.mark.parametrize("n", [-1, 101, 1000])
def test_out_of_range(n):
    with pytest.raises(ValueError):
        to_binary(n)


@pytest.mark.parametrize("n", [3.5, "10", None])
def test_not_integer(n):
    with pytest.raises(TypeError):
        to_binary(n)