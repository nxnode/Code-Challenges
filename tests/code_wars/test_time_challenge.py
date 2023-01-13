from code_challenges.code_wars.time_challenge import readable_time


def test_readable_time():
    assert readable_time(0) == "00:00:00"
    assert readable_time(5) == "00:00:05"
    assert readable_time(60) == "00:01:00"
    assert readable_time(86399) == "23:59:59"
    assert readable_time(359999) == "99:59:59"
