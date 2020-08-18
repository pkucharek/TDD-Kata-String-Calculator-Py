from typing import List


def add(arguments: str) -> int:
    numbers: List[str] = arguments.split(",")
    if (
        len(numbers) == 1
        and numbers[0] == ""
    ):
        return 0
    if (
        len(numbers) == 1
        and numbers[0] != ""
    ):
        return int(numbers[0])
    if len(numbers) == 2:
        return sum_numbers(numbers)
    return -1


def sum_numbers(numbers: List[str]) -> int:
    a: int = int(numbers[0])
    b: int = int(numbers[1])
    return a + b
