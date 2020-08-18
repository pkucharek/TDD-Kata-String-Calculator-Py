import pytest

from main.calculator import add


@pytest.mark.parametrize("numbers,expected", [
    ("", 0),
    ("1", 1),
    ("1,2", 3),
    ("2,1", 3),
    ("35,12", 47),
    ("35,0", 35),
    ("35,0,25,50,70,2", 182),
])
def test__when_given_numbers__returns_expected_value(numbers: str, expected: int) -> None:
    assert add(numbers) == expected


@pytest.mark.parametrize("numbers,expected", [
    ("1\n0", 1),
    ("35\n0,25\n50,70\n2", 182),
    ("1\n2,3\n4", 10)
])
def test__when_new_line_character__returns_expected_value(numbers: str, expected: int) -> None:
    assert add(numbers) == expected


@pytest.mark.parametrize("numbers,expected", [
    ("//;\n1;1", 2),
    ("//#\n3#4#2", 9),
    ("//abc\n45abc3abc8", 56)
])
def test__when_declaring_different_delimiter__returns_expected_value(numbers: str, expected: int) -> None:
    assert add(numbers) == expected
