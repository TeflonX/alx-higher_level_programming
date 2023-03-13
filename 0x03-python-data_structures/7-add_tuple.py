#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = len(tuple_a)
    y = len(tuple_b)

    if x == 0:
        new_list1 = list(tuple_a)
        for i in range(2):
            new_list1.append(0)
        tuple_a = new_list1
        tuple(tuple_a)
    if y == 0:
        new_list2 = list(tuple_b)
        for j in range(2):
            new_list2.append(0)
        tuple_b = new_list2
        tuple(tuple_b)
    if x == 1:
        new_list1 = list(tuple_a)
        for i in range(1):
            new_list1.append(0)
        tuple_a = new_list1
        tuple(tuple_a)
    if y == 1:
        new_list2 = list(tuple_b)
        for j in range(1):
            new_list2.append(0)
        tuple_b = new_list2
        tuple(tuple_b)

    val_a = tuple_a[0] + tuple_b[0]
    val_b = tuple_a[1] + tuple_b[1]

    new_tuple = (val_a, val_b)
    return (new_tuple[0:2])
