#!/usr/bin/python3
def best_score(a_dictionary):
    key_list = list(a_dictionary)
    if not a_dictionary:
        return (None)
    if a_dictionary is not None:
        new_list = []
        for x in key_list:
            new_list.append(a_dictionary[x])
        new_list.sort()
        return (new_list[-1])
