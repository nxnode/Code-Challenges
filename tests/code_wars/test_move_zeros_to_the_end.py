# https://www.codewars.com/kata/52597aa56021e91c93000cb0


from code_challenges.code_wars.move_zeros_to_the_end import move_zeros_to_end


def test_move_zeros_to_end():
    assert move_zeros_to_end([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [
        1,
        2,
        1,
        1,
        3,
        1,
        0,
        0,
        0,
        0,
    ]
    assert move_zeros_to_end(
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
    ) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert move_zeros_to_end([0, 0]) == [0, 0]
    assert move_zeros_to_end([0]) == [0]
    assert move_zeros_to_end([]) == []
