#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)

    key_list = list(a_dictionary)
    if not key_list:
        return (None)

    new_list = []
    for x in key_list:
        new_list.append(a_dictionary[x])
    new_list.sort()
    return (new_list[-1])
