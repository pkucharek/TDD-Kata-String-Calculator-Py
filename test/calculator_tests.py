import pytest

from main.calculator import add
from main.negatives_not_allowed import NegativesNotAllowedException


def test__returns_0__when_input_is_empty():
    assert add("") == 0


def test__returns_argument__when_argument_is_digit():
    assert add("1") == 1


@pytest.mark.parametrize("numbers,sum_of_numbers", [
    ("1,2", 3),
    ("2,1", 3),
    ("35,12", 47),
    ("35,0", 35),
    ("35,0,25,50,70,2", 182),
])
def test__returns_sum_of_numbers__when_arguments_are_numbers_separated_by_comma(
        numbers: str, sum_of_numbers: int) -> None:
    assert add(numbers) == sum_of_numbers


@pytest.mark.parametrize("numbers,sum_of_numbers", [
    ("1\n0", 1),
    ("35\n0,25\n50,70\n2", 182),
    ("1\n2,3\n4", 10)
])
def test__returns_sum_of_numbers__when_arguments_are_numbers_separated_by_new_line_character_or_comma(
        numbers: str, sum_of_numbers: int) -> None:
    assert add(numbers) == sum_of_numbers


@pytest.mark.parametrize("numbers,sum_of_numbers", [
    ("//;\n1;1", 2),
    ("//#\n3#4#2", 9),
    ("//abc\n45abc3abc8", 56)
])
def test__returns_sum_of_numbers__when_different_delimiter_is_declared(numbers: str, sum_of_numbers: int) -> None:
    assert add(numbers) == sum_of_numbers


@pytest.mark.parametrize("numbers,negative_numbers", [
    ("-1,1", "-1"),
    ("-2,-4,0,-5", "-2, -4, -5"),
    ("//abc\n-45abc3abc-8", "-45, -8")
])
def test__throws_negatives_not_allowed_exception_with_list_of_negative_numbers__when_passed_negative_numbers(
        numbers, negative_numbers):
    with pytest.raises(NegativesNotAllowedException) as e:
        add(numbers)
    assert str(e.value) == f"Negatives not allowed: {negative_numbers}"


@pytest.mark.parametrize("numbers,sum_of_numbers", [
    ("1,1001", 1),
    ("12000,1000,1", 1001),
])
def test__ignores_arguments_greater_than_1000(numbers, sum_of_numbers):
    assert add(numbers) == sum_of_numbers
