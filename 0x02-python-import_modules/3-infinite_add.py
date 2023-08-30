#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sum_total = 0

    if len(sys.argv) == 1:
        print(0)
        exit()

    for i, num in enumerate(sys.argv):
        if i == 0:
            continue
        sum_total += int(num)
    print(sum_total)
