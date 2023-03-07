#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        w = ord(str[i])
        if w > 96 and w < 123:
            w -= 32
        print("{:c}".format(w), end='')
    print("{}".format('\n'), end='')
