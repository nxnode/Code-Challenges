def reshape_matrix(matrix, r, c):
    new_matrix = []
    new_row = []

    if len(matrix) * len(matrix[0]) != r * c:
        return "no"
    if r < 1 or c < 1:
        return "no"
    for row in matrix:
        for column in row:
            new_row.append(column)
            if len(new_row) == c:
                new_matrix.append(new_row)
                new_row = []

    return new_matrix


if __name__ == "__main__":
    assert reshape_matrix([[1, 2], [3, 4]], r=1, c=4) == [[1, 2, 3, 4]]
