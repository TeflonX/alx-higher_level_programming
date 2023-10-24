#!/usr/bin/python3
def safe_print_division(a, b):
    ret_value = 0
    try:
        ret_value = a / b
    except (TypeError, ZeroDivisionError):
        ret_value = None
    finally:
        print("Inside result: {}".format(ret_value))
        return (ret_value)
