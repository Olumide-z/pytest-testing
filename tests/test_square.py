import pytest
from src.pytest_testing.shapes import Square

# running 3 tests using one function


@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (9, 81)])
def test_square_area(side_length, expected_area):
    square = Square(side_length)
    assert square.area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", [(5, 20), (4, 16), (9, 36)])
def test_square_perimeter(side_length, expected_perimeter):
    square = Square(side_length)
    assert square.perimeter() == expected_perimeter
