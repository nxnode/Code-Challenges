# https://www.codewars.com/kata/54da5a58ea159efa38000836

from code_challenges.code_wars.find_the_odd_int import odd_freq

test_list = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]

assert odd_freq([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]) == 5
assert odd_freq([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) == -1
assert odd_freq([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) == 5
assert odd_freq([10]) == 10
assert odd_freq([10, 10, 10]) == 10
assert odd_freq([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]) == 10
assert odd_freq([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]) == 1
