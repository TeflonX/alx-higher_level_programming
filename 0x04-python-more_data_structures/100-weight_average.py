#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    sum_1 = 0
    divisor = 0
    for index_1, index_2 in my_list:
        sum_1 += index_1 * index_2
        divisor += index_2
    return (sum_1 / divisor)
