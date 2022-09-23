# https://www.codewars.com/kata/5266876b8f4bf2da9b000362

from code_challenges.code_wars.who_likes_it import who_likes


def test_who_likes():
    assert who_likes([]) == "no one likes this"
    assert who_likes(["Peter"]) == "Peter likes this"
    assert who_likes(["Jacob", "Alex"]) == "Jacob and Alex like this"
    assert who_likes(["Max", "John", "Mark"]) == "Max, John and Mark like this"
    assert (
        who_likes(["Alex", "Jacob", "Mark", "Max"])
        == "Alex, Jacob and 2 others like this"
    )
