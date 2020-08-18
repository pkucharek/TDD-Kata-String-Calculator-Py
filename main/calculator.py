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
    return sum_numbers(numbers)


def sum_numbers(numbers: List[str]) -> int:
    summary: int = 0
    for number in numbers:
        summary += int(number)
    return summary
