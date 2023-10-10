#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)
    if a == 0:
        tuple_a = (0, 0)
    if a == 1:
        tuple_a += (0,)
    if b == 0:
        tuple_b = (0, 0)
    if b == 1:
        tuple_b += (0,)

    new_list = []
    for i in range(2):
        add_no = tuple_a[i] + tuple_b[i]
        new_list.append(add_no)
    return tuple(new_list)
