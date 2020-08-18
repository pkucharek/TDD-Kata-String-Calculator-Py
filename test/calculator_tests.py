import pytest

from main.calculator import add


@pytest.mark.parametrize("numbers,expected", [
    ("", 0),
    ("1", 1),
    ("1,2", 3),
    ("2,1", 3)
])
def test__when_given_numbers__returns_expected_value(numbers, expected):
    assert add(numbers) == expected
