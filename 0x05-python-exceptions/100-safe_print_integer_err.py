#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    ret_value = True
    try:
        print("{:d}".format(value))
    except Exception as error:
        ret_value = False
        print( 'Exception: {}'.format(error), file=sys.stderr)
    return (ret_value)
