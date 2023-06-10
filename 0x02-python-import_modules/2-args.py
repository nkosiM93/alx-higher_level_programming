#!/usr/bin/python3

a = "arguments"

if __name__ == "__main__":
    import sys

    args = len(sys.argv) - 1
    if args == 1:
        print("{:d} argument:".format(args))
    else:
        print("{:d} {:s}".format(args, a), end='')
        if args == 0:
            print('.')
            exit()
        print(":")

    for i, v in enumerate(sys.argv):
        if i == 0:
            continue
        print("{:d}: {:s}".format(i, v))
