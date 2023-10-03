#!/usr/bin/python3
for i in range(100):
    if ((i // 10) > (i % 10)) or ((i // 10) == (i % 10)):
        continue
    elif i == 89:
        print(i)
    else:
        print("{}{}, ".format(i // 10, i % 10), end='')
