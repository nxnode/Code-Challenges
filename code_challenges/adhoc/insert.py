def insert(num, nums):
    number_amount = len(nums) - 1
    for i, char in enumerate(nums):
        if num < nums[i]:
            nums[i:i] = [num]
            break
        if i == number_amount:
            nums.append(num)
            break
