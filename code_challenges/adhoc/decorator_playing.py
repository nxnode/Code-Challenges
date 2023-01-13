from functools import lru_cache, wraps

import pytest


def timer(func):
    import time

    @wraps
    def wrapper(*args, **kwargs):
        now = time.time()
        print("runs code before")
        result = func(*args, **kwargs)
        print(f"time:{time.time() - now}")
        print("runs code after")
        return result

    return wrapper


@timer
def new_func(a, b="string"):
    print("newfunc")
    return "1,2,3"


@lru_cache(maxsize=2)
def long_time(string):
    import time

    print("taking a while")
    for _ in string:
        time.sleep(1)
    return "finished"


@pytest.mark.parametrize("a, b", [(False, False), (True, False), (False, True)])
def test_test(a, b):
    assert a or b


if __name__ == "__main__":
    print("main")
    print(long_time("yesss"))
    print(long_time("yesss"))
