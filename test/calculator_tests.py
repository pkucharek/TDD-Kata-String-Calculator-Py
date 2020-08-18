from main.calculator import add


def test_when_empty_arguments_returns0():
    assert add("") == 0


def test__when_argument_is_one__returns1():
    assert add("1") == 1


def test__when_arguments_are_1_and_2__returns_3():
    assert add("1,2") == 3


def test__when_arguments_are_2_and_1__returns_3():
    assert add("2,1") == 3
