def insert(num, nums):
    for i in range(len(nums)):
        if num < nums[i]:
            nums.insert(i, num)
            break
