# https://adventofcode.com/2022/day/1

from code_challenges.advent_of_code.day_1_elf_with_most_calories import (
    count_elf_calories,
)


def test_count_elf_calories():
    assert count_elf_calories("./tests/data/calories.txt") == 71471
