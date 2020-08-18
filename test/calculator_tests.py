from main.calculator import add


def test_when_empty_arguments_returns0():
    assert add("") == 0
