#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for x in list(a_dictionary):
        new_dict[x] = a_dictionary[x] * 2
    return (new_dict)
