class NegativesNotAllowedException(Exception):
    def __init__(self, negative_numbers: str, message: str = "Negatives not allowed: ") -> None:
        super().__init__(message + negative_numbers)
