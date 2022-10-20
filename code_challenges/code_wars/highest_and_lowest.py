# https://www.codewars.com/kata/554b4ac871d6813a03000035


def max_and_min(digits):
    num_list = [int(num) for num in digits.split()]
    if len(num_list) < 2:
        return f"{num_list[0]} {num_list[0]}"
    eval_nums = [num_list[0], num_list[1]]
    for num in num_list:
        if num > eval_nums[0]:
            eval_nums[0] = num
        if num < eval_nums[1]:
            eval_nums[1] = num
    return f"{eval_nums[0]} {eval_nums[1]}"
