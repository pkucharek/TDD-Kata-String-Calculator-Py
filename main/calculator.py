import re
from typing import List


def add(arguments: str) -> int:
    numbers = prepare_numbers(arguments)
    if are_numbers_empty(numbers):
        return 0
    return sum_numbers(numbers)


def prepare_numbers(arguments: str) -> List[str]:
    if arguments.startswith("//"):
        separator: str = re.search("//(.+)\n", arguments).group(1)
        arguments = arguments.replace(f"//{separator}\n", "")
    else:
        separator: str = "[\\n,]"
    return re.split(separator, arguments)


def are_numbers_empty(numbers: List[str]) -> bool:
    return len(numbers) == 1 and numbers[0] == ""


def sum_numbers(numbers: List[str]) -> int:
    summary: int = 0
    for number in numbers:
        summary += int(number)
    return summary
