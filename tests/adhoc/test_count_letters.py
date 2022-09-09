from code_challenges.adhoc.count_letters import count_letters


def test_count_letters():
    assert (
        count_letters("aabbbcc") == "b"
    ), f'expected b but got {count_letters("aabbbcc")}'
