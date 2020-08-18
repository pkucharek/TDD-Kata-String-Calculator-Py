class NegativesNotAllowedException(Exception):
    def __init__(self, negative_numbers, message="Negatives not allowed: "):
        super().__init__(message + negative_numbers)
