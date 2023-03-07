#!/usr/bin/python3
def remove_char_at(str, n):
    list1 = list(str)
    for i in range(len(str)):
        if i != n:
            list2[i] = list1[i]
    print("{:c}".format(list2))
