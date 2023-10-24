#!/usr/bin/python3
def safe_print_integer(value):
    ret_value = True
    try:
        print("{:d}".format(value))
    except:
        ret_value = False
    return (ret_value)
