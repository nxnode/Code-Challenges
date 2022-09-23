def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = []
        for line in file.readlines():
            lines.append(line.rstrip())
    return lines


def append_file(path, lines):
    with open(path, "a", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")


def write_file(path, lines):
    with open(path, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")
