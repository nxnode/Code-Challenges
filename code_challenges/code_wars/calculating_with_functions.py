# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python


def zero(math_func=None):
    if not math_func:
        return 0
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
    def _plus(x):
        return x + y

    return _plus


def minus(y):
    def _minus(x):
        return x - y

    return _minus


def times(y):
    def _times(x):
        return x * y

    return _times


def divided_by(y):
    def _divided_by(x):
        return x // y

    return _divided_by


if __name__ == "__main__":
    assert one(divided_by(nine())) == 9
