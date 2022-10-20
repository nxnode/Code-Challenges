# https://www.codewars.com/kata/55c45be3b2079eccff00010f

from code_challenges.code_wars.your_order_please import sort_order


def test_sort_order():
    assert sort_order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
    assert (
        sort_order("4of Fo1r pe6ople g3ood th5e the2")
        == "Fo1r the2 g3ood 4of th5e pe6ople"
    )
    assert sort_order("") == ""
