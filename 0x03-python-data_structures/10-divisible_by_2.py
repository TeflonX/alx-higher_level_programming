#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    s = len(my_list)
    new_list = my_list.copy()
    for i in range(s):
        if new_list[i] % 2 == 0:
            new_list[i] = True
        elif new_list[i] % 2 != 0:
            new_list[i] = False
    return (new_list)
