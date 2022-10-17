# https://www.codewars.com/kata/52b7ed099cdc285c300001cd


def sum_of_intervals(test):
    # intervals = [(1, 4), (7, 10), (3, 5)]
    # new_interval = []
    # count_int = 0
    # for i in len(intervals):
    #     start, end = intervals[i]

    #     res = [
    #         num for num in intervals if all(ele >= start and ele <= end for ele in num)
    #     ]
    #     new_interval.append(res[0])
    #     print(f"start: {start} || end:  {end}")
    #     print(f"res: {res[0]}")
    #     print(f"new_interval: {new_interval}")
    #     print(f"num: {num}  || num[0]: {num[0]} || num[1]: {num[1]}")
    #     x = num[0]
    #     y = num[1]
    #     if "full_range" in new_interval:
    #         eval_range = range(
    #             new_interval["full_range"][0][0], new_interval["full_range"][0][1]
    #         )
    #         if (
    #             x in range(int(new_interval["full_range"][0]))
    #             and y > new_interval["full_range"][0][1]
    #         ):
    #             new_interval["full_range"][1] = [y]
    #             new_interval["Sum"] += [y - new_interval["full_range"][1] - x]
    #         elif x not in range(new_interval["full_range"][0][0],) and y not in range(
    #             new_interval["full_range"][0]
    #         ):
    #             new_interval["full_range"].append(num)
    #             new_interval["Sum"] += y - x
    #     else:
    #         new_interval["full_range"] = [(x, y)]
    #     print(f"new_interval: {new_interval}")
    # print(f"new_interval: {new_interval}")