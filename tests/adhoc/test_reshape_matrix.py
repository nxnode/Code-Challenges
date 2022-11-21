from code_challenges.adhoc.reshape_matrix import reshape_matrix


def test_reshape_matrix():
    assert reshape_matrix([[1, 2], [3, 4]], r=1, c=4) == [[1, 2, 3, 4]]
    assert reshape_matrix([[1, 2], [3, 4], [5, 6], [7, 8]], r=2, c=4) == [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
    ]
    assert reshape_matrix([[1, 2], [3, 4]], r=1, c=5) == "no"
    assert reshape_matrix([[1, 2], [3, 4]], r=1, c="wrong") == "no"
    assert reshape_matrix([[1, 2], [3, 4]], r=1, c=-1) == "no"
