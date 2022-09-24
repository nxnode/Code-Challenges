from code_challenges.adhoc.file_operations import append_file, read_file, write_file


def test_read_file():
    lines = ["1234", "4567"]
    write_file("./tests/data/the_data.txt", lines)
    assert read_file("./tests/data/the_data.txt") == lines


def test_append_file():
    lines = read_file("./tests/data/the_data.txt")
    append_file("./tests/data/the_data.txt", lines)
    assert read_file("./tests/data/the_data.txt") == lines + lines


def test_write_file():
    lines = ["1234", "4567"]
    write_file("./tests/data/the_data.txt", lines)
    assert read_file("./tests/data/the_data.txt") == lines
