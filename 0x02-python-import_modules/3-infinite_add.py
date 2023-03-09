#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s = len(sys.argv)
    if s - 1 == 0:
        print("{}".format(s - 1))
    elif s - 1 > 0:
        sum = 0
        for i in range(1, s):
            sum += int(sys.argv[i])
        print("{}".format(sum))
