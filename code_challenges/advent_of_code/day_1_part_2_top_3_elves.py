# https://adventofcode.com/2022/day/1#part2


def count_calories(path):
    elf_calories = {1: {"total": 0}}
    elf_id = 1
    with open(path, "r", encoding="utf-8") as file:
        total_lines = []
        for line in file.readlines():
            if line.rstrip() != "":
                elf_calories[elf_id]["total"] += int(line.rstrip())
            else:
                total_lines.append(elf_calories[elf_id]["total"])
                elf_id += 1
                elf_calories[elf_id] = {"total": 0}
    total_lines.sort(reverse=True)
    return total_lines[0] + total_lines[1] + total_lines[2]


if __name__ == "__main__":
    test_path = count_calories("./tests/data/calories.txt")
