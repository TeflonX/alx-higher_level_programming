#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    s = len(my_list)
    new_list = my_list.copy()
    for i in range(s):
        if new_list[i] % 2 == 0:
            new_list[i] = True
#        if new_list[i] == 1:
#            new_list[i] = False
        if new_list[i] % 2 > 0 and new_list[i] != True:
            new_list[i] = False;
    print(new_list)
    return (new_list)
