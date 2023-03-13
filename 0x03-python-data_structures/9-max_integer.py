#!/usr/bin/python3
def max_integer(my_list=[]):
    s = len(my_list)
    w = len(my_list)
    if s == 0:
        return (None)
    i = 0
    while(i < 1):
        j = 0
        while (j < s - 1):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
            j += 1
        i += 1
    return my_list[w - 1]
