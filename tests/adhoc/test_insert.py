from code_challenges.adhoc.insert import insert


def test_insert():
    nums = [1, 2, 4, 5, 6]
    insert(3, nums)
    assert nums == [1, 2, 3, 4, 5, 6]


def test_insert2():
    nums = [1, 2, 4, 5, 6]
    insert(-15, nums)
    assert nums == [-15, 1, 2, 4, 5, 6]


def test_insert3():
    nums = [1, 2, 4, 5, 6]
    insert(10, nums)
    assert nums == [1, 2, 4, 5, 6, 10]
