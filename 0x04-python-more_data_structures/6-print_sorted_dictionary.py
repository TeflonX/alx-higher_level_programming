#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_list = list(a_dictionary)
    for i in sorted(new_list):
        print('{}: {}'.format(i, a_dictionary[i]))
