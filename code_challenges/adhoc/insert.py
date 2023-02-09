def insert_target(target, num_array, low=0, high=None):
    low = max(low, 0)
    if high is None:
        high = len(num_array)
    while low < high:
        middle = (low + high) // 2
        if num_array[middle] < target:
            low = middle + 1
        else:
            high = middle
    return num_array.insert(low, target)


if __name__ == "__main__":
    insert_target(3, [1, 2, 4, 5, 6])
