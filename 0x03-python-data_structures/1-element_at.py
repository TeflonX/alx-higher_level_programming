#!/usr/bin/python3
def element_at(my_list, idx):
    s = len(my_list)
    if idx < 0:
        return (None)
    if idx > s - 1:
        return (None)
    if idx >= 0 and idx <= s - 1:
        for i in range(s):
            if i == idx:
                return (my_list[i])
