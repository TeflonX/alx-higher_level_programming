#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    s = len(my_list)
    if idx < 0 or idx > s - 1:
        return my_list
    if idx >= 0 and idx <= s - 1:
        for i in range(s):
            if i == idx:
                my_list[i] = element
        return my_list
