# https://www.codewars.com/kata/5629db57620258aa9d000014


from code_challenges.code_wars.strings_mix import (
    create_freq_maps,
    find_string_differences,
)


def test_create_freq_maps():
    assert {"a": 1, "b": 1, "c": 1}, {"a": 2, "b": 3, "c": 3} == create_freq_maps(
        "abcSDF12%  ", "SAFD*4 aabbbccc"
    )


def test_find_string_differences():
    assert (
        find_string_differences("Are they here", "yes, they are here")
        == "2:eeeee/2:yy/=:hh/=:rr"
    )
    assert (
        find_string_differences(
            "Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp"
        )
        == "2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz"
    )
    assert (
        find_string_differences(
            "looping is fun but dangerous", "less dangerous than coding"
        )
        == "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"
    )
    assert (
        find_string_differences(" In many languages", " there's a pair of functions")
        == "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"
    )
    assert (
        find_string_differences("Lords of the Fallen", "gamekult") == "1:ee/1:ll/1:oo"
    )
    assert find_string_differences("codewars", "codewars") == ""
    assert (
        find_string_differences("A generation must confront the looming ", "codewarrs")
        == "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"
    )
