#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    s = len(my_list)
    my_list.reverse()
    reversed_list = my_list.copy()
    for i in range(s):
        print("{:d}".format(reversed_list[i]))
