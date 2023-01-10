# https://adventofcode.com/2022/day/1#part2

from code_challenges.advent_of_code.day_1_part_2_top_3_elves import count_calories


def test_count_elf_calories():
    assert count_calories("./tests/data/calories.txt") == 211189
