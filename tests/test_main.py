import time
import pytest
from main import get_weather, add, division


def test_get_weather():
    assert get_weather(21) == 'HOT'


def test_add():
    result = add(5, 10)
    assert result == 15, f"Expected 15, got {result}"

    result = add(-1, 1)
    assert result == 0, f"Expected 0, got {result}"

    result = add(0, 0)
    assert result == 0


def test_add_strings():
    result = add("I like ", "Burgers")
    assert result == 'I like Burgers'


def test_division():
    result = division(4, 2)
    assert result == 2


def test_division_by_zero():
    # we are expecting a division error
    with pytest.raises(ZeroDivisionError):
        division(10, 0)


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = division(4, 2)
    assert result == 2


@pytest.mark.skip(reason='This feature is currently broken')
def test_add():
    assert add(1, 2) == 3


@pytest.mark.xfail(reason='We know we cannot divide by zero')
def test_divide_zero_broken():
    division(4, 0)
