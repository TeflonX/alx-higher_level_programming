#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    my_list = list(a_dictionary)
    for x in my_list:
        if a_dictionary[x] == value:
            del a_dictionary[x]
    return a_dictionary
