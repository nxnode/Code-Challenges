# https://www.codewars.com/kata/55c45be3b2079eccff00010f


def sort_order(order):
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    order_lst = order.split()
    order = ""
    for num in numbers:
        for word in order_lst:
            if str(num) in word:
                order += f"{word} "
    return order.rstrip()
