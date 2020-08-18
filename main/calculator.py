import re
from typing import List


def add(arguments: str) -> int:
    if arguments.startswith("//"):
        separator: str = re.search("//(.+)\n", arguments).group(1)
        arguments = arguments.replace(f"//{separator}\n", "")
    else:
        separator: str = "[\\n,]"
    numbers: List[str] = re.split(separator, arguments)
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
