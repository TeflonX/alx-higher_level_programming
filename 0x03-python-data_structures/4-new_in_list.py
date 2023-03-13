#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    s = len(new_list)
    if idx < 0 or idx > s - 1:
        return my_list
    if idx >= 0 and idx <= s - 1:
        for i in range(s):
            if i == idx:
                new_list[i] = element
        return new_list
