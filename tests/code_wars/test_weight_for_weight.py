import pytest

from code_challenges.code_wars.weight_for_weight import convert_and_sort_weights


@pytest.mark.parametrize(
    "test_weights,expected_weights",
    [
        ("103 123 4444 99 2000", "2000 103 123 4444 99"),
        (
            "2000 10003 1234000 44444444 9999 11 11 22 123",
            "11 11 2000 10003 22 123 1234000 44444444 9999",
        ),
        ("", ""),
    ],
)
def test_convert_and_sort_weights(test_weights, expected_weights):
    assert convert_and_sort_weights(test_weights) == expected_weights
