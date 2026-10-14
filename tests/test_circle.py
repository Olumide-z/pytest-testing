import math
from src.pytest_testing.shapes import Circle

# class based test

# class based test comes with two functions that can be useful
# 1 setup method - it is defined to run setup of codes before each test method
# 2 tear down method - to run tear down code after each test methods


class TestCircle:

    def setup_method(self, method):
        print(f'setting up {method}')
        self.circle = Circle(10)

    def teardown_method(self, method):
        print(f'tearing down {method}')
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_paramter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected
