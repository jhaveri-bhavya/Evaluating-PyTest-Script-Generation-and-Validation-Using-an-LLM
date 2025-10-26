import pytest
from solutions.square_perimeter import square_perimeter

def test_values():
    assert square_perimeter(10) == 40
    assert square_perimeter(5) == 20
    assert square_perimeter(4) == 16
