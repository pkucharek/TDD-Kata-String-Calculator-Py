from main.calculator import add


def test_when_empty_arguments_returns0():
    assert add("") == 0


def test__when_argument_is_one__returns1():
    assert add("1") == 1