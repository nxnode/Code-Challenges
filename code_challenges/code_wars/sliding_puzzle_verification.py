def is_solved(matrix):
    nums = []
    for block in matrix:
        for num in block:
            nums.append(num)
    for i in range(len(nums) - 2):
        first, second = nums[i : i + 2]
        if first + 1 != second:
            return False
    return True
