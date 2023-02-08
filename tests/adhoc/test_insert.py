import pytest
from code_challenges.adhoc.insert import insert


@pytest.mark.parametrize(
    "number_to_insert,sorted_test_list, expected_insertion",
    [
        (3, [1, 2, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
        (-15, [1, 2, 3, 4, 5, 6], [-15, 1, 2, 3, 4, 5, 6]),
        (10, [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 10]),
    ],
)
def test_insert(number_to_insert, sorted_test_list, expected_insertion):
    insert(number_to_insert, sorted_test_list)
    assert sorted_test_list == expected_insertion
