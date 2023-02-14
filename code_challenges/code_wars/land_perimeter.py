# https://www.codewars.com/kata/5839c48f0cf94640a20001d3/python


def perimeter(area):
    perimeter_count = 0
    min_y = 0
    min_x = 0
    max_y = len(area) - 1
    max_x = len(area[0]) - 1
    for y, row in enumerate(area):
        for x, column in enumerate(row):
            if column == "X":
                if y - 1 < min_y or area[y - 1][x] == "O":
                    perimeter_count += 1
                if x - 1 < min_x or row[x - 1] == "O":
                    perimeter_count += 1
                if x + 1 > max_x or row[x + 1] == "O":
                    perimeter_count += 1
                if y + 1 > max_y or area[y + 1][x] == "O":
                    perimeter_count += 1

    return f"Total land perimeter: {perimeter_count}"
