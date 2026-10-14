# this is a like a global file, incase we need something globally
import pytest
from src.pytest_testing.shapes import Rectangle


@pytest.fixture
def my_rectangle():
    return Rectangle(10, 20)


@pytest.fixture
def weird_rectangle():
    return Rectangle(5, 6)
