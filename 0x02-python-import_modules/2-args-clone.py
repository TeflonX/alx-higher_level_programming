#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    counter = 0
    for i in range(1, len(argv)):
        counter += 1

    if counter == 0:
        print("{} arguments.".format(counter))
    elif counter == 1:
        print("{} argument:".format(counter))
        print("{}: {}".format(counter, argv[1]))
    elif counter > 1:
        print("{} arguments:".format(counter))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
