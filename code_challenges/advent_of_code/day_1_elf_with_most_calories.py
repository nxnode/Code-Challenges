# https://adventofcode.com/2022/day/1


def count_elf_calories(path):
    elf_calories = {1: {"total": 0, "cal_list": []}}
    elf_id = 1
    elf_calories["highest"] = 0
    with open(path, "r", encoding="utf-8") as file:
        lines = []
        for line in file.readlines():
            lines.append(line.rstrip())
    for calorie in lines:
        if calorie != "":
            elf_calories[elf_id]["total"] += int(calorie)
            elf_calories[elf_id]["cal_list"].append(calorie)
        else:
            if elf_calories[elf_id]["total"] > elf_calories["highest"]:
                elf_calories["highest"] = elf_calories[elf_id]["total"]
            elf_id += 1
            elf_calories[elf_id] = {"total": 0, "cal_list": []}

    return elf_calories["highest"]


if __name__ == "__main__":
    test_path = count_elf_calories("./tests/data/calories.txt")
