# https://www.codewars.com/kata/5297bf69649be865e6000922/train/python

from code_challenges.code_wars.simple_sentences import simple_sentences


def test_simple_sentences():
    assert simple_sentences(["hello", "world"]) == "hello world."
    assert (
        simple_sentences(
            ["Quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
        )
        == "Quick brown fox jumped over the lazy dog."
    )
    assert simple_sentences(["hello", ",", "my", "dear"]) == "hello, my dear."
    assert simple_sentences(["one", ",", "two", ",", "three"]) == "one, two, three."
    assert (
        simple_sentences(
            [
                "One",
                ",",
                "two",
                "two",
                ",",
                "three",
                "three",
                "three",
                ",",
                "4",
                "4",
                "4",
                "4",
            ]
        )
        == "One, two two, three three three, 4 4 4 4."
    )
    assert simple_sentences(["hello", "world", "."]) == "hello world."
    assert simple_sentences(["Bye", "."]) == "Bye."
    assert simple_sentences(["hello", "world", ".", ".", "."]) == "hello world."
    assert (
        simple_sentences(
            [
                "The",
                "Earth",
                "rotates",
                "around",
                "The",
                "Sun",
                "in",
                "365",
                "days",
                ",",
                "I",
                "know",
                "that",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
                ".",
            ]
        )
        == "The Earth rotates around The Sun in 365 days, I know that."
    )
