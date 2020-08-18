import pytest

from main.calculator import add


@pytest.mark.parametrize("numbers,expected", [
    ("", 0),
    ("1", 1),
    ("1\n0", 1),
    ("1,2", 3),
    ("2,1", 3),
    ("35,12", 47),
    ("-35,0", -35),
    ("-35,0,25,50,70,-2", 108),
    ("-35,0,25,50,70,-2", 108),
    ("-35\n0,25\n50,70\n-2", 108),
    ("1\n2,3\n4", 10)
])
def test__when_given_numbers__returns_expected_value(numbers: str, expected: int) -> None:
    assert add(numbers) == expected
