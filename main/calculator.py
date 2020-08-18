import re
from typing import List

from main.negatives_not_allowed import NegativesNotAllowedException


def add(arguments: str) -> int:
    numbers: List[str] = prepare_numbers(arguments)
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
    negative_numbers: List[str] = []
    for str_number in numbers:
        int_number: int = int(str_number)
        if is_negative(int_number):
            negative_numbers.append(str_number)
        if is_possible_to_add(int_number):
            summary += int_number
    if negative_numbers:
        raise_negatives_not_allowed_exception(negative_numbers)
    return summary


def is_negative(number: int) -> bool:
    return number < 0


def is_possible_to_add(number: int) -> bool:
    return number <= 1000


def raise_negatives_not_allowed_exception(negative_numbers: List[str]) -> None:
    negative_numbers_str: str = str(negative_numbers)
    negative_numbers_str = re.sub("[\['\]]", "", negative_numbers_str)
    raise NegativesNotAllowedException(negative_numbers_str)
