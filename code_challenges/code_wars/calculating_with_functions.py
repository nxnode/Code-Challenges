# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python


def zero(math_func=None):
    if not math_func:
        return 0
    else:
        return math_func(0)


def one(math_func=None):
    if not math_func:
        return 1
    else:
        return math_func(1)


def two(math_func=None):
    if not math_func:
        return 2
    else:
        return math_func(2)


def three(math_func=None):
    if not math_func:
        return 3
    else:
        return math_func(3)


def four(math_func=None):
    if not math_func:
        return 4
    else:
        return math_func(4)


def five(math_func=None):
    if not math_func:
        return 5
    else:
        return math_func(5)


def six(math_func=None):
    if not math_func:
        return 6
    else:
        return math_func(6)


def seven(math_func=None):
    if not math_func:
        return 7
    else:
        return math_func(7)


def eight(math_func=None):
    if not math_func:
        return 8
    else:
        return math_func(8)


def nine(math_func=None):
    if not math_func:
        return 9
    else:
        return math_func(9)


def plus(y):
    return lambda x: x + y


def minus(y):
    return lambda x: x - y


def times(y):
    return lambda x: x * y


def divided_by(y):
    return lambda x: x // y


if __name__ == "__main__":
    assert one(divided_by(nine())) == 9
