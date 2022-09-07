# Code Wars - https://www.codewars.com/kata/56c5847f27be2c3db20009c3/train/python
# Subtract the sum
# did not perform a true test because it is too time consuming to do the manual
# math to create a answer key to check the fucntion against. Otherwise, I would
# be using the function to test itself - not ideal

# Issue reported with Code Wars - no solution possible with actual attempt
# returns ""returned 'pineapple' and should be 'apple'
# even with changing every pineapple to apple one by one in my answer key
# it still returns same error

import random
from code_challenges.code_wars.subtract_the_sums import subtract_sum

# fruit as a dictionary with fruit as key and list of numbers as values
# fruit_dict = {
#     "apple": [99, 90, 81, 72, 63, 54, 45, 36, 27, 18, 9],
#     "banana": [96, 94, 92, 73, 71, 50, 48, 29, 25, 6, 4],
#     "cherry": [89, 87, 85, 66, 64, 62, 43, 41, 22, 20],
#     "cucumber": [80, 78, 59, 57, 55, 34, 13, 11],
#     "grape": [86, 84, 82, 61, 40, 38, 19, 17, 15],
#     "kiwi": [93, 91, 70, 68, 49, 47, 26, 24, 3, 1],
#     "melon": [97, 95, 76, 74, 53, 51, 32, 30, 28, 7, 5],
#     "orange": [83, 60, 58, 39, 37, 35, 16, 14],
#     "pear": [88, 69, 67, 65, 46, 44, 42, 23, 21, 2],
#     "pineapple": [100, 98, 79, 77, 75, 56, 52, 33, 31, 12, 10, 8],
# }


fruit_dict = [
    "kiwi",
    "pear",
    "kiwi",
    "banana",
    "melon",
    "banana",
    "melon",
    "pineapple",
    "apple",
    "pineapple",
    "cucumber",
    "pineapple",
    "cucumber",
    "orange",
    "grape",
    "orange",
    "grape",
    "apple",
    "grape",
    "cherry",
    "pear",
    "cherry",
    "pear",
    "kiwi",
    "banana",
    "kiwi",
    "apple",
    "melon",
    "banana",
    "melon",
    "pineapple",
    "melon",
    "pineapple",
    "cucumber",
    "orange",
    "apple",
    "orange",
    "grape",
    "orange",
    "grape",
    "cherry",
    "pear",
    "cherry",
    "pear",
    "apple",
    "pear",
    "kiwi",
    "banana",
    "kiwi",
    "banana",
    "melon",
    "pineapple",
    "melon",
    "apple",
    "cucumber",
    "pineapple",
    "cucumber",
    "orange",
    "cucumber",
    "orange",
    "grape",
    "cherry",
    "apple",
    "cherry",
    "pear",
    "cherry",
    "pear",
    "kiwi",
    "pear",
    "kiwi",
    "banana",
    "apple",
    "banana",
    "melon",
    "pineapple",
    "melon",
    "pineapple",
    "cucumber",
    "pineapple",
    "cucumber",
    "apple",
    "grape",
    "orange",
    "grape",
    "cherry",
    "grape",
    "cherry",
    "pear",
    "cherry",
    "apple",
    "kiwi",
    "banana",
    "kiwi",
    "banana",
    "melon",
    "banana",
    "melon",
    "pineapple",
    "apple",
    "pineapple",
]


# 155, 150, 135, 134, 133, 125 all become 99
def test_subtract_sum():
    for i in range(0,101):
        greater_than_ninety_nine = 0
        # all numbers > 99 will reduct to 99
        if i > 99:
            greater_than_ninety_nine = 99
        else:
            greater_than_ninety_nine = i
        assert subtract_sum(greater_than_ninety_nine) == fruit_dict[greater_than_ninety_nine]
