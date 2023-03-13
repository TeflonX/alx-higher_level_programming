#!/usr/bin/pyhton3
def initialize_with_zero(x, tuple_a=()):
    new_list = list(tuple_a)
    for i in range(x):
        new_list.append(0)
    return (new_list)

def add_tuple(tuple_a=(), tuple_b=()):
    x = len(tuple_a)
    y = len(tuple_b)
 
    if x == 0:
        list(tuple_a)
        tuple_a = initialize_with_zero(2, tuple_a)
        tuple(tuple_a)
    if y == 0:
        list(tuple_b) 
        tuple_b = initialize_with_zero(2, tuple_b)
        tuple(tuple_b)
    if x == 1:
        list(tuple_a) 
        tuple_a = initialize_with_zero(1, tuple_a)
        tuple(tuple_a)
    if y == 1:
        list(tuple_b) 
        tuple_b = initialize_with_zero(1, tuple_b)
        tuple(tuple_b)

    i = tuple_a[0] + tuple_b[0]
    j = tuple_a[1] + tuple_b[1]

    return (i, j)
